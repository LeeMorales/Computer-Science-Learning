#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;
const unsigned COLO_SIZE = 3;
const unsigned ROW_SIZE = 3;

string get_input_file(string& in_file);
void read_square_from_file(unsigned square[COLO_SIZE][ROW_SIZE], ifstream& file);
bool validate_square();
void print_square();

int main()
{
  ifstream in_file;
  string filename;
  get_input_file(filename);
  read_square_from_file(square, in_file);
  validate_square();
  print_square();
  return 0;
}

string get_input_file(string& in_file)
{
  ifstream file;
  string filename;
  cout << "Enter a filename for processing: ";
  cin >> filename;
  bool done = false;
  while (!done)
  {
    file.open(filename);
    if (file.fail())
    {
      cout << "Could not open foobar.txt. Please try again. " << endl;
      cout << "Enter a filename for processing: ";
      cin >> filename;
    }
    else
    {
      done = true;
    }
  }
}

void read_square_from_file(unsigned square[ROW_SIZE][COLO_SIZE], ifstream& file)
{
  
  for (unsigned row = 0; row < ROW_SIZE; row++)
  {
    for (unsigned col = 0; col < COLO_SIZE; col++)
    {
      file >> square[row][col];
    }
  }
  file.close();
}

bool validate_square()
{
  
}

void print_square()
{
  bool done = false;
  while (!done)
  {
    string filename;
    cout << "+---+---+---+" << endl << "|" << get_input_file(filename) << "|" << endl;
  }
}