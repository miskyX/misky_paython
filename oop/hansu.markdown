#函数
## 定义函数与调用函数
## 函数的参数
  - 实参与形参：形参是个变量（代表），实参是值
  - 形参是在定义函数的时候括号里面的变量
  - 实参是实在调用函数的时候括号里面的值（或变量）
  - 传递参数的三种方法：①位置排序；②关键字说明；③默认值
    - 函数举例：
      def display(name,age,sex="girl"):
    - 位置实参； display("sky",18)
    - 关键字实参；display(name = "sky",age = 18)
    - 默认值(默认值形参一般放在最后面)，如果后面不定义实参值，那么默认使用默认值
## 返回值(return语句)
  - return语句返回一个或一组值，统称为返回值（加工后的生成值）
  - 调用返回值时，需要提供一个变量，来用于存储返回值
  -  让形参变得可选，默认为空，用if语句画出两条路径，核心概念是 非空为ture,如： if middle_name:代表如果有中间名，则
  - 能返回的内容很多，如简单值，字典等
## 传递列表
  - 传递列表的意义：函数选用实参值时直接从列表里面访问取值
  - 传递任意数量的实参：用*号作为通配符+形参名称，如def make_names(*yanse) ,就可以传入任意多种颜色值，空元组
## 函数与模块
  - 过程：将函数存在独立的文件中（模块），使用的时候用import语句将模块导入到主程序中，实现函数的调用，或运行模块中的代码。
  - 创建模块，模块的拓展名为.py文件,模块（module)
### 调用模块的方法
  - 导入整个模块：可以使用这个模块中的所有函数
    - ①导入：import 模块名，②调用：模块名.函数名
          module_name.function_name
  - 导入特定函数：
    - 方法：①from 模块名 import 函数名
           from module_name import function_name
           ②用逗号分隔函数名，可以调用导入多个函数
           from module_name import function_0,function_1,function_2
  - 用as给函数或模块指定别名
    - 意义：避免与当前程序中的名称冲突，或者函数名称太长，为了精简
    - 给函数指定别名：form module_name import function_name as new_function_name
    - 给模块指定别名: import module_name as new_module_name
    - 
                