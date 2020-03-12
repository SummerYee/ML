# -*- coding: utf-8 -*-
# @Author  : 王小易 / SummerYee
# @Time    : 2020/3/12 14:53
# @File    : 机器学习(吴恩达) 1.py
# @Software: PyCharm

#include<iostream>
using namespace  std;
int main()
{
    int n;
    cin >> n;
    while (n>=0)
        {
        for (int i = 1; i < n + 1; i++)
            {
                if (n%i == 0)
                {
                    cout << i<<"   ";
                }
            }
    cout<<endl;
    cin >> n;
        }
    system("pause");
    return 0;
}
