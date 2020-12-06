# 중앙대 오픈소스SW와 파이썬 프로그래밍 (조용진)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

오픈소스SW와 파이썬 프로그래밍 03분반 팀 과제

## 조작 방법

본 게임은 장애물 피하기 게임으로서 장애물에 닿지 않고 최대한 오래 피하는 것이 목적이다.

캐릭터는 키보드 방향키를 통해서 움직일 수 있다. 위쪽 방향키를 통해 2중 점프를 할 수 있고, 아래쪽 방향키를 통해 캐릭터 크기를 줄일 수 있다. 그리고 왼쪽, 오른쪽 방향키를 통해 캐릭터를 화면에서 움직일 수 있다.

목숨인 하트는 기본적으로 3개 주어지고, 가끔 화면에 장애물 대신 나타나는 하트에 캐릭터가 닿으면 하트 개수가 1개 증가한다.

장애물에 닿을 때마다 하트가 1개씩 없어지고, 0개가 되면 게임이 종료된다.

장애물을 피할 때마다 콤보가 증가하며 장애물 속도가 점점 빨라진다. 콤보는 캐릭터가 장애물에 닿으면 초기화된다.

## 실행 방법

1. 파이썬 외부 라이브러리 설치

```shell
> python -m pip install --upgrade pip
> python -m pip install bangtal
> python -m pip install black
```

2. 프로젝트 다운로드

```shell
> git clone https://github.com/donghae0414/2020OSW_FINAL.git
> cd 2020OSW_FINAL
```

3. 프로그램 실행

```shell
> python _2020OSW_FINAL.py
```

## 개발 환경

- Git
- Python v3.8.5
- Visual Studio 2019 or Visual Studio Code

## 사용한 라이브러리

- bangtal v0.23
- black v19.10

## 개발 환경 설정

1. 프로젝트 다운로드

```shell
> git clone https://github.com/donghae0414/2020OSW_FINAL.git
> cd 2020OSW_FINAL
```

2. 브랜치 변경

```shell
> git checkout (브랜치 이름)
```

3. 변경 사항 반영

```shell
> git add (파일 이름)
```

4. 커밋 생성

```shell
> python -m black .
> git commit -m "커밋 메시지"
```

5. 원격 저장소에 업로드

```shell
> git fetch
> git push -u master origin
```

만약 fetch 후 외부 저장소에 변경 사항이 있으면 `git pull`을 통해 해당 변경 사항을 자신의 로컬 저장소에 반영한다.

## 프로젝트 구조

- .git

Git 관련 설정 파일이 들어 있다.

- .vscode

Visual Studio Code 관련 설정 파일이 들어 있다.

- Images

프로젝트에서 쓰이는 이미지 파일이 들어 있다.

- Models

프로젝트에서 쓰이는 `bangtal.Object` 관련 파일이 들어 있다.

- Timers

프로젝트에서 쓰이는 `bangtal.Timer` 관련 파일이 들어 있다.

- \_2020OSW_FINAL.py

프로젝트 진입점 파일이다.

## 브랜치 전략

![](http://postfiles7.naver.net/MjAxODAyMDNfOTgg/MDAxNTE3NjI3MzI0NjU1.V2GkhqrdgVSj0N7n8PDlWb9JvEQInMis5jW1b7QnCE8g.PQtKm7LOuraB3UeBICJ-byEe4SOTiWfIzQylWvzAPxog.PNG.aufcl4858/kF7Uf.png?type=w2)

### main 브랜치

- Protected branch (+ 직접 커밋 금지)

- 배포용 (production)

- 항상 1개 존재

- release 브랜치만 이 브랜치에 병합할 수 있다.

- 각 배포 커밋마다 tag로 버전을 기록한다.

### develop 브랜치

- Protected branch

- 개발용 (development)

- 항상 1개 존재

- feature 브랜치를 이 브랜치로 병합한다.

- 버그 수정 등으로 release 브랜치에 새로운 커밋이 있으면 해당 사항을 반영하기 위해 release 브랜치를 develop 브랜치와도 병합한다.

### release 브랜치

- develop 브랜치 유지를 위해 배포가 필요할 때마다 develop를 기반으로 분화한다.

- 배포할 때마다 생성되고 버그 수정 후 다른 브랜치(main, develop)와 병합된다.

### feature 브랜치

- 개수 제한 없음

- 분업의 단위

- develop 브랜치를 기반으로 feature 브랜치를 만들어 작업한 후 develop 브랜치로 병합한다.

- feature 브랜치 이름은 `feature/YY-MM-DD/기능명`으로 한다.

- feature 브랜치를 develop에 병합하기 전에 PR에서 코드 리뷰를 받는 것을 권장한다.

- 여러 사람이 한 feature 브랜치에서 공동으로 작업하는 것을 지양한다.
