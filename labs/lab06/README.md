<div align="center">
<h1><a id="intro">Лабораторная работа №6</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Балашов Д.В.-8b9aff" alt="Contributor Badge"></a></div>

***

Салют :wave:,<br>
Данная лабораторная работа посвещена изучению аудита безопасности `Docker` при использовании `Docker Bench Security`. Мы рассмотрим как с ним работать. Мы разберем как проверить конфигурации безопасности и выявить их не корректность, как произвести чекап с `CIS Docker Benchmark v1.6.0`.


***

## Задание

- [x] 1. Необходимо установить `Docker Engine` для Linux

```bash
┌──(.venv)─(kali㉿kali)-[~/work/course_labs/labs/lab06]
└─$ sudo apt-get install -y docker.io
[sudo] password for kali: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
docker.io is already the newest version (27.5.1+dfsg4-1).
Solving dependencies... Done
0 upgraded, 0 newly installed, 0 to remove and 959 not upgraded.
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/work/course_labs/labs/lab06]
└─$ sudo usermod -aG docker "$USER"
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/work/course_labs/labs/lab06]
└─$ sudo systemctl start docker
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/work/course_labs/labs/lab06]
└─$ docker pull docker/docker-bench-security
Using default tag: latest
latest: Pulling from docker/docker-bench-security
cd784148e348: Pull complete 
48fe0d48816d: Pull complete 
164e5e0f48c5: Pull complete 
378ed37ea5ff: Pull complete 
Digest: sha256:ddbdf4f86af4405da4a8a7b7cc62bb63bfeb75e85bf22d2ece70c204d7cfabb8
Status: Downloaded newer image for docker/docker-bench-security:latest
docker.io/docker/docker-bench-security:latest

```

- [x] 2. Проверьте работу докера и сделать скрипт `audit.sh` исполняемым
```bash
┌──(.venv)─(kali㉿kali)-[~/work/course_labs/labs/lab06]
└─$ ls -la audit.sh
-rwxrwxr-x 1 kali kali 9700 Jan 13 11:48 audit.sh
```

- [x] 3. Развернуть уязвимое приложение как отдельные стенды

```bash
┌──(.venv)─(kali㉿kali)-[~/work/course_labs/labs/lab06]
└─$ docker-compose -f vulnerable-app.yml up -d 
WARN[0000] /home/kali/work/course_labs/labs/lab06/vulnerable-app.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Running 10/10
 ✔ debug-shell Pulled                                                                                   2.9s 
   ✔ 1074353eec0d Already exists                                                                        0.0s 
 ✔ vulnerable-web Pulled                                                                                5.0s 
   ✔ 119d43eec815 Already exists                                                                        0.0s 
   ✔ 700146c8ad64 Pull complete                                                                         2.8s 
   ✔ d989100b8a84 Pull complete                                                                         2.8s 
   ✔ 500799c30424 Pull complete                                                                         2.8s 
   ✔ 10b68cfefee1 Pull complete                                                                         2.8s 
   ✔ 57f0dd1befe2 Pull complete                                                                         2.8s 
   ✔ eaf8753feae0 Pull complete                                                                         2.8s 
WARN[0005] Found orphan containers ([vulnerable-app insecure-db]) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up. 
[+] Running 4/4
 ✔ Container debug-shell                                                  St...                         0.2s 
 ✔ Container vulnerable-nginx                                             Recreated                     0.1s 
 ! debug-shell Published ports are discarded when using host network mode                               0.0s 
 ✔ Container vulnerable-web                                               Started                       0.2s 
```

- [x] 4. Запустите скрипт из `venv` и проанализируйте то, что вывело на терминале и что вывело при конвертировании

```bash
┌──(.venv)─(kali㉿kali)-[~/work/course_labs/labs/lab06]
└─$ sed -i 's|-v /usr/bin:/usr/bin:ro||' audit.sh

                                                                                                                          
┌──(.venv)─(kali㉿kali)-[~/work/course_labs/labs/lab06]
└─$ DOCKER_BENCH_IMAGE=jauderho/docker-bench-security:latest ./audit.sh

Starting Docker CIS & Image Security Audit

Detected platform: Linux
Using docker-bench-security image: jauderho/docker-bench-security:latest
Reports will be saved to: ./audit_reports/

Trivy not found, skipping image vulnerability scan for jauderho/docker-bench-security:latest

Trivy not found, skipping lab images scan

Linux host detected – configuring mounts for CIS Docker Benchmark coverage

Mounting /usr/bin/containerd
Mounting /usr/bin/runc
Mounting /usr/lib/systemd
Mounting /etc/docker
Mounting /var/log
Running Docker Bench Security container (CIS host audit)

# --------------------------------------------------------------------------------------------
# Docker Bench for Security v1.6.0                                                                                        
#                                                                                                                         
# Docker, Inc. (c) 2015-2026                                                                                              
#                                                                                                                         
# Checks for dozens of common best-practices around deploying Docker containers in production.                            
# Based on the CIS Docker Benchmark 1.6.0.                                                                                
# --------------------------------------------------------------------------------------------                            

Initializing 2026-01-14T19:09:59


Section A - Check results
WARNING: This output is designed for human readability. For machine-readable output, please use --format.
error: no such object: 1.35GB
error: no such object: 8.44MB
error: no such object: 1.6GB
error: no such object: 51.6MB
error: no such object: 1.21GB
error: no such object: 2.49GB
error: no such object: 2.49GB
error: no such object: 2.49GB
error: no such object: 2.49GB
error: no such object: 2.49GB
error: no such object: 2.49GB
error: no such object: 2.49GB
error: no such object: 157MB
error: no such object: 1.62GB
error: no such object: 157MB
error: no such object: 46.8MB
error: no such object: 2.83GB
error: no such object: 157MB
error: no such object: 138MB
error: no such object: 141MB
error: no such object: 157MB
error: no such object: 335MB
error: no such object: 61.9MB
error: no such object: 161MB
error: no such object: 276MB
error: no such object: 453MB
error: no such object: 54.3MB
error: no such object: 2.4GB
error: no such object: 78.1MB

[INFO] 1 - Host Configuration
[INFO] 1.1 - Linux Hosts Specific Configuration
[WARN] 1.1.1 - Ensure a separate partition for containers has been created (Automated)
[INFO] 1.1.2 - Ensure only trusted users are allowed to control Docker daemon (Automated)
[INFO]       * Users: kali
[WARN] 1.1.3 - Ensure auditing is configured for the Docker daemon (Automated)
[WARN] 1.1.4 - Ensure auditing is configured for Docker files and directories -/run/containerd (Automated)
[WARN] 1.1.5 - Ensure auditing is configured for Docker files and directories - /var/lib/docker (Automated)
[WARN] 1.1.6 - Ensure auditing is configured for Docker files and directories - /etc/docker (Automated)
[INFO] 1.1.7 - Ensure auditing is configured for Docker files and directories - docker.service (Automated)
[INFO]        * File not found
[INFO] 1.1.8 - Ensure auditing is configured for Docker files and directories - containerd.sock (Automated)
[INFO]        * File not found
[INFO] 1.1.9 - Ensure auditing is configured for Docker files and directories - docker.socket (Automated)
[INFO]        * File not found
[WARN] 1.1.10 - Ensure auditing is configured for Docker files and directories - /etc/default/docker (Automated)
[INFO] 1.1.11 - Ensure auditing is configured for Dockerfiles and directories - /etc/docker/daemon.json (Automated)
[INFO]        * File not found
[WARN] 1.1.12 - 1.1.12 Ensure auditing is configured for Dockerfiles and directories - /etc/containerd/config.toml (Automated)
[INFO] 1.1.13 - Ensure auditing is configured for Docker files and directories - /etc/sysconfig/docker (Automated)
[INFO]        * File not found
[WARN] 1.1.14 - Ensure auditing is configured for Docker files and directories - /usr/bin/containerd (Automated)
[INFO] 1.1.15 - Ensure auditing is configured for Docker files and directories - /usr/bin/containerd-shim (Automated)
[INFO]         * File not found
[INFO] 1.1.16 - Ensure auditing is configured for Docker files and directories - /usr/bin/containerd-shim-runc-v1 (Automated)
[INFO]         * File not found
[INFO] 1.1.17 - Ensure auditing is configured for Docker files and directories - /usr/bin/containerd-shim-runc-v2 (Automated)
[INFO]         * File not found
[WARN] 1.1.18 - Ensure auditing is configured for Docker files and directories - /usr/bin/runc (Automated)
[INFO] 1.2 - General Configuration
[NOTE] 1.2.1 - Ensure the container host has been Hardened (Manual)
[PASS] 1.2.2 - Ensure that the version of Docker is up to date (Manual)
[INFO]        * Using 27.5.1+4 which is current
[INFO]        * Check with your operating system vendor for support and security maintenance for Docker

[INFO] 2 - Docker daemon configuration
[NOTE] 2.1 - Run the Docker daemon as a non-root user, if possible (Manual)
[WARN] 2.2 - Ensure network traffic is restricted between containers on the default bridge (Scored)
[PASS] 2.3 - Ensure the logging level is set to 'info' (Scored)
[PASS] 2.4 - Ensure Docker is allowed to make changes to iptables (Scored)
[PASS] 2.5 - Ensure insecure registries are not used (Scored)
[PASS] 2.6 - Ensure aufs storage driver is not used (Scored)
[INFO] 2.7 - Ensure TLS authentication for Docker daemon is configured (Scored)
[INFO]      * Docker daemon not listening on TCP
[INFO] 2.8 - Ensure the default ulimit is configured appropriately (Manual)
[INFO]      * Default ulimit doesn't appear to be set
[WARN] 2.9 - Enable user namespace support (Scored)
[PASS] 2.10 - Ensure the default cgroup usage has been confirmed (Scored)
[PASS] 2.11 - Ensure base device size is not changed until needed (Scored)
[WARN] 2.12 - Ensure that authorization for Docker client commands is enabled (Scored)
[WARN] 2.13 - Ensure centralized and remote logging is configured (Scored)
[WARN] 2.14 - Ensure containers are restricted from acquiring new privileges (Scored)
[PASS] 2.15 - Ensure live restore is enabled (Scored) (Incompatible with swarm mode)
[WARN] 2.16 - Ensure Userland Proxy is Disabled (Scored)
[INFO] 2.17 - Ensure that a daemon-wide custom seccomp profile is applied if appropriate (Manual)
[INFO] Ensure that experimental features are not implemented in production (Scored) (Deprecated)

[INFO] 3 - Docker daemon configuration files
[INFO] 3.1 - Ensure that the docker.service file ownership is set to root:root (Automated)
[INFO]      * File not found
[INFO] 3.2 - Ensure that docker.service file permissions are appropriately set (Automated)
[INFO]      * File not found
[INFO] 3.3 - Ensure that docker.socket file ownership is set to root:root (Automated)
[INFO]      * File not found
[INFO] 3.4 - Ensure that docker.socket file permissions are set to 644 or more restrictive (Automated)
[INFO]      * File not found
[PASS] 3.5 - Ensure that the /etc/docker directory ownership is set to root:root (Automated)
[PASS] 3.6 - Ensure that /etc/docker directory permissions are set to 755 or more restrictively (Automated)
[INFO] 3.7 - Ensure that registry certificate file ownership is set to root:root (Automated)
[INFO]      * Directory not found
[INFO] 3.8 - Ensure that registry certificate file permissions are set to 444 or more restrictively (Automated)
[INFO]      * Directory not found
[INFO] 3.9 - Ensure that TLS CA certificate file ownership is set to root:root (Automated)
[INFO]      * No TLS CA certificate found
[INFO] 3.10 - Ensure that TLS CA certificate file permissions are set to 444 or more restrictively (Automated)
[INFO]       * No TLS CA certificate found
[INFO] 3.11 - Ensure that Docker server certificate file ownership is set to root:root (Automated)
[INFO]       * No TLS Server certificate found
[INFO] 3.12 - Ensure that the Docker server certificate file permissions are set to 444 or more restrictively (Automated)
[INFO]       * No TLS Server certificate found
[INFO] 3.13 - Ensure that the Docker server certificate key file ownership is set to root:root (Automated)
[INFO]       * No TLS Key found
[INFO] 3.14 - Ensure that the Docker server certificate key file permissions are set to 400 (Automated)
[INFO]       * No TLS Key found
[PASS] 3.15 - Ensure that the Docker socket file ownership is set to root:docker (Automated)
[PASS] 3.16 - Ensure that the Docker socket file permissions are set to 660 or more restrictively (Automated)
[INFO] 3.17 - Ensure that the daemon.json file ownership is set to root:root (Automated)
[INFO]       * File not found
[INFO] 3.18 - Ensure that daemon.json file permissions are set to 644 or more restrictive (Automated)
[INFO]       * File not found
[PASS] 3.19 - Ensure that the /etc/default/docker file ownership is set to root:root (Automated)
[PASS] 3.20 - Ensure that the /etc/default/docker file permissions are set to 644 or more restrictively (Automated)
[INFO] 3.21 - Ensure that the /etc/sysconfig/docker file permissions are set to 644 or more restrictively (Automated)
[INFO]       * File not found
[INFO] 3.22 - Ensure that the /etc/sysconfig/docker file ownership is set to root:root (Automated)
[INFO]       * File not found
[INFO] 3.23 - Ensure that the Containerd socket file ownership is set to root:root (Automated)
[INFO]       * File not found
[INFO] 3.24 - Ensure that the Containerd socket file permissions are set to 660 or more restrictively (Automated)
[INFO]       * File not found

[INFO] 4 - Container Images and Build File
[WARN] 4.1 - Ensure that a user for the container has been created (Automated)
[WARN]      * Running as root: registry.1.nj0a26m36wrk6i6brsp0bjtes
[NOTE] 4.2 - Ensure that containers use only trusted base images (Manual)
[NOTE] 4.3 - Ensure that unnecessary packages are not installed in the container (Manual)
[NOTE] 4.4 - Ensure images are scanned and rebuilt to include security patches (Manual)
[WARN] 4.5 - Ensure Content trust for Docker is Enabled (Automated)
[WARN] 4.6 - Ensure that HEALTHCHECK instructions have been added to container images (Automated)
[WARN]      * No Healthcheck found: [lab05-client:latest]
[WARN]      * No Healthcheck found: [lab05-server:latest]
[WARN]      * No Healthcheck found: [ilyadock1/hellow-appsec-world:latest kov/hellow-appsec-world:latest hellow-appsec-world:latest]
[WARN]      * No Healthcheck found: [ilyadock1/hellow-appsec-world:latest kov/hellow-appsec-world:latest hellow-appsec-world:latest]
[WARN]      * No Healthcheck found: [ilyadock1/hellow-appsec-world:latest kov/hellow-appsec-world:latest hellow-appsec-world:latest]
[WARN]      * No Healthcheck found: [lab05-web:latest]
[WARN]      * No Healthcheck found: [nginx:alpine]
[WARN]      * No Healthcheck found: [nginx:latest]
[WARN]      * No Healthcheck found: [hadoop/submit:3.4.2]
[WARN]      * No Healthcheck found: [hadoop/basic:3.4.2]
[WARN]      * No Healthcheck found: [jupyterlab/core:4.4.9]
[WARN]      * No Healthcheck found: [spark/core:3.5.7]
[WARN]      * No Healthcheck found: [flink/core:2.1.1]
[WARN]      * No Healthcheck found: [hive/core:4.0.1]
[WARN]      * No Healthcheck found: [127.0.0.1:5000/mpi:latest]
[WARN]      * No Healthcheck found: [python:3.11-alpine]
[WARN]      * No Healthcheck found: [postgres:16-alpine]
[WARN]      * No Healthcheck found: [alpine:latest]
[WARN]      * No Healthcheck found: [mariadb:12.1.2]
[WARN]      * No Healthcheck found: [postgres:17.6]
[WARN]      * No Healthcheck found: [ubuntu:latest]
[WARN]      * No Healthcheck found: [apache/hive:4.0.1]
[INFO] 4.7 - Ensure update instructions are not used alone in the Dockerfile (Manual)
[INFO]      * Update instruction found: [lab05-client:latest]
[INFO]      * Update instruction found: [lab05-server:latest]
[INFO]      * Update instruction found: [ilyadock1/hellow-appsec-world:latest kov/hellow-appsec-world:latest hellow-appsec-world:latest]
[INFO]      * Update instruction found: [ilyadock1/hellow-appsec-world:latest kov/hellow-appsec-world:latest hellow-appsec-world:latest]
[INFO]      * Update instruction found: [ilyadock1/hellow-appsec-world:latest kov/hellow-appsec-world:latest hellow-appsec-world:latest]
[INFO]      * Update instruction found: [lab05-web:latest]
[INFO]      * Update instruction found: [hadoop/submit:3.4.2]
[INFO]      * Update instruction found: [hadoop/historyserver:3.4.2]
[INFO]      * Update instruction found: [hadoop/nodemanager:3.4.2]
[INFO]      * Update instruction found: [hadoop/resourcemanager:3.4.2]
[INFO]      * Update instruction found: [hadoop/namenode:3.4.2]
[INFO]      * Update instruction found: [hadoop/datanode:3.4.2]
[INFO]      * Update instruction found: [hadoop/basic:3.4.2]
[INFO]      * Update instruction found: [jupyterlab/core:4.4.9]
[INFO]      * Update instruction found: [spark/core:3.5.7]
[INFO]      * Update instruction found: [flink/core:2.1.1]
[INFO]      * Update instruction found: [hive/core:4.0.1]
[INFO]      * Update instruction found: [postgres:17.6]
[INFO]      * Update instruction found: [apache/hive:4.0.1]
[NOTE] 4.8 - Ensure setuid and setgid permissions are removed (Manual)
[INFO] 4.9 - Ensure that COPY is used instead of ADD in Dockerfiles (Manual)
[INFO]      * ADD in image history: [hadoop/submit:3.4.2]
[INFO]      * ADD in image history: [hadoop/historyserver:3.4.2]
[INFO]      * ADD in image history: [hadoop/nodemanager:3.4.2]
[INFO]      * ADD in image history: [hadoop/resourcemanager:3.4.2]
[INFO]      * ADD in image history: [hadoop/namenode:3.4.2]
[INFO]      * ADD in image history: [hadoop/datanode:3.4.2]
[INFO]      * ADD in image history: [hadoop/basic:3.4.2]
[INFO]      * ADD in image history: [jupyterlab/core:4.4.9]
[INFO]      * ADD in image history: [spark/core:3.5.7]
[INFO]      * ADD in image history: [flink/core:2.1.1]
[INFO]      * ADD in image history: [127.0.0.1:5000/mpi:latest]
[INFO]      * ADD in image history: [mariadb:12.1.2]
[INFO]      * ADD in image history: [ubuntu:latest]
[NOTE] 4.10 - Ensure secrets are not stored in Dockerfiles (Manual)
[NOTE] 4.11 - Ensure only verified packages are installed (Manual)
[NOTE] 4.12 - Ensure all signed artifacts are validated (Manual)

[INFO] 5 - Container Runtime
[WARN] 5.1 - Ensure swarm mode is not Enabled, if not needed (Automated)
[WARN] 5.2 - Ensure that, if applicable, an AppArmor Profile is enabled (Automated)
[WARN]      * No AppArmorProfile Found: vulnerable-web
[WARN] 5.3 - Ensure that, if applicable, SELinux security options are set (Automated)
[WARN]      * No SecurityOptions Found: registry.1.nj0a26m36wrk6i6brsp0bjtes
[WARN] 5.4 - Ensure that Linux kernel capabilities are restricted within containers (Automated)
[WARN]      * Capabilities added: CapAdd=[ALL] to vulnerable-web
[WARN] 5.5 - Ensure that privileged containers are not used (Automated)
[WARN]      * Container running in Privileged mode: vulnerable-web
[WARN] 5.6 - Ensure sensitive host system directories are not mounted on containers (Automated)
[WARN]      * Sensitive directory / mounted in: vulnerable-web
[PASS] 5.7 - Ensure sshd is not run within containers (Automated)
[PASS] 5.8 - Ensure privileged ports are not mapped within containers (Automated)
[PASS] 5.9 - Ensure that only needed ports are open on the container (Manual)
[WARN] 5.10 - Ensure that the host's network namespace is not shared (Automated)
[WARN]      * Container running with networking mode 'host': vulnerable-web
[WARN] 5.11 - Ensure that the memory usage for containers is limited (Automated)
[WARN]       * Container running without memory restrictions: vulnerable-web
[WARN]       * Container running without memory restrictions: registry.1.nj0a26m36wrk6i6brsp0bjtes
[WARN] 5.12 - Ensure that CPU priority is set appropriately on containers (Automated)
[WARN]       * Container running without CPU restrictions: vulnerable-web
[WARN]       * Container running without CPU restrictions: registry.1.nj0a26m36wrk6i6brsp0bjtes
[WARN] 5.13 - Ensure that the container's root filesystem is mounted as read only (Automated)
[WARN]       * Container running with root FS mounted R/W: vulnerable-web
[WARN]       * Container running with root FS mounted R/W: registry.1.nj0a26m36wrk6i6brsp0bjtes
[PASS] 5.14 - Ensure that incoming container traffic is bound to a specific host interface (Automated)
[PASS] 5.15 - Ensure that the 'on-failure' container restart policy is set to '5' (Automated)
[WARN] 5.16 - Ensure that the host's process namespace is not shared (Automated)
[WARN]       * Host PID namespace being shared with: vulnerable-web
[PASS] 5.17 - Ensure that the host's IPC namespace is not shared (Automated)
[PASS] 5.18 - Ensure that host devices are not directly exposed to containers (Manual)
[INFO] 5.19 - Ensure that the default ulimit is overwritten at runtime if needed (Manual)
[INFO]       * Container no default ulimit override: vulnerable-web
[INFO]       * Container no default ulimit override: registry.1.nj0a26m36wrk6i6brsp0bjtes
[PASS] 5.20 - Ensure mount propagation mode is not set to shared (Automated)
[PASS] 5.21 - Ensure that the host's UTS namespace is not shared (Automated)
[WARN] 5.22 - Ensure the default seccomp profile is not Disabled (Automated)
[WARN]       * Default seccomp profile disabled: vulnerable-web
[NOTE] 5.23 - Ensure that docker exec commands are not used with the privileged option (Automated)
[NOTE] 5.24 - Ensure that docker exec commands are not used with the user=root option (Manual)
[PASS] 5.25 - Ensure that cgroup usage is confirmed (Automated)
[WARN] 5.26 - Ensure that the container is restricted from acquiring additional privileges (Automated)
[WARN]       * Privileges not restricted: vulnerable-web
[WARN]       * Privileges not restricted: registry.1.nj0a26m36wrk6i6brsp0bjtes
[WARN] 5.27 - Ensure that container health is checked at runtime (Automated)
[WARN]       * Health check not set: vulnerable-web
[WARN]       * Health check not set: registry.1.nj0a26m36wrk6i6brsp0bjtes
[INFO] 5.28 - Ensure that Docker commands always make use of the latest version of their image (Manual)
[WARN] 5.29 - Ensure that the PIDs cgroup limit is used (Automated)
[WARN]       * PIDs limit not set: vulnerable-web
[WARN]       * PIDs limit not set: registry.1.nj0a26m36wrk6i6brsp0bjtes
[PASS] 5.30 - Ensure that Docker's default bridge 'docker0' is not used (Manual)
[PASS] 5.31 - Ensure that the host's user namespaces are not shared (Automated)
[WARN] 5.32 - Ensure that the Docker socket is not mounted inside any containers (Automated)
[WARN]       * Docker socket shared: vulnerable-web

[INFO] 6 - Docker Security Operations
[INFO] 6.1 - Ensure that image sprawl is avoided (Manual)
[INFO]      * There are currently: 27 images
[INFO] 6.2 - Ensure that container sprawl is avoided (Manual)
[INFO]      * There are currently a total of 40 containers, with only 3 of them currently running

[INFO] 7 - Docker Swarm Configuration
[PASS] 7.1 - Ensure that the minimum number of manager nodes have been created in a swarm (Automated)
[WARN] 7.2 - Ensure that swarm services are bound to a specific host interface (Automated)
[WARN] 7.3 - Ensure that all Docker swarm overlay networks are encrypted (Automated)
[WARN]      * Unencrypted overlay network: ingress (swarm)
[INFO] 7.4 - Ensure that Docker's secret management commands are used for managing secrets in a swarm cluster (Manual)
[WARN] 7.5 - Ensure that swarm manager is run in auto-lock mode (Automated)
[NOTE] 7.6 - Ensure that the swarm manager auto-lock key is rotated periodically (Manual)
[INFO] 7.7 - Ensure that node certificates are rotated as appropriate (Manual)
[INFO] 7.8 - Ensure that CA certificates are rotated as appropriate (Manual)
[INFO] 7.9 - Ensure that management plane traffic is separated from data plane traffic (Manual)


Section C - Score

[INFO] Checks: 117
[INFO] Score: -13


CIS audit output saved to: ./audit_reports/text/docker-bench-security-cis.txt

Converting Trivy JSON reports to XLSX/ODT formats...

Audit complete!
Reports directory structure:
   ./audit_reports/
   ├── json/          (Trivy JSON outputs)
   ├── text/          (CIS audit text outputs)
   ├── xlsx/          (Excel spreadsheets)
   └── odt/           (OpenDocument Text files)

For CIS Docker Benchmark details, see:
https://www.cisecurity.org/benchmark/docker
```

Анализ вывода audit.sh и конвертирования
Что вывелось в терминале (Docker Bench / CIS)

Скрипт запустил контейнер Docker Bench for Security и выполнил проверки CIS Docker Benchmark. Итог:

Checks: 117

Score: -13 (много предупреждений WARN)

Результат сохранился в файл:
./audit_reports/text/docker-bench-security-cis.txt

- [x] 5. Проведите анализ уязвимостей, опишите их причину возникновения

#### Host Configuration (1.x)

Много WARN про отсутствие отдельного раздела под контейнеры и про аудит (auditd) для каталогов Docker (/var/lib/docker, /etc/docker, и т.д.).
Это означает, что на хосте нет настроенного аудита изменений критичных файлов Docker → снижается обнаруживаемость атак/изменений.

#### Docker daemon configuration (2.x)

WARN 2.9 Enable user namespace support → userns-remap не включён.

WARN 2.12 authorization for Docker client commands → нет централизованной авторизации для docker-команд.

WARN 2.13 centralized and remote logging → нет централизованных логов.

WARN 2.16 Userland Proxy is Disabled → userland-proxy не отключён (в ряде конфигураций это рекомендация CIS).

#### Container Images (4.x)

WARN 4.6 HEALTHCHECK ... No Healthcheck found у многих образов → отсутствует healthcheck.

WARN 4.5 Content trust ... → Docker Content Trust не включён.

#### Container Runtime (5.x) — самое критичное
По твоему выводу контейнер vulnerable-web (и ещё registry...) имеет набор опасных настроек:

WARN 5.4 Capabilities added: CapAdd=[ALL]

WARN 5.5 Container running in Privileged mode

WARN 5.10 networking mode 'host'

WARN 5.16 Host PID namespace being shared

WARN 5.13 root FS mounted R/W

WARN 5.11/5.12 no memory/cpu limits

WARN 5.32 Docker socket shared

Это признаки очень высокого риска компрометации хоста при взломе контейнера.

#### Swarm (7.x)

включён swarm и есть WARN про unencrypted overlay network: ingress, binding интерфейса и auto-lock. Если swarm не используется в лабе — лучше отключать.

конвертер отработал корректно, но входных данных не было, т.к. Trivy отсутствует.
***
#### Ниже — самые важные “уязвимости/мисконфигурации” и их причины:

A) Privileged container (WARN 5.5)

Причина: контейнер запущен с --privileged (или эквивалентно в compose/daemon).
Плохо: контейнер получает почти полный доступ к ядру/устройствам.

B) Все capabilities (WARN 5.4 CapAdd=[ALL])

Причина: контейнеру добавлены все Linux capabilities (вместо принципа минимальных привилегий).
Плохо: расширяет возможности атакующего внутри контейнера (mount, raw sockets, ptrace и т.п. — зависит от capability).

C) host network (WARN 5.10)

Причина: контейнер запущен в режиме --network host.
Плохо: сетевой стек общий с хостом → легче делать перехват/сканирование/обход сетевых политик.

D) shared host PID namespace (WARN 5.16)

Причина: контейнер запущен с --pid host.
Плохо: процессы хоста видны из контейнера, повышает риск атак на процессы/инфо-утечек.

E) Docker socket mounted (WARN 5.32)

Причина: в контейнер примонтирован /var/run/docker.sock.
Плохо: это фактически “root-доступ к Docker”. Если атакующий попадёт в контейнер, он может управлять Docker на хосте (создавать privileged-контейнеры, монтировать / и т.д.).

F) Нет лимитов ресурсов (WARN 5.11/5.12/5.29)

Причина: не заданы ограничения CPU/memory/pids.
Плохо: возможен DoS — контейнер может выесть память/CPU и положить хост/службы.

G) Root filesystem writable (WARN 5.13)

Причина: rootfs контейнера RW по умолчанию.
Плохо: проще закрепляться (persistence) и модифицировать окружение.

H) Нет healthcheck (WARN 4.6, WARN 5.27)

Причина: в Dockerfile/compose не задан HEALTHCHECK.
Плохо: система оркестрации/мониторинга не видит деградацию сервиса, сложнее обнаружить компрометацию/падение.

I) User namespaces не включены (WARN 2.9)

Причина: не настроен userns-remap.
Плохо: снижает изоляцию между root в контейнере и хостом (хотя это не “прямой root”, но риск выше).

***
- [x] 6. Опишите влияния уязвимостей, их сценарий атаки

#### Сценарий CR (компрометация хоста через контейнер)

Атакующий находит уязвимость в веб-сервисе vulnerable-web (например, RCE в приложении, уязвимый модуль, плохая конфигурация).

Получив shell в контейнере, он использует:

docker.sock (WARN 5.32) или

privileged+capabilities (WARN 5.5/5.4)

Дальше типовой путь:

через docker.sock создаёт новый контейнер с -v /:/host и --privileged, читает/меняет файлы хоста → полный захват хоста;

либо использует привилегии для доступа к устройствам/ядру → эскалация на хост.
Влияние: полный контроль над системой, доступ к секретам, lateral movement по сети.

#### Сценарий DL (утечка данных)

Компрометируется контейнер vulnerable-web или app.

Через доступ к сети хоста (--network host) и отсутствие сегментации атакующий может сканировать внутренние сервисы.

Если на хосте/в контейнере доступны конфиги/логи/переменные окружения, можно добыть креды/ключи.

Данные эксфильтруются наружу.
Влияние: утечка БД/секретов/конфигураций, возможные дальнейшие атаки.

#### Сценарий DoS (отказ в обслуживании)

При отсутствии ограничений CPU/memory/pids контейнер может:

случайно или намеренно “съесть” ресурсы → падение сервисов и хоста.

***

#### 1) docker-compose.yml — риски
insecure-db (PostgreSQL)

Небезопасно:

POSTGRES_PASSWORD=root — пароль тривиальный и хранится в явном виде → легко подобрать/утечь (git, логи, docker inspect).

ports: "5432:5432" — база доступна снаружи (на всех интерфейсах), расширяет поверхность атаки (сканирование, brute-force, эксплойты).

креды совпадают с тем, что в DB_URL приложения → одна утечка = полный доступ к БД.

Риски:

DL высокий: прямой доступ к данным при подборе/утечке пароля.

CR средний: БД может стать точкой входа/плацдармом в сети контейнеров (внутреннее перемещение).

app (python)

Небезопасно:

APP_SECRET_KEY=hardcoded-in-env — секрет в YAML → утечёт в git/логи/inspect.

DB_URL=...:root@... — пароль в строке подключения прямо в YAML.

DEBUG=true — повышает информативность ошибок, иногда даёт доступ к отладочным механизмам → облегчает эксплуатацию.

volumes: ./app:/app:rw — контейнер может писать в код на хосте. При RCE атакующий внедрит бэкдор в файлы проекта (устойчивое закрепление).

Риски:

DL высокий: утечка секретов, строк подключения, внутренней информации через debug/логи.

CR высокий: RCE в контейнере + RW-mount → подмена кода на хосте, закрепление.

vulnerable-web (nginx)

Небезопасно/сомнительно:

ports: "8080:80" — открыт наружу на всех интерфейсах. Для локальной лабораторной лучше ограничить 127.0.0.1:8080:80.

Плюсы: nginx.conf:ro, no-new-privileges:true, user: nginx — это хорошо.

Риски:

CR средний: внешний доступ повышает шанс эксплуатации уязвимостей/ошибок конфигурации.

DL средний: если через nginx проксируются внутренние данные, утечка возможна при неправильной конфигурации.

#### 2) Сценарии реализации рисков для docker-compose.yml
DL (утечка данных)

Сценарий: утечка compose/YAML или доступ к контейнеру

docker-compose.yml попадает в чужие руки (репозиторий, архив, шаринг) или атакующий получает доступ к контейнеру и делает docker inspect.

Видит DB_URL и пароль root, APP_SECRET_KEY.

Подключается к Postgres (порт 5432 открыт наружу) и выгружает данные → DL.

CR (компрометация)

Сценарий: RCE в app + RW volume

В app находится уязвимость (например, небезопасная обработка данных).

Атакующий получает выполнение кода внутри контейнера.

Благодаря ./app:/app:rw он модифицирует app.py на хосте (внедряет бэкдор).

Бэкдор сохраняется после перезапуска → компрометация проекта/хоста (CR).

Исправленный docker-compose.yml

```yml
version: "3.8"

services:
  vulnerable-web:
    image: nginx:alpine
    container_name: vulnerable-nginx
    depends_on:
      - insecure-db
      - app
    ports:
      - "127.0.0.1:8080:80"
    volumes:
      - ./config/nginx.conf:/etc/nginx/nginx.conf:ro
    user: "nginx"
    read_only: true
    security_opt:
      - no-new-privileges:true

  insecure-db:
    image: postgres:16-alpine
    container_name: insecure-db
    environment:
      POSTGRES_DB: vulnapp
      POSTGRES_USER: vulnuser
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    secrets:
      - db_password
    # Не публикуем порт БД наружу (доступен в сети docker)
    # Если нужно подключаться с хоста: "127.0.0.1:5432:5432"
    # ports:
    #   - "127.0.0.1:5432:5432"
    volumes:
      - ./db/init.sql:/docker-entrypoint-initdb.d/init.sql:ro
      - dbdata:/var/lib/postgresql/data
    security_opt:
      - no-new-privileges:true

  app:
    image: python:3.11-alpine
    container_name: vulnerable-app
    depends_on:
      - insecure-db
    working_dir: /app
    volumes:
      - ./app:/app:ro
    command: ["python", "app.py"]
    environment:
      DEBUG: "false"
      DB_HOST: insecure-db
      DB_PORT: "5432"
      DB_NAME: vulnapp
      DB_USER: vulnuser
    secrets:
      - db_password
      - app_secret_key
    read_only: true
    security_opt:
      - no-new-privileges:true
    ports:
      - "127.0.0.1:5001:5000"

volumes:
  dbdata:

secrets:
  db_password:
    file: ./secrets/db_password.txt
  app_secret_key:
    file: ./secrets/app_secret_key.txt
```
#### vulnerable-app.yml — риски

vulnerable-web

Критично небезопасно:

privileged: true + cap_add: [ALL] → контейнер почти как root на хосте.

network_mode: host → общий сетевой стек с хостом.

pid: host → общий процессный namespace (видны процессы хоста).

user: "0:0" → контейнер работает root’ом.

security_opt: apparmor:unconfined и seccomp:unconfined → отключены профили защиты.

volumes: /:/hostroot:rw → полный доступ на запись ко всей ФС хоста.

- /var/run/docker.sock:/var/run/docker.sock → фактически полный контроль Docker на хосте из контейнера.

./config/nginx.conf:...:rw → конфиг можно менять из контейнера.

ADMIN_PASSWORD, DB_PASSWORD, FLAG в env → секреты в явном виде.

command: apt-get update && apt-get install ... при старте → тянет пакеты на лету (нестабильно и небезопасно), увеличивает поверхность атаки.

Риски:

CR максимальный (критический): это почти гарантированный захват хоста при любом RCE в контейнере.

DL максимальный: доступ к /hostroot и к Docker сокету → утечка любых данных хоста/контейнеров.

debug-shell

Критично небезопасно:

privileged: true, network_mode: host, pid: host, user: 0:0

ports: "22:22" — открывает SSH наружу

SSH_PASSWORD=password, PermitRootLogin=yes, PasswordAuthentication=yes → root по паролю “password”

/:/hostroot:rw → полный RW доступ к хосту

Риски:

CR критический: любой извне может попытаться зайти по SSH (bruteforce, угадывание) и получит root.

DL критический: доступ к файловой системе хоста.

#### Сценарии реализации рисков для vulnerable-app.yml
CR (компрометация хоста)

Сценарий 1: SSH в debug-shell

Порт 22 открыт наружу.

root/password легко угадывается/подбирается.

Злоумышленник получает shell в контейнере, который privileged и с /hostroot:rw.

Модифицирует /hostroot/etc/sudoers, добавляет ключи в /hostroot/root/.ssh/authorized_keys → полный захват хоста.

Сценарий 2: docker.sock из vulnerable-web

RCE или доступ в контейнер vulnerable-web.

Через /var/run/docker.sock запускается новый контейнер с --privileged -v /:/host.

Дальше чтение/изменение файлов хоста → CR.

DL (утечка данных)

В vulnerable-web или debug-shell есть доступ к /hostroot:rw.

Читаются /hostroot/home/*, /hostroot/etc/*, ключи, конфиги, базы, токены.

Данные выводятся наружу (curl, scp, и т.д.) → DL.

Исправленный vulnerable-app.yml

```yml
version: "3.8"

services:
  vulnerable-web:
    image: nginx:alpine
    container_name: vulnerable-web
    user: "nginx"
    ports:
      - "127.0.0.1:8080:80"
    volumes:
      - ./config/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./backup:/var/backups:rw
    read_only: true
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL

  debug-shell:
    image: alpine:latest
    container_name: debug-shell
    # НЕ публикуем SSH наружу. Для отладки: docker exec -it debug-shell sh
    command: ["sh", "-c", "sleep infinity"]
    read_only: true
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
```

- [ ] 8. Сделайте анализ уязвимостей из сгенерированных файлов .odt, .xslx и опишите их в отчете. Файлы конвертируются в эти директории

```bash
"├── json/          (Trivy JSON outputs)"
"├── text/          (CIS audit text outputs)"
"├── xlsx/          (Excel spreadsheets)"
"└── odt/           (OpenDocument Text files)"
```

1.Контейнер vulnerable-web запущен с избыточными привилегиями (privileged, CapAdd=ALL, host network/pid, RW rootfs, docker.sock), что при любой уязвимости в веб-сервисе позволяет атакующему полностью скомпрометировать хост. Это формирует критический риск CR.

2.Секреты и учётные данные (пароли БД, ключи приложения, FLAG) хранятся в YAML и переменных окружения, что упрощает их утечку через репозиторий, логи или docker inspect. Это создаёт высокий риск DL даже без эксплуатации CVE.

3.Отсутствие ограничений ресурсов и healthcheck позволяет контейнерам потреблять неограниченное CPU/память и усложняет обнаружение отказов и компрометации, что повышает риск DoS и скрытых атак.

4.Использование host-namespace (network, pid) и монтирование чувствительных каталогов хоста (/, /var/run/docker.sock) разрушает изоляцию контейнеров и делает модель безопасности Docker неэффективной.

- [x] 9. Подготовьте отчет `gist`.
- [x] 10. Почистите кеш от `venv` и остановите уязвимостей приложение, почистите контейнера

```bash
$ rm -rf venv
$ docker-compose -f demo-vulnerable-app.yml down
$ docker system prune -f
```

***

Copyright (c) 2026 Stratienko Ilya
