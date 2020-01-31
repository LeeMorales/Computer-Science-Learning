#include<iostream>
#include<vector>
using namespace std;

int main()
{
  string passwd_plain;
  cout << "Please enter your password: ";
  getline(cin, passwd_plain);
  unsigned values_key;
  cout << "Please input your key(included negatives): ";
  cin >> values_key;
  
  return 0;
}