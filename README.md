### AI 관련 기사 가져오기

1. FastAPI를 통한 서버 구현
2. Airflow를 통한 자동화 구현
3. Elasticsearch를 통한 검색 엔진 구현

---
### 기사 API 준비
[newsapi.org](https://newsapi.org)

---
### 실행 방법

#### 0. 가상환경 세팅
```bash
conda create -n NAME python=3.11
conda activate NAME
```

#### 1. FastAPI 구동
```bash
uvicorn backend.news_main:app --reload
```

#### 2. Elasticsearch 구동
- Elasticsearch 다운로드

```bash
cd /Elasticsearch/bin | elasticsearch.bat
```

#### 3. Airflow 구동
- Docker for desktop 다운로드
- localhost:8080의 Airflow web ui에서 확인 가능

```bash
cd ./airflow/ | docker-compose up --build -d
```