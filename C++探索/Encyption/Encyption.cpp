#include<iostream>
#include<vector>
#include<string>
#include<sstream>
using namespace std;


/**
 * #purpose	: 字符串转十六进制字符串
 * #note	: 可用于汉字字符串
 * #param str		: 要转换成十六进制的字符串
 * #param separator	: 十六进制字符串间的分隔符
 * #return	: 接收转换后的字符串
 */
string strToHex(string str);


int main()
{
  string passwd_plain;
  cout << "Please enter your password: ";
  getline(cin, passwd_plain);
  cout << "The transfer result is" << strToHex(passwd_plain) << endl;
  
  return 0;
}

string strToHex(string str)
{
	const string hex = "0123456789ABCDEF";
  stringstream ss;
 
	for (string::size_type i = 0; i < str.size(); ++i)
		ss << hex[(unsigned char)str[i] >> 4] << hex[(unsigned char)str[i] & 0xf] << " ";
	
	return ss.str();
}