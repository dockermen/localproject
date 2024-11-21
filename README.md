# localproject
### Setting
```shell
git config --global user.name "ChenZhilong"
git config --global user.email "qq.com"
ssh-keygen -t rsa -b 4096 -C "你的邮箱"
git init
git remote add origin https://github.com/dockermen/localproject.git

#使用http代理 
git config --global http.proxy http://127.0.0.1:10809
git config --global https.proxy https://127.0.0.1:10809
#使用socks5代理
git config --global http.proxy socks5://127.0.0.1:10808
git config --global https.proxy socks5://127.0.0.1:10808
```

撤回命令

```shell
#未暂存的修改：使用 git checkout -- <file>
#已暂存的修改：使用 git reset HEAD <file>
#最近的提交：使用 git reset --soft HEAD~1 或 git reset HEAD~1
#撤回多个提交：使用 git reset --soft HEAD~n
#通过创建反向提交撤回：使用 git revert <commit>
```

