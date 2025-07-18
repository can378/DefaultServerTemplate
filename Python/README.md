# Python Web Server Template

### 1) 가상환경

1. 가상환경 생성

```
python -m venv venv
```

2. 가상환경 활성화

```
venv\Scripts\activate
```

### 2) .env 설정
```
  DATABASE_URL=mysql+pymysql://유저:비번@호스트:포트/데이터베이스이름
```

### 3) 실행
```
  uvicorn app.main:app --reload
```




