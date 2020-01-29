#include<iostream>
#include<vector>

using namespace std;

void selection_sort(vector<int> &array);

int main()
{
    vector<int> array;
    selection_sort(array);
    return 0;
}

void selection_sort(vector<int> &array)
{
    //设定要选择查找的数组的大小
    size_t size = array.size();
    //开始循环查找
    for(size_t select_indx = 0; select_indx < size - 1; select_indx++)
    {
        //初始化最小值
        int smallest_value = array.at(select_indx);
        //初始化最大值
        size_t smallest_indx = select_indx;
        for (size_t compare_indx = select_indx +1; compare_indx < size; compare_indx++)
        {
            //如果比较值小于最小值则将最小值赋值为这个比较值
            if(array.at(compare_indx) < smallest_value)
            {
                smallest_value = array.at(compare_indx);
                smallest_indx = compare_indx;
            }
        } 
        //交换最小值和选择值
        swap(array.at(smallest_indx), array.at(select_indx));
    }
}