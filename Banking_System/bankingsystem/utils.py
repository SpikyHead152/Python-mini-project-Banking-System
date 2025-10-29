"""
utils.py — helper utilities

1. generate_account_id(prefix="ACC"):
   - Use uuid.uuid4().hex[:6] to generate a short unique ID.

2. current_timestamp():
   - Return timestamp as string, e.g. "2025-09-17 10:15:00".
"""

# import uuid
# from datetime import datetime

def generate_account_id(prefix="ACC"):
    # TODO: return f"{prefix}-{uuid.uuid4().hex[:6]}"
    pass

def current_timestamp():
    # TODO: return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pass
"""
utils.py
Small helper utilities used across the project:
- make_id(): short unique account id
- now(): current timestamp string
"""

import uuid
from datetime import datetime

def make_id(prefix='ACC'):
    """
    Return a short id string for accounts.
    Example: 'ACC-4f3a2b'
    """
    # use uuid4 and slice for brevity
    uid = uuid.uuid4().hex[:6]
    return f"{prefix}-{uid}"

def now():
    """
    Return current datetime as 'YYYY-MM-DD HH:MM:SS'
    (keeps format consistent with the rest of project)
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
