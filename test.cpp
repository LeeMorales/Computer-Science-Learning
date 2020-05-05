#include <iostream>
#include <vector>

using namespace std;

size_t find_minimum(vector<int> vector_of_values);
int get_rand_in_range(int low_limit, int high_limit);

int main()
{
  int seed = (time(nullptr));
  srand(seed);
  const int low = 1;
  const int high = 100;
  vector<int> vector_of_values;
  for(unsigned loop = 0; loop < high; loop++)
  {
    vector_of_values.push_back(get_rand_in_range(low,high));
  }
  cout << "The number in the vector is: " ;
  for(unsigned looptimes = 0; looptimes < vector_of_values.size(); looptimes++)
  {
    cout << vector_of_values.at(looptimes) << " ";
  }
  int min = find_minimum(vector_of_values);
  cout << endl << "The minium value is: " << min;
  return 0;
}

int get_rand_in_range(int low_limit, int high_limit)
{
  int random_number = rand() % (high_limit - low_limit + 1) + low_limit;
  return random_number;
}

size_t find_minimum(vector<int> vector_of_values)
{
  const unsigned MAX = 0;
  const unsigned MIN = 100;
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
