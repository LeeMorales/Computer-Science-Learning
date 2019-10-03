//
//  Pay_Calculator.cpp
//  Pay_Calculator
//
//  Created by Hengyi Li on 2019/8/22.
//  Copyright © 2019 Miles Lee. All rights reserved.

//Hengyi Li

#include <iostream>
using namespace std;

int main(){
  double hours;
  double rate;
  double pay;

  cout <<"How many hours did you work?";
  cin >> hours;

  cout <<"How much do you get paid per hour?";
  cin >> rate;

  pay = hours * rate;

  cout <<"You have earned $" << pay << endl;
  return 0;
}

