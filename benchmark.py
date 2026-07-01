import time

from id_generator.generator import SnowflakeGenerator

generator = SnowflakeGenerator(worker_id=1)

COUNT = 1_000_000

start = time.perf_counter()

for _ in range(COUNT):
    generator.generate_id()

end = time.perf_counter()

print(f"Generated {COUNT:,} IDs")
print(f"Time: {end-start:.3f} sec")
print(f"Rate: {COUNT/(end-start):,.0f} IDs/sec")