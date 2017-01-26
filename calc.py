#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GPA CALCULATOR

for students in Southeast University
"""
import math

def is_number(s_test):
    """
    check if the string is number
    """
    try:
        float(s_test)
        return True
    except ValueError:
        return False

def get_grades_int(data):
    """
    return int grades
    """
    if data == 100:
        return 4.8
    elif data >= 60:
        ten = math.floor(data / 10)
        bit = data % 10
        m_ten = ten - 5.0
        if bit < 3:
            m_bit = 0.0
        elif bit < 6:
            m_bit = 5.0
        else:
            m_bit = 8.0
        result = m_ten + m_bit / 10.0
        formatted_result = float('%0.1f'%result)
        return formatted_result
    else:
        return 0.0

def get_grades_string(data):
    """
    return string grades
    """
    if data == "优":
        grades = 4.5
    elif data == "良":
        grades = 3.5
    elif data == "中":
        grades = 2.5
    elif data == "及格":
        grades = 1.5
    else:
        grades = 0.0
    return grades

def get_grades(data):
    """
    return the grades
    """
    if is_number(data):
        grades = get_grades_int(int(data))
    else:
        grades = get_grades_string(data)
    print('单项绩点:', grades)
    return grades


def process(datas):
    """
    process the data and calculate the result
    """
    credit = 0.0
    grades = 0.0
    for data in datas:
        if data.get('opt') == 'Normal':
            this_credit = float(data.get('credit'))
            this_grade = float('%0.1f'%(get_grades(data.get('score')) * this_credit))
            credit += this_credit
            grades += this_grade
    grades = float('%0.3f'%grades)
    print("总绩点:", grades, "总学分:", credit)
    return grades / credit

def main():
    """
    define main function
    """
    print('======================\n===== 绩点计算器 =====\n====（东南大学用）====\n======================')
    # store all data
    data_set = []
    with open('data.csv', 'r') as grade_file:
        # open the data file
        for line in grade_file:
            item = line.split(",")
            if len(item) == 7:
                item.append("Normal")
            data_set.append({
                'num': item[0],
                'year': item[1],
                'code': item[2],
                'name': item[3],
                'credit': item[4],
                'score': item[5],
                'type': item[6],
                'opt': item[7]
            })
    result = float('%0.3f'%process(data_set))
    print("The result is ", result)

if __name__ == "__main__":
    main()
