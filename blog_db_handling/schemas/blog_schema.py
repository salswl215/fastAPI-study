from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from pydantic.dataclasses import dataclass

# Pydantic 모델 사용 시 유효성 검사 진행 > DB에서 이미 validation 진행하기에 중복으로 검사할 필요는 없음
class BlogInput(BaseModel):
    title: str = Field(..., min_length=2, max_length=200)
    author: str = Field(..., max_length=100)
    content: str = Field(..., min_length=2, max_length=4000)
    image_loc: Optional[str] = Field(None, max_length=400)  # type을 Optional[str]로 표시 필요
    #image_loc: Annotated[str, Field(None, max_length=400)] = None

class Blog(BlogInput):
    id:int
    modified_dt: datetime

# 그 경우 그냥 dataclass 사용!
@dataclass
class BlogData:
    id: int
    title: str
    author: str
    content: str
    modified_dt: datetime
    image_loc: str | None = None