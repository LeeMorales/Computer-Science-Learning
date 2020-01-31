#include<iostream>
#include<vector>
using namespace std;

int main()
{
  vector<string> alphabet ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
  vector<string> alphabet_upper['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
  string passwd_plain;
  cout << "Please enter your password: ";
  getline(cin, passwd_plain);
  unsigned values_key;
  cout << "Please input your key(included negatives): ";
  cin >> values_key;
  

}