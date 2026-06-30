import time

from .config import (
    EPOCH,
    MAX_SEQUENCE,
    MAX_WORKER_ID,
    SEQUENCE_BITS,
    TIMESTAMP_SHIFT,
    WORKER_SHIFT,
)


class SnowflakeGenerator:
    def __init__(self, worker_id: int):
        if worker_id < 0 or worker_id > MAX_WORKER_ID:
            raise ValueError(
                f"Worker ID must be between 0 and {MAX_WORKER_ID}"
            )

        self.worker_id = worker_id
        self.sequence = 0
        self.last_timestamp = -1