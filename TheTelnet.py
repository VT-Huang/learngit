import telnetlib
import time
def do_telnet(host, username, password, command):
    '''''Telnet远程登录：Windows客户端连接Linux服务器'''
    try:


        # 连接Telnet服务器
        tn = telnetlib.Telnet(host.encode('ascii'), port=23, timeout=10)
        tn.set_debuglevel(2)

        # 输入登录用户名
        tn.read_until(b'Username: ')
        tn.write(username.encode('ascii') + b"\n")

        # 输入登录密码
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b"\n")

        tn.write(command.encode('ascii')+b'\n')

        tn.write(b'\r\n')

        tn.write(b'\exit\n')

        line = tn.read_all().decode('ascii')
        t = './'+time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))+'.txt'
        try:
            f = open(t,'a')
            f.write(line)
            f.close()
        except OSError as reason:
            print('输出错误:'+str(reason))
    except:
        print ("连接失败！")
        return

if __name__=='__main__':
     # 配置选项
    Host = '150.242.58.33' # Telnet服务器IP
    username = '999group'   # 登录用户名
    password = '999999999'  # 登录密码
    command = 'show run'

    do_telnet(Host, username, password, command)