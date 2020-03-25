python 学习记录
	安装包就是解释器。默认是cpython,vscode这些就是编译器，IDE等
	1 安装python 3.8.1 官网对应安装windows版本。安装过程一定注意勾选环境变量。
	2 安装完成 在cmd运行python看是否可以正常运行  出现（>>>）并且测试pip list是否成功
	3 安装第三方包，直接在cmd分别运行pip install flake8  pip install yapf (联网状态自动下载安装)
	4 安装VScode 安装完成首先打开extension  插件管理 分别安装chinese语言包和python
	5 基本安装配置已经完成。创建本地文件夹。并且新建py文件测试看下是否可以调试
	6 按照提示安装扩展包  在设置-用户设置里找到 python.autoComplete.addBrackets 启用
	  这样自动补全会补全括号 （默认自动补全只补全单词项）

	  注意新版jason需要在右上角图标那里找到
	  研究launch.json  setting.json区别

	7 vscode 报错信息
		IndentationError: unindent does not match any outer indentation level  一般是前后空格缩进问题

	8 python知识点
		for......else......的执行顺序为：

		当迭代对象完成所有迭代后且此时的迭代对象为空时，如果存在else子句则执行else子句，没有则继续执行后续代码；
		如果迭代对象因为某种原因（如带有break关键字）提前退出迭代，则else子句不会被执行，程序将会直接跳过else子句继续执行后续代码

		1.break:跳出循环,不再执行Python break语句,就像在C语言中,打破了最小封闭for或while循环。 break语句用来终止循环语句,即循环条件没有False条件或者序列还没被完全递归完,也会...
		2.continue:跳出本次循环,执行下一次Python continue 语句跳出本次循环,而break跳出整个循环。 continue 语句用来告诉Python跳过当前循环的剩余语句,然后继续进行下一轮循环...
		3 return 退出最近的一个def
		4 面向对象，只要有init函数（写了这句）那么在实际生成类的对象时会首先自动调用该函数，而不需要手动运行该函数。self传递的是对象本身！
		  分清楚实例属性，形参，实参区别  
		5  分清属性和函数   __init__()函数  __dict__  就是属性，不带括号 一定注意
		6    文件操作。单独文件名的话保存路径是固定的 和当前py无关。好像跟工作目录相关