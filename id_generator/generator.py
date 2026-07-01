import threading
import time

from .config import (
    EPOCH,
    MAX_SEQUENCE,
    MAX_WORKER_ID,
    TIMESTAMP_SHIFT,
    WORKER_SHIFT,
)
from .exceptions import ClockMovedBackwardsException


class SnowflakeGenerator:

    def __init__(self, worker_id: int):

        if worker_id < 0 or worker_id > MAX_WORKER_ID:
            raise ValueError(
                f"Worker ID must be between 0 and {MAX_WORKER_ID}"
            )

        self.worker_id = worker_id
        self.sequence = 0
        self.last_timestamp = -1
        self.lock = threading.Lock()

    def _current_timestamp(self):
        return int(time.time() * 1000)

    def _wait_next_millis(self, current_timestamp):

        while current_timestamp <= self.last_timestamp:
            current_timestamp = self._current_timestamp()

        return current_timestamp

    def generate_id(self):

        with self.lock:

            current_timestamp = self._current_timestamp()

            # Clock moved backwards
            if current_timestamp < self.last_timestamp:
                raise ClockMovedBackwardsException(
                    "Clock moved backwards. Refusing to generate ID."
                )

            # Same millisecond
            if current_timestamp == self.last_timestamp:

                self.sequence = (self.sequence + 1) & MAX_SEQUENCE

                if self.sequence == 0:
                    current_timestamp = self._wait_next_millis(
                        current_timestamp
                    )

            else:
                self.sequence = 0

            self.last_timestamp = current_timestamp

            snowflake_id = (
                ((current_timestamp - EPOCH) << TIMESTAMP_SHIFT)
                | (self.worker_id << WORKER_SHIFT)
                | self.sequence
            )

            return snowflake_id