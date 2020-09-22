// A program to display the contents of a file
// Jon Beck
// 2 December 2019

#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
using namespace std;
                           
int main(int argc, char* argv[])
{
  const unsigned COLUMNS = 10;
  const unsigned FIRST_WIDTH = 5;
  const unsigned WIDTH = 6;
  string filename;
  if (argc == 1)
  {
    cout << "Enter filename: ";
    getline(cin, filename);
  }
  else
  {
    filename = argv[1];
  }

  fstream file;
  file.open(filename, ios::in | ios::binary);
  if (file.fail())
  {
    cerr << "Error opening file" << endl;
    return 1;
  }

  file.seekg(0L);

  cout << right << showbase;
  char abyte;
  bool done = false;
  unsigned count = 0;

  while (!done)
  {
    file.read(&abyte, 1);

    if (file.eof())
    {
      done = true;
    }
    else
    {
      if (count % COLUMNS == 0)
      {
        cout << dec << setw(FIRST_WIDTH) << count;
      }

      uint16_t as_number = static_cast<uint16_t>(abyte) & 0x00ff;

      if (as_number > 0x20 && as_number <= 0x7f)
      {
        cout << setw(WIDTH) << abyte; // display printing characters
      }
      else if (as_number == 0x20)
      {
        cout << setw(WIDTH) << "sp";
      }
      else
      {
        cout << hex << setw(WIDTH) << as_number;
      }

      count++;

      if (count % COLUMNS == 0)
      {
        cout << endl;
      }
    }
  }

  file.close();
  if (count % COLUMNS != 0)
  {
    cout << endl;
  }
  return 0;
}