//Hengyi Li
//A Program to compute the Celsius equivalents of two Fahrenheit
//temperature values.

#include <iostream>
using  namespace std;

int main()
{
  cout << "this program converts two Fahrenheit temperature readings "
       << "to Celsius" << endl;

  double fahrenhit_temp;
  cout << "Please enter the first F temperature: ";
  cin >> fahrenhit_temp;

  double celsius_temp = (fahrenhit_temp - 32.0) * (5.0 / 9.0);
  cout << "That is equal to " << celsius_temp << " degrees C" << endl;

  cout << "Please enter the second F temperature: ";
  cin >> fahrenhit_temp;

  celsius_temp = (fahrenhit_temp - 32.0) * (5.0 / 9.0);
  cout << "That is equal to " << celsius_temp << " degrees C" << endl;
}