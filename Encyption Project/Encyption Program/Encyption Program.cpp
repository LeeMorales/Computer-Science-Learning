// Encyption Program.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
  //初始化程序，用户输入密钥
  unsigned number_of_digits;
  cout << "How many digits of your password?" << endl;
  string* user_keychain = new string[number_of_digits];

  //用户密钥输入并存入Array
  cout << "Please input the password that you want to encypted one key in once: ";
  string chain;
  for (unsigned looptimes = 0; looptimes < number_of_digits; looptimes++)
  {
    cin >> chain;
    user_keychain[looptimes] = chain;
  }
  vector<string> keychain;
  for (unsigned looptimes = 0; looptimes < number_of_digits; looptimes++)
  {
    keychain.at(looptimes) = user_keychain[looptimes];
  }
  cout << "Starting the caesar encyption, please type the public key" << endl;
  unsigned moveDigits;
  cin >> moveDigits;


}



























// 运行程序: Ctrl + F5 或调试 >“开始执行(不调试)”菜单
// 调试程序: F5 或调试 >“开始调试”菜单

// 入门使用技巧: 
//   1. 使用解决方案资源管理器窗口添加/管理文件
//   2. 使用团队资源管理器窗口连接到源代码管理
//   3. 使用输出窗口查看生成输出和其他消息
//   4. 使用错误列表窗口查看错误
//   5. 转到“项目”>“添加新项”以创建新的代码文件，或转到“项目”>“添加现有项”以将现有代码文件添加到项目
//   6. 将来，若要再次打开此项目，请转到“文件”>“打开”>“项目”并选择 .sln 文件
