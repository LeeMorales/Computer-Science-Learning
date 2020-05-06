#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;
int findPeakElement(vector<int>& nums);

int main() 
{
  vector<int> nums = {1,2,1,3,5,6,4};
  cout << findPeakElement(nums);
  return 0;
}
int findPeakElement(vector<int>& nums) 
{
  if(nums.size() == 0)
  {
    return -1;
  }

  int left = 0;
  int right = nums.size();
  int mid;
  while(left < right)
  {
    mid = left + (right - left) / 2;
    if(mid > left && mid > right)
    {
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