// The API isBadVersion is defined for you.
// bool isBadVersion(int version);
#include<iostream>
#include<string> 
#include<cstring>
#include<cstdlib>

using namespace std;

class Solution 
{
  public:
      int firstBadVersion(int n) 
      {
        bool done = false;
        unsigned count = 0;
        while(!done)
        {
          count++;
          if(firstBadVersion(count) == true)
          {
            done = true;
          }
        }
        return count;
      }
};

int stringToInteger(string input) 
{
    return stoi(input);
}

int main() 
{
    string line;
    while (getline(cin, line)) {
        int n = stringToInteger(line);
        getline(cin, line);
        int bad = stringToInteger(line);
        
        int ret = Solution().firstBadVersion(n, bad);

        string out = to_string(ret);
        cout << out << endl;
    }
    return 0;
}