from typing import Dict, Optional, Any
from datetime import datetime, timedelta
import jwt

from config import SECRET_KEY, EXPIRATION_SEC

__all__ = ['encode', 'decode']

def encode(payload: Dict[str, Any]) -> str:
    payload['exp'] = datetime.utcnow() + timedelta(seconds=EXPIRATION_SEC)
    print(payload)
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode(encoded: str) -> Optional[Dict[str, str]]:
    try:
        d = jwt.decode(encoded, SECRET_KEY, leeway=0, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.DecodeError:
        return None
    return d


if __name__ == '__main__':
    encoded = encode({
        "username": "admin"
    })
    print(encoded)
    import time
    time.sleep(10)
    print(decode(encoded))
