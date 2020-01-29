//Hengyi Li
//This Program is to decide the magic square
//This Program finished by Hengyi Li on 04：56 PM, 19 Oct, 2019
//Copyright @ 2019 Hengyi Li. All rights reserved.

#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;
const unsigned SIZE = 3;


/**
 * This function is used to validate the square
 * @return an boolean value that can decide is the square or not
 */
bool validate_square(unsigned square[SIZE][SIZE]);

/**
 * The function prompts the user for a filename.
 * @param in_file if for reference the get the input file form the disk
 * @return the number that in the file
 */
void get_input_file(ifstream &in_file);

/**
 * This function is used for print out the square
 */
void print_square(unsigned square[SIZE][SIZE]);

/**
 * This fuction is used to read the square from the file.
 * @param square this is an 2-d array
 * @param file  get the filre from the disk.
 */
void read_square_from_file(unsigned square[SIZE][SIZE], ifstream &file);

int main()
{
  ifstream in_file;
  string filename;
  get_input_file(in_file);

  unsigned square[SIZE][SIZE];
  read_square_from_file(square, in_file);
  print_square(square);

  if (validate_square(square))
  {
    cout << "This is a valid magic square." << endl;
  }
  else
  {
    cout << "This is not a valid magic square." << endl;
  }
  return 0;
}

void get_input_file(ifstream &in_file)
{
  ifstream file;
  string filename;
  cout << "Enter a filename for processing: ";
  getline(cin, filename);
  bool done = false;
  while (!done)
  {
    file.open(filename);
    if (file.fail())
    {
      cout << "Could not open" << "  " << filename << "  "
           <<"Please try again. "<< endl;
      cout << "Enter a filename for processing: ";
      getline(cin, filename);
    }
    else
    {
      done = true;
    }
  }
}

bool validate_square(unsigned square[SIZE][SIZE])
  {
    unsigned first_row = 0;
    unsigned second_row = 0;
    unsigned third_row = 0;
    unsigned first_col = 0;
    unsigned second_col = 0;
    unsigned third_col = 0;
    unsigned first_diagonal = 0;
    unsigned second_diagonal = 0;

    for (unsigned row = 0; row < SIZE; row++)
    {
      first_col += square[row][0];
    }

    for (unsigned row = 0; row < SIZE; row++)
    {
      second_col += square[row][1];
    }

    for (unsigned row = 0; row < SIZE; row++)
    {
      third_col += square[row][2];
    }

    for (unsigned col = 0; col < SIZE; col++)
    {
      first_row += square[0][col];
    }

    for (unsigned col = 0; col < SIZE; col++)
    {
      second_row += square[1][col];
    }

    for (unsigned col = 0; col < SIZE; col++)
    {
      third_row += square[2][col];
    }

    for (unsigned row = 0; row < SIZE; row++)
    {
      first_diagonal += square[row][row];
    }

    for (unsigned row = 0; row < SIZE; row++)
    {
      second_diagonal += square[SIZE - row - 1][row];
    }

    return (first_col == second_col && first_col == third_col &&
            first_col == first_row && first_col == second_row &&
            first_col == third_row && first_col == first_diagonal &&
            first_col == second_diagonal);
  }

void print_square(unsigned square[SIZE][SIZE])
{
  cout << "+---+---+---+" << endl;
  for (unsigned row = 0; row < SIZE; row++)
  {
     cout << "| " ;
    for (unsigned col = 0; col < SIZE; col++)
    {
      cout << square[row][col] << " | " ;
    }
    cout << endl << "+---+---+---+" << endl;
  }

}

void read_square_from_file(unsigned square[SIZE][SIZE], ifstream &file)
{
  for (unsigned row = 0; row < SIZE; row++)
  {
    for (unsigned col = 0; col < SIZE; col++)
    {
      file >> square[row][col];
    }
  }
  file.close();
}
