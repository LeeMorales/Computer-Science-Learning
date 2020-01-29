//Hengyi Li
//This Program is to play the rock scissors and papaer game
//This Program finished by Hengyi Li on 04：56 PM, 19 Oct, 2019
//Copyright @ 2019 Hengyi Li. All rights reserved.

#include <iostream>
#include <iomanip>
#include <istream>
#include <fstream>
#include <cstdlib>
#include <ctime>

using namespace std;

/**
 * This function is used to get the human's choice
 * @return return the human choice
 */
string get_human_choice();

/**
 * This function is used to get the computer choice
 * @return return the computer choice
 */
string get_computer_choice();

/**
 * This function is used to calculate the winner
 * @param human_move use for human's move
 * @param computer_move use for computer's move
 * @param result use to decide the result
 */
void calculate_winner(string human_move, string computer_move, string 
&result);

/**
 * This function is used to create the report
 * @param total used to get the numbers of the total games.
 * @param human_won used to get the times that human won
 * @param draw use to get the draw games.
 */
void create_report(unsigned total, unsigned human_won,
                   unsigned draw);

/**
 * This function is to get random choice for the computer choice
 * @param low to get the lowest number
 * @param high to get the hightest number
 * @return  the random number
 */
unsigned int get_rand_in_range(unsigned low, unsigned high);

/**
 * This function is used to decided the program will go on or not
 * @return  a boolean flag to decide the program will go or not
 */
bool play_again();

//主程序
int main()
{
  unsigned total = 0;
  unsigned human_won = 0;
  unsigned computer_won = 0;
  unsigned draw = 0;
  //欢迎界面
  cout << "Welcome to RPS" << endl;
  do
  {
      string result;
      string human_move = get_human_choice();
      string computer_move = get_computer_choice();
      calculate_winner(human_move, computer_move, result);
      if (result == "human_won")
      {
        human_won++;
      }
      else if (result == "computer_won")
      {
        computer_won++;
      }
      else
      {
        draw++;
      }
      total++;
    }while(play_again());
  create_report(total, human_won, draw);
  return 0;
}

//获取输入选择
string get_human_choice()
{
  cout << "Choose (r)ock, (p)aper, or (s)cissors: ";
  string human_choice;
  getline(cin, human_choice);
  if (human_choice == "r" || human_choice == "p" || human_choice == "s")
  {
    cout << "Computer Choose " << get_computer_choice() << endl;
    if (human_choice == "s")
    {
      return "scissors";
    }
    else if (human_choice == "p")
    {
      return "paper";
    }
    else if (human_choice == "r")
    {
      return "rock";
    }
    else
    {
      return "Invalid Choice";
    }
  }
  else
  {
    cout << "Invalid Choice" << endl;
    cout << "Choose (r)ock, (p)aper, or (s)cissors: ";
    getline(cin,human_choice);
  }
}

//获取电脑选择
string get_computer_choice()
{
  const unsigned MIN_NUMBER = 1;
  const unsigned MAX_NUMBER = 3;
  unsigned computer_choice = get_rand_in_range(MIN_NUMBER, MAX_NUMBER);
  if (computer_choice == MAX_NUMBER)
  {
    return "scissors";
  }
  else if (computer_choice == MIN_NUMBER)
  {
    return "rock";
  }
  else
  {
    return "paper";
  }
}

//计算赢家
void calculate_winner(string human_move, string computer_move, string &
result)
{
  if (human_move == computer_move)
  {
    cout << "No winner; it was a draw." << endl;
    result = "draw";
  }
  else if (human_move == "scissors" && computer_move == "paper")
  {
    cout << "Human won. Congratulations!" << endl;
    result = "human_won";
  }
  else if (human_move == "scissors" && computer_move == "rock")
  {
    cout << "Computer won. Better luck next time." << endl;
    result = "computer_won";
  }
  else if (human_move == "paper" && computer_move == "scissors")
  {
    cout << "Computer won. Better luck next time." << endl;
    result = "computer_won";
  }
  else if (human_move == "paper" && computer_move == "rock")
  {
    cout << "Computer won. Better luck next time." << endl;
    result = "computer_won";
  }
  else if (human_move == "rock" && computer_move == "scissors")
  {
    cout << "Human won. Congratulations!" << endl;
    result = "human_won";
  }
  else if (human_move == "rock" && computer_move == "paper")
  {
    cout << "Human won. Congratulations! " << endl;
    result = "human_won";
  }
}

//输出到文件
void create_report(unsigned total, unsigned human_won, unsigned draw)
{
  const unsigned WIDTH = 4;
  const unsigned PRECISION = 4;
  const unsigned WIDTH_OF_PCT = 4;
  const unsigned PERCENTAGE = 100;
  ofstream output_file;
  output_file.open("../result.txt");
  output_file << left << "Total games:   " << setw(WIDTH) << right << total <<
              endl << "           #   Pct" << endl << left << "Human   "
              << setw(WIDTH) <<
              right << human_won << setw(WIDTH_OF_PCT)
              << setprecision(PRECISION) <<
              fixed << (human_won / total) * PERCENTAGE << "%" << endl << left
              << "Computer"
              << setw(WIDTH) << right << total - human_won - draw
              << setw(WIDTH_OF_PCT)
              << setprecision(PRECISION) << fixed
              << ((total - human_won - draw) / total) *
                 PERCENTAGE << "%" << endl << left << "Draws   "
              << setw(WIDTH) << right <<
              draw << setw(WIDTH_OF_PCT) << setprecision(PRECISION) << fixed
              << (draw /
                  total) * PERCENTAGE << "%" << endl;
  output_file.close();
}

//判断是否继续程序
bool play_again()
{
  string choose;
  cout << "Play again? (y or n): ";
  getline(cin,choose);
  if (choose == "n")
  {
    return true;
  }
}

//设置随机数
unsigned get_rand_in_range(unsigned low, unsigned high)
{
  auto seed = static_cast<unsigned int>(time(nullptr));
  srand(seed);
  unsigned value = rand() % (high - low + 1) + low;
  return value;
}

