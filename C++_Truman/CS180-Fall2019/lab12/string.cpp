//Hengyi Li
//This Program is to generate a username for the student’s network and email
// accounts.
//This Program Created by Hengyi Li on 11:37 AM, Nov 12, 2019
//This Program has been done by Hengyi Li on 4：55 PM, Nov 16, 2019.
//Copyright @ 2019 Hengyi Li. All rights reserved.

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
  const unsigned NAME_WIDTH = 30;
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

  ofstream username_file("../usernames.txt");
  char line[MAX_INPUT_LINE_LENGTH];

  while (data_file.getline(line, MAX_INPUT_LINE_LENGTH))
  {
    vector<string> fields;
    split(line, fields);
    string id = fields.at(0);
    cout<< id << endl;

    // the rest of the code for the output here
    string first_name = fields.at(1);
    string last_name = fields.at(2);
    string names = last_name + "," + first_name;

    username_file  << left
                  << setw(NAME_WIDTH)
                  << names
                  << static_cast<char>(tolower(first_name.at(0)))
                  << static_cast<char>(tolower(last_name.at(0)))
                  << id.at(4) << id.at(5) << id.at(6) << id.at (7)
                  << endl;
  }

  data_file.close();
  username_file.close();

  return 0;
}


void split(const char* line, vector<string>& tokens)
{
   const char DELIMITER[] {","};
   const char* token_end = strstr(line, DELIMITER);
   size_t number_of_characters = static_cast<size_t>(token_end - line);

  string id;
  for (size_t count = 0; count < number_of_characters; count++)
  {
    id += line[count];
  }
  tokens.push_back(id);



  const char* first_name = strstr(token_end + 1, DELIMITER);
  size_t number_of_characters_word = static_cast<size_t>(first_name - token_end);

  string first;
  for (size_t count = 1; count < number_of_characters_word; count++)
  {
    first += token_end[count];
  }
  tokens.push_back(first);

  const char* last_name = strstr(first_name + 1, LIMITER);
  tokens.push_back(last_name);
 }
