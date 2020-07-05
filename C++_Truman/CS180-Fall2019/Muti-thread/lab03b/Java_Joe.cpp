//Hengyi Li
//This Program is to calculate the price of the order
//This Program finished by Hengyi Li on 5��17 PM, 11 Sep, 2019
//Copyright © 2019 Hengyi Li. All rights reserved.

#include <iostream>
#include <ctime>
#include <iomanip>
#include <cstdlib>
#include <thread>

using namespace std;

/**
 * This function is to get the user input
 * @param name is the name of the user. 
 * @param colombian_quantity is the total amount of the colombian
 * @param deca_quantity is the total amount of the deca
 * @param chai_quantity is the total amount of the chai
 */
void get_user_input(string name, unsigned colombian_quantity, unsigned deca_quantity, unsigned chai_quantity);

double calculation(unsigned colombian_quantity, unsigned deca_quantity, unsigned chai_quantity);

/**
 * This function is to get the numer in random
 * @param MAX_VALUE is the max limit of the random number
 * @param MIN_VALUE is the min limit of the random number
 * @return the random number that generated.
 */
double get_random_bonus(const unsigned MAX_VALUE, const unsigned MIN_VALUE);

int main() 
{

  const unsigned LABEL_WIDTH_COLOM = 14;
  const unsigned LABEL_WIDTH_ORGAN = 12;
  const unsigned LABEL_WIDTH_HEAVEN = 12;
  const unsigned PRECISION = 2;
  const unsigned MAX_VALUE = 5;
  const unsigned MIN_VALUE = 1;
  unsigned colombian_quantity;
  unsigned deca_quantity;
  unsigned chai_quantity;
  string name;

  get_user_input(name,colombian_quantity,deca_quantity,chai_quantity);

  calculation(colombian_quantity,deca_quantity,chai_quantity);

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

  double bonus = get_random_bonus(MAX_VALUE, MIN_VALUE);     
  cout << "Bonus Discount" << setw(LABEL_WIDTH_COLOM)
       << bonus << endl;
  cout << "Grand Total   " << setw(LABEL_WIDTH_COLOM)
       << total - bonus << endl;
  cout << endl << "Thank you for your ordering !" << endl;

  return 0;

}

double get_random_bonus(const unsigned MAX_VALUE, const unsigned MIN_VALUE)
{
     
     unsigned seed = static_cast<unsigned int>(time(nullptr));
     srand(seed);
     double bonus_discount = static_cast<double>(rand() % (MAX_VALUE - MIN_VALUE + 1) + MIN_VALUE);

     return bonus_discount;
}

void get_user_input(string name, unsigned colombian_quantity, unsigned deca_quantity, unsigned chai_quantity)
{
   cout << "Welcome to Java Joe's!" << endl;
   cout << "Enter your name: ";
   getline (cin,name);
   cout << "How many ounces of Colombian, Decaf, and Chai?: ";
   cin >> colombian_quantity >> deca_quantity >> chai_quantity;
   cout << endl << "Invoice for Fred Flintstone" << endl;    
}

double calculation(unsigned colombian_quantity, unsigned deca_quantity, unsigned chai_quantity)
{ 
  const double UNIT_PRICE_COLOMBIAN= 0.35;
  const double UNIT_PRICE_DECAF = 0.85;
  const double UNIT_PRICE_CHAI= 1.10;
  
  double amount_colom_supr =  colombian_quantity * UNIT_PRICE_COLOMBIAN;
  double amount_organ_gold =  deca_quantity * UNIT_PRICE_DECAF;
  double amount_heavn_chai =  chai_quantity * UNIT_PRICE_CHAI;
  double total =  amount_colom_supr + amount_organ_gold + amount_heavn_chai;

  return amount_colom_supr, amount_organ_gold, amount_heavn_chai;
}

void output()
{
     
}