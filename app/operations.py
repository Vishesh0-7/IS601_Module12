# app/operations.py
import logging
log = logging.getLogger(__name__)

def add(a: float, b: float) -> float:
    res = a + b
    log.debug("add(%s, %s)=%s", a, b, res)
    return res

def sub(a: float, b: float) -> float:
    res = a - b
    log.debug("sub(%s, %s)=%s", a, b, res)
    return res

def mul(a: float, b: float) -> float:
    res = a * b
    log.debug("mul(%s, %s)=%s", a, b, res)
    return res

def div(a: float, b: float) -> float:
    if b == 0:
        log.error("Attempted division by zero: div(%s, %s)", a, b)
        raise ZeroDivisionError("Division by zero")
    res = a / b
    log.debug("div(%s, %s)=%s", a, b, res)
    return res
