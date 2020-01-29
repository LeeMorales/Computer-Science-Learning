#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const size_t ARRAY_SIZE = 100;
int main()
{
  ifstream data_file;
  data_file.open("data.txt");

  vector<int> values_vector; // a vector of values
  int values_array[ARRAY_SIZE]; // an array of values

  int value;
  size_t value_count = 0;
  while (data_file >> value)
  {
    values_array[value_count] = value;
    value_count++;
  }
  data_file.close();
  cout << "Read " << value_count << " values from data.txt" << endl;
  
  //sort array
  sort(values_array, values_array + value_count);

  for (unsigned looptimes = 0; looptimes < value_count; looptimes++)
  {
    cout << values_array[looptimes] << endl;
  }

return 0;
}