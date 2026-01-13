# 写在系统学习Linux命令前面（一些技巧和规律）

**各种命令浩如烟海，不可能全部熟练掌握再去用，常使用`man <命令>;<命令>--help`去查看手册和帮助**

- 短参数，“-”+一个字母（可以组合写，如-lrs）

  - -f

    - force

    - follow

    - file

      > `tar -cvf test.tar a.txt b.txt`

  - -n

    - number
    - no

  - -k

    - keep
    - kill

  - -o

    - output
    - option

  - -p

    - port
    - parent（父目录）
    - permission（权限）

  - -q

    - quiet

  - -s

    - silent
    - size
    - sort

  - -r

    - recursive（递归）
    - reverse（反向）

  - -v

    - version
    - verbose

  - -x

    - extract(解压)
    - execute（执行）

  - -y

    - yes

  - -z

    - compress(压缩)

  - -u

    - user
    - update

  - -h

    - help
    - human

  - -m

    - model（模式）
    - message（消息）

  - -l

    - list（列表）
    - long（详细）

  - -a

    - all(显示所有)
    - append（追加）

  - ...........

- 长参数，“--“+单词
  - **--help**
  - --version
  - --verbose(更详细输出)
  - --quiet
  - --dry-run
  - recursive
  - force
  - interactive(交互确认)
  - ..........

# 常用命令

- 帮助与自救

  - `man <命令>`
  - `命令 --help`
  - `whatis 命令`（一句话简介）
  - `which 命令`/`type 命令`（命令在哪/命令是不是别名）

- 文件与目录

  - `ls -lah`
  - `cd <目录>`
  - `pwd`
  - `mkdir -p a/b/c`
  - `touch a.txt`
  - `cp -r <源> <目标>`
  - `mv <源> <目标>`
  - `rm -i <文件>`
  - `rm -rf <目录>`
  - `ln -s <目标> <连接名>` 

- 看文件内容（排查问题）

  - `cat <file>`
  - `less <file>`(分页查看)
  - `head -n 20 <file>`(看前20行)
  - `tail -n 20 <file>`
  - `tail -f log`(实时追踪日志)

- 搜索与过滤（配合|很好用）

  - `grep -n "关键字" <file>`(搜索并显示行号)
  - `gerp -ri "关键字 <dir/>"(递归搜索目录)`
  - `find /path -name "*.log"`
  - `find . -type f -size +100M`(找大文件)

- 压缩与打包

  - `tar -czvf a.tar.gz dir/`（压缩，指定文件名为a.tar.gz）
  - `tar -xzvf a.tar.gz`(解压)
  - `zip -r a.zip dir/`(zip 打包)
  - `unzip a.zip`(解压 zip)

- 权限与用户

  - `chmod 644 file` / `chmod +x script.sh`(改权限)
  - `chown user:group file`(改属主/属组)
  - `id`(查看当前用户信息)
  - `whoami`(我是谁)
  - `sudo 命令`(提权执行)

- 进程与系统状态

  - `ps aux`(查看进程)
  - `top` / `htop`(实时资源)
  - `kill PID`(结束进程（强制：`kill -9 PID`）)
  - `free -h`(内存)
  - `df -h`(磁盘占用)
  - `du -sh *`(当前目录各项占用)
  - `uptime`(运行时间/负载)

- 网络

  - `ip a`(看网卡 IP（老系统也可能用 `ifconfig`）)
  - `ping 8.8.8.8`(连通性)
  - `curl -I https://example.com`(看响应头)
  - `wget URL`(下载)
  - `ssh user@host`(远程登录)
  - `scp a.txt user@host:/path/`(拷文件到远程)

- 管道与重定向

  - `|`：管道，把前一个输出交给后一个

    > ps aux | grep nginx

  - `>`：覆盖写入

    > echo hello > a.txt

  - `>>`：追加写入

    > echo hello >> a.txt

  - `2>`：把错误输出重定向

    > cmd 2> err.log

  - `&>`：标准输出+错误都重定向

    > cmd &> all.log

- 服务与日志

  - `systemctl status nginx`(看服务状态)
  - `systemctl start/stop/restart nginx`(启停/重启)
  - `journalctl -u nginx -e`：(看服务日志（到底部）)
  - `journalctl -u nginx -f`：(跟踪日志)

  

  

