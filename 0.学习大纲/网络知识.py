
【经验之谈】这里所说的数据帧“收”是指交换机端口接收从对端设备发来的数据帧，
而不是接收从交换机内部的另一个端口发来的数据帧，
因为在交换机内部中传输的数据帧都是带有VLAN标签的,
无论是从哪种交换机端口发来的数据帧。
三层是IP 协议，不看mac地址和vlan标签了
三台三层互联 注意stp问题
单区域 OSPF 组网
    咸安业务 192.168.1.128/25 vlan 100
            192.168.1.128/25 vlan 110
    机关业务 192.168.2.0/24 vlan 200
    通山业务 192.168.3.0/24 vlan 300

交换机管理地址
    咸安接入 100.100.1.1/24 
    机关接入 100.100.2.1/24
    通山接入 100.100.3.1/24

    loopback 地址
    咸安汇聚 1.1.1.1 32
    机关汇聚 2.2.2.2 32
    通山汇聚 3.3.3.3 32


接入层交换机配置
    给指定端口打vlan，给上联口打trunk，并且允许通过指定vlan
    int etherenet 0/0/21
    port link-type access
    port default vlan 100

    int e0/0/11 #  上联口
    port link-type trunk
    port trunk allow-pass vlan all

    配置静态路由，默认所有ip访问 下一跳

汇聚层交换机配置
    配置vlan，充当网关
    vlan 100
    int vlan 100
    ip add 192.168.1.254 24

    int g0/0/11
    port link-type trunk
    port trunk allow-pass vlan all

    5700三层口不够。给相邻两个5700的二层接口配置同一个vlan。然后vlan设置ip通信
    interface Vlanif12
    ip address 200.200.200.1 255.255.255.252
    int g0/0/1 # 三层之间互联口
    port link-type access
    port default vlan 12

    配置loopback地址。为OSPF做准备
    int loopback 0 # 创建loopback
    ip add 1.1.1.1 32 跨了三层不考虑网段？

开始配置 OSPF
    ospf 1 route-id *
    area 0
    然后发布路由，相当于发布所有接口
    两边都要配置。所有对接的接口两边都要配置
    配置完成可能需要reset ospf process
