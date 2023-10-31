import gzip
import os
from datetime import datetime

from sh import pg_dump

DATABASES = [
    "dm_vietnam",
    "bot_cambo",
    "bot_vietnam",
    "dm_nigeria",
    "dm_cambodia",
    "bot_nigeria",
    "warninger",
]

BACKUP_PATH = "/root/yandex_uploader/tempbackup/"


def backup():
    for db in DATABASES:
        date = datetime.now().strftime("%Y-%m-%d")
        filename = os.path.join(BACKUP_PATH, f"{db}-{date}.sql")
        with gzip.open(f"{filename}.gz", "wb") as f:
            pg_dump("-h", "localhost", db, _out=f)


if __name__ == "__main__":
    backup()
