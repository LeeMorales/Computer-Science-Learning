// GPU_Accerlating_Calculation.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

// dcomupte.cpp - 运行GPU程序的程序

#include <stdio.h>
#include <windows.h>
#include <d3d11.h>
#include <d3dcompiler.h>
#include <atlbase.h> // CComPtr<T>
#pragma comment(lib, "d3d11.lib")
#pragma comment(lib, "d3dcompiler.lib")

// CComPtr<T> g_obj的使用
// 初始化：&g_obj
// 已经初始化取地址：&g_obj.p
// 调用成员函数：g_obj->
// 释放：g_obj = NULL;

// 工具类型，HRESULT返回值转换为此类型，可自动抛出异常
struct comexcept { explicit comexcept(HRESULT ret) : hr(ret) { if (FAILED(hr)) throw* this; } HRESULT hr; };

// 基础对象
CComPtr<ID3D11Device> g_dev; // 设备对象
CComPtr<ID3D11DeviceContext> g_immctx; // 设备上下文对象
D3D_FEATURE_LEVEL g_level; // Direct3D支持级别
CComPtr<ID3DBlob> g_cs_sort_code; // GPU程序编译后的字节码
CComPtr<ID3D11ComputeShader> g_cs_sort; // GPU程序对象

// 资源对象
CComPtr<ID3D11Buffer> g_constbuf; // 常量内存
CComPtr<ID3D11Buffer> g_gpubuf; // GPU内存
CComPtr<ID3D11ShaderResourceView> g_gpubuf_srv; // GPU内存Shader资源视图绑定（多步Shader计算会用到）
CComPtr<ID3D11UnorderedAccessView> g_gpubuf_uav; // GPU内存乱序访问视图绑定
CComPtr<ID3D11Buffer> g_cpubuf; // CPU内存（用来读取GPU内存数据）

// 常量内存的结构
// 注意：大小必须是16的倍数，否则会失败
typedef struct ConstBuffer
{
	UINT a;
	UINT b;
	UINT c;
	UINT d;
}ConstBuffer;

#define NUM_ELEMENTS 16

void DoCompute();

// 入口点（初始化资源）
int main(int argc, char* argv[])
{
	// 支持的设备级别
	D3D_FEATURE_LEVEL dlevel[] = {
		D3D_FEATURE_LEVEL_11_0,
		D3D_FEATURE_LEVEL_10_1,
		D3D_FEATURE_LEVEL_10_0,
	};

	// 创建设备
	// D3D_DRIVER_TYPE_HARDWARE = 使用GPU
	// D3D_DRIVER_TYPE_WARP = 使用CPU
	(comexcept)D3D11CreateDevice(NULL, D3D_DRIVER_TYPE_HARDWARE, NULL, 0, dlevel, sizeof dlevel / sizeof dlevel[0],
		D3D11_SDK_VERSION, &g_dev, &g_level, &g_immctx);

	// 检查是否支持Compute Shader 4.0
	D3D11_FEATURE_DATA_D3D10_X_HARDWARE_OPTIONS hwopts;
	(comexcept)g_dev->CheckFeatureSupport(D3D11_FEATURE_D3D10_X_HARDWARE_OPTIONS, &hwopts, sizeof(hwopts));
	if (!hwopts.ComputeShaders_Plus_RawAndStructuredBuffers_Via_Shader_4_x)
		(comexcept)E_FAIL;

	// 编译HLSL
	CComPtr<ID3DBlob> cs_errors;
	HRESULT hrcompile = D3DCompileFromFile(L"dcompute.hlsl", NULL, NULL, "main", "cs_4_0", 0, 0, &g_cs_sort_code, &cs_errors);
	if (cs_errors)
	{
		printf("%s", cs_errors->GetBufferPointer());
		return 0; // 直接结束程序而不是抛出异常，确保能显示编译错误
	}
	(comexcept)hrcompile;

	// 创建Compute Shader
	(comexcept)g_dev->CreateComputeShader(g_cs_sort_code->GetBufferPointer(), g_cs_sort_code->GetBufferSize(), NULL, &g_cs_sort);

	// 创建常量内存（必须是16的倍数，对应b0寄存器）
	D3D11_BUFFER_DESC constant_buffer_desc = {
		sizeof(ConstBuffer), D3D11_USAGE_DEFAULT, D3D11_BIND_CONSTANT_BUFFER, 0, 0, 0
	};
	(comexcept)g_dev->CreateBuffer(&constant_buffer_desc, NULL, &g_constbuf);

	// 创建GPU内存
	D3D11_BUFFER_DESC buffer_desc = {
		NUM_ELEMENTS * sizeof(UINT), D3D11_USAGE_DEFAULT, D3D11_BIND_UNORDERED_ACCESS | D3D11_BIND_SHADER_RESOURCE,
		0, D3D11_RESOURCE_MISC_BUFFER_STRUCTURED, sizeof(UINT)
	};
	(comexcept)g_dev->CreateBuffer(&buffer_desc, NULL, &g_gpubuf);

	// 创建GPU内存的Shader资源视图绑定（对应t0寄存器）
	D3D11_SHADER_RESOURCE_VIEW_DESC srvbuffer_desc = { DXGI_FORMAT_UNKNOWN, D3D11_SRV_DIMENSION_BUFFER };
	srvbuffer_desc.Buffer.NumElements = NUM_ELEMENTS;
	(comexcept)g_dev->CreateShaderResourceView(g_gpubuf, &srvbuffer_desc, &g_gpubuf_srv);

	// 创建GPU内存的乱序访问视图绑定（对应u0寄存器）
	D3D11_UNORDERED_ACCESS_VIEW_DESC uavbuffer_desc = { DXGI_FORMAT_UNKNOWN, D3D11_UAV_DIMENSION_BUFFER };
	uavbuffer_desc.Buffer.NumElements = NUM_ELEMENTS;
	(comexcept)g_dev->CreateUnorderedAccessView(g_gpubuf, &uavbuffer_desc, &g_gpubuf_uav);

	// 创建CPU传输内存
	D3D11_BUFFER_DESC readback_buffer_desc = {
		NUM_ELEMENTS * sizeof(UINT), D3D11_USAGE_STAGING, 0, D3D11_CPU_ACCESS_READ, 0, sizeof(UINT)
	};
	(comexcept)g_dev->CreateBuffer(&readback_buffer_desc, NULL, &g_cpubuf);

	DoCompute();

	return 0;
}

// 计算主程序
void DoCompute(void)
{
	// 设置常量内存为1,2,3,4
	// 并将常量内存绑定到b0寄存器
	ConstBuffer cb = { 1, 2, 3, 4 };
	g_immctx->UpdateSubresource(g_constbuf, 0, NULL, &cb, 0, 0);
	g_immctx->CSSetConstantBuffers(0, 1, &g_constbuf.p); // 引用已创建的对象要用&xxx.p而不是&xxx

	// 设置GPU内存为0
	// 并将GPU内存绑定到u0寄存器
	UINT buf[NUM_ELEMENTS] = { 0 };
	g_immctx->UpdateSubresource(g_gpubuf, 0, NULL, &buf[0], 0, 0);
	g_immctx->CSSetUnorderedAccessViews(0, 1, &g_gpubuf_uav.p, NULL);

	// 进行运算（4,4,1线程组，注意cs_4_0只支持M,N,1，只有cs_5_0才支持M,N,P）
	g_immctx->CSSetShader(g_cs_sort, NULL, 0);
	g_immctx->Dispatch(4, 1, 1);

	// 将GPU内存数据复制到CPU
	D3D11_MAPPED_SUBRESOURCE mapped = { 0 };
	g_immctx->CopyResource(g_cpubuf, g_gpubuf);
	(comexcept)g_immctx->Map(g_cpubuf, 0, D3D11_MAP_READ, 0, &mapped);
	memcpy(&buf[0], mapped.pData, NUM_ELEMENTS * sizeof(UINT));
	g_immctx->Unmap(g_cpubuf, 0);

	// 显示数据
	for (int i = 0; i < NUM_ELEMENTS; i++)
	{
		printf("%d ", buf[i]);
	}
	printf("\n");
}
// 运行程序: Ctrl + F5 或调试 >“开始执行(不调试)”菜单
// 调试程序: F5 或调试 >“开始调试”菜单
