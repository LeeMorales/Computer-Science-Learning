// A program to create a binary inventory data file
// Jon Beck
// 30 November 2019

#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

const unsigned MAX_DESCRIPTION_WIDTH = 25;

struct Part
{
    char code [MAX_DESCRIPTION_WIDTH];
    uint16_t current_quantity;
    uint16_t max_quantity;
};

int main()
{
  vector<Part> parts;

  parts.push_back({"Thermistor", 703, 950});
  parts.push_back({"Thyratron", 117, 185});
  parts.push_back({"Inclinometer", 670, 770});
  parts.push_back({"Rectifier", 312, 545});
  parts.push_back({"Darlington NPN", 11, 15});
  parts.push_back({"Yagi antenna", 205, 930});
  parts.push_back({"MOSFET", 43, 100});
  parts.push_back({"Nixie tube", 333, 900});
  parts.push_back({"DIAC", 115, 760});
  parts.push_back({"Klystron", 3, 10});
  parts.push_back({"Stepping motor", 117, 510});
  parts.push_back({"Piezoelectric crystal", 154, 820});

  fstream file;
  file.open("../inventory.inv", ios::out | ios::binary);
  file.seekp(0L);

  for (auto part : parts)
  {
    file.write(reinterpret_cast<char*>(&part), sizeof part);
  }

  file.close();
  cout << parts.size() << " records written" << endl;
  return 0;
}