~~~
sudo apt update -y
sudo apt full-upgrade -y
sudo apt install -y ack antlr3 asciidoc autoconf automake autopoint binutils bison build-essential \
bzip2 ccache cmake cpio curl device-tree-compiler fastjar flex gawk gettext gcc-multilib g++-multilib \
git gperf haveged help2man intltool libc6-dev-i386 libelf-dev libfuse-dev libglib2.0-dev libgmp3-dev \
libltdl-dev libmpc-dev libmpfr-dev libncurses5-dev libncursesw5-dev libpython3-dev libreadline-dev \
libssl-dev libtool lrzsz mkisofs msmtp ninja-build p7zip p7zip-full patch pkgconf python2.7 python3 \
python3-pyelftools python3-setuptools qemu-utils rsync scons squashfs-tools subversion swig texinfo \
uglifyjs upx-ucl unzip vim wget xmlto xxd zlib1g-dev

pip3 install pyelftools
sudo apt-get install python3-socks python3-pip 


export ALL_PROXY=socks5://192.168.153.1:10808 && export GOPROXY=https://goproxy.io,direct && source ~/.bashrc
export ALL_PROXY=socks5://192.168.17.1:10808 && export GOPROXY=https://goproxy.cn,direct && source ~/.bashrc
~~~

```shell
docker run -itd --rm --privileged -v /dev:/dev \
    --name docker-ubuntu-lxde-novnc \
    -p 6080:80 \
    -p 5901:5900 \
    -e HTTP_PASSWORD=password \
    -e VNC_PASSWORD=password \
    -e PUID=1000 \
    -e PGID=1000 \
    -e USER=ubuntu \
    -e PASSWORD=ubuntu \
    -v ~/work:/home/ubuntu/work \
    -e RESOLUTION=1280x720 \
    -e GOPROXY=https://goproxy.cn \
    -e ALL_PROXY=socks5://192.168.153.1:10808 \
    docker-ubuntu-lxde-novnc:latest

docker run --rm --privileged -v /dev:/dev \
    --name docker-ubuntu-lxde-novnc \
    -p 6080:80 \
    -p 5901:5900 \
    -e HTTP_PASSWORD=password \
    -e VNC_PASSWORD=password \
    -e PUID=1000 \
    -e PGID=1000 \
    -e USER=ubuntu \
    -e PASSWORD=ubuntu \
    -v ~/work:/home/ubuntu/work \
    -e RESOLUTION=1280x720 \
    docker-ubuntu-lxde-novnc:latest

docker run --rm --privileged -v /dev:/dev \
    --name docker-lede \
    -p 6080:80 \
    -p 5902:5900 \
    -e HTTP_PASSWORD=password \
    -e VNC_PASSWORD=password \
    -e PUID=1000 \
    -e PGID=1000 \
    -e USER=ubuntu \
    -e PASSWORD=ubuntu \
    -v ./work:/home/ubuntu/work \
    -e RESOLUTION=1280x720 \
    docker-lede:latest

```

ubuntu扩容

```shell
sudo fdisk /dev/sda
p
d
n 
Do you want to remove the signature? [Y]es/[N]o: n 
w

sudo pvresize /dev/sda3
sudo vgdisplay   #10G根据 vgdisplay 中的free PE 的大小确定
#sudo lvextend -L +10G /dev/ubuntu-vg/ubuntu-lv
sudo lvextend -r -l +100%FREE /dev/mapper/ubuntu--vg-ubuntu--lv
sudo resize2fs /dev/ubuntu-vg/ubuntu-lv
```

```
shell
Rx:000069-
01 04 F4 00 DC 00 0A 00 1A 00 25 00 00 00 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 09 0C 00 00 00 00 00 00 09 0B 00 00 00 00 00 00 09 09 00 00 00 00 00 00 09 0A 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 FF D8 FF D8 00 1C D9 A7

```

Docker

```shell
sudo apt-get install docker docker.io
#sudo groupadd docker
sudo gpasswd -a $USER docker
newgrp docker
sudo chmod a+rw /var/run/docker.sock
```

Qemu

```shell
docker pull --platform linux/arm64 arm64v8/ubuntu
docker run --rm -t --platform linux/arm64 arm64v8/ubuntu uname -m
$USER
docker run --rm -it -v ./py-ubuntu:/home/ubuntu/py-ubuntu  --platform linux/arm arm32v7/ubuntu
```

