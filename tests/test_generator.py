from id_generator.generator import SnowflakeGenerator


def test_unique_ids():

    generator = SnowflakeGenerator(worker_id=1)

    ids = set()

    for _ in range(100000):
        ids.add(generator.generate_id())

    assert len(ids) == 100000


def test_monotonic_ids():

    generator = SnowflakeGenerator(worker_id=1)

    previous = generator.generate_id()

    for _ in range(10000):
        current = generator.generate_id()

        assert current > previous

        previous = current