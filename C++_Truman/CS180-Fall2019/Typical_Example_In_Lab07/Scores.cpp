//Program PUPOSE
//NAME

#include <fstream>
#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
  const unsigned HIGHEST_SCORE = 100;
  const unsigned LOWEST_SCORE = 0;

                                                             //打开文件
  ifstream input_file;
  input_file.open("scores.txt");
  ofstream output_file;
  output_file.open("grade_report.txt");

  //读第一个数字，也就是分数的数量
  unsigned number_of_scores;
  input_file >> number_of_scores;

  //换行
  string dummy;
  getline(input_file, dummy);

  //获取用户名字
  string name;
  while (getline(input_file, name))
  {

    unsigned score_sum = 0;
    unsigned highest_score = LOWEST_SCORE;
    unsigned lowest_score = HIGHEST_SCORE;

    //for循环用来重复一个一个读入数字
    for (unsigned loop_times = 0;loop_times < number_of_scores; loop_times++)
    {
      unsigned score;
      input_file >> score;
      //计算最大最小分数
      if(score > lowest_score)
      {
        lowest_score = score;
      }
      if (loop_times == 0)
      {
        highest_score = score;
        cout << "First Highest Score: " << highest_score << endl;
      }
      else
      {
        if (score > highest_score)
        {
          highest_score = score;
          cout << "Found A Higher Score: " << highest_score << endl;
        }
      }

      //计算总分
      score_sum += score;
    }
    //计算平均分
    double average = static_cast<double>(score_sum) / number_of_scores;

    //换行
    getline(input_file, dummy);

    //输出文件
    output_file << name << "  " << lowest_score <<"  " << highest_score <<
    "  "<<"  "<< average << endl;
  }
  //关闭文件
  input_file.close();
  output_file.close();
  return 0;
}
