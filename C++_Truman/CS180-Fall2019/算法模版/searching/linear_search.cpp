#include<iostream>
#include<vector>

using namespace std;

size_t linear_search(const vector<int> &array, size_t values);

int main()
{
    vector<int> array;
    size_t values;
    linear_search(array, values);
    return 0;
}

size_t linear_search(const vector<int> &array, size_t values)
{
    size_t index = 0;
    size_t size = array.size();
    size_t position = size;
    bool found = false;

    while(!found && index < size)
    {
        if(array.at(index) == values)
        {
            found = true;
            position = index;
        }
        index++;
    }
    return position;
}