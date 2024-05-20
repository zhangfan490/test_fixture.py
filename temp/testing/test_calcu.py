#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time :  15:48
# @Python -version:3.8.6
# @Author coco
# @File : test_calcu.py
'''
补全计算器中加法和除法的测试用例
使用参数化完成测试用例的自动生成
在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
注意：

使用等价类，边界值，因果图等设计测试用例
测试用例中添加断言，验证结果
灵活使用 setup(), teardown() , setup_class(), teardown_class()
'''
import pytest
import yaml

from temp.python_code.calcu import Calculator


with open("./datas/calcu.yaml",encoding='utf-8') as f:
    #取yaml文件中add的所有数据
    datas = yaml.safe_load(f)
    datas_add = datas['add']
    add_datas = datas_add['datas']
    add_ids = datas_add['myid']
    datas_div = datas['div']
    div_datas = datas_div['datas']
    div_ids = datas_div['myid']


class TestCalc:

    #定义类级别setup
    def setup_class(self):
        print("开始计算")
        #实例化计算器；实例变量需要加 self.
        self.calc = Calculator()

    # 定义类级别teardown
    def teardown_class(self):
        print("结束计算")

#参数化,使用ids 对测试用例进行命名
    @pytest.mark.parametrize(
        "a,b,expect",
        add_datas,ids=add_ids
    )

    #定义加法测试用例
    def test_add1(self, a, b,expect):
        # 实例化计算器类
        # calc = Calculator()
        # 调用 add 方法
        result = self.calc.add(a, b)
        #判断结果是为小数，保留取2位小数结果
        if isinstance(result,float):
            result = round(result,2)
        # 得到结果后写断言
        assert result == expect

#参数化,使用ids 对测试用例进行命名
    @pytest.mark.parametrize(
        "a,b,expect",
        div_datas,ids=div_ids
    )

    #定义除法测试用例
    def test_div1(self, a, b,expect):
        # 实例化计算器类
        # calc = Calculator()
        # 调用 div 方法
        result = self.calc.div(a, b)
        #判断结果是为小数，保留取2位小数结果
        if isinstance(result,float):
            result = round(result,2)
        # 得到结果后写断言
        assert result == expect

