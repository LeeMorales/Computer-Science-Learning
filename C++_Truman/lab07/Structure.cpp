#include <iostream>
#include <fstream>
#include <istream>

using namespace std;

int main()
{
  ifstream in_file;
  in_file.open("scores.txt");

  unsigned number_of_scores;
  in_file >> number_of_scores;
  cout << "The number of scores is: " << number_of_scores << endl;

  string dummy;
  getline(in_file, dummy);

  string line;
  while (getline(in_file, line))
  {
    cout << line << endl;
    in_file.close();
  }
  return 0;
}
