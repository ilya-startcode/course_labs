<div align="center">
<h1><a id="intro">Лабораторная работа №2</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Стратиенко_И._С.-8b9aff" alt="Contributor Badge"></a></div>

***

Данная лабораторная работа посвещена изучению *nix машин и как они работают, позволяет приобрести навыки для работы с терминалом/ консолью и приобрести знания по работе ОС. В лабоработрной работе описываются материалы по командам, скриптам и подключаемым приложениям.

***

## Задание

- ✔ 1. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ who | wc -I
$ id
$ whoami
$ hostnamectl
```

- ✔ 2. Выведите утилитой `tree` список вложенности дерева диреторий для каталога своего пользователя. Далее используйте `ls -a` и укажите отличие от `ls -l`.
- ✔ 3. Используйте утилиту `file` и `df` для определения какая файловая система на разделе `/dev/sda1`.
- ✔ 4. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ which vi
$ locate hello.py
$ sudo updatedb
$ locate hello
$ touch screen
$ find ~ -name screen
$ locate screen
$ sudo updated
$ locate screen
```

- ✔ 5. Используйте конструкцию и вставьте ее в созданный файл ранее. Подключите `pygame` - используем исключительно для стилизации окна.

```py
import pygame
pygame.init()

# Устанавливаем размеры окна
screen_width = 800
screen_height = 600
window_size = (screen_width, screen_height)
pygame.display.set_mode(window_size) # Создаем окно

# Задаем цвет фона
bg_color = (255, 255, 255)
pygame.draw.rect(screen, bg_color, [0, 0, screen_width, screen_height], 1)

# Выводим текст на экран
font = pygame.font.SysFont(None, 75)
text = font.render("Hello appsec world*", True, (0, 255, 0))
text_rect = text.get_rect()
text_rect.center = (400, 300)
screen.blit(text, text_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
pygame.display.flip() # Обновляем экран
```

- ✔ 6. Сделайте `commit` и `push` в свой репозиторий с изменениями в `master branch`. На следующих лабораторных работах мы вернемся к этому файлу.
- ✔ 7. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ groups
$ useradd smallman
$ userdel smallman -rf
$ useradd smallman
$ passwd smallman
$ usermod smallman -c 'Hach Hachov Hacherovich,239,45-67,499-239-45-33'
$ passwd smallman
$ id smallman
$ groupadd -g 1500 readgroup
$ usermod -aG readgroup smallman
$ chmod 666 screen 
```


- ✔ 8. Выведите группу прав для `screen` и измените, что бы файл был доступен только для чтения созданному пользователю и выведите права этого польователя для измененного файла только используя `readgroup`.
- ✔ 9. Используйте `POSIX ACL`. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ touch nmapres.txt
$ setfacl -m u:smallman:rw nmapres.txt
$ setfacl -m g:readgroup:r nmapres.txt
$ getfacl nmapres.txt
```

- ✔ 10. Сохраните файл внутри локального репозитория, так как следующая работа будет подразумевать запись в нее данных о nmap.
- ✔ 11. Для закрепления выведите все списки групп пользователей на вашей ОС и права на верхнеуровневые каталоги.
- ✔ 12. Выведите все права для файлов и директорий локального репозитория которые имеют различные пользователи  (без использования длинных путей)
- ✔ 13. Выведите процессы которые у вас запущены в термине и вне его.
- ✔ 14. Оформить `README.md` по аналогии и использовать `shield`, etc.
- ✔ 15. Составить `gist` отчет и отправить ссылку личным сообщением

## Выполнение задания

- ✔ 1. Выведите на терминале и проанализируйте следующие команды консоли

```bash
──(.venv)─(kali㉿kali)-[~/work/lab02]
└─$ who | wc -l
id
whoami
hostnamectl

1
uid=1000(kali) gid=134(docker) groups=134(docker),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),100(users),101(netdev),103(scanner),107(bluetooth),120(lpadmin),129(wireshark),130(kaboxer),1000(kali)
kali
 Static hostname: kali
       Icon name: computer-vm
         Chassis: vm 🖴
      Machine ID: b69758c0cad3481e967dcad827001d56
         Boot ID: 2161359842364db88a7fe629ea0dc89f
  Virtualization: oracle
Operating System: Kali GNU/Linux Rolling          
          Kernel: Linux 6.17.10+kali-amd64
    Architecture: x86-64
 Hardware Vendor: innotek GmbH
  Hardware Model: VirtualBox
Hardware Version: 1.2
Firmware Version: VirtualBox
   Firmware Date: Fri 2006-12-01
    Firmware Age: 19y 1month 1w 6d 
```

- ✔ 2. Выведите утилитой `tree` список вложенности дерева диреторий для каталога своего пользователя. Далее используйте `ls -a` и укажите отличие от `ls -l`.
```bash
┌──(.venv)─(kali㉿kali)-[~/work/lab02]
└─$ tree ~ -L 2
ls -a ~
ls -l ~

/home/kali
├── Desktop
│   ├── brute
│   ├── datasets
│   ├── hadoop-3.3.6.tar.gz
│   ├── lab02-out
│   ├── parallel_cpp
│   ├── parallel_cpp.tar.gz
│   ├── parallel_docker_hadoop_spark
│   ├── parallel_docker_hive_flink
│   ├── parallel_docker_mpi
│   ├── parallel_exam_96
│   ├── parallel_hadoop
│   ├── parallel_hive_flink
│   ├── parallel_openmp
│   ├── parallel_spark
│   ├── realhuman_phill.txt
│   └── start hdfs
├── Documents
├── Downloads
│   ├── brute.zip
│   ├── datasets.zip
│   ├── grgbbgbtbt.txt
│   ├── ереара(1).txt
│   ├── ереара(2).txt
│   ├── ереара(3).txt
│   ├── ереара(4).txt
│   ├── ереара(5).txt
│   └── ереара.txt
├── hadoop
│   ├── bin
│   ├── etc
│   ├── include
│   ├── lib
│   ├── libexec
│   ├── LICENSE-binary
│   ├── licenses-binary
│   ├── LICENSE.txt
│   ├── NOTICE-binary
│   ├── NOTICE.txt
│   ├── README.txt
│   ├── sbin
│   └── share
├── Music
├── Pictures
├── Public
├── secrets
│   └── gist_pat.txt
├── Templates
├── Videos
└── work
    ├── course_labs
    ├── lab01
    └── lab02

34 directories, 20 files
.                 .profile
..                Public
.bash_logout      secrets
.bashrc           .ssh
.bashrc.original  .sudo_as_admin_successful
.cache            Templates
.config           .vboxclient-clipboard-tty7-control.pid
.dbus             .vboxclient-clipboard-tty7-service.pid
Desktop           .vboxclient-display-svga-x11-tty7-control.pid
.dmrc             .vboxclient-draganddrop-tty7-control.pid
Documents         .vboxclient-draganddrop-tty7-service.pid
Downloads         .vboxclient-hostversion-tty7-control.pid
.face             .vboxclient-seamless-tty7-control.pid
.face.icon        .vboxclient-vmsvga-session-tty7-control.pid
.gitconfig        Videos
.gnupg            .viminfo
.gvfs             work
hadoop            .Xauthority
.ICEauthority     .xsession-errors
.java             .xsession-errors.old
.local            .zprofile
.mozilla          .zsh_history
Music             .zshrc
Pictures
total 44
drwxr-xr-x 13 kali kali   4096 Jan 13 13:59 Desktop
drwxr-xr-x  2 kali kali   4096 Dec 26 05:29 Documents
drwxr-xr-x  2 kali kali   4096 Dec 27 08:52 Downloads
drwxr-xr-x 10 kali kali   4096 Jun 18  2023 hadoop
drwxr-xr-x  2 kali kali   4096 Dec 26 05:29 Music
drwxr-xr-x  2 kali kali   4096 Dec 26 05:29 Pictures
drwxr-xr-x  2 kali kali   4096 Dec 26 05:29 Public
drwx------  2 kali docker 4096 Jan 13 12:43 secrets
drwxr-xr-x  2 kali kali   4096 Dec 26 05:29 Templates
drwxr-xr-x  2 kali kali   4096 Dec 26 05:29 Videos
drwxrwxr-x  5 kali kali   4096 Jan 13 13:57 work
#ls: показывает содержимое каталога. Отличие: ls -a показывает содержимое и скрытые файлы, ls -l: выводит в формате: права, владелец, группа, размер, дата, имя
```
- ✔ 3. Используйте утилиту `file` и `df` для определения какая файловая система на разделе `/dev/sda1`.
```bash
┌──(.venv)─(kali㉿kali)-[~/work/lab02]
└─$ sudo file -s /dev/sda1
/dev/sda1: Linux rev 1.0 ext4 filesystem data, UUID=8a84b405-db00-4b28-a5bc-48ecaa65880d, volume name "root" (needs journal recovery) (extents) (64bit) (large files) (huge files)
                                                                                              
┌──(.venv)─(kali㉿kali)-[~/work/lab02]
└─$ df -Th /dev/sda1
Filesystem     Type  Size  Used Avail Use% Mounted on
/dev/sda1      ext4   79G   50G   25G  68% /
```
- ✔ 4. Выведите на терминале и проанализируйте следующие команды консоли

```bash
──(.venv)─(kali㉿kali)-[~/work/lab02]
└─$ which vi

/usr/bin/vi
                                                                                              
┌──(.venv)─(kali㉿kali)-[~/work/lab02]
└─$ locate hello.py

/home/kali/work/course_labs/labs/lab02/exmpl_hello.py
/home/kali/work/course_labs/labs/lab05/source/hello.py
/home/kali/work/lab01/hello.py
/home/kali/work/lab02/exmpl_hello.py
/usr/lib/python3/dist-packages/mitmproxy/contrib/kaitaistruct/dtls_client_hello.py
/usr/lib/python3/dist-packages/mitmproxy/contrib/kaitaistruct/tls_client_hello.py
                                                                                              
┌──(.venv)─(kali㉿kali)-[~/work/lab02]
└─$ sudo updatedb
                                                                                              
┌──(.venv)─(kali㉿kali)-[~/work/lab02]
└─$ locate hello   
/boot/grub/i386-pc/hello.mod
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/material/templates/.icons/simple/hellofresh.svg
/home/kali/work/course_labs/labs/lab02/exmpl_hello.py
/home/kali/work/course_labs/labs/lab05/source/hello.py
/home/kali/work/lab01/hello.py
/home/kali/work/lab02/exmpl_hello.py
/home/linuxbrew/.linuxbrew/Homebrew/Library/Homebrew/test/support/fixtures/elf/hello
/home/linuxbrew/.linuxbrew/Homebrew/Library/Homebrew/test/support/fixtures/elf/hello_with_rpath
/home/linuxbrew/.linuxbrew/Homebrew/Library/Homebrew/test/support/fixtures/elf/libhello.so.0
/usr/lib/grub/i386-pc/hello.mod
/usr/lib/python2.7/__phello__.foo.py
/usr/lib/python2.7/__phello__.foo.pyc
/usr/lib/python3/dist-packages/dsinternals/common/data/hello
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/CustomKeyInformation.py
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/CustomKeyInformationVolumeType.py
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/KeyCredential.py
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/KeyCredentialEntryType.py
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/KeyCredentialVersion.py
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/KeyFlags.py
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/KeySource.py
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/KeyStrength.py
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/KeyUsage.py
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/VolumeType.py
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/__init__.py
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/__pycache__
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/fidoAuthenticatorFlags.py
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/fidoCOSE.py
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/__pycache__/CustomKeyInformation.cpython-313.pyc
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/__pycache__/CustomKeyInformationVolumeType.cpython-313.pyc
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/__pycache__/KeyCredential.cpython-313.pyc
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/__pycache__/KeyCredentialEntryType.cpython-313.pyc
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/__pycache__/KeyCredentialVersion.cpython-313.pyc
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/__pycache__/KeyFlags.cpython-313.pyc
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/__pycache__/KeySource.cpython-313.pyc
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/__pycache__/KeyStrength.cpython-313.pyc
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/__pycache__/KeyUsage.cpython-313.pyc
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/__pycache__/VolumeType.cpython-313.pyc
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/__pycache__/__init__.cpython-313.pyc
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/__pycache__/fidoAuthenticatorFlags.cpython-313.pyc
/usr/lib/python3/dist-packages/dsinternals/common/data/hello/__pycache__/fidoCOSE.cpython-313.pyc
/usr/lib/python3/dist-packages/mitmproxy/contrib/kaitaistruct/dtls_client_hello.ksy
/usr/lib/python3/dist-packages/mitmproxy/contrib/kaitaistruct/dtls_client_hello.py
/usr/lib/python3/dist-packages/mitmproxy/contrib/kaitaistruct/tls_client_hello.ksy
/usr/lib/python3/dist-packages/mitmproxy/contrib/kaitaistruct/tls_client_hello.py
/usr/lib/python3/dist-packages/mitmproxy/contrib/kaitaistruct/__pycache__/dtls_client_hello.cpython-313.pyc
/usr/lib/python3/dist-packages/mitmproxy/contrib/kaitaistruct/__pycache__/tls_client_hello.cpython-313.pyc
/usr/lib/python3/dist-packages/mitmproxy/proxy/layers/quic/_client_hello_parser.py
/usr/lib/python3/dist-packages/mitmproxy/proxy/layers/quic/__pycache__/_client_hello_parser.cpython-313.pyc
/usr/lib/python3.13/__hello__.py
/usr/lib/python3.13/__phello__
/usr/lib/python3.13/__phello__/__init__.py
/usr/lib/python3.13/__phello__/__pycache__
/usr/lib/python3.13/__phello__/spam.py
/usr/lib/python3.13/__phello__/__pycache__/__init__.cpython-313.pyc
/usr/lib/python3.13/__phello__/__pycache__/spam.cpython-313.pyc
/usr/lib/python3.13/__pycache__/__hello__.cpython-313.pyc
/usr/lib/x86_64-linux-gnu/perl5/5.40/Tk/demos/widget_lib/hello.pl
/usr/lib/x86_64-linux-gnu/rubygems-integration/3.3.0/gems/ffi-1.17.2/samples/hello.rb
/usr/lib/x86_64-linux-gnu/rubygems-integration/3.3.0/gems/ffi-1.17.2/samples/hello_ractor.rb
/usr/share/cmake-3.31/Modules/IntelVSImplicitPath/hello.f
/usr/share/doc/gawk/examples/network/hello-serv.awk
/usr/share/doc/hyperion/Examples/helloworld.exe
/usr/share/doc/hyperion/Examples/helloworld64.EXE
/usr/share/doc/perl-tk/examples/hello
/usr/share/doc/python-odf-doc/examples/helloworld.py
/usr/share/doc/python3-dasbus/examples/03_helloworld
/usr/share/doc/python3-dasbus/examples/03_helloworld/client.py
/usr/share/doc/python3-dasbus/examples/03_helloworld/common.py
/usr/share/doc/python3-dasbus/examples/03_helloworld/server.py
/usr/share/doc/python3-xlsxwriter/docs/_static/hello01.png
/usr/share/doc/python3-xlsxwriter/examples/hello_world.py
/usr/share/doc/texlive-doc/plain/transparent-io/Transparent-IO-hello.tex
/usr/share/metasploit-framework/data/exploits/CVE-2016-4557/hello
/usr/share/metasploit-framework/modules/exploits/linux/mysql/mysql_yassl_hello.rb
/usr/share/metasploit-framework/modules/exploits/windows/mssql/ms02_056_hello.rb
/usr/share/metasploit-framework/modules/exploits/windows/mysql/mysql_yassl_hello.rb
/usr/share/metasploit-framework/vendor/bundle/ruby/3.3.0/gems/ffi-1.16.3/samples/hello.rb
/usr/share/metasploit-framework/vendor/bundle/ruby/3.3.0/gems/ffi-1.16.3/samples/hello_ractor.rb
/usr/share/metasploit-framework/vendor/bundle/ruby/3.3.0/gems/mini_portile2-2.8.9/test/assets/test-cmake-1.0/hello.c
/usr/share/python-odf/examples/helloworld.py
                                                                                              
┌──(.venv)─(kali㉿kali)-[~/work/lab02]
└─$ touch screen                                 
                                                                                              
┌──(.venv)─(kali㉿kali)-[~/work/lab02]
└─$ find ~ -name screen
/home/kali/work/lab02/screen
                                                                                              
┌──(.venv)─(kali㉿kali)-[~/work/lab02]
└─$ locate screen
/etc/screenrc
/etc/alternatives/desktop-lockscreen.xml
/etc/init.d/screen-cleanup
/etc/pam.d/xfce4-screensaver
/etc/rcS.d/S01screen-cleanup
/etc/tmpfiles.d/screen-cleanup.conf
/etc/xdg/kscreenlockerrc
/etc/xdg/autostart/xfce4-screensaver.desktop
/etc/xdg/menus/xfce4-screensavers.menu
/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-screensaver.xml
/home/kali/.config/xfce4/desktop/icons.screen0.yaml
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/bandit/formatters/screen.py
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/bandit/formatters/__pycache__/screen.cpython-313.pyc
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/material/templates/.icons/fontawesome/brands/screenpal.svg
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/material/templates/.icons/fontawesome/solid/mobile-screen-button.svg
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/material/templates/.icons/fontawesome/solid/mobile-screen.svg
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/material/templates/.icons/fontawesome/solid/tablet-screen-button.svg
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/material/templates/.icons/material/cellphone-screenshot.svg
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/material/templates/.icons/material/fit-to-screen-outline.svg
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/material/templates/.icons/material/fit-to-screen.svg
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/material/templates/.icons/material/fullscreen-exit.svg
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/material/templates/.icons/material/fullscreen.svg
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/material/templates/.icons/material/monitor-screenshot.svg
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/material/templates/.icons/material/projector-screen-off-outline.svg
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/material/templates/.icons/material/projector-screen-off.svg
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/material/templates/.icons/material/projector-screen-outline.svg
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/material/templates/.icons/material/projector-screen-variant-off-outline.svg
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/material/templates/.icons/material/projector-screen-variant-off.svg
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/material/templates/.icons/material/projector-screen-variant-outline.svg
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/material/templates/.icons/material/projector-screen-variant.svg
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/material/templates/.icons/material/projector-screen.svg
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/material/templates/.icons/material/screen-rotation-lock.svg
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/material/templates/.icons/material/screen-rotation.svg
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/material/templates/.icons/octicons/screen-full-16.svg
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/material/templates/.icons/octicons/screen-full-24.svg
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/material/templates/.icons/octicons/screen-normal-16.svg
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/material/templates/.icons/octicons/screen-normal-24.svg
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/material/templates/.icons/simple/screencastify.svg
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/pip/_vendor/rich/screen.py
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/pip/_vendor/rich/__pycache__/screen.cpython-313.pyc
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/rich/screen.py
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/rich/__pycache__/screen.cpython-313.pyc
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/safety/formatters/screen.py
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/safety/formatters/__pycache__/screen.cpython-313.pyc
/home/kali/work/lab02/screen
```

- ✔ 5. Используйте конструкцию и вставьте ее в созданный файл ранее. Подключите `pygame` - используем исключительно для стилизации окна.

```bash
┌──(.venv)─(kali㉿kali)-[~/work/lab02]
└─$ python screen.py 
/home/kali/work/course_labs/.venv/lib/python3.13/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
pygame 2.6.1 (SDL 2.28.4, Python 3.13.9)
Hello from the pygame community. https://www.pygame.org/contribute.html```

- ✔ 6. Сделайте `commit` и `push` в свой репозиторий с изменениями в `master branch`. На следующих лабораторных работах мы вернемся к этому файлу.
```bash
┌──(.venv)─(kali㉿kali)-[~/work/lab02]
└─$ git add screen.py
git status
git commit -S -m "feat: add pygame hello window"
git push
git log --oneline --decorate -10

On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   screen.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md
        exmpl_hello.py
        pygamesteel.py

[main (root-commit) fa113ef] feat: add pygame hello window
 1 file changed, 26 insertions(+)
 create mode 100644 screen.py
fatal: The current branch main has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin main

To have this happen automatically for branches without a tracking
upstream, see 'push.autoSetupRemote' in 'git help config'.

fa113ef (HEAD -> main) feat: add pygame hello window
```
- ✔ 7. Выведите на терминале и проанализируйте следующие команды консоли

```bash
┌──(root㉿kali)-[/home/kali/work/lab02]
└─# useradd smallman
                                                                                              
┌──(root㉿kali)-[/home/kali/work/lab02]
└─# userdel smallman -rf
userdel: smallman mail spool (/var/mail/smallman) not found
userdel: smallman home directory (/home/smallman) not found
                                                                                              
┌──(root㉿kali)-[/home/kali/work/lab02]
└─# useradd smallman    
                                                                                              
┌──(root㉿kali)-[/home/kali/work/lab02]
└─# passwd smallman
New password: 
Retype new password: 
passwd: password updated successfully
                                                                                              
┌──(root㉿kali)-[/home/kali/work/lab02]
└─# usermod smallman -c 'Hach Hachov Hacherovich,239,45-67,499-239-45-33'
                                                                                              
┌──(root㉿kali)-[/home/kali/work/lab02]
└─# passwd smallman                                                      
New password: 
Retype new password: 
passwd: password updated successfully
                                                                                              
┌──(root㉿kali)-[/home/kali/work/lab02]
└─# id smallman
uid=1001(smallman) gid=1001(smallman) groups=1001(smallman)
                                                                                              
┌──(root㉿kali)-[/home/kali/work/lab02]
└─# groupadd -g 1500 readgroup
groupadd: group 'readgroup' already exists
                                                                                                                                                            
┌──(root㉿kali)-[/home/kali/work/lab02]
└─# usermod -aG readgroup smallman
                                                                                                                                                            
┌──(root㉿kali)-[/home/kali/work/lab02]
└─# chmod 666 screen              
chmod: cannot access 'screen': No such file or directory
                                                                                                                                                            
┌──(root㉿kali)-[/home/kali/work/lab02]
└─# chmod 666 screen.py 
```

- ✔ 8. Выведите группу прав для `screen` и измените, что бы файл был доступен только для чтения созданному пользователю и выведите права этого польователя для измененного файла только используя `readgroup`.
```bash
┌──(root㉿kali)-[/home/kali/work/lab02]
└─# ls -l screen.py
-rw-rw-rw- 1 kali docker 589 Jan 13 14:27 screen.py
                                                                                                                                                            
┌──(root㉿kali)-[/home/kali/work/lab02]
└─# sudo chgrp readgroup screen.py
                                                                                                                                                            
┌──(root㉿kali)-[/home/kali/work/lab02]
└─# sudo chmod 640 screen.py
                                                                                                                                                            
┌──(root㉿kali)-[/home/kali/work/lab02]
└─# ls -l screen.py
-rw-r----- 1 kali readgroup 589 Jan 13 14:27 screen.py

```
- ✔ 9. Используйте `POSIX ACL`. Выведите на терминале и проанализируйте следующие команды консоли

```bash
┌──(root㉿kali)-[/home/kali/work/lab02]
└─# touch nmapres.txt
                                                                                                                                                            
┌──(root㉿kali)-[/home/kali/work/lab02]
└─# setfacl -m u:smallman:rw nmapres.txt
                                                                                                                                                            
┌──(root㉿kali)-[/home/kali/work/lab02]
└─# setfacl -m g:readgroup:r nmapres.txt
                                                                                                                                                            
┌──(root㉿kali)-[/home/kali/work/lab02]
└─# getfacl nmapres.txt
# file: nmapres.txt
# owner: root
# group: root
user::rw-
user:smallman:rw-
group::r--
group:readgroup:r--
mask::rw-
other::r--

```

- ✔ 10. Сохраните файл внутри локального репозитория, так как следующая работа будет подразумевать запись в нее данных о nmap.
```bash
┌──(root㉿kali)-[/home/kali/work/lab02]
└─# git add nmapres.txt
┌──(root㉿kali)-[/home/kali/work/lab02]
└─# git commit -m "for nmap"                                  
[main 0f2d720] for nmap
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 nmapres.txt
┌──(.venv)─(kali㉿kali)-[~/work/lab02]
└─$ git push -u origin main

Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 10 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 1.17 KiB | 1.17 MiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To github.com:ilya-startcode/lab02.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.

```
- ✔ 11. Для закрепления выведите все списки групп пользователей на вашей ОС и права на верхнеуровневые каталоги.
```bash
┌──(.venv)─(kali㉿kali)-[~/work/lab02]
└─$ ls -ld /*
lrwxrwxrwx   1 root root          7 Nov 10 04:50 /bin -> usr/bin
drwxr-xr-x   3 root root       4096 Jan 13 10:27 /boot
drwxr-xr-x  18 root root       3220 Jan 13 11:31 /dev
drwxr-xr-x 190 root root      12288 Jan 13 14:39 /etc
drwxr-xr-x   4 root root       4096 Jan 13 12:46 /home
lrwxrwxrwx   1 root root         34 Jan 13 10:26 /initrd.img -> boot/initrd.img-6.17.10+kali-amd64
lrwxrwxrwx   1 root root         33 Dec  2 22:02 /initrd.img.old -> boot/initrd.img-6.16.8+kali-amd64
lrwxrwxrwx   1 root root          7 Nov 10 04:50 /lib -> usr/lib
lrwxrwxrwx   1 root root          9 Nov 10 04:50 /lib64 -> usr/lib64
drwx------   2 root root      16384 Dec  2 22:01 /lost+found
drwxr-xr-x   3 root root       4096 Jan 13 10:35 /media
drwxr-xr-x   2 root root       4096 Dec  2 21:29 /mnt
drwxr-xr-x   4 root root       4096 Jan 13 10:36 /opt
dr-xr-xr-x 343 root root          0 Jan 13 11:31 /proc
drwx------   7 root root       4096 Jan 13 14:46 /root
drwxr-xr-x  39 root root        960 Jan 13 11:32 /run
lrwxrwxrwx   1 root root          8 Nov 10 04:50 /sbin -> usr/sbin
drwxr-xr-x   3 root root       4096 Dec  2 21:34 /srv
-rw-------   1 root root 1000000000 Dec  2 22:02 /swap
dr-xr-xr-x  13 root root          0 Jan 13 11:31 /sys
drwxrwxrwt  15 root root        380 Jan 13 14:48 /tmp
drwxr-xr-x  15 root root       4096 Jan 13 10:44 /usr
drwxr-xr-x  12 root root       4096 Jan 13 10:44 /var
lrwxrwxrwx   1 root root         31 Jan 13 10:26 /vmlinuz -> boot/vmlinuz-6.17.10+kali-amd64
lrwxrwxrwx   1 root root         30 Dec  2 22:02 /vmlinuz.old -> boot/vmlinuz-6.16.8+kali-amd64
                                                                                                                                                            
┌──(.venv)─(kali㉿kali)-[~/work/lab02]
└─$ cat /etc/group
root:x:0:
daemon:x:1:
bin:x:2:
sys:x:3:
adm:x:4:kali
tty:x:5:
disk:x:6:
lp:x:7:
mail:x:8:
news:x:9:
uucp:x:10:
man:x:12:
proxy:x:13:
kmem:x:15:
dialout:x:20:kali
fax:x:21:
voice:x:22:
cdrom:x:24:kali
floppy:x:25:kali
tape:x:26:
sudo:x:27:kali
audio:x:29:kali
dip:x:30:kali
www-data:x:33:
backup:x:34:
operator:x:37:
list:x:38:
irc:x:39:
src:x:40:
shadow:x:42:
utmp:x:43:
video:x:44:kali
sasl:x:45:
plugdev:x:46:kali
staff:x:50:
games:x:60:
users:x:100:kali
nogroup:x:65534:
systemd-journal:x:999:
systemd-network:x:998:
crontab:x:997:
input:x:996:
sgx:x:995:
clock:x:994:
kvm:x:993:
render:x:992:
netdev:x:101:kali
systemd-timesync:x:991:
messagebus:x:990:
_ssh:x:102:
scanner:x:103:saned,kali
tss:x:104:
tcpdump:x:105:
plocate:x:106:
bluetooth:x:107:kali
avahi:x:108:
nm-openvpn:x:109:
nm-openconnect:x:988:
pipewire:x:987:
lightdm:x:110:
saned:x:111:
polkitd:x:986:
rtkit:x:112:
colord:x:985:
pcscd:x:984:
kali-trusted:x:113:
mysql:x:114:
stunnel4:x:983:stunnel4
geoclue:x:115:
Debian-snmp:x:116:
sslh:x:117:
ssl-cert:x:118:postgres
i2c:x:119:
lpadmin:x:120:kali
redsocks:x:121:
kismet:x:122:
_gophish:x:123:
sambashare:x:989:
redis:x:124:_gvm
postgres:x:125:
mosquitto:x:126:
inetsim:x:127:
_gvm:x:128:
wireshark:x:129:kali
kali:x:1000:
kaboxer:x:130:kali
rdma:x:132:
nvpd:x:133:
docker:x:134:kali
vboxdrmipc:x:982:
vboxsf:x:981:
readgroup:x:1500:smallman
smallman:x:1001:
readgroup1:x:1501:
```
- ✔ 12. Выведите все права для файлов и директорий локального репозитория которые имеют различные пользователи  (без использования длинных путей)
```bash
┌──(.venv)─(kali㉿kali)-[~/work/lab02]
└─$ ls -l    
total 4
-rw-rw-r--  1 kali docker      0 Jan 13 13:57 exmpl_hello.py
-rw-rw-r--+ 1 root root        0 Jan 13 14:41 nmapres.txt
-rw-rw-r--  1 kali docker      0 Jan 13 13:57 pygamesteel.py
-rw-rw-r--  1 kali docker      0 Jan 13 13:57 README.md
-rw-r-----  1 kali readgroup 589 Jan 13 14:27 screen.py
```
- ✔ 13. Выведите процессы которые у вас запущены в термине и вне его.
```bash
┌──(.venv)─(kali㉿kali)-[~/work/lab02]
└─$ ps -a 
    PID TTY          TIME CMD
  16562 pts/0    00:00:05 zsh
 107982 pts/0    00:00:00 ps
                                                                                                                                                            
┌──(.venv)─(kali㉿kali)-[~/work/lab02]
└─$ ps -x
    PID TTY      STAT   TIME COMMAND
   3166 ?        Ss     0:00 /usr/lib/systemd/systemd --user
   3168 ?        S      0:00 (sd-pam)
   3188 ?        Ss     0:00 /usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
   3189 ?        S<sl   0:00 /usr/bin/pipewire
   3191 ?        SLsl   0:00 /usr/bin/gnome-keyring-daemon --foreground --components=pkcs11,secrets --control-directory=/run/user/1000/keyring
   3192 ?        Ss     0:00 /usr/bin/mpris-proxy
   3193 ?        S<sl   0:00 /usr/bin/wireplumber
   3194 ?        Ssl    0:00 /usr/bin/pipewire -c filter-chain.conf
   3195 ?        S<Lsl   0:00 /usr/bin/pipewire-pulse
   3209 ?        Ssl    0:01 xfce4-session
   3291 ?        Ssl    0:00 /usr/libexec/at-spi-bus-launcher
   3298 ?        S      0:00 /usr/bin/dbus-daemon --config-file=/usr/share/defaults/at-spi2/accessibility.conf --nofork --print-address 12 --address=unix:pa
   3308 ?        Sl     0:01 /usr/libexec/at-spi2-registryd --use-gnome-session
   3316 ?        Ss     0:00 /usr/bin/ssh-agent -s
   3328 ?        Sl     0:36 xfwm4
   3333 ?        Ssl    0:00 /usr/libexec/gvfsd
   3339 ?        Sl     0:00 /usr/libexec/gvfsd-fuse /run/user/1000/gvfs -f
   3369 ?        Sl     0:01 xfsettingsd
   3375 ?        Ssl    0:00 /usr/libexec/dconf-service
   3376 ?        Sl     0:01 xfce4-panel
   3382 ?        Sl     0:00 Thunar --daemon
   3392 ?        Sl     0:06 xfdesktop
   3397 ?        Sl     0:01 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libwhiskermenu.so 1 16777223 wh
   3402 ?        Sl     0:31 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libcpugraph.so 13 16777228 cpug
   3403 ?        Sl     0:00 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libsystray.so 14 16777229 systr
   3404 ?        Sl     0:20 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libgenmon.so 15 16777230 genmon
   3405 ?        Sl     0:00 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libpulseaudio-plugin.so 16 1677
   3406 ?        Sl     0:00 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libnotification-plugin.so 17 16
   3407 ?        Sl     0:00 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libxfce4powermanager.so 18 1677
   3414 ?        Sl     0:00 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libactions.so 22 16777234 actio
   3456 ?        Ssl    0:00 /usr/lib/x86_64-linux-gnu/xfce4/notifyd/xfce4-notifyd
   3476 ?        Sl     0:00 xiccd
   3480 ?        S      0:00 /usr/bin/python3 /usr/share/system-config-printer/applet.py
   3490 ?        Sl     0:00 /usr/libexec/polkit-mate-authentication-agent-1
   3496 ?        Sl     0:01 xfce4-screensaver
   3501 ?        Sl     0:00 nm-applet
   3507 ?        Sl     0:00 /usr/libexec/geoclue-2.0/demos/agent
   3509 ?        Sl     0:00 xfce4-power-manager
   3515 ?        Sl     0:00 /usr/bin/python3 /usr/bin/blueman-applet
   3517 ?        Ssl    0:00 xcape -e Super_L Control_L Escape
   3702 ?        Ssl    0:00 /usr/libexec/gvfs-udisks2-volume-monitor
   3738 ?        Ssl    0:00 /usr/libexec/gvfs-gphoto2-volume-monitor
   3747 ?        Ssl    0:01 /usr/libexec/gvfs-afc-volume-monitor
   3759 ?        Ssl    0:00 /usr/libexec/gvfs-goa-volume-monitor
   3763 ?        Ssl    0:00 /usr/libexec/bluetooth/obexd
   3768 ?        Ssl    0:00 /usr/libexec/gvfs-mtp-volume-monitor
   3828 ?        Ssl    0:00 /usr/libexec/gvfsd-metadata
   3839 ?        Sl     0:00 /usr/libexec/gvfsd-trash --spawner :1.24 /org/gtk/gvfs/exec_spaw/0
   3981 ?        Rl     0:42 /usr/bin/qterminal
   3984 ?        Ssl    0:00 /usr/libexec/xdg-desktop-portal
   3993 ?        Ssl    0:00 /usr/libexec/xdg-permission-store
   3998 ?        Ssl    0:00 /usr/libexec/xdg-document-portal
   4008 ?        Ssl    0:00 /usr/libexec/xdg-desktop-portal-gtk
   4017 pts/0    Ss     0:02 /usr/bin/zsh
   4851 ?        S      0:00 VBoxClient --clipboard
   4852 ?        Sl     0:00 VBoxClient --clipboard
  12539 ?        Ss     0:00 ssh-agent -s
  14981 ?        Sl     4:59 x-www-browser
  14987 ?        Sl     0:00 /usr/lib/firefox-esr/crashhelper 14981 9 /tmp/ 11
  15078 ?        Sl     0:00 /usr/lib/firefox-esr/firefox-esr -contentproc -parentBuildID 20251106203603 -prefsHandle 0:34236 -prefMapHandle 1:271190 -sandb
  15097 ?        Sl     0:10 /usr/lib/firefox-esr/firefox-esr -contentproc -isForBrowser -prefsHandle 0:34361 -prefMapHandle 1:271190 -jsInitHandle 2:242716
  15104 ?        Sl     0:00 /usr/lib/firefox-esr/firefox-esr -contentproc -parentBuildID 20251106203603 -prefsHandle 0:34361 -prefMapHandle 1:271190 -sandb
  15178 ?        Sl     0:00 /usr/lib/firefox-esr/firefox-esr -contentproc -isForBrowser -prefsHandle 0:42826 -prefMapHandle 1:271190 -jsInitHandle 2:242716
  15241 ?        Sl     0:00 /usr/lib/firefox-esr/firefox-esr -contentproc -parentBuildID 20251106203603 -sandboxingKind 0 -prefsHandle 0:42973 -prefMapHand
  15251 ?        Sl     0:20 /usr/lib/firefox-esr/firefox-esr -contentproc -isForBrowser -prefsHandle 0:40156 -prefMapHandle 1:271190 -jsInitHandle 2:242716
  15274 ?        Sl     5:01 /usr/lib/firefox-esr/firefox-esr -contentproc -isForBrowser -prefsHandle 0:40156 -prefMapHandle 1:271190 -jsInitHandle 2:242716
  15302 ?        Sl     0:26 /usr/lib/firefox-esr/firefox-esr -contentproc -isForBrowser -prefsHandle 0:40156 -prefMapHandle 1:271190 -jsInitHandle 2:242716
  15415 ?        Sl     0:24 /usr/lib/firefox-esr/firefox-esr -contentproc -isForBrowser -prefsHandle 0:40156 -prefMapHandle 1:271190 -jsInitHandle 2:242716
  15422 ?        Sl     0:40 /usr/lib/firefox-esr/firefox-esr -contentproc -isForBrowser -prefsHandle 0:40156 -prefMapHandle 1:271190 -jsInitHandle 2:242716
  16562 pts/0    S      0:05 /usr/bin/zsh
  21800 ?        Ssl    0:00 /usr/bin/speech-dispatcher -s -t 0
  21817 ?        Z      0:00 [sd_espeak-ng-mb] <defunct>
  21818 ?        S      0:00 /usr/lib/speech-dispatcher-modules/sd_espeak-ng /etc/speech-dispatcher/modules/espeak-ng.conf
  21819 ?        Sl     0:01 /usr/lib/speech-dispatcher-modules/sd_dummy /etc/speech-dispatcher/modules/dummy.conf
  21822 ?        S      0:00 /usr/lib/speech-dispatcher-modules/sd_espeak-ng /etc/speech-dispatcher/modules/
  21855 ?        Sl     0:07 /usr/lib/firefox-esr/firefox-esr -contentproc -isForBrowser -prefsHandle 0:40318 -prefMapHandle 1:271190 -jsInitHandle 2:242716
  28289 ?        Sl     0:06 /usr/lib/firefox-esr/firefox-esr -contentproc -isForBrowser -prefsHandle 0:40318 -prefMapHandle 1:271190 -jsInitHandle 2:242716
  29451 ?        Sl     0:06 /usr/lib/firefox-esr/firefox-esr -contentproc -isForBrowser -prefsHandle 0:40318 -prefMapHandle 1:271190 -jsInitHandle 2:242716
  55411 ?        SLsl   0:05 /usr/bin/gpg-agent --supervised
  78483 ?        Sl     0:36 /usr/bin/mousepad /home/kali/Desktop/lab02-out
 108087 pts/0    R+     0:00 ps -x
                                                                                                                                                            
┌──(.venv)─(kali㉿kali)-[~/work/lab02]
└─$ pstree 
systemd─┬─ModemManager───3*[{ModemManager}]
        ├─NetworkManager───3*[{NetworkManager}]
        ├─VBoxClient───VBoxClient───3*[{VBoxClient}]
        ├─VBoxDRMClient───4*[{VBoxDRMClient}]
        ├─VBoxService───8*[{VBoxService}]
        ├─accounts-daemon───3*[{accounts-daemon}]
        ├─agetty
        ├─colord───3*[{colord}]
        ├─containerd───13*[{containerd}]
        ├─containerd-shim─┬─docker-init───run.sh───java───72*[{java}]
        │                 └─11*[{containerd-shim}]
        ├─containerd-shim─┬─registry───7*[{registry}]
        │                 └─11*[{containerd-shim}]
        ├─crashhelper───{crashhelper}
        ├─cron
        ├─dbus-daemon
        ├─dockerd─┬─docker-proxy───8*[{docker-proxy}]
        │         ├─docker-proxy───7*[{docker-proxy}]
        │         └─21*[{dockerd}]
        ├─haveged
        ├─lightdm─┬─Xorg───{Xorg}
        │         ├─lightdm─┬─xfce4-session─┬─Thunar───4*[{Thunar}]
        │         │         │               ├─agent───3*[{agent}]
        │         │         │               ├─applet.py
        │         │         │               ├─blueman-applet───5*[{blueman-applet}]
        │         │         │               ├─nm-applet───5*[{nm-applet}]
        │         │         │               ├─polkit-mate-aut───4*[{polkit-mate-aut}]
        │         │         │               ├─xfce4-panel─┬─8*[wrapper-2.0───4*[{wrapper-2.0}]]
        │         │         │               │             └─4*[{xfce4-panel}]
        │         │         │               ├─xfce4-power-man───4*[{xfce4-power-man}]
        │         │         │               ├─xfce4-screensav───4*[{xfce4-screensav}]
        │         │         │               ├─xfdesktop───4*[{xfdesktop}]
        │         │         │               ├─xfsettingsd───5*[{xfsettingsd}]
        │         │         │               ├─xfwm4───25*[{xfwm4}]
        │         │         │               ├─xiccd───3*[{xiccd}]
        │         │         │               └─4*[{xfce4-session}]
        │         │         └─3*[{lightdm}]
        │         └─3*[{lightdm}]
        ├─mousepad───6*[{mousepad}]
        ├─pcscd───6*[{pcscd}]
        ├─polkitd───3*[{polkitd}]
        ├─qterminal─┬─zsh───zsh───pstree
        │           └─11*[{qterminal}]
        ├─rtkit-daemon───2*[{rtkit-daemon}]
        ├─2*[ssh-agent]
        ├─systemd─┬─(sd-pam)
        │         ├─at-spi-bus-laun─┬─dbus-daemon
        │         │                 └─4*[{at-spi-bus-laun}]
        │         ├─at-spi2-registr───3*[{at-spi2-registr}]
        │         ├─dbus-daemon
        │         ├─dconf-service───3*[{dconf-service}]
        │         ├─gnome-keyring-d───4*[{gnome-keyring-d}]
        │         ├─gpg-agent───{gpg-agent}
        │         ├─gvfs-afc-volume───4*[{gvfs-afc-volume}]
        │         ├─gvfs-goa-volume───3*[{gvfs-goa-volume}]
        │         ├─gvfs-gphoto2-vo───3*[{gvfs-gphoto2-vo}]
        │         ├─gvfs-mtp-volume───3*[{gvfs-mtp-volume}]
        │         ├─gvfs-udisks2-vo───4*[{gvfs-udisks2-vo}]
        │         ├─gvfsd─┬─gvfsd-trash───4*[{gvfsd-trash}]
        │         │       └─3*[{gvfsd}]
        │         ├─gvfsd-fuse───6*[{gvfsd-fuse}]
        │         ├─gvfsd-metadata───3*[{gvfsd-metadata}]
        │         ├─mpris-proxy
        │         ├─obexd───4*[{obexd}]
        │         ├─pipewire───2*[{pipewire}]
        │         ├─pipewire───{pipewire}
        │         ├─pipewire-pulse───2*[{pipewire-pulse}]
        │         ├─speech-dispatch─┬─sd_dummy───2*[{sd_dummy}]
        │         │                 ├─2*[sd_espeak-ng]
        │         │                 ├─sd_espeak-ng-mb
        │         │                 └─4*[{speech-dispatch}]
        │         ├─wireplumber───5*[{wireplumber}]
        │         ├─2*[xdg-desktop-por───5*[{xdg-desktop-por}]]
        │         ├─xdg-document-po─┬─fusermount3
        │         │                 └─6*[{xdg-document-po}]
        │         ├─xdg-permission-───3*[{xdg-permission-}]
        │         └─xfce4-notifyd───4*[{xfce4-notifyd}]
        ├─systemd-journal
        ├─systemd-logind
        ├─systemd-udevd
        ├─udisksd───6*[{udisksd}]
        ├─upowerd───3*[{upowerd}]
        ├─x-www-browser─┬─Isolated Servic───28*[{Isolated Servic}]
        │               ├─Isolated Web Co───36*[{Isolated Web Co}]
        │               ├─Isolated Web Co───29*[{Isolated Web Co}]
        │               ├─Isolated Web Co───28*[{Isolated Web Co}]
        │               ├─Isolated Web Co───27*[{Isolated Web Co}]
        │               ├─Privileged Cont───28*[{Privileged Cont}]
        │               ├─RDD Process───4*[{RDD Process}]
        │               ├─Socket Process───5*[{Socket Process}]
        │               ├─Utility Process───4*[{Utility Process}]
        │               ├─3*[Web Content───17*[{Web Content}]]
        │               ├─WebExtensions───26*[{WebExtensions}]
        │               └─128*[{x-www-browser}]
        └─xcape───{xcape}
```
- ✔ 14. Оформить `README.md` по аналогии и использовать `shield`, etc.
- ✔ 15. Составить `gist` отчет и отправить ссылку личным сообщением


**Вопрос из прошлой лабораторной**: Для чего нужен флаг -u в команде git push -u origin main
Флаг ```-u``` = ```--set-upstream``` устанавливает upstream-связь между локальной веткой и удалённой. После чего можно будет просто прописывать git push без указания конкретной ветки.

```bash
-u, --set-upstream
    For every branch that is up to date or successfully pushed, add upstream (tracking)
    reference, used by argument-less git-pull(1) and other commands. For more information,
    see branch.<name>.merge in git-config(1).
```

***
