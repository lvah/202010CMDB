from django.shortcuts import render, HttpResponse
# 导入配置文件中的信息， 扫描的网段列表、执行的命令(自动采集的主机信息)
from CMDB.settings import scanhosts, commands
# 导入扫描需要的函数
from .utils import get_active_hosts,is_ssh_up,login_ssh_passwd
# 导入数据库模型
from .models import  Server,User
# Create your views here.
# 路由-视图函数: /scanhosts/
def do_scanhosts(request):
    # 需要完成的需求3： 用户在网页上填写需要扫描的主机网段， 开始扫描。
    # 依次扫描配置文件中的所有网段/所有主机
    for net_host in scanhosts:
        # 获取该网段存活的所有主机
        active_hosts = get_active_hosts(net_host)
        # 判断主机的ssh端口是否打开，如果打开就是Linux，可以采集主机信息，否则目前无法采集。
        for host in active_hosts:
            # 如果ssh端口存活， 则代表Linux系统，可以批量执行命令采集主机信息并自动保存到数据库中。
            if is_ssh_up(host):
                # 通过ORM将将主机信息存储到数据库, 实例化对象，指定属性名
                server = Server(IP=host)
                # 需要完成的功能1： 远程执行命令，采集到主机信息(MAC, hostname...)， 存储到数据库中.
                # 等讲完面向对象的反射机制，再来写代码

                server.save() # 将服务器信息保存到数据库中
            # 如果ssh端口不存活，代表大概率不是Linux系统, 此处不能采集主机信息，则不做操作
            else:
                pass
    # 需要完成的功能2: 扫描完成后， 返回用户扫描的所有主机信息并以表格方式展现在页面中。
    return  HttpResponse("扫描完成")

