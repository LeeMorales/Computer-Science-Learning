import io
import random
import numpy as np
import pyopencl as cl

def dump_step(data, chunk_size):
    """顯示排序過程"""
    msg = io.StringIO('')
    div = io.StringIO('')
    for idx, item in enumerate(data):
        if idx % chunk_size == 0:
            if idx > 0:
                msg.write(' ||')
                div.write('   ')
            div.write(' --')
        else:
            msg.write('  ') 
            div.write('------')
        msg.write(' {:2d}'.format(item))

    out = msg.getvalue()
    if chunk_size == 1: print(' ' + '-' * (len(out) - 1))
    print(out)
    print(div.getvalue())
    msg.close()
    div.close()

def cl_merge_sort_sbs(data_in):
    # 配置計算資源，編譯 OpenCL 程式
    ctx = cl.Context(dev_type=cl.device_type.GPU)
    prg = cl.Program(ctx, CL_CODE).build()
    queue = cl.CommandQueue(ctx)
    mf = cl.mem_flags

    # 資料轉換成 numpy 形式以利轉換為 OpenCL Buffer
    data_np = np.int64(data_in)
    buff_np = np.empty_like(data_np)

    # 建立緩衝區，並且複製數值到緩衝區
    data = cl.Buffer(ctx, mf.READ_WRITE | mf.COPY_HOST_PTR, hostbuf=data_np)
    buff = cl.Buffer(ctx, mf.READ_WRITE | mf.COPY_HOST_PTR, hostbuf=buff_np)

    # 設定合併前初始狀態
    data_len = np.int32(len(data_np))
    chunk_size = np.int32(1)

    dump_step(data_np, chunk_size)
    while chunk_size < data_len:
        # 更新分組大小，每一回合變兩倍
        chunk_size <<= 1
        # 換算平行作業組數 
        group_size = ((data_len - 1) // chunk_size) + 1
        # 進行分組合併作業
        prg.merge(queue, (group_size,), (1,), chunk_size, data_len, data, buff)
        # 將合併結果作為下一回合的原始資料
        temp = data
        data = buff
        buff = temp
        # 顯示此回合狀態
        cl.enqueue_copy(queue, data_np, data)
        dump_step(data_np, chunk_size)

    queue.finish()
    data.release()
    buff.release()

def main():
    n = random.randint(5, 16)
    data = []
    for i in range(n):
        data.append(random.randint(1, 99))
    cl_merge_sort_sbs(data)

if __name__ == '__main__':
    main()