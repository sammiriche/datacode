# 更改360升级服务器地址
def alter_add(file,old_str,new_str):
    # 先打开文件，将内容保存到列表中
    with open(file,'r',encoding='utf-8') as f:
        result = f.readlines()
    # 然后以写的方式打开文件
    with open(file,'w',encoding='utf-8') as f_w:
        for i in result:
            if old_str in i:
                i = i.replace(old_str,new_str)
            f_w.write(i) 

a = 'sev=10.229.241.38:18000'
b = 'sev=xnfbd.hb.sgcc.com.cn:80'
file = 'C:\\Program Files (x86)\\360\\360Safe\\deepscan\\smart.dat'

alter_add(file,a,b)