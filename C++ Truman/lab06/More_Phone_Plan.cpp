//Hengyi Li
//This Program is to decide the phone plan
//This Program finished by Hengyi Li on 8：22 PM, 26 Sep, 2019
//Copyright @ 2019 Hengyi Li. All rights reserved.

#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
  const double ADDITIONAL_DATA_COSTS_A = 9.99;
  const double ADDITIONAL_DATA_COSTS_B = 4.99;
  const double MAX_DATA_IN_PLAN_A = 4.0;
  const double MAX_DATA_IN_PLAN_B = 8.0;
  const unsigned PRECISION = 2;
  bool judge;
  for (string input_choice; input_choice != "Q"; judge = false)
  {
    cout << "Choose the plan (A, B ,Or C) or Q to quit: ";
    cin >> input_choice;
    if (input_choice == "A" || "B" || "C" || "Q")
    {
      if (input_choice == "A")
      {
        double data_usage;
        cout << "How many gigs of data did you use? ";
        cin >> data_usage;
        while (data_usage < 0)
        {
          cout << "Data usage cannot be negative. Please re-enter: ";
          cin >> data_usage;
        }
        double plan_a;
        double invoice_total_a;
        double base_cost_a = 39.99;
        if (data_usage > MAX_DATA_IN_PLAN_A)
        {
          plan_a =
              (data_usage - MAX_DATA_IN_PLAN_A) * ADDITIONAL_DATA_COSTS_A;
          invoice_total_a = base_cost_a + plan_a;
          cout << "Invoice Total " << setprecision(PRECISION) << fixed
               << invoice_total_a << endl << endl;
        }
        else
        {
          invoice_total_a = base_cost_a;
          cout << "Invoice Total " << setprecision(PRECISION) << fixed
               << invoice_total_a << endl << endl;
        }
      }
      else if (input_choice == "B")
      {
        double data_usage;
        cout << "How many gigs of data did you use? ";
        cin >> data_usage;
        while (data_usage <= 0)
        {
          cout << "Data usage cannot be negative. Please re-enter: ";
          cin >> data_usage;
        }
        double plan_b;
        double invoice_total_b;
        double base_cost_b = 59.99;
        if (data_usage > MAX_DATA_IN_PLAN_B)
        {
          plan_b =
              (data_usage - MAX_DATA_IN_PLAN_B) * ADDITIONAL_DATA_COSTS_B;
          invoice_total_b = base_cost_b + plan_b;
          cout << "Invoice total " << setprecision(PRECISION) << fixed
               << invoice_total_b << endl << endl;
        }
        else
        {
          invoice_total_b = base_cost_b;
          cout << "Invoice total " << setprecision(PRECISION) << fixed
               << invoice_total_b << endl << endl;
        }
      }
      else if (input_choice == "C")
      {
        double base_cost_c = 69.99;
        double invoice_total_c;
        invoice_total_c = base_cost_c;
        cout << "Invoice total " << setprecision(PRECISION) << fixed
             << invoice_total_c << endl << endl;
      }
      else if (input_choice == "Q")
      {
        judge = true;
      }
      else
      {
        cout << "Invaild Choice." << endl;
      }
    }
  }

  return 0;

}
