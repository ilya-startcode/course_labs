<div align="center">
<h1><a id="intro">Лабораторная работа №5</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Балашов.Д.В.-8b9aff" alt="Contributor Badge"></a></div>

***

Данная лабораторная работа посвещена изучению Docker и как с ним работать. Эта лабораторная работа послужит подпоркой для старта в выявлении и определении уязвимостей на уровне сканирования контейнеров при сборке приложений. 

***

## Задание

- [ ] 1. Поставьте `Docker` и `buildkit`

```bash
$ brew install buildkit
$ brew install docker
```

- [ ] 2. Перейдите в `source` и выведите на терминале, далее проанализируйте следующие команды консоли

```bash
┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ docker buildx build -t hellow-appsec-world .
[+] Building 10.1s (13/13) FINISHED                                                                docker:default
 => [internal] load build definition from Dockerfile                                                         0.0s
 => => transferring dockerfile: 429B                                                                         0.0s 
 => [internal] load metadata for docker.io/library/python:3.11-slim                                          2.0s 
 => [internal] load .dockerignore                                                                            0.0s
 => => transferring context: 2B                                                                              0.0s 
 => [internal] load build context                                                                            0.0s 
 => => transferring context: 477B                                                                            0.0s 
 => [builder 1/4] FROM docker.io/library/python:3.11-slim@sha256:c24e9effa2821a6885165d930d939fec2af0dcf819  3.7s 
 => => resolve docker.io/library/python:3.11-slim@sha256:c24e9effa2821a6885165d930d939fec2af0dcf819276138f1  0.0s
 => => sha256:89abad2fb0c3633705054018ae09caae4bd0e0febf57fb57a96fd41769c94e12 1.75kB / 1.75kB               0.0s 
 => => sha256:fa659464a114c340e31c7b7954a1aa679de7e7f5346e4b5804e8422b2596aff9 5.47kB / 5.47kB               0.0s 
 => => sha256:119d43eec815e5f9a47da3a7d59454581b1e204b0c34db86f171b7ceb3336533 29.77MB / 29.77MB             1.9s 
 => => sha256:5b09819094bb89d5b2416ff2fb03f68666a5372c358cfd22f2b62d7f6660d906 1.29MB / 1.29MB               1.1s
 => => sha256:3e731abb5c1dd05aef62585d392d31ad26089dc4c031730e5ab0225aef80b3f2 14.36MB / 14.36MB             1.4s
 => => sha256:c24e9effa2821a6885165d930d939fec2af0dcf819276138f11dd45e200bd032 10.37kB / 10.37kB             0.0s
 => => sha256:0b2bf04f68e9f306a8a83f57c6ced322a23968bf3d5acebc07e055c090240826 250B / 250B                   1.5s 
 => => extracting sha256:119d43eec815e5f9a47da3a7d59454581b1e204b0c34db86f171b7ceb3336533                    1.1s
 => => extracting sha256:5b09819094bb89d5b2416ff2fb03f68666a5372c358cfd22f2b62d7f6660d906                    0.1s
 => => extracting sha256:3e731abb5c1dd05aef62585d392d31ad26089dc4c031730e5ab0225aef80b3f2                    0.6s 
 => => extracting sha256:0b2bf04f68e9f306a8a83f57c6ced322a23968bf3d5acebc07e055c090240826                    0.0s
 => [builder 2/4] WORKDIR /hello                                                                             0.1s 
 => [builder 3/4] COPY requirements.txt .                                                                    0.0s 
 => [builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt         2.7s 
 => [stage-1 3/6] COPY --from=builder /wheels /wheels                                                        0.0s 
 => [stage-1 4/6] COPY requirements.txt .                                                                    0.0s 
 => [stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt                        1.2s 
 => [stage-1 6/6] COPY hello.py .                                                                            0.0s 
 => exporting to image                                                                                       0.1s 
 => => exporting layers                                                                                      0.1s 
 => => writing image sha256:743c942938742217d8e6d275f227a4fe24f9b2ff1b04d3bad043366e072d41cb                 0.0s
 => => naming to docker.io/library/hellow-appsec-world                  
 
 
 ┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ docker run hellow-appsec-world
hello appsec world

┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ docker run --rm -it hellow-appsec-world
hello appsec world

┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ docker save -o hello.tar hellow-appsec-world

                                                                                                                  
┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ docker load -i hello.tar
Loaded image: hellow-appsec-world:latest
```
- [ ] 3. Откройте `Dockerfile` и сделайте его анализ. Сделайте `commit`
```dockerfile
┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ cat Dockerfile 
# Этап 1: сборка зависимостей
FROM python:3.11-slim AS builder
WORKDIR /hello
# Копируем файл с зависимостями
COPY requirements.txt . 
# Устанавливаем зависимости в отдельную директорию wheelhouse для кеширования
RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt

# Этап 2: запускаемый образ
FROM python:3.11-slim
WORKDIR /hello
# Копируем файл с зависимостями
COPY --from=builder /wheels /wheels # Копируем собранные wheel-пакеты
COPY requirements.txt . 
# Устанавливаем зависимости из wheel-пакетов
RUN pip install --no-index --find-links=/wheels -r requirements.txt
# Копируем исходный код приложения
COPY hello.py .

# Переменные окружения для улучшенной работы Python
ENV PYTHONUNBUFFERED=1
# Запускаем приложение
CMD ["python", "hello.py"] 


┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ git add Dockerfile
                                                                                                                  
┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ git commit -m "lab5: analyse original Dockerfile"
[lab05-ilya ffe261c] lab5: analyse original Dockerfile
 1 file changed, 14 insertions(+), 5 deletions(-)```

- [ ] 4. Замените в `Dockerfile`значение скрипта на `python` тем, который вы сделали ранее в прошлых лабораторных работах. Вложите свой файл `python` в директорию. Сделайте анализ своего измененного `Dockerfile` и внесите изменения. Сделайте `commit`. 

```py
import base64
import typer


def main(
    name: str = typer.Argument(...),
    lastname: str = typer.Option("", "--lastname", "-l"),
) -> None:
    greeting = base64.b64decode(b"SGVsbG8gYXBwc2Vjd29ybGQ=").decode()
    tail = f"@{name}" + (f" {lastname}" if lastname else "")
    typer.echo(f"{greeting} from {tail}")


if __name__ == "__main__":
    typer.run(main)

┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ git add hello.py                                 
                                                                                                                  
┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ git commit -m "lab5: use custom hello.py & multi-stage build"
[lab05-ilya 68a910f] lab5: use custom hello.py & multi-stage build
 1 file changed, 10 insertions(+), 12 deletions(-)
```

- [ ] 5. Выведите на терминале и проанализируйте следующие команды консоли. Сравните хеш сумму вашего архива с `image.tar` из репозитория, выведите на терминал.

```bash
┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ docker buildx build -t hellow-appsec-world .
[+] Building 0.5s (13/13) FINISHED                                                                 docker:default
 => [internal] load build definition from Dockerfile                                                         0.0s
 => => transferring dockerfile: 1.12kB                                                                       0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                          0.4s
 => [internal] load .dockerignore                                                                            0.0s
 => => transferring context: 2B                                                                              0.0s
 => [internal] load build context                                                                            0.0s
 => => transferring context: 65B                                                                             0.0s
 => [builder 1/4] FROM docker.io/library/python:3.11-slim@sha256:c24e9effa2821a6885165d930d939fec2af0dcf819  0.0s
 => CACHED [builder 2/4] WORKDIR /hello                                                                      0.0s
 => CACHED [builder 3/4] COPY requirements.txt .                                                             0.0s
 => CACHED [builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt  0.0s
 => CACHED [stage-1 3/6] COPY --from=builder /wheels /wheels                                                 0.0s
 => CACHED [stage-1 4/6] COPY requirements.txt .                                                             0.0s
 => CACHED [stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt                 0.0s
 => CACHED [stage-1 6/6] COPY hello.py .                                                                     0.0s
 => exporting to image                                                                                       0.0s
 => => exporting layers                                                                                      0.0s
 => => writing image sha256:e39aed33563bffcae7e8b662662822340c3c61620c22f9f76aecb13ede5b1603                 0.0s
 => => naming to docker.io/library/hellow-appsec-world                                                       0.0s
                                                                                                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ docker run hellow-appsec-world ilya           
Hello appsecworld from @ilya

┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ docker save -o hello_your_project.tar hellow-appsec-world
                                                                                                                 
┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ sha256sum hellow_your_project.tar
sha256sum: hellow_your_project.tar: No such file or directory
                                                                                                                 
┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ sha256sum hello_your_project.tar 
c884b5994540b246d7d729ed474e367a0ba9497f53c748d771d3b01dfa255474  hello_your_project.tar
                                                                                                                 
┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ docker load -i hello_your_project.tar
Loaded image: hellow-appsec-world:latest

                                                     
┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ docker run hellow-appsec-world ilya 
Hello appsecworld from @ilya


┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ docker load -i hello.tar             
The image hellow-appsec-world:latest already exists, renaming the old one with ID sha256:e39aed33563bffcae7e8b662662822340c3c61620c22f9f76aecb13ede5b1603 to empty string
Loaded image: hellow-appsec-world:latest
                                                                                                                 
┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ sha256sum hello.tar 
4c4cf30cd103c1ef1d5213403741044bfb6add2c1710e751a63b973f74a8b60f  hello.tar
```

- [ ] 6. Доработайте свой `python` скрипт подключаемыми библиотеками, далее их необходимо разместить в `requirements.txt`. Размещение библиотек в следующем формате:

```
┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ cat > requirements.txt <<'EOF'
flask==3.0.2
werkzeug==3.0.1
requests==2.28.1
typer==0.12.5
EOF```

```py
import base64
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    name   = request.args.get("name",   default="user", type=str)
    lastname = request.args.get("lastname", default="",   type=str)
    greeting = base64.b64decode(b"SGVsbG8gYXBwc2Vjd29ybGQ=").decode()
    tail     = f"@{name}" + (f" {lastname}" if lastname else "")
    return f"{greeting} from {tail}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
 ```

- [ ] 7. Сделайте `commit`. Повторите сборку приложения по вашему `Dockerfile` для доработанного скрипта `python`. Сохраните `image` в виде .`tar` архива. Сделайте `commit`.

```
┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ git add requirements.txt hello.py 
                                                                                                                 
┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ git commit -m "lab5: add requirements.txt & Flask-wrapper for typer script"
[lab05-ilya b09a6c3] lab5: add requirements.txt & Flask-wrapper for typer script
 2 files changed, 13 insertions(+), 9 deletions(-)

 ┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ docker buildx build -t hellow-appsec-world .
[+] Building 1.0s (13/13) FINISHED                                                                docker:default
 => [internal] load build definition from Dockerfile                                                        0.0s
 => => transferring dockerfile: 1.12kB                                                                      0.0s 
 => [internal] load metadata for docker.io/library/python:3.11-slim                                         0.9s 
 => [internal] load .dockerignore                                                                           0.0s
 => => transferring context: 2B                                                                             0.0s 
 => [internal] load build context                                                                           0.0s 
 => => transferring context: 547B                                                                           0.0s 
 => [builder 1/4] FROM docker.io/library/python:3.11-slim@sha256:c24e9effa2821a6885165d930d939fec2af0dcf81  0.0s 
 => CACHED [builder 2/4] WORKDIR /hello                                                                     0.0s 
 => CACHED [builder 3/4] COPY requirements.txt .                                                            0.0s 
 => CACHED [builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.tx  0.0s 
 => CACHED [stage-1 3/6] COPY --from=builder /wheels /wheels                                                0.0s 
 => CACHED [stage-1 4/6] COPY requirements.txt .                                                            0.0s 
 => CACHED [stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt                0.0s 
 => [stage-1 6/6] COPY hello.py .                                                                           0.0s 
 => exporting to image                                                                                      0.0s 
 => => exporting layers                                                                                     0.0s 
 => => writing image sha256:2c4bd2d430b861d176e549783287507f66bff813b2871ec114ca329153e4c47d                0.0s 
 => => naming to docker.io/library/hellow-appsec-world                                                      0.0s 
                                                                                                                 
┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ docker run -p 8000:5000 hellow-appsec-world 
 * Serving Flask app 'hello'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.                                                                                                            
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
^C                                    


┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ docker save -o hello_with_deps.tar hellow-appsec-world
                                                                                                                 
┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ git add hello_with_deps.tar
                                                                                                                 
┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ git commit -m "add hello-with_deps.tar image"
[lab05-ilya cc44ccd] add hello-with_deps.tar image
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 labs/lab05/source/hello_with_deps.tar 
```

- [ ] 8. Выведите на терминале и проанализируйте следующие команды консоли

```bash
┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ docker login

USING WEB-BASED LOGIN
To sign in with credentials on the command line, use 'docker login -u <username>'

Your one-time device confirmation code is: JDSP-FDKD
Press ENTER to open your browser or submit your device code here: https://login.docker.com/activate

Waiting for authentication in the browser…

WARNING! Your password will be stored unencrypted in /home/kali/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credential-stores

Login Succeeded


┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ docker info | grep -i username

 Username: ilyadock1
                                                                                                               
┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ docker tag hellow-appsec-world ilyadock1/hellow-appsec-world
                                                                                                               
┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ docker push ilyadock1/hellow-appsec-world                
Using default tag: latest
The push refers to repository [docker.io/ilyadock1/hellow-appsec-world]
09a9d53f3465: Pushed 
ecd902aa28a7: Pushed 
4f94a640bf7c: Pushed 
ec6574a715e5: Pushed 
24eb23f5d2c3: Pushed 
49d74831a287: Pushed 
5d89b1d5fc98: Pushed 
523062ea36b5: Pushed 
e50a58335e13: Pushed 
latest: digest: sha256:9a1421241d4fdd32eb2be9449683dd1a69b98ee09fa00e9a8e092472a6fdf6e2 size: 2202


┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$  docker inspect ilyadock1/hellow-appsec-world
[
    {
        "Id": "sha256:2c4bd2d430b861d176e549783287507f66bff813b2871ec114ca329153e4c47d",
        "RepoTags": [
            "ilyadock1/hellow-appsec-world:latest",
            "kov/hellow-appsec-world:latest",
            "hellow-appsec-world:latest"
        ],
        "RepoDigests": [
            "ilyadock1/hellow-appsec-world@sha256:9a1421241d4fdd32eb2be9449683dd1a69b98ee09fa00e9a8e092472a6fdf6e2"
        ],
        "Parent": "",
        "Comment": "buildkit.dockerfile.v0",
        "Created": "2026-01-14T09:41:56.820346553-05:00",
        "DockerVersion": "",
        "Author": "",
        "Config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "LANG=C.UTF-8",
                "GPG_KEY=A035C8C19219BA821ECEA86B64E628F8D684696D",
                "PYTHON_VERSION=3.11.14",
                "PYTHON_SHA256=8d3ed8ec5c88c1c95f5e558612a725450d2452813ddad5e58fdb1a53b1209b78",
                "PYTHONUNBUFFERED=1"
            ],
            "Cmd": null,
            "Image": "",
            "Volumes": null,
            "WorkingDir": "/hello",
            "Entrypoint": [
                "python",
                "hello.py"
            ],
            "OnBuild": null,
            "Labels": null
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 157203584,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/i2juv1p661kh8saeweak6x6k4/diff:/var/lib/docker/overlay2/dilpdqobxyy5fkm8uh3dwl1g8/diff:/var/lib/docker/overlay2/j226rw3b4vdu5433z2bfwasi8/diff:/var/lib/docker/overlay2/xjjddj8i97ee5vlpnt9dughos/diff:/var/lib/docker/overlay2/84a5ce2bbd43133dd4ee2029144726a7b30fd16167c262f241730bf3f4c8c7b5/diff:/var/lib/docker/overlay2/346263ed9efd8d453f4bd75c66265c82b884d36e7193ecd6253723d8ee0abf90/diff:/var/lib/docker/overlay2/2f2e36e715a1ae6288d4b805beeb5465734498b6734e6fae802b070168497d35/diff:/var/lib/docker/overlay2/3b059de688d23ce0b522e1844198c3c80d6d2da91896b20793632961ed01ed75/diff",
                "MergedDir": "/var/lib/docker/overlay2/p49yqsqedwvi1w78nu59076rj/merged",
                "UpperDir": "/var/lib/docker/overlay2/p49yqsqedwvi1w78nu59076rj/diff",
                "WorkDir": "/var/lib/docker/overlay2/p49yqsqedwvi1w78nu59076rj/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:e50a58335e1366e2581fe61794c1651afe2fe04e881e795aa166f24f4fc78d92",
                "sha256:523062ea36b5189e9ea6d7d86850296d1d7b5b4418109217e7ac12e13273fbba",
                "sha256:5d89b1d5fc98cb4fa0c3a8ac89cf83932b8b287e318b7761badd4b9ce58b3ecb",
                "sha256:49d74831a2871d1733e397932626f721303aef93edc180602b0877d68c6cbf5a",
                "sha256:24eb23f5d2c3163d0940480fc365722383ea382eab72c03d9bdc790cd4e6473d",
                "sha256:ec6574a715e54378f03811a6311d3f303d61ea096ec37a6869e1b4025a4473cb",
                "sha256:4f94a640bf7cd4a1439ef63436213f162be9508023abfd69ae1d9a6ec4805fee",
                "sha256:ecd902aa28a72ddbc468c083fb324fe80f899c40aa2972e3076251e4ed70dc51",
                "sha256:09a9d53f3465357fe600a76c7c28f4d7b143a6ae70befb170fca3c4f2bb5e66e"
            ]
        },
        "Metadata": {
            "LastTagTime": "2026-01-14T09:50:23.091597304-05:00"
        }
    }
]
                                                                                                               
┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ docker container create --name first hellow-appsec-world
d20d08dc92cea7c5ba7178728ae7e790c434fe415874ed6c22dc34028b21fce4



┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ docker image pull geminishkvdev/hello-appsec-world 
Using default tag: latest
latest: Pulling from geminishkvdev/hello-appsec-world
no matching manifest for linux/amd64 in the manifest list entries
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ docker inspect geminishkvdev/hello-appsec-world
[]
Error: No such object: geminishkvdev/hello-appsec-world


┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ docker container create --name second hellow-appsec-world
28f61543feb33a4c875025c1bb6f80ab2c6afbe85098729ccea5d37a8f608bd4
```

- [ ] 9. Выведите на терминале и проанализируйте в консоли процессы, которые запущены, владельцев по пользователям

```bash 
                                                                              
──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ docker container run -it ubuntu /bin/bash
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
20043066d3d5: Already exists 
Digest: sha256:c35e29c9450151419d9448b0fd75374fec4fff364a27f176fb458d472dfc9e54
Status: Downloaded newer image for ubuntu:latest
root@6a2fe6d15e80:/# ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.1  0.0   4596  3960 pts/0    Ss   14:56   0:00 /bin/bash
root           9  0.0  0.0   7896  4060 pts/0    R+   14:56   0:00 ps aux
root@6a2fe6d15e80:/# 
```
 
- [ ] 10. Выведите оба контейнера first и second на терминал
```
┌──(.venv)─(kali㉿kali)-[~/…/course_labs/labs/lab05/source]
└─$ docker ps -a | grep -E "first|second"
6a2fe6d15e80   ubuntu                         "/bin/bash"               49 seconds ago       Exited (0) 9 seconds ago                                                                                                                                      sad_elgamal
28f61543feb3   hellow-appsec-world            "python hello.py"         About a minute ago   Created                                                                                                                                                       second
d20d08dc92ce   hellow-appsec-world            "python hello.py"         4 minutes ago        Created                                                                                                                                                       first```
- [ ] 11. Перейдите в основной корень `lab05` и выведите на терминале, и проанализируйте

```bash 
┌──(.venv)─(kali㉿kali)-[~/work/course_labs/labs/lab05]
└─$ docker-compose up --build
WARN[0000] /home/kali/work/course_labs/labs/lab05/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Building 7.8s (25/25) FINISHED                                                            docker:default
 => [server internal] load build definition from Dockerfile                                             0.0s
 => => transferring dockerfile: 419B                                                                    0.0s 
 => [client internal] load metadata for docker.io/library/python:3.11-slim                              0.4s 
 => [server internal] load .dockerignore                                                                0.0s
 => => transferring context: 2B                                                                         0.0s 
 => [server internal] load build context                                                                0.0s 
 => => transferring context: 63B                                                                        0.0s 
 => [client builder 1/4] FROM docker.io/library/python:3.11-slim@sha256:c24e9effa2821a6885165d930d939f  0.0s 
 => CACHED [client builder 2/4] WORKDIR /app                                                            0.0s 
 => CACHED [server builder 3/4] COPY requirements.txt .                                                 0.0s 
 => CACHED [server builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requ  0.0s 
 => CACHED [server stage-1 3/6] COPY --from=builder /wheels /wheels                                     0.0s 
 => CACHED [server stage-1 4/6] COPY requirements.txt .                                                 0.0s 
 => [server stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt            1.4s 
 => [server stage-1 6/6] COPY app.py .                                                                  0.0s
 => [server] exporting to image                                                                         0.1s
 => => exporting layers                                                                                 0.1s
 => => writing image sha256:c7f769bb9291afe8c727be28e99532c9074652d6cf51a2b943debf0c905e1e25            0.0s
 => => naming to docker.io/library/lab05-server                                                         0.0s 
 => [server] resolving provenance for metadata file                                                     0.0s 
 => [client internal] load build definition from Dockerfile                                             0.0s
 => => transferring dockerfile: 425B                                                                    0.0s 
 => [client internal] load .dockerignore                                                                0.0s 
 => => transferring context: 2B                                                                         0.0s 
 => [client internal] load build context                                                                0.0s 
 => => transferring context: 576B                                                                       0.0s 
 => [client builder 3/4] COPY requirements.txt .                                                        0.0s 
 => [client builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirement  4.1s 
 => [client stage-1 3/6] COPY --from=builder /wheels /wheels                                            0.0s
 => [client stage-1 4/6] COPY requirements.txt .                                                        0.0s 
 => [client stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt            1.4s 
 => [client stage-1 6/6] COPY client.py .                                                               0.0s 
 => [client] exporting to image                                                                         0.1s 
 => => exporting layers                                                                                 0.1s 
 => => writing image sha256:fa97d1e55887d17a994c4a88c1e79385b3d0e175db945d1c878b01eff274ba5f            0.0s 
 => => naming to docker.io/library/lab05-client                                                         0.0s 
 => [client] resolving provenance for metadata file                                                     0.0s 
[+] Running 5/5
 ✔ client                    Built                                                                      0.0s 
 ✔ server                    Built                                                                      0.0s 
 ✔ Network lab05_app_net     Created                                                                    0.2s 
 ✔ Container lab05-server-1  Created                                                                    0.0s 
 ✔ Container lab05-client-1  Created                                                                    0.0s 
Attaching to client-1, server-1
server-1  |  * Serving Flask app 'app'
server-1  |  * Debug mode: off
server-1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
server-1  |  * Running on all addresses (0.0.0.0)
server-1  |  * Running on http://127.0.0.1:8000
server-1  |  * Running on http://172.20.0.2:8000
server-1  | Press CTRL+C to quit
server-1  | 172.20.0.3 - - [14/Jan/2026 14:58:37] "GET / HTTP/1.1" 200 -
client-1  | 
client-1  |     <html>                                                                                       
client-1  |     <head><title>Colorful Output</title></head>                                                  
                                                                                                             
                                                                                                             
w Enable Watch      
```

- [ ] 12. Откройте соседнее окно терминала и и выведите на терминале

```bash 
┌──(kali㉿kali)-[~/work/course_labs/labs/lab05]
└─$ open -a "Google Chrome" http://localhost:8000
xdg-open: unexpected option '-a'
Try 'xdg-open --help' for more information.
                                                                                                             
┌──(kali㉿kali)-[~/work/course_labs/labs/lab05]
└─$ curl -I http://localhost:8000
HTTP/1.1 200 OK
Server: Werkzeug/2.3.7 Python/3.11.14
Date: Wed, 14 Jan 2026 15:00:21 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 761
Connection: close
```

- [ ] 13. Остановите работу `docker-compose`.

```bash 
┌──(.venv)─(kali㉿kali)-[~/work/course_labs/labs/lab05]
└─$ docker ps -a                         
CONTAINER ID   IMAGE                          COMMAND                   CREATED          STATUS                       PORTS                                                                                                                             NAMES
2ddb726ce3a0   lab05-client                   "python client.py"        2 minutes ago    Exited (0) 16 seconds ago                                                                                                                                      lab05-client-1
f577d462b790   lab05-server                   "python app.py"           2 minutes ago    Exited (137) 5 seconds ago                                                                                                                                     lab05-server-1
6a2fe6d15e80   ubuntu                         "/bin/bash"               5 minutes ago    Exited (0) 4 minutes ago                                                                                                                                       sad_elgamal
28f61543feb3   hellow-appsec-world            "python hello.py"         5 minutes ago    Created                                                                                                                                                        second
d20d08dc92ce   hellow-appsec-world            "python hello.py"         9 minutes ago    Created                                                                                                                                                        first
30144d12eefa   hellow-appsec-world            "python hello.py"         19 minutes ago   Exited (0) 19 minutes ago                                                                                                                                      intelligent_rosalind
1130dd1e2f27   154db30a4008                   "python hello.py"         21 minutes ago   Exited (1) 20 minutes ago                                                                                                                                      sharp_bouman
f7c3396d333a   e14ccc7bd47c                   "python hello.py"         24 minutes ago   Exited (1) 24 minutes ago                                                                                                                                      awesome_lovelace
a4f1b87a7766   e39aed33563b                   "python hello.py ilya"    31 minutes ago   Exited (0) 31 minutes ago                                                                                                                                      lucid_jennings
a06dd8acd00e   e39aed33563b                   "python hello.py"         31 minutes ago   Exited (2) 31 minutes ago                                                                                                                                      zen_dubinsky
e9f28f3148de   e39aed33563b                   "python hello.py ilya"    33 minutes ago   Exited (0) 33 minutes ago                                                                                                                                      quizzical_easley
7fabac185b2d   e39aed33563b                   "python hello.py ily…"    33 minutes ago   Exited (2) 33 minutes ago                                                                                                                                      infallible_margulis
bf857cfb963f   a884ca2664c4                   "ilya stratienko"         35 minutes ago   Created                                                                                                                                                        vigilant_chatterjee
999c88b96224   a884ca2664c4                   "python hello.py"         35 minutes ago   Exited (2) 35 minutes ago                                                                                                                                      elegant_sutherland
01dd42632438   6ed5842510de                   "python hello.py"         36 minutes ago   Exited (1) 36 minutes ago                                                                                                                                      stoic_dijkstra
4a5243d8ccef   6ed5842510de                   "python hello.py"         39 minutes ago   Exited (1) 39 minutes ago                                                                                                                                      keen_haslett
7c55ed75dabc   743c94293874                   "python hello.py"         52 minutes ago   Exited (0) 52 minutes ago                                                                                                                                      loving_matsumoto
8eac96d2f8cf   registry:2                     "/entrypoint.sh /etc…"    22 hours ago     Up 22 hours                  5000/tcp                                                                                                                          registry.1.k1oo72vz5ese0d6q3lo9kb539
07e17e50978a   registry:2                     "/entrypoint.sh /etc…"    23 hours ago     Exited (255) 22 hours ago    5000/tcp                                                                                                                          registry.1.08xbgp3f0dctddr4n66yhhxr7
b8b9d08c8f17   registry:2                     "/entrypoint.sh /etc…"    23 hours ago     Exited (255) 23 hours ago    5000/tcp                                                                                                                          registry.1.q9z9btf8xnexwm01ax0n7t13i
5016406d4962   registry:2                     "/entrypoint.sh /etc…"    23 hours ago     Exited (2) 23 hours ago                                                                                                                                        registry.1.jnhfh816618gx8fxwhg0cmd4y
30742c7eaf69   registry:2                     "/entrypoint.sh /etc…"    24 hours ago     Exited (2) 24 hours ago                                                                                                                                        registry.1.y0wv3vcllfkxy74z91q7lt2c1
c252673047ff   hadoop/historyserver:3.4.2     "/entrypoint.sh /run…"    2 weeks ago      Exited (255) 24 hours ago    0.0.0.0:8188->8188/tcp, :::8188->8188/tcp                                                                                         parallel_docker_hadoop_spark-historyserver-1
de4dcdafc7d1   hadoop/nodemanager:3.4.2       "/entrypoint.sh /run…"    2 weeks ago      Exited (255) 24 hours ago    0.0.0.0:8042->8042/tcp, :::8042->8042/tcp                                                                                         parallel_docker_hadoop_spark-nodemanager-1
e33ddcc8240a   jupyterlab/core:4.4.9          "/bin/sh -c 'jupyter…"    2 weeks ago      Exited (255) 24 hours ago    0.0.0.0:8888->8888/tcp, :::8888->8888/tcp                                                                                         jupyterlab
d5e1b062edb9   spark/core:3.5.7               "/bin/bash -c ' /opt…"    2 weeks ago      Exited (255) 24 hours ago                                                                                                                                      parallel_docker_hadoop_spark-spark-worker-2
59362b000dd3   spark/core:3.5.7               "/bin/bash -c ' /opt…"    2 weeks ago      Exited (255) 24 hours ago                                                                                                                                      parallel_docker_hadoop_spark-spark-worker-1
23211d8d8d2d   hadoop/resourcemanager:3.4.2   "/run.sh"                 2 weeks ago      Exited (255) 24 hours ago    0.0.0.0:8088->8088/tcp, :::8088->8088/tcp                                                                                         parallel_docker_hadoop_spark-resourcemanager-1
05372977cb69   hadoop/datanode:3.4.2          "/entrypoint.sh /run…"    2 weeks ago      Up 22 hours (healthy)        0.0.0.0:9864->9864/tcp, :::9864->9864/tcp                                                                                         parallel_docker_hadoop_spark-datanode-1
a7f842cf5dc9   hadoop/namenode:3.4.2          "/entrypoint.sh /run…"    2 weeks ago      Exited (255) 24 hours ago    0.0.0.0:9870->9870/tcp, :::9870->9870/tcp                                                                                         parallel_docker_hadoop_spark-namenode-1
3a2c7bfe2cde   spark/core:3.5.7               "/bin/bash -c '\n /op…"   2 weeks ago      Exited (255) 24 hours ago    0.0.0.0:4040->4040/tcp, :::4040->4040/tcp, 0.0.0.0:7077->7077/tcp, :::7077->7077/tcp, 0.0.0.0:8080->8080/tcp, :::8080->8080/tcp   parallel_docker_hadoop_spark-spark-master-1
dad223b4772c   apache/hive:4.0.1              "sh -c /entrypoint.sh"    2 weeks ago      Exited (255) 2 weeks ago     9083/tcp, 10000/tcp, 10002/tcp                                                                                                    parallel_docker_hive_flink-hiveserver2-standalone-1
3bf7612022dc   flink/core:2.1.1               "/docker-entrypoint.…"    2 weeks ago      Exited (255) 2 weeks ago     6123/tcp, 8081/tcp                                                                                                                parallel_docker_hive_flink-taskmanager-1
d2120aa2ca6c   apache/hive:4.0.1              "sh -c /entrypoint.sh"    2 weeks ago      Exited (255) 2 weeks ago     9083/tcp, 10000/tcp, 10002/tcp                                                                                                    parallel_docker_hive_flink-metastore-standalone-1
0b23584c3604   flink/core:2.1.1               "/docker-entrypoint.…"    2 weeks ago      Exited (255) 2 weeks ago     6123/tcp, 0.0.0.0:8081->8081/tcp, :::8081->8081/tcp                                                                               jobmanager
6ab5a85568be   mariadb:12.1.2                 "docker-entrypoint.s…"    2 weeks ago      Exited (255) 2 weeks ago     0.0.0.0:3306->3306/tcp, :::3306->3306/tcp                                                                                         mariadb
e8cd4a2ba094   postgres:17.6                  "docker-entrypoint.s…"    2 weeks ago      Exited (255) 2 weeks ago     5432/tcp                                                                                                                          parallel_docker_hive_flink-some-postgres-1
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/work/course_labs/labs/lab05]
└─$ docker ps -q
8eac96d2f8cf
05372977cb69
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/work/course_labs/labs/lab05]
└─$ docker images                                     
REPOSITORY                      TAG       IMAGE ID       CREATED          SIZE
lab05-client                    latest    fa97d1e55887   3 minutes ago    138MB
lab05-server                    latest    c7f769bb9291   3 minutes ago    141MB
ilyadock1/hellow-appsec-world   latest    2c4bd2d430b8   19 minutes ago   157MB
kov/hellow-appsec-world         latest    2c4bd2d430b8   19 minutes ago   157MB
hellow-appsec-world             latest    2c4bd2d430b8   19 minutes ago   157MB
<none>                          <none>    154db30a4008   21 minutes ago   157MB
<none>                          <none>    e14ccc7bd47c   25 minutes ago   157MB
<none>                          <none>    a884ca2664c4   36 minutes ago   150MB
<none>                          <none>    e39aed33563b   36 minutes ago   150MB
<none>                          <none>    6ed5842510de   39 minutes ago   135MB
<none>                          <none>    743c94293874   54 minutes ago   135MB
hadoop/submit                   3.4.2     7051645ebc15   2 weeks ago      2.49GB
hadoop/historyserver            3.4.2     a2610f720654   2 weeks ago      2.49GB
hadoop/nodemanager              3.4.2     3c271148df9e   2 weeks ago      2.49GB
hadoop/resourcemanager          3.4.2     39aa427dc126   2 weeks ago      2.49GB
hadoop/datanode                 3.4.2     28d41b35d870   2 weeks ago      2.49GB
hadoop/namenode                 3.4.2     409cfd96ab85   2 weeks ago      2.49GB
hadoop/basic                    3.4.2     5729b681307b   2 weeks ago      2.49GB
jupyterlab/core                 4.4.9     4533a9e0c709   2 weeks ago      2.83GB
spark/core                      3.5.7     795dbd7dbf1d   2 weeks ago      2.4GB
flink/core                      2.1.1     8b469af469ef   2 weeks ago      1.21GB
hive/core                       4.0.1     5e6d98d49085   2 weeks ago      1.62GB
<none>                          <none>    502f1cff94ba   2 weeks ago      3.22GB
127.0.0.1:5000/mpi              latest    1454b4f07617   2 weeks ago      1.35GB
mariadb                         12.1.2    f90bc2981a93   7 weeks ago      335MB
postgres                        17.6      50903ccdcab5   2 months ago     453MB
ubuntu                          latest    c3a134f2ace4   2 months ago     78.1MB
apache/hive                     4.0.1     9bb619cde186   15 months ago    1.6GB
registry                        <none>    26b2eb03618e   2 years ago      25.4MB
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/work/course_labs/labs/lab05]
└─$ docker ps -q | xargs docker stop
8eac96d2f8cf
05372977cb69
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/work/course_labs/labs/lab05]
└─$  docker compose down 
WARN[0000] /home/kali/work/course_labs/labs/lab05/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Running 3/3
 ✔ Container lab05-client-1  Removed                                                                    0.0s 
 ✔ Container lab05-server-1  Removed                                                                    0.0s 
 ✔ Network lab05_app_net     Removed 
```
- [ ] 14. Доработайте `docker-compose` и скрипт, который вы подготовили ранее, что бы вы смогли воспроизвести шаги п.11 по п.13 с демонстрацией. Сделайте `commit`.

```
┌──(.venv)─(kali㉿kali)-[~/work/course_labs/labs/lab05]
└─$ git add docker-compose.yml                   
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/work/course_labs/labs/lab05]
└─$ git commit -m "lab5: change docker-compose.yml"
[lab05-ilya dcbe73a] lab5: change docker-compose.yml
 1 file changed, 5 insertions(+), 19 deletions(-)
                                                                                                             
┌──(.venv)─(kali㉿kali)-[~/work/course_labs/labs/lab05]
└─$ cat docker-compose.yml 
services:
  web:
    build:
      context: ./source
      dockerfile: Dockerfile
    ports:
      - "8000:5000"
```

- [ ] 15. Залейте изменения в свой удаленный репозиторий, проверьте историю `commit`.
- [ ] 16. Подготовьте отчет `gist`.
 
***

Copyright (c) 2025 Stratienko Ilya
