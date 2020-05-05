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

size_t find_minimum(vector<int> values)
{
  int min = values[0];
  size_t min_index = 0;
  for (size_t index = 0; index < values.size(); index++)
  {
    if (values[index] < min)
    {
      min = values[index];
      min_index = index;
    }
  }
  return min_index;
}