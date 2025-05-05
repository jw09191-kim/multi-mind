from datetime import datetime, timedelta

def get_today_string(format="%Y-%m-%d") -> str:
    return datetime.now().strftime(format)

def get_now_string(format="%Y-%m-%d_%H-%M-%S") -> str:
    return datetime.now().strftime(format)

def get_kst_now():
    return datetime.utcnow() + timedelta(hours=9)
