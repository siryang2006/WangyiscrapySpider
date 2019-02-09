#pip install bs4 
pip install xpath

sudo yum install -y vim wget
#下载jdk：
wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.rpm

#安装jdk：
sudo rpm -ivh jdk-8u131-linux-x64.rpm

#打开配置：
sudo vim /etc/profile
最后添加：
JAVA_HOME=/usr/java/jdk1.8.0_131
CLASSPATH=%JAVA_HOME%/lib:%JAVA_HOME%/jre/lib
PATH=$PATH:$JAVA_HOME/bin:$JAVA_HOME/jre/bin
export PATH CLASSPATH JAVA_HOME

#重新载入：
source /etc/profile

#是否安装成功：
java -version

# 获取rpm包
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.1.0.rpm
 
 # 安装
rpm -ivh elasticsearch-6.1.0.rpm
 
 # 启动
systemctl start elasticsearch

# 查看状态
systemctl status elasticsearch

 # 设置开机启动
systemctl enable elasticsearch

#开启9200端口
firewall-cmd --add-port=9200/tcp --permanent
firewall-cmd --reload


# 安装net-tools 
yum install -y net-tools

 # 检查9200是否有监听
netstat -antp |grep 9200

curl http://127.0.0.1:9200

#yum安装kibana
 # 获取安装包
wget https://artifacts.elastic.co/downloads/kibana/kibana-6.1.0-x86_64.rpm
 
 # 安装
sudo rpm -ivh kibana-6.1.0-x86_64.rpm

git clone https://github.com/anbai-inc/Kibana_Hanization.git
cd Kibana_Hanization/
sudo python ./main.py /usr/share/kibana


# 启动 
sudo systemctl start kibana

 # 查看状态 
sudo systemctl status kibana

 # 设置开机启动 
sudo systemctl enable kibana

# 设置防火墙 
sudo firewall-cmd --add-port=5601/tcp --permanent
sudo firewall-cmd --reload

#redis
#redis官网地址：http://www.redis.io/
#    最新版本：2.8.3
#    在Linux下安装Redis非常简单，具体步骤如下（官网有说明）：#
#     1、下载源码，解压缩后编译源码。#
$ wget http://download.redis.io/releases/redis-2.8.3.tar.gz#
$ tar xzf redis-2.8.3.tar.gz#
$ cd redis-2.8.3
$ make

#2、编译完成后，在Src目录下，有四个可执行文件redis-server、redis-benchmark、redis-cli和redis.conf。然后拷贝到一个目录下。

mkdir /usr/redis
cd ./src
cp redis-server /usr/redis
cp redis-benchmark /usr/redis
cp redis-cli /usr/redis
cd ..
cp redis.conf /usr/redis
cd /usr/redis

#3、启动Redis服务。
$ redis-server redis.conf
#4、然后用客户端测试一下是否启动成功。

$ redis-cli

redis> set foo bar

OK

redis> get foo

"bar"