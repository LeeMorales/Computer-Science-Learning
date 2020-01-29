//Hengyi Li
//This Program is to calculate the price of the order
//This Program finished by Hengyi Li on 5£º17 PM, 11 Sep, 2019
//Copyright Â© 2019 Hengyi Li. All rights reserved.

#include <iostream>
#include <ctime>
#include <iomanip>
#include <cstdlib>
using namespace std;

int main() {
  const double UNIT_PRICE_COLOMBIAN= 0.35;
  const double UNIT_PRICE_DECAF = 0.85;
  const double UNIT_PRICE_CHAI= 1.10;
  const unsigned LABEL_WIDTH_COLOM = 14;
  const unsigned LABEL_WIDTH_ORGAN = 12;
  const unsigned LABEL_WIDTH_HEAVEN = 12;
  const unsigned PRECISION = 2;
  const unsigned MAX_VALUE = 5;
  const unsigned MIN_VALUE = 1;
  unsigned colombian_quantity;
  unsigned deca_quantity;
  unsigned chai_quantity;

  cout << "Welcome to Java Joe's!" << endl;
  cout << "Enter your name: ";
  string name;
  getline (cin,name);

  cout << "How many ounces of Colombian, Decaf, and Chai?: ";
  cin >> colombian_quantity >> deca_quantity >> chai_quantity;
  cout << endl << "Invoice for Fred Flintstone" << endl;

  double amount_colom_supr;
  amount_colom_supr =  colombian_quantity * UNIT_PRICE_COLOMBIAN;
  double amount_organ_gold;
  amount_organ_gold =  deca_quantity * UNIT_PRICE_DECAF;
  double amount_heavn_chai;
  amount_heavn_chai =  chai_quantity * UNIT_PRICE_CHAI;
  double total;
  total =  amount_colom_supr + amount_organ_gold + amount_heavn_chai;

  cout << "                  Colom Supr  Organ Gold  Heavn Chai" << endl;
  cout << "                  ----------  ----------  ----------" << endl;
  cout << "Quantity (oz) "<< setw(LABEL_WIDTH_COLOM)
       << setprecision(PRECISION) << fixed << colombian_quantity
       << setw(LABEL_WIDTH_ORGAN)
       << deca_quantity << setw(LABEL_WIDTH_HEAVEN)
       << chai_quantity << endl;
  cout << "Unit Price    " << setw(LABEL_WIDTH_COLOM)
       << UNIT_PRICE_COLOMBIAN
       << setw(LABEL_WIDTH_ORGAN)
       << UNIT_PRICE_DECAF
       << setw(LABEL_WIDTH_ORGAN)
       << UNIT_PRICE_CHAI << endl;
  cout << "Amount        "  << setw(LABEL_WIDTH_COLOM)
       << amount_colom_supr
       << setw(LABEL_WIDTH_ORGAN)
       << amount_organ_gold << setw(LABEL_WIDTH_HEAVEN)
       << amount_heavn_chai << endl;
  cout << endl << "Total:        " << setw(LABEL_WIDTH_COLOM)
       << total << endl;


  unsigned seed = static_cast<unsigned int>(time(nullptr));
  srand(seed);
  double bonus_discount
       = static_cast<double>(rand() % (MAX_VALUE - MIN_VALUE + 1)
       + MIN_VALUE);
  cout << "Bonus Discount" << setw(LABEL_WIDTH_COLOM)
       << bonus_discount << endl;
  cout << "Grand Total   " << setw(LABEL_WIDTH_COLOM)
       << total - bonus_discount << endl;
  cout << endl << "Thank you for your ordering !" << endl;

  return 0;

}
