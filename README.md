# Лабораторная работа №1  

<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Шмаков_И._С.-8b9aff" alt="Contributor Badge"></a></div>

***

Стратиенко Илья 
ИУ10-96

## Данная лабораторная работа посвещена изучению систем обмена данными. Работа позволит ознакомиться с базовыми навыками необходимыми для произведения commit changes, публикации изменний в удаленный репозиторий, обновлениями данных для них, fork и тд.


## Задание

✅ 1. Зарегистрироваться на почтовом сервисе **Gmail**. В случае наличия аккаунта - не требуется

✅ 2. Зарегистрироваться на сервисе совместной разработки **GitHub**. В случае наличия аккаунта требуется произвести дополнительные настройки и обновить данные персонификации

✅ 3. Отправить зарегистрированный адрес почтового ящика личным сообщением

✅ 4. Отправить зарегистрированный логин личным сообщением

✅ 5. Ознакомиться со ссылками учебного материала и формализованными требованиями из основного описания

✅ 6. Сгенирировать **SSH** ключ и добавть его в список ключей для сервиса **GitHub**
<img width="1868" height="911" alt="image" src="https://gist.github.com/user-attachments/assets/972db388-c90f-4d08-89a0-e51b52a0bd01" />

✅ 7. Сгенерировать Personal Token с правами gist и сохранить его в файл
<img width="1894" height="594" alt="image" src="https://gist.github.com/user-attachments/assets/97024ca8-0aa2-458d-beab-a054cf901766" />


✅8. Сгенерировать GnuPG для подтверждения подписания коммитов и возможно использование Х.509 (включить в отчет описание, что такое smimesign)

smimesign — инструмент для подписи Git-коммитов с помощью сертификатов X.509 / S/MIME, в отличие от GPG. Используется в корпоративных политиках. GitHub распознаёт такие подписи как Verified.
<img width="1868" height="911" alt="image" src="https://gist.github.com/user-attachments/assets/5b584d92-5c28-4490-9d72-e82f5eaad73d" />


✅9. Подготовить глобальные переменные окружения для GitHub
```bash
┌──(.venv)─(kali㉿kali)-[~/work/lab01]
└─$ git config --list                            
user.name=ilya
user.email=stratienko_ilya03@mail.ru
user.signingkey=982096EAB4AB4A62
init.defaultbranch=main
pull.rebase=false
core.editor=nano
color.ui=auto
credential.https://github.com.helper=
credential.https://github.com.helper=!/usr/bin/gh auth git-credential
credential.https://gist.github.com.helper=
credential.https://gist.github.com.helper=!/usr/bin/gh auth git-credential
commit.gpgsign=true
tag.gpgsign=true
gpg.program=gpg
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
remote.origin.url=git@github.com:ilya-startcode/lab01.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.main.remote=origin
branch.main.merge=refs/heads/main
```

✅10. Ознакомиться с материалами gh сервиса и использовать их для авторизации, commit, pull request и тд.

```bash
┌──(.venv)─(kali㉿kali)-[~/work/lab01]
└─$ gh auth status                               
github.com
  ✓ Logged in to github.com account ilya-startcode (keyring)
  - Active account: true
  - Git operations protocol: https
  - Token: ghp_*************************************
  - Token scopes: 'gist', 'read:org', 'repo', 'workflow'
```

✅11. Выполнить инструкцию учебного материала
✅12. Оформить README.md по аналогии и использовать shield, etc.
✅13. Составить gist отчет и отправить ссылку личным сообщением

***

Создайте локальный репозиторий на машине, проинициализируйте репозиторий
``` bash
┌──(.venv)─(kali㉿kali)-[~]
└─$ mkdir risk_lab1
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~]
└─$ cd risk_lab1 
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git init         
Initialized empty Git repository in /home/kali/risk_lab1/.git/
```
Авторизуйтесь и используйте GitHub CLI для создания удаленного репозитория
``` bash
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ gh repo create lab1 --public  
✓ Created repository ilya-startcode/lab1 on github.com
  https://github.com/ilya-startcode/lab1
```
Создайте пустой README.md
``` bash
──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ touch README.md                              
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git add README.md
```

Используйте указание URL своего созданного репозитория для присвоения ветки master статуса origin
``` bash
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git branch -M master
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git remote add origin https://github.com/ilya-startcode/lab1.git
```
В локальном репозитории и сделайте commit
Сделайте публикацию своего commit с флагом -S в удаленный репозиторий
``` bash
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git commit -S -m "Initial commit"
[master (root-commit) 4c43240] Initial commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
 
 ┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git push -u origin master                                       
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 394 bytes | 394.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To github.com:ilya-startcode/lab1.git
 * [new branch]      master -> master
branch 'master' set up to track 'origin/master'.

```
Создайте файл hello.py в локальном репозитории. Реализуйте Hello appsec world на языке python используя несколько интерпретаторов с "грязным" кодом
``` bash
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ cat hello.py          
#!/usr/bin/env python
# intentionally dirty python code
# works in: python3 / python / pypy

import sys, os

# бесполезные переменные
a = None
b = 0
c = ""

def f(x=None):
    if x is None:
        pass
    else:
        return x
    return None

# "грязная" сборка строки
msg = ""
for i in ["H","e","l","l","o"," ","a","p","p","s","e","c"," ","w","o","r","l","d"]:
    msg = msg + i

# бессмысленные операции
if b == 0:
    c = msg
else:
    c = f(msg)

try:
    raise Exception("noise")
except Exception as e:
    _ = str(e)

print(c)
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git status
On branch master
Your branch is up to date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        hello.py

nothing added to commit but untracked files present (use "git add" to track)

┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git add hello.py           
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git commit -S -m "hello.py dirty version"
[master 6eca995] hello.py dirty version
 1 file changed, 35 insertions(+)
 create mode 100755 hello.py

```

Измените исходный код, что бы скрипт запрашивал имя пользователя и выводил Hello appsec world from @name
``` bash
                                                    
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ cat hello.py          
#!/usr/bin/env python
# dirty python hello appsec world
# works in python3 / python / pypy

import sys, os

# бесполезные переменные
x = None
y = 1
z = ""

def useless(a=None):
    if a:
        return a
    return None

# запрос имени (грязно)
try:
    name = input("Enter your name: ")
except Exception:
    name = "anonymous"

if name is None or name == "":
    name = "anonymous"

# грязная сборка строки
parts = [
    "H","e","l","l","o"," ",
    "a","p","p","s","e","c"," ",
    "w","o","r","l","d"," ",
    "f","r","o","m"," ",
    "@", name
]

msg = ""
for p in parts:
    msg = msg + str(p)

# бессмысленная логика
if y == 1:
    z = msg
else:
    z = useless(msg)

try:
    raise RuntimeError("noise")
except RuntimeError:
    pass

print(z)
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git add hello.py                         
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git commit -S -m "Improve hello.py - add username input"
[master d5007e2] Improve hello.py - add username input
 1 file changed, 37 insertions(+), 22 deletions(-)
```
Сделайте commit с флагом -S и сделайте публикацию в удаленный репозиторий. Проверьте вывод истории изменений
В локальном репозитории создайте ветку patch1 и внесите изменения исправлению кода и модернизации до следующего вида, что бы код был рабочим. Сделайте публикацию своего commit с флагом -S в удаленный репозиторий:
``` bash
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git checkout -b patch1

Switched to a new branch 'patch1'
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git branch

  master
* patch1
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ cat > hello.py <<'EOF'
#!/usr/bin/env python3
"""
Hello AppSec World
Secure and clean version
"""

def main() -> None:
    try:
        name = input("Enter your name: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nInput interrupted.")
        return

    if not name:
        name = "anonymous"

    print(f"Hello appsec world from @{name}")


if __name__ == "__main__":
    main()
EOF

                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ ./hello.py 
Enter your name: ilya
Hello appsec world from @ilya
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git add hello.py 
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git push -u origin patch1
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 10 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 1.70 KiB | 1.70 MiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: 
remote: Create a pull request for 'patch1' on GitHub by visiting:
remote:      https://github.com/ilya-startcode/lab1/pull/new/patch1
remote: 
To github.com:ilya-startcode/lab1.git
 * [new branch]      patch1 -> patch1
branch 'patch1' set up to track 'origin/patch1'.
```
Доработайте материалы и также опишите их в отчете:

Проверьте, что ветка patch1 в удалённом репозитории
Создайте pull-request в виде patch1 -> master
В ветке patch1 добавьте в исходный код комментарии и убедитесь, что есть указанные изменения в pull-request
В удалённый репозитории выполните слияние pull-request для patch1 -> master и удалите ветку patch1
Стяните последние актуальные изменения и просмотрите историю изменений для master
Удалите локальную ветку patch1
``` bash
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ gh pr create --base master --head patch1

Creating pull request for patch1 into master in ilya-startcode/lab1

? Title (required) patch1
? Body <Received>
? What's next? Submit
https://github.com/ilya-startcode/lab1/pull/1
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ gh pr merge 1 --merge
✓ Merged pull request ilya-startcode/lab1#1 (patch1)
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git push origin --delete patch1
To github.com:ilya-startcode/lab1.git
 - [deleted]         patch1
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git checkout master
M       hello.py
Switched to branch 'master'
Your branch is ahead of 'origin/master' by 2 commits.
  (use "git push" to publish your local commits)
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git pull
remote: Enumerating objects: 1, done.
remote: Counting objects: 100% (1/1), done.
remote: Total 1 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (1/1), 891 bytes | 891.00 KiB/s, done.
From github.com:ilya-startcode/lab1
   4c43240..df99b75  master     -> origin/master
Updating d5007e2..df99b75
Fast-forward
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git log --decorate --oneline -n 3
df99b75 (HEAD -> master, origin/master, origin/HEAD) Merge pull request #1 from ilya-startcode/patch1
d5007e2 (patch1) Improve hello.py - add username input
6eca995 hello.py dirty version
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git branch -d patch1
Deleted branch patch1 (was d5007e2).
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git branch          
* master
```

Создайте новую локальную ветку patch2.
Измените code style по своему усмотрению
Сделайте публикацию своего commit с флагом -S в удаленный репозиторий и создайте pull-request patch2 -> master

``` bash 
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git checkout -b patch2
Switched to a new branch 'patch2'
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git branch            
  master
* patch2
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ cat > hello.py <<'EOF'
#!/usr/bin/env python3
"""Hello AppSec World (patch2 style)."""

PROMPT = "Enter your name: "
DEFAULT_NAME = "anonymous"


def format_greeting(name: str) -> str:
    name = (name or "").strip() or DEFAULT_NAME
    return f"Hello appsec world from @{name}"


def read_name() -> str:
    try:
        return input(PROMPT)
    except (EOFError, KeyboardInterrupt):
        return ""


def main() -> None:
    print(format_greeting(read_name()))


if __name__ == "__main__":
    main()
EOF

                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git add hello.py 
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git commit -S -m "patch2: restyle hello.py"
[patch2 63ef7d1] patch2: restyle hello.py
 1 file changed, 25 insertions(+), 50 deletions(-)
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git push -u origin patch2
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 10 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 766 bytes | 766.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: 
remote: Create a pull request for 'patch2' on GitHub by visiting:
remote:      https://github.com/ilya-startcode/lab1/pull/new/patch2
remote: 
To github.com:ilya-startcode/lab1.git
 * [new branch]      patch2 -> patch2
branch 'patch2' set up to track 'origin/patch2'.
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ gh pr create --base master --head patch2

Creating pull request for patch2 into master in ilya-startcode/lab1

? Title (required) patch2
? Body <Received>
? What's next? Submit
https://github.com/ilya-startcode/lab1/pull/2
```
В ветке master удаленного репозитория явно измените комментарий
Увидите, что в pull-request появились расхождения
Локально сделайте rebase и исправьте расхождения (это называется конфликт)
``` bash                                                                     
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git fetch origin      

remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 1.03 KiB | 1.03 MiB/s, done.
From github.com:ilya-startcode/lab1
   df99b75..f549c4b  master     -> origin/master
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git log --oneline --decorate -5 origin/master

f549c4b (origin/master, origin/HEAD) Add comment in Russian for conflict demonstration
df99b75 (master) Merge pull request #1 from ilya-startcode/patch1
d5007e2 Improve hello.py - add username input
6eca995 hello.py dirty version
4c43240 Initial commit
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git checkout patch2
git rebase origin/master

Already on 'patch2'
Your branch is up to date with 'origin/patch2'.
Auto-merging hello.py
CONFLICT (content): Merge conflict in hello.py
error: could not apply 63ef7d1... patch2: restyle hello.py
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
hint: Disable this message with "git config set advice.mergeConflict false"
Could not apply 63ef7d1... # patch2: restyle hello.py
```
Сделайте commit и опубликуйте изменения в ветке patch2
Убедитесь, что пропали конфликтны.
``` bash
                                                                     
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git rebase --continue 
[detached HEAD 509e7ad] patch2: restyle hello.py
 1 file changed, 26 insertions(+), 48 deletions(-)
Successfully rebased and updated refs/heads/patch2.
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ git push -f          
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 10 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 806 bytes | 806.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To github.com:ilya-startcode/lab1.git
 + 63ef7d1...509e7ad patch2 -> patch2 (forced update)
```                                                      
Сделайте merge для pull-request patch2 -> master.
``` bash                                                                     
┌──(.venv)─(kali㉿kali)-[~/risk_lab1]
└─$ gh pr merge 2 --merge                                                                                
✓ Merged pull request ilya-startcode/lab1#2 (patch2)
```
Подготовьте отчет gist.
Продемонстрируйте в материалах отчета историю коммитов на локальном и удаленном репозитории.
Stratienko Ilya

