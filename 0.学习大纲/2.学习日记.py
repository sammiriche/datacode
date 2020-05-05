    python篇
        1 语法基础，疑难复习（菜鸟教程）
            day 0224 学习到运算符
            注意循环语句 break continue return  区别，比如在递归函数
            准备看p38小甲鱼

        2 简单的算法练习
        3 pyqt5学习
            PyQt5从入门到项目实战 1-8
        4 github安装注册使用
    网络知识篇
        开刷华为IP基础快速入门
        ensp模拟器使用
    LINUX，DOCKER篇
        linux基础入门
        docker命令熟悉
        离线源搭建
        离线仓库搭建
    系统封装和电脑知识
        解决win10无法关机问题，封装新版win10
        了解10代英特尔和3系AMD变动

    github 常用篇
        git push origin master 推送到远程仓库
        git pull origin master 从远程仓库拉取
        git reset --hard 放弃本地修改。方便下一步直接拉取远程仓库不报错

    anaconda 
        直接安装anaconda 安装完成使用navigator 配置虚拟环境，
        然后再vscode 设置python.venv 添加虚拟环境路径。此时运行相关py文件可能会提示缺少包。
        虚拟环境和工程文件路径好像没有关系
        以后可以在状态栏直接单击环境进行切换
        在虚拟环境安装pyqt5
        先激活虚拟环境
        activate first_dir
        升级pip（激活环境后升级对应环境pip）
        最好是切换到虚拟环境目录使用cmd。再使用升级命令
        最后安装（可能需要加--user）
        pip  install --user  PyQt5 -i https://pypi.douban.com/simple
        安装完成可能提示pyqt5.sip模块找不到。
        进入虚拟环境  activate 名称 进入之后前缀有虚拟环境名称，此时pip就只会在虚拟环境运行
        退出 deactivate 
        在对应的虚拟环境运行pip list 可以对比安装包的不同
        针对PYQT5  需要先安装pyqt5-sip  再安装pyqt5-tools 不然会报错

        对应环境下运行pip freeze > requirement.txt 可以生成包列表
        切到另外一个环境 pip install -r requirement.txt  可以完整的复制包列表。包括版本
        
