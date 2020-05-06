#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;
int findPeakElement(vector<int> &nums);

int main() 
{
  vector<int> nums;
  nums.push_back(1);
  nums.push_back(2);
  nums.push_back(1);
  nums.push_back(3);
  nums.push_back(5);
  nums.push_back(6);
  nums.push_back(4);
  cout << findPeakElement(nums);
  return 0;
}
int findPeakElement(vector<int> &nums) 
{
  if(nums.size() == 0)
  {
    return -1;
  }

  int left = 0;
  int right = nums.size();
  int mid;
  bool done = false;
  while(!done)
  {
    mid = left + (right - left) / 2;
    if(mid > left && mid > right)
    {
      done = true;
      return mid;
    }
    else if(mid > left && mid < right)
    {
      mid = right - 1;
    }
    else
    {
      mid = left + 1;
    }
  }
return nums.at(mid);
}