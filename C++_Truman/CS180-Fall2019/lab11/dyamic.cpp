//Hengyi Li
//This Program is for show a Dynamic Array
//This Program Created by Hengyi Li on 11:37 AM, Nov 5, 2019
//This Program has been done by Hengyi Li on 0：55 AM, Nov 9, 2019.
//Copyright @ 2019 Hengyi Li. All rights reserved.

#include <random>
#include <ctime>
#include <iostream>
#include <vector>

using namespace std;

/**
 * This function is to sort the array
 * @param values_array get the array that reads from the file
 * @param value_count get how many numbers that put in the array
 */
void sort_array(int values_of_array[], unsigned value_count);

/**
 * This function is to generate the array
 * @param values_of_array is the array that we generate
 * @param user_allocated_size is the size of the array.
 */
void generate_the_array(int values_of_array[], unsigned user_allocated_size);

/**
 * This function is to output the array
 * @param values_of_array get the array that need to be output
 * @param user_allocated_size get the number of the value that in the array
 */
void
out_put_the_array(const int values_of_array[], unsigned user_allocated_size);

/**
 * This function is to get the median of the array
 * @param values_of_array is the array that we need to get the median value
 * @param user_allocated_size get the size of the array
 */
void median_of_array(const int values_of_array[], unsigned
user_allocated_size, vector<int> &vector_of_values);

/**
 * This function is to get the user input
 * @param user_allocated_size is to get the size of the array from the user
 */
void get_user_input(unsigned &user_allocated_size);

/**
 * This function is to get the smallest value in the array
 * @param values_of_array is the array that we need to get the smallest
 * value in it
 */
void small_value_in_array(const int values_of_array[]);

/**
 * This function is to get he biggest value of the array
 * @param values_of_array is the array that we need to find the biggest value
 * @param user_allocated_sizen is the size of the array
 */
void biggest_value_in_array(const int values_of_array[], unsigned
&user_allocated_size);

int main()
{
  unsigned user_allocated_size;
  vector<int> vector_of_values;
  get_user_input(user_allocated_size);

  int *values = new int[user_allocated_size];

  generate_the_array(values, user_allocated_size);
  sort_array(values, user_allocated_size);
  out_put_the_array(values, user_allocated_size);
  small_value_in_array(values);
  biggest_value_in_array(values, user_allocated_size);
  median_of_array(values, user_allocated_size, vector_of_values);

  delete[] values;
  return 0;
}

void get_user_input(unsigned &user_allocated_size)
{
  cout << "Enter the number of values: ";
  cin >> user_allocated_size;
}

void sort_array(int values_of_array[], unsigned value_count)
{
  for (size_t pass_indx = value_count - 1; pass_indx > 0; pass_indx--)
  {
    for (size_t compare_indx = 0; compare_indx < pass_indx; compare_indx++)
    {
      if (values_of_array[compare_indx] > values_of_array[compare_indx + 1])
      {
        swap(values_of_array[compare_indx],
             values_of_array[compare_indx + 1]);
      }
    }
  }
}


void generate_the_array(int values_of_array[], unsigned user_allocated_size)
{
  unsigned random;
  unsigned small;
  unsigned biggest;
  cout << "Enter the minimum value: ";
  cin >> small;
  cout << "Enter the max value: ";
  cin >> biggest;
  auto seed = static_cast<unsigned int>(time(nullptr));
  srand(seed);
  for (unsigned looptimes = 0; looptimes < user_allocated_size; looptimes++)
  {
    unsigned value = rand() % (biggest - small + 1) + small;
    random = value;
    values_of_array[looptimes] = random;
  }
}

void
out_put_the_array(const int values_of_array[], unsigned user_allocated_size)
{
  cout << "The values in order: [";
  for (size_t position = 0; position < user_allocated_size; position++)
  {
    if (position == user_allocated_size - 1)
    {
      cout << values_of_array[position];
    }
    else
    {
      cout << values_of_array[position] << ", ";
    }
  }
  cout << "]";
}

void small_value_in_array(const int values_of_array[])
{
  cout << endl << "The smallest value in the array is " << values_of_array[0]
       << endl;
}

void biggest_value_in_array(const int values_of_array[], unsigned &
user_allocated_size)
{
  cout << "The largest value in the array is " <<
       values_of_array[user_allocated_size - 1] << endl;
}

void median_of_array(const int values_of_array[], unsigned
user_allocated_size, vector<int> &vector_of_values)
{
  for (unsigned copytimes = 0; copytimes < user_allocated_size; copytimes++)
  {
    vector_of_values.push_back(values_of_array[copytimes]);
  }
  if (user_allocated_size % 2 == 1)
  {
    cout << vector_of_values.at(user_allocated_size / 2 - 1);
  }
  else
  {
    double middle;
    middle = (vector_of_values.at(user_allocated_size / 2) +
              vector_of_values.at((user_allocated_size / 2) - 1)) / 2.0;
    cout << "The median value is " << middle << endl;
  }
}
