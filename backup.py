import gzip
import os
from datetime import datetime
from shutil import copyfileobj

from dotenv import load_dotenv
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


def backup():
    load_dotenv()
    backup_path = os.getenv("PGBACKUP_PATH")
    temp_path = os.getenv("PGTEMP_PATH")
    for db in DATABASES:
        date = datetime.now().strftime("%Y-%m-%d")
        temp_filename = os.path.join(temp_path, f"{db}-{date}.sql")
        filename = os.path.join(backup_path, f"{db}-{date}.sql.gz")

        # Dump database
        with open(temp_filename, "wb") as f:
            pg_dump("-h", "localhost", db, _out=f)

        # Compress file
        with open(temp_filename, "rb") as f_in:
            with gzip.open(filename, "wb") as f_out:
                copyfileobj(f_in, f_out)
        os.remove(temp_filename)


if __name__ == "__main__":
    backup()
