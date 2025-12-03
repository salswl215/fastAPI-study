from fastapi import FastAPI
import asyncio
import time

app = FastAPI()

# long-running I/O-bound 작업 시뮬레이션
# async 함수의 선언 시 async 키워드 사용
# I/O Bound 작업(외부 시스템(DB/File) 응답 대기가 대부분인 작업)의 경우 비동기 방식이 권장됨
async def long_running_task():
    # 특정 초동안 수행 시뮬레이션
    # async 함수 호출 시 await > async로 선언된 비동기 함수에서 수행 (예외, asyncio event loop에서 바로 호출)
    # 물리적으로 cpu가 다른 일 할 수 있음!
    await asyncio.sleep(20)
    return {"status": "long_running task completed"}

# @app.get("/task")
# async def run_task():
#     result = await long_running_task()
#     return result

# 동기 방식으로 동작
# async 제외하고 함수 선언 시 별도의 thread로 처리
# 멀티프로세스 ; uvicorn main:app --port=8081 --workers=4 --port=8081
@app.get("/task")
async def run_task():
    time.sleep(20)
    return {"status": "long_running task completed"}

@app.get("/quick")
async def quick_response():
    return {"status": "quick response"}