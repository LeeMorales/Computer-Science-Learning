#include <iostream>
#include <vector>

using namespace std;

size_t binary_search(const vector<int> &array, size_t values);

int main()
{
    vector<int> array;
    size_t values;
    binary_search(array, values);
    return 0;
}

size_t binary_search(const vector<int> &array, size_t values)
{
    size_t first = 0;
    size_t last = array.size() - 1;
    size_t size = array.size();
    size_t position = size;
    bool found = false;

    while(!found && first < last && last < array.size())
    {
        size_t middle = (first + last) / 2;
        if(array.at(middle) == values)
        {
            found = true;
            position = middle;
        }
        else if(array.at(middle) > values)
        {
            last = middle - 1;
        }
        else
        {
            first = middle + 1;
        }    
    }
    return position;
}