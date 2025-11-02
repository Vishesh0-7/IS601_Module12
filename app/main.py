# app/main.py
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import logging, time
from app import operations as ops

# ----- Logging setup -----
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
log = logging.getLogger("calculator")

app = FastAPI(title="FastAPI Calculator", version="1.0.0")

# Static UI
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Request logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()
    log.info("REQ %s %s", request.method, request.url.path)
    try:
        response = await call_next(request)
        elapsed = (time.time() - start) * 1000
        log.info("RES %s %s -> %s in %.2f ms", request.method, request.url.path, response.status_code, elapsed)
        return response
    except Exception as e:
        log.exception("Unhandled error on %s %s", request.method, request.url.path)
        return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})

@app.get("/", response_class=HTMLResponse)
def index():
    with open("app/static/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/add")
def add(a: float, b: float):
    return {"result": ops.add(a, b)}

@app.get("/sub")
def sub(a: float, b: float):
    return {"result": ops.sub(a, b)}

@app.get("/mul")
def mul(a: float, b: float):
    return {"result": ops.mul(a, b)}

@app.get("/div")
def div(a: float, b: float):
    try:
        return {"result": ops.div(a, b)}
    except ZeroDivisionError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/calc")
def calc(op: str, a: float, b: float):
    op = op.lower()
    funcs = {"add": ops.add, "sub": ops.sub, "mul": ops.mul, "div": ops.div}
    if op not in funcs:
        raise HTTPException(status_code=400, detail="Unsupported operation")
    try:
        return {"op": op, "result": funcs[op](a, b)}
    except ZeroDivisionError as e:
        raise HTTPException(status_code=400, detail=str(e))
