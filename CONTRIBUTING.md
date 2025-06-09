# Description of contribution

see also <https://github.com/FreeBSD-Ask/FreeBSD-Ask/wiki>please.


how to use git to pull this project

the project is too large and may result in a buffer spill and change the guit profile to achieve an expansion of the buffer zone:

THE FOLLOWING IS AN EXAMPLE OF A DOCUMENT __CODESPAN_0_ THAT IS AVAILABLE;

```
[filter "lfs"]
	required = true
	clean = git-lfs clean -- %f
	smudge = git-lfs smudge -- %f
	process = git-lfs filter-process
[user]
	name = # 你的用户名
	email = # 你的邮箱
	signingkey = # 你的密钥 ID，使用密钥签名时需要
[commit]
  gpgsign = true # 使用密钥签名时需要
[core]
	autocrlf = true
[http]
	proxy = http://localhost:7890 # 设置使用 http 代理
	postBuffer = 1048576000 # 扩大缓冲区，约 1 GB
	maxRequestBuffer = 1048576000 # 扩大缓冲区，约 1 GB
```
