"""
1.0
争取在3月6号前完成
个人信息，包含姓名，工作部门，IP，MAC，
信息查询，练习正则匹配
增删查改（其中新增在get，set等添加if语句）
拓展，通过excel保存，修改，导入导出个人信息台帐
掌握练习开放小项目的逻辑思维过程
总体流程 建类，类里建立需要实现功能的函数 然后在run函数里统一调用。!!! 最后的综合面板建类。相当于封装了。run方法在其中

2.0
涉及到的知识
面向对象的概念，类的静态方法 
import导入用法
正则表达式 检查输入匹配问题
os.path模块判断文件是否存在和是否为空
pickle模块序列化和反序列化功能的使用
文件打开和关闭必须配对操作。后面修改版使用with open 试试
文件导入和导出成excel格式的问题

3.0在数据库和GUI之前最后一个版本，主要是复习语法和逻辑
实时保存修改信息，不用单独去一个子列

4.0 验证配合mysql的使用，常用语法和参数传递
验证修饰器的用法？通用型
数据库的连接与关闭封装成函数还没解决？
数据库异常和回滚的操作
添加从表格导入导出功能


5.0 删除员工类功能（用作装饰器练习使用）
尝试封装数据库连接与关闭成函数，方便调用。
测试异常的语法和理解
固定路径导入导出表格。（复习语法使用）

6.0
理解函数与类的区别。将数据操作封装成类看看.部分语句逻辑可能性
开始建两张表。数据库操作和用户管理分别建立类 /csdn枫奇教程
命名规则的统一问题
__enter__方法什么作用？
理解import语句的执行。将数据库初始化放在类外面.这样只会执行一次
当然还是要判断是否存在。
更新学习记录
"""

# 问题：
# 1 输出 超过8个字符后，制表符控制无法对齐 输出对齐问题
# 2 编辑信息后，如果直接显示信息不完整，尝试通过列表拼接
# 3 改为使用 with open() 方式忘记关闭
# 4 search功能的实现
# 5 考虑将正则判断单独建类还是加到员工类里去加判断呢？
# 6 输入mac的各种格式统一显示问题 添加函数转换mac格式
# 7 表格导入导出操作涉及同步问题 合并表格类。只采用表格保存数据。否则还会出现数据重复问题
# 8 表格的单独导入导出修改成保存信息模块，在构造方法调用。研究单独使用添加文件对话框方式导入第三方表格
# 9 批量删除，可以研究下
