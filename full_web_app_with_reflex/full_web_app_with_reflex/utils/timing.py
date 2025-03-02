from datetime import datetime,timezone

from sqlmodel import Field

def get_utc_now() -> datetime:
    return datetime.now(timezone.utc)