# SlimLang
本项目主要借助antlr，学习如何自创编程语言。

## 环境
1. Java(用于运行antlr)
2. Python3(用于解析自定义代码并运行)
```
pip install antlr4-python3-runtime==4.7.1
```
注意：antlr4-python3-runtime版本必须和antlr4的版本一致，否则会有奇怪的错

## 当前进度
1. 变量定义
2. 算术运算
3. 逻辑运算
4. 条件语句
5. 循环语句
6. 打印语句

TODO:
* 函数定义
* 字符串
* 数组

## 运行
1. 生成词法分析器和语法分析器
```
cd src
./antlr -Dlanguage=Python3 Expr.g4 -no-listener -visitor
```
2. 编写自定义代码
提供了一个示例代码：input.slim
```
i = 0
sum_odd = 0
sum_even = 0

while (i < 10) {
    if (i % 2 == 0) {
        sum_even = sum_even + i
        print(sum_even)
    } else {
        sum_odd = sum_odd + i
        print(sum_odd)
    }
    i = i + 1
}

print(sum_odd)
```
3. 运行
```
slim input.slim
```

