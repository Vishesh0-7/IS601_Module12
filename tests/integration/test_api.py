from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "ok"

def test_add_endpoint():
    res = client.get("/add", params={"a": 3, "b": 2})
    assert res.status_code == 200 and res.json()["result"] == 5

def test_sub_endpoint():
    res = client.get("/sub", params={"a": 3, "b": 2})
    assert res.status_code == 200 and res.json()["result"] == 1

def test_mul_endpoint():
    res = client.get("/mul", params={"a": 3, "b": 2})
    assert res.status_code == 200 and res.json()["result"] == 6

def test_div_endpoint_ok():
    res = client.get("/div", params={"a": 6, "b": 3})
    assert res.status_code == 200 and res.json()["result"] == 2

def test_div_endpoint_by_zero():
    res = client.get("/div", params={"a": 1, "b": 0})
    assert res.status_code == 400
    assert "Division by zero" in res.json()["detail"]

def test_calc_router_invalid_op():
    res = client.get("/calc", params={"op":"pow", "a":2, "b":3})
    assert res.status_code == 400
