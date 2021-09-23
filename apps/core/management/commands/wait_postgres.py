import logging
import os
from time import time, sleep

import psycopg2
from django.core.management.base import BaseCommand

check_timeout = os.getenv("POSTGRES_CHECK_TIMEOUT", 30)
check_interval = os.getenv("POSTGRES_CHECK_INTERVAL", 1)
interval_unit = "second" if check_interval == 1 else "seconds"
config = {
    "dbname": os.getenv("POSTGRES_DB", "postgres"),
    "user": os.getenv("POSTGRES_USER", "postgres"),
    "password": os.getenv("POSTGRES_PASSWORD", ""),
    "host": os.getenv("POSTGRES_HOST", "db"),
}

start_time = time()
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


class Command(BaseCommand):
    def handle(self, *args, **options):
        success = False
        while time() - start_time < check_timeout:
            try:
                conn = psycopg2.connect(**config)
                success = True
                conn.close()
                break
            except psycopg2.OperationalError:
                logger.info(
                    f"Postgres isn't ready. "
                    f"Waiting for {check_interval} {interval_unit}..."
                )
                sleep(check_interval)

        if success:
            logger.info("Postgres is ready! ✨ 💅")
            self.stdout.write(self.style.SUCCESS("Postgres is ready! ✨ 💅"))
        else:
            self.stdout.write(
                self.style.ERROR(
                    "We could not connect to Postgres within {check_timeout} seconds."
                )
            )
            logger.error(
                f"We could not connect to Postgres within {check_timeout} seconds."
            )
