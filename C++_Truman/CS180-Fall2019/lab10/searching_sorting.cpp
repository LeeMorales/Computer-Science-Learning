//Hengyi Li
//This Program is for searching and sorting
//This Program Created by Hengyi Li on 11：36 AM,29 Oct, 2019
//This Program has been done by Hengyi Li on 1:07 AM, 2 Nov, 2019.
//Copyright @ 2019 Hengyi Li. All rights reserved.

#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

const size_t ARRAY_SIZE = 100;

// function Javadoc and prototypes here

/**
 * This function is to sort the array
 * @param values_array get the array that reads from the file
 * @param value_count get how many numbers that put in the array
 */
void sort_array(int values_array[ARRAY_SIZE], size_t value_count);

/**
 * This function is used to copy aray to the vector
 * @param values_array get the values that in the array
 * @param values_vector initialize a vector that can store the array
 * @param value_count get how many numbers in the array
 */
void copy_array_to_vector(int values_array[ARRAY_SIZE], vector<int>
&values_vector, unsigned value_count);

/**
 * This function is used to do a linear search in the array
 * @param values_array get the values that from the array
 * @param values_count get how many numbes that in the array
 * @param value get the numbers that from the array.
 * @return the search result.
 */
size_t linear_search_array(const int values_array[ARRAY_SIZE], size_t
values_count, int value);

/**
 * This function is used to do a binary search in the vector.
 * @param values_vector is the searching place
 * @param value is the numbers that from the array
 * @return the searching result
 */
size_t binary_search_vector(const vector<int> &values_vector, int value);

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
  sort_array(values_array, value_count);
  copy_array_to_vector(values_array, values_vector, value_count);
  bool done = false;
  while (!done)
  {
    cout << endl << "Enter a value to search for: ";
    cin >> value;
    if (value != 0)
    {
      size_t position = linear_search_array(values_array, value_count, value);
      if (position == value_count)
      {
        cout << "Value was not found in the array" << endl;
      }
      else
      {
        cout << "Value is in the array at position " << position << endl;
      }

      position = binary_search_vector(values_vector, value);

      if (position == values_vector.size())
      {
        cout << "Value was not found in the vector" << endl;
      }
      else
      {
        cout << "Value is in the vector at position " << position << endl;
      }
    }
    else
    {
      done = true;
    }
  } // while !done
  return 0;
}

// function definitions here
void sort_array(int values_array[ARRAY_SIZE], size_t value_count)
{
  for (size_t pass_indx = value_count - 1; pass_indx > 0; pass_indx--)
  {
    for (size_t compare_indx = 0; compare_indx < pass_indx; compare_indx++)
    {
      if (values_array[compare_indx] > values_array[compare_indx + 1])
      {
        swap(values_array[compare_indx], values_array[compare_indx + 1]);
      }
    }
  }
}

void copy_array_to_vector(int values_array[ARRAY_SIZE], vector<int>
&values_vector, unsigned value_count)
{
  for (unsigned copytimes = 0; copytimes < value_count; copytimes++)
  {
    values_vector.push_back(values_array[copytimes]);
  }

}

size_t linear_search_array(const int values_array[ARRAY_SIZE], size_t
values_count, int value)
{
  size_t index = 0;
  size_t size = values_count;
  size_t position = size;
  bool found = false;
  while (index < size && !found)
  {
    if (values_array[index] == value)
    {
      found = true;
      position = index;
    }
    index++;
  }
  return position;
}

size_t binary_search_vector(const vector<int> &values_vector, int value)
{
  size_t first = 0;
  size_t last = values_vector.size() - 1;
  size_t position = values_vector.size();
  bool found = false;
  while (!found && first <= last && last < values_vector.size())
  {
    size_t middle = (first + last) / 2;
    if (values_vector.at(middle) == value)
    {
      position = middle;
      found = true;
    }
    else if (values_vector.at(middle) > value)
    {
      last = middle - 1;
    }
    else
    {
      first = middle + 1;
    }
  }
  return position;
}
