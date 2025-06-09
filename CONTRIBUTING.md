# Description of contribution

See also <https://github.com/FreeBSD-Ask/FreeBSD-Ask/wiki>please.


How to use git to pull this project

The project is too large and may result in a buffer spill and change the guit profile to achieve an expansion of the buffer zone:

The following is an example of a document available `.gitconfig ' ;

````
[filter "lfs" ]
= true
clean =get-lfs clean-%f
smudge =get-lfs smudge-%f
Process =get-lfs filler-process
[user]
Name = # Your username
# Your mailbox
Signingkey = # Your key ID, required for key signature
[commit]
gpgsign = true# needs when signing with key
[core]
= true
[http]
Proxy = http://localhost:7890# Settings with http proxy
PostBuffer = 1048576000
maxRequestBuffer = 1048576000
````
