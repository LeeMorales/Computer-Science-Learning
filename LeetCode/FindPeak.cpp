#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <algorithm>


using namespace std;

class Solution 
{
public:
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
};
void trimLeftTrailingSpaces(string &input);
void trimRightTrailingSpaces(string &input);
vector<int> stringToIntegerVector(string input);


int main() 
{
    string line;
    while (getline(cin, line)) 
    {
        vector<int> nums = stringToIntegerVector(line);
        
        int ret = Solution().findPeakElement(nums);

        string out = to_string(ret);
        cout << out << endl;
    }
    return 0;
}
void trimLeftTrailingSpaces(string &input) 
{
    input.erase(input.begin(), find_if(input.begin(), input.end(), [](int ch) { return !isspace(ch);}));
}

void trimRightTrailingSpaces(string &input) 
{
    input.erase(find_if(input.rbegin(), input.rend(), [](int ch) {return !isspace(ch);}).base(), input.end());
}

vector<int> stringToIntegerVector(string input) 
{
    vector<int> output;
    trimLeftTrailingSpaces(input);
    trimRightTrailingSpaces(input);
    input = input.substr(1, input.length() - 2);
    stringstream ss;
    ss.str(input);
    string item;
    char delim = ',';
    while (getline(ss, item, delim)) 
    {
        output.push_back(stoi(item));
    }
    return output;
}
