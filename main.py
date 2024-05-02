from utils.Trees.Treap import Treap
from utils.Trees.ScapegoatTree import ScapegoatTree
from utils.Trees.SplayTree import SplayTree
from utils.Tests import test_generator, test_handler
from utils.Tests.test_generator import TestConfig
def main():
    test_configs_treaps = [
                            TestConfig(1_000_000, 1_000_000),
                            TestConfig(1_000_000, 1_000_000_000),
                            TestConfig(1_000_000, 1_000_000_000_000),
                            TestConfig(1_000_000, 1_000_000_000_000_000),
                            TestConfig(1_000_000, 1_000_000_000_000_000_000),
                            #TestConfig(10_000_000, 1_000_000),
                            #TestConfig(10_000_000, 1_000_000_000),
                            #TestConfig(10_000_000, 1_000_000_000_000),
                            #TestConfig(10_000_000, 1_000_000_000_000_000),
                            #TestConfig(30_000_000, 10_000_000),
                            #TestConfig(100_000_000, 1_000_000_000),
                            ]
    
    test_generator.generate_test("Treaps/Treaps_insert", test_configs_treaps)
    test_generator.generate_test("Treaps/Treaps_search", test_configs_treaps)
    test_generator.generate_test("Treaps/Treaps_remove", test_configs_treaps)
    
    treap_insert_path = "tests/random_generated/Treaps/Treaps_insert"
    treap_search_path = "tests/random_generated/Treaps/Treaps_search"
    treap_remove_path = "tests/random_generated/Treaps/Treaps_remove"
    
    for test_i, test_s, test_r in zip(
                                    test_handler.read_file(treap_insert_path),
                                    test_handler.read_file(treap_search_path),
                                    test_handler.read_file(treap_remove_path),
                                    ):
        #The number of priority possibilites = 10 * max_size
        print(f"Test {test_i.index}({test_i.length, test_i.max_value}):")
        treap = Treap(0, 10 * test_i.length)

        treap.blockInsert(test_i.array)
        treap.printTreapInfo()
        treap.blockSearch(test_s.array)
        treap.blockRemove(test_r.array)

if __name__ == "__main__":
    main()