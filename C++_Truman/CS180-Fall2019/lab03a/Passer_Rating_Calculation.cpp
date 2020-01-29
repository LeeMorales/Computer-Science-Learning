//Hengyi Li
//This Program is to calculate the passer rate in American NFL
//This Program finished by Hengyi Li on 12:11 PM, 3 Sep, 2019
//Copyright © 2019 Hengyi Li. All rights reserved.

#include <iostream>
using namespace std;

int  main()
{
  double completions;
  cout << "Enter the number of completions: ";
  cin >> completions;

  double attempts;
  cout << "Enter the number of attempts: ";
  cin >> attempts;

  double yards;
  cout << "Enter the number of yards: ";
  cin >> yards;

  double touchdowns;
  cout << "Enter the number of touchdowns: ";
  cin >> touchdowns;

  double interceptions;
  cout << "Enter the number of interceptions: ";
  cin >> interceptions;

  double scaled_completions;
  scaled_completions = ((completions / attempts) * 100.0 - 30.0) / 20.0;

  double scaled_yards;
  scaled_yards = ((yards / attempts) - 3.0) / 4.0;

  double scaled_touchdowns;
  scaled_touchdowns = touchdowns / attempts * 20.0;

  double scaled_interceptions;
  scaled_interceptions = 2.375 - 25.0 * (interceptions / attempts);

  double rating;
  rating = ((scaled_completions + scaled_yards + scaled_touchdowns
            + scaled_interceptions) / 6.0) * 100.0;
  cout << endl << "The player's rating is: " << rating << endl;

  return 0;

}
