"""A decorator that retries a function a fixed number of times on
exception, with optional delay between attempts."""
import time
from functools import wraps


def retry(times: int = 3, delay: float = 0.0, exceptions=(Exception,)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    last_exc = exc
                    if attempt < times and delay:
                        time.sleep(delay)
            raise last_exc

        return wrapper

    return decorator
