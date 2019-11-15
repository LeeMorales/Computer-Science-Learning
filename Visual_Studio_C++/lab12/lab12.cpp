// Your Name Here
// The program purpose here

#include <cctype>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

/**
 * break a string into three tokens at commas
 * @param line the string containing tokens and commas
 * @param tokens a vector that contains the tokens after they have been
 * found
 */
void split(const char* line, vector<string>& tokens);


int main(int argc, char* argv[])
{
  const unsigned ID_WIDTH = 8;
  const unsigned COMMA_WIDTH = 1;
  const unsigned NAME_WIDTH = 15;
  const unsigned MAX_INPUT_LINE_LENGTH = ID_WIDTH + 2 * COMMA_WIDTH +
    NAME_WIDTH;
  const unsigned PAD_LENGTH = 5;
  const unsigned OUTPUT_COLUMN_ONE = NAME_WIDTH + PAD_LENGTH;

  if (argc != 2)
  {
    cout << "usage: " << argv[0] << " filename" << endl;
    return 1;
  }

  ifstream data_file(argv[1]);
  if (data_file.fail())
  {
    cout << "could not open data file " << argv[1] << endl;
    return 2;
  }

  ofstream username_file("usernames.txt");
  char line[MAX_INPUT_LINE_LENGTH];

  while (data_file.getline(line, MAX_INPUT_LINE_LENGTH))
  {
    vector<string> fields;
    split(line, fields);

    string id = fields.at(0);
    cout << id << endl;

    // the rest of the code for the output here
  }

  data_file.close();
  username_file.close();

  return 0;
}

void split(const char* line, vector<string>& tokens)
{
   char DELIMITER[]{ "," };

   const char* token_end = strstr(line, DELIMITER);
  size_t number_of_characters = static_cast<size_t>(token_end - line);

  string id;
  for (size_t count = 0; count < number_of_characters; count++)
  {
    id += line[count];
  }
  tokens.push_back(id);

}