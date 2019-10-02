//Hengyi Li
//This Program is to decide the phone plan
//This Program finished by Hengyi Li on 8：22 PM, 26 Sep, 2019
//Copyright @ 2019 Hengyi Li. All rights reserved.

#include <iostream>
#include <iomanip>
#include <fstream>
#include <istream>

using namespace std;

int main()
{
  ifstream in_file;
  in_file.open("/Users/leemiles/Desktop/lab07/scores.txt");

  unsigned number_of_scores;
  in_file >> number_of_scores;
  cout << "The number of scores is: " << number_of_scores << endl;

  string dummy;
  getline(in_file, dummy);

  string line;
  while (getline(in_file, line))
  {
    string name_of_user;
    getline(in_file, name_of_user);
    for (unsigned loop_times = number_of_scores;
         loop_times <= number_of_scores;
         loop_times++)
    {
      string numbers;
      getline(in_file, numbers);
    }
    unsigned numbers;
    double average_score;
    average_score = (numbers / number_of_scores);
    double highest_score;

    double lowest_score;

    if (average_score >= 90)
    {
      cout << name_of_user << average_score << highest_score << lowest_score
           << "A" << endl;
    } else if (average_score >= 80 && average_score < 90)
    {
      cout << name_of_user << average_score << highest_score << lowest_score
           << "B" << endl;
    } else if (average_score >= 70 && average_score < 80)
    {
      cout << name_of_user << average_score << highest_score << lowest_score
           << "C" << endl;
    } else
    {
      cout << name_of_user << average_score << highest_score << lowest_score
           << "D" << endl;
    }
    in_file.close();
  }
  return 0;
}
