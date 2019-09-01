import paramiko
client = paramiko.SSHClient()
private_key = paramiko.RSAKey.from_private_key_file('D:/ssh/usEast01-sshkey-devuser.pem')
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  #必须加，否则报错找不到主机
client.connect(hostname='54.204.52.128',username='devuser',pkey= private_key )
stdin, stdout, stderr = client.exec_command('pwd')
print(stdout.readline())
client.close()

import paramiko

transport = paramiko.Transport(('hostname', 22))
transport.connect(username='zhangqigao', password='123')

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('/tmp/location.py', '/tmp/test.py')
# 将remove_path 下载到本地 local_path
sftp.get('remove_path', 'local_path')

transport.close()