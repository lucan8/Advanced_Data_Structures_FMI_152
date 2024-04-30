import random
from typing import List


class TestConfig:
    def __init__(self, length: int, max_value: int):
        self.length = length
        self.max_value = max_value


def generate_test(test_name: str, test_configs: List[TestConfig]):
    print(f"Generating tests for {test_name}", end="", flush=True)
    path = f"tests/random_generated/{test_name}"

    with open(path, "w") as output_file:
        output_file.write(f"{len(test_configs)}\n")

        for config in test_configs:
            output_file.write(f"{config.length} {config.max_value}\n")

            array = [str(random.randint(0, config.max_value))
                     for i in range(config.length)]
            for num in array:
                output_file.write(f"{num} ")
            output_file.write("\n")
    print("(done)")