#include <iostream>
#include <vector>

using namespace std;

void bubble_sort(vector<int> &array);

int main()
{
    vector<int> values_of_array;
    bubble_sort(values_of_array);
    return 0;
}

void bubble_sort(vector<int> &array)
{
    for(size_t pass_indx = array.size(); pass_indx > 0; pass_indx--)
    {
        for(size_t compare_indx = 0; compare_indx < pass_indx; compare_indx++)
        {
            if(array.at(compare_indx) > array.at(compare_indx + 1))
            {
                switch(array.at(compare_indx), array.at(compare_indx + 1));
            }
        }
    }
}