## How to install Hadoop in linux machine ?
    1. Go to download page of official apache hadoop(https://hadoop.apache.org/releases.html)
    2. Copy link of binary files in tar.gz format(eg: https://dlcdn.apache.org/hadoop/common/hadoop-3.4.0/hadoop-3.4.0.tar.gz)
    3. "wget link" - Use this command to download hadoop in linux machine
    4. "tar -xvzf file_name.tar.gz" - to unzip hadoop
    5. "vi ~/.bashrc" - Setup paths in bashrc. Use below template and change the path according to your system
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export PATH=$PATH:$JAVA_HOME
export HADOOP_HOME="/root/hadoop/hadoop-2.9.0"
export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib"
    6.Copy paste configurations of 4 files from my basic config files to the files in /hadoop-version/etc/hadoop/*
    7.For marped-site.xml alone you need to create the file manually as same as marped-site.xml.template then paste the content

## To start hdfs
 1. Check for port confilct using "netstat -tuln | grep 8030" replace 8030 with configured ports
 2. start-dfs.sh
 3. "jps -l " - See Namenode,Datanode & SecondaryNameNode are running

## To start yarn
1. Check for port confilct using "netstat -tuln | grep 8030" replace 8030 with configured ports
2. start-yarn.sh
3. "jps -l " - See ResourceManager & NodeManager are running
