#include <iostream>
#include <vector>

using namespace std;

size_t find_minimum(vector<int> vector_of_values)
{
  const unsigned MAX = 0;
  const unsigned MIN = -1;
  int smallest = MIN;
  int biggest = MAX;
  for (unsigned looptimes = 0; looptimes < vector_of_values.size(); looptimes++)
  {
    if(vector_of_values.at(looptimes) > biggest && vector_of_values.at(looptimes) < smallest)
    {
      smallest = vector_of_values.at(looptimes);
    }
    else
    {
      biggest = vector_of_values.at(looptimes);
    }
  }
  return smallest;
}
P