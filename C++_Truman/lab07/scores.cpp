//Hengyi Li
//This Program is to decide the phone plan
//This Program finished by Hengyi Li on 11：20 AM, 5 Oct, 2019
//Copyright @ 2019 Hengyi Li. All rights reserved.

#include <iostream>
#include <iomanip>
#include <fstream>
#include <istream>

using namespace std;

int main()
{
  const unsigned PRECISION = 2;
  const unsigned WIDTH = 21;
  const unsigned WIDTH_BETWEEN_LINE = 10;
  const double A_GRADE = 90.0;
  const double B_GRADE = 80.0;
  const double C_GRADE = 70.0;
  const double D_GRADE = 60.0;
  //Open File
  ifstream in_file;
  in_file.open("scores.txt");

  //Header Of the number of scores
  unsigned number_of_scores;
  in_file >> number_of_scores;

  //Change the cursor place
  string line;
  string dummy;
  getline(in_file, dummy);

  //ready for output file
  ofstream output_file;
  output_file.open("grade_report.txt");

  //get the name of the user
  while (getline(in_file, line))
  {
    unsigned max_score = 0;
    unsigned min_score = 100;

    double average;
    double total_scores = 0;
    //Main Loop of the Names, Average score, Max score, Min score
    for (unsigned loop_times = 0; loop_times < number_of_scores; loop_times++)
    {
      //average scores
      unsigned numbers_read_from_the_text;
      in_file >> numbers_read_from_the_text;

      total_scores += numbers_read_from_the_text;
      average = (total_scores / number_of_scores);

      //Min and max scores
      if (numbers_read_from_the_text < min_score)
      {
        min_score = numbers_read_from_the_text;
      } else if (numbers_read_from_the_text > max_score)
      {
        max_score = numbers_read_from_the_text;
      }

      //boolean flag to let the loop stop
      bool flag = false;
      do
      {
        //test on the console
        cout << line << right << setw(WIDTH) << min_score << "  " << max_score
             << "  " << setprecision(PRECISION) << fixed << average;
        if (average >= A_GRADE)
        {
          cout << "A" << endl;
        } else if (average >= B_GRADE && average < A_GRADE)
        {
          cout << "B" << endl;
        } else if (average >= C_GRADE && average < B_GRADE)
        {
          cout << "C" << endl;
        } else if (average >= D_GRADE && average < C_GRADE)
        {
          cout << "D" << endl;
        } else
        {
          cout << "F" << endl;
        }
        flag = true;
      } while (!flag);
    }
    //move the cursor
    getline(in_file, dummy);

    //output everything
    cout << "Now writing data to the file" << endl;
    output_file << right << setw(WIDTH) << line << left <<
                setw(WIDTH_BETWEEN_LINE) << "  " << setw(WIDTH_BETWEEN_LINE)
                << min_score <<
                setw
                    (WIDTH_BETWEEN_LINE)
                << max_score << setw(WIDTH_BETWEEN_LINE) << setprecision
                    (PRECISION)
                << fixed << average;
    if (average >= A_GRADE)
    {
      output_file << setw(WIDTH_BETWEEN_LINE) << "A" << endl;
    } else if (average >= B_GRADE && average < A_GRADE)
    {
      output_file << setw(WIDTH_BETWEEN_LINE) << "B" << endl;
    } else if (average >= C_GRADE && average < B_GRADE)
    {
      output_file << setw(WIDTH_BETWEEN_LINE) << "C" << endl;
    } else if (average >= D_GRADE && average < C_GRADE)
    {
      output_file << setw(WIDTH_BETWEEN_LINE) << "D" << endl;
    } else
    {
      output_file << setw(WIDTH_BETWEEN_LINE) << "F" << endl;
    }

    cout << "Done." << endl;
  }

  //close the file
  output_file.close();
  in_file.close();
  return 0;
}