from utils.Trees.Treap import Treap
from utils.Trees.ScapegoatTree import ScapegoatTree
from utils.Trees.SplayTree import SplayTree
from utils.Tests import test_generator, test_handler
from utils.Tests.test_generator import TestConfig

def main():
    # Treaps tests
    test_configs_treaps = [
                            TestConfig(1_000_000, 1_000_000),
                            TestConfig(1_000_000, 1_000_000_000),
                            TestConfig(1_000_000, 1_000_000_000_000),
                            TestConfig(1_000_000, 1_000_000_000_000_000),
                            TestConfig(1_000_000, 1_000_000_000_000_000_000),
                            # TestConfig(10_000_000, 1_000_000),
                            # TestConfig(10_000_000, 1_000_000_000),
                            # TestConfig(10_000_000, 1_000_000_000_000),
                            # TestConfig(10_000_000, 1_000_000_000_000_000),
                            # TestConfig(30_000_000, 10_000_000),
                            # TestConfig(100_000_000, 1_000_000_000),
                            ]

    test_generator.generate_test("Treaps/Treaps_insert", test_configs_treaps)
    test_generator.generate_test("Treaps/Treaps_search", test_configs_treaps)
    test_generator.generate_test("Treaps/Treaps_remove", test_configs_treaps)

    # The GOAT tests
    test_configs_scapegoat = [
                            TestConfig(1_000_000, 1_000_000),
                            TestConfig(1_000_000, 10_000_000),
                            TestConfig(1_000_000, 100_000_000),
                            TestConfig(4_200_000, 420_690),
                            TestConfig(6_666_666, 77_777),
                            TestConfig(6_666_666, 7_777_777),
                            TestConfig(1_000_000, 420_690),
                            ]

    test_generator.generate_test("Scapegoat/Scapegoat_insert", test_configs_scapegoat)
    test_generator.generate_test("Scapegoat/Scapegoat_search", test_configs_scapegoat)
    test_generator.generate_test("Scapegoat/Scapegoat_remove", test_configs_scapegoat)

    treap_insert_path = "tests/random_generated/Treaps/Treaps_insert"
    treap_search_path = "tests/random_generated/Treaps/Treaps_search"
    treap_remove_path = "tests/random_generated/Treaps/Treaps_remove"

    print("Testing Treaps...")
    for test_i, test_s, test_r in zip(
                                    test_handler.read_file(treap_insert_path),
                                    test_handler.read_file(treap_search_path),
                                    test_handler.read_file(treap_remove_path),
                                    ):
        #The number of priority possibilites = 10 * max_size
        print(f"Test {test_i.index}: (length={test_i.length}, max_value={test_i.max_value})")
        treap = Treap(0, 10 * test_i.length)

        treap.blockInsert(test_i.array)
        treap.printTreapInfo()
        treap.blockSearch(test_s.array)
        treap.blockRemove(test_r.array)

    scapegoat_insert_path = "tests/random_generated/Scapegoat/Scapegoat_insert"
    scapegoat_search_path = "tests/random_generated/Scapegoat/Scapegoat_search"
    scapegoat_remove_path = "tests/random_generated/Scapegoat/Scapegoat_remove"

    print("Testing Scapegoat...")
    for test_i, test_s, test_r in zip(
                                    test_handler.read_file(scapegoat_insert_path),
                                    test_handler.read_file(scapegoat_search_path),
                                    test_handler.read_file(scapegoat_remove_path),
                                    ):
        print(f"Test {test_i.index}: (length={test_i.length}, max_value={test_i.max_value})")
        scapegoat = ScapegoatTree(0.7)
        scapegoat.blockInsert(test_i.array)
        scapegoat.blockSearch(test_s.array)
        scapegoat.blockRemove(test_r.array)


if __name__ == "__main__":
    main()
