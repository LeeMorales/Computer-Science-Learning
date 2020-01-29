#include <iomanip>
#include <iostream>
#include <fstream>
#include <random>

using namespace std;

/**
 * Prompt for and input a valid choice from a human player
 * @return the choice
 */
string get_human_choice();

/**
 * generate a choice for the computer player
 * @return the choice
 */
string get_computer_choice();

/**
 * Figure out the winner, given two players' moves
 * @param human_choice the first player's move
 * @param ciomputer_choice the second player's move
 * @param winner winner who win
 */
void calculate_winner(string human_choice, string ciomputer_choice, string &
winner);

/**
 * Write the results of a game to a file, given the statistics of game
 * @param total_game how many games were played
 * @param human_wins how many games the human won
 * @param draws how many games were tie game
 */
void create_report(unsigned total_game, unsigned human_wins, unsigned draws);

/**
 * Prompt for and determine whether the user wants to play again or not
 * @return the decision of whether to play again or not
 */
bool play_again();

/**
 * Get a random value between low and high.
 * @param low the smallest random value
 * @param high the largest randome value
 * @return a random value between the low and high
 */
unsigned get_rand_in_range(unsigned low, unsigned high);

int main() {
  cout << "Welcome to the RPS" << endl;
  srand(static_cast<unsigned>(time(nullptr)));

  unsigned total_game = 0;
  unsigned human_wins = 0;
  unsigned draws = 0;

  bool done = false;
  while (!done) {
    string human_choice = get_human_choice();
    string computer_choice = get_computer_choice();
    cout << "Computer chose" << computer_choice << endl;
    string result;
    calculate_winner(human_choice, computer_choice, result);

    total_game++;
    if (result == "draw") {
      cout << "No winner; it was a draw." << endl << endl;
      draws++;
    } else if (result == "human_win") {
      cout << "Human won. Congratulations!" << endl << endl;
      human_wins++;
    } else {
      cout << "Computer won. Better luck next time." << endl << endl;
    }
    done = !play_again();
  }
  cout << "Thank you for playing" << endl;
  create_report(total_game, human_wins, draws);
  return 0;
}

string get_human_choice() {
  bool valid_choice;
  string choice;
  do {
    cout << "Choose (r)ock, (p)aper, or (s)cissors: ";
    getline(cin, choice);

    valid_choice = choice == "r" || "p" || "s";
    if (!valid_choice) {
      cout << "Invalid choice" << endl;
    }
  } while (!valid_choice);
  if (choice == "r") {
    return "rock";
  } else if (choice == "p") {
    return "paper";
  } else {
    return "scissors";
  }
}

string get_computer_choice() {
  const unsigned LOW_CODE = 1;
  const unsigned HIGH_CODE = 3;
  unsigned code = get_rand_in_range(LOW_CODE, HIGH_CODE);
  if (code == LOW_CODE) {
    return "rock";
  }
  if (code == HIGH_CODE) {
    return "paper";
  }
  return "scissors";
}

void calculate_winner(string human_choice, string computer_choice, string
& winner)
{
if (human_choice == computer_choice)
{
winner = "draw";
}
else if (human_choice == "rock" && computer_choice == "scissors" || human_choice == "scissors" && computer_choice == "paper" || human_choice == "paper" && computer_choice == "rock")
{
winner = "human win";
}
else
{
winner = "computer win";
}
}

bool play_again() {
  string choice;
  cout << "Play again? (y or n): ";
  getline(cin, choice);
  return choice == "y" || choice == "Y";
}

unsigned get_rand_in_range(unsigned low, unsigned high) {
  return static_cast<unsigned>(rand()) % (high - low + 1) + low;
}

void create_report(unsigned total_game, unsigned human_wins, unsigned draws) {
  const unsigned LABEL_WIDTH = 9;
  const unsigned NUMBERS_WIDTH = 3;
  const unsigned PCT_WIDTH = 6;
  const unsigned PRECISION = 1;

  ofstream game_results;

  game_results.open("game_results.txt");
  game_results << fixed << setprecision(PRECISION);

  double human_pct = 100.0 * human_wins / total_game;
  unsigned computer_wins = total_game - draws - human_wins;
  double computer_pct = 100.0 * computer_wins / total_game;
  double draw_pct = 100.0 * draws / total_game;

  game_results << "Total games: " << total_game << endl;
  game_results << left << setw(LABEL_WIDTH) << " " << right
               << setw(NUMBERS_WIDTH) << "#" << setw(PCT_WIDTH) << "Pct"
               << endl;
  game_results << left << setw(LABEL_WIDTH) << "Human" << right
               << setw(NUMBERS_WIDTH) << human_wins << setw(PCT_WIDTH)
               << human_pct << endl;
  game_results << left << setw(LABEL_WIDTH) << "Computer" << right
               << setw(NUMBERS_WIDTH) << computer_wins << setw(PCT_WIDTH)
               << computer_pct << endl;
  game_results << left << setw(LABEL_WIDTH) << "Draws" << right
               << setw(NUMBERS_WIDTH) << draws << setw(PCT_WIDTH) << draw_pct
               << endl;

  game_results.close();
}