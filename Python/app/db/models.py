from app.db.database import Base

# 모든 모델 import
from app.A.models import A1, A2
from app.B.models import B1
from app.C.models import C1

# 이거 추가해야 main.py에서 Base를 사용할 수 있음
__all__ = ["Base", "A1", "A2", "B1", "C1"]
