from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import engine
from app.db import models  #모든 모델 로딩
from app.A.router import router as a_router
from app.B.router import router as b_router
from app.C.router import router as c_router

# FastAPI 앱 생성
app = FastAPI(title="test")

# 라우터 등록
app.include_router(a_router)
app.include_router(b_router)
app.include_router(c_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def test_db_connection():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        print("✅ DB 연결 성공")
    except Exception as e:
        print("DB 연결 실패:", e)
    finally:
        db.close()

test_db_connection()