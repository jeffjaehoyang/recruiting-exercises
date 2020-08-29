import unittest
import solution


class TestSolution(unittest.TestCase):
    def test_one_warehouse(self):
        result = solution.allocate_inventory(
            {"apple": 1}, [{"name": "owd", "inventory": {"apple": 1}}]
        )
        self.assertEqual(result, [{"owd": {"apple": 1}}])

    def test_multiple_warehouse(self):
        result = solution.allocate_inventory(
            {"apple": 10},
            [
                {"name": "owd", "inventory": {"apple": 5}},
                {"name": "dm", "inventory": {"apple": 5}},
            ],
        )
        self.assertEqual(result, [{"owd": {"apple": 5}}, {"dm": {"apple": 5}}])

    def test_unshippable_order_1(self):
        result = solution.allocate_inventory(
            {"apple": 1}, [{"name": "owd", "inventory": {"apple": 0}}]
        )
        self.assertEqual(result, [])

    def test_unshippable_order_2(self):
        result = solution.allocate_inventory(
            {"apple": 2}, [{"name": "owd", "inventory": {"apple": 1}}]
        )
        self.assertEqual(result, [])

    def test_unrelated_item(self):
        result = solution.allocate_inventory(
            {"apple": 10, "grape": 8, "orange": 5, "mango": 1},
            [
                {"name": "owd", "inventory": {"apple": 1, "grape": 5, "mango": 1}},
                {
                    "name": "mercado",
                    "inventory": {"apple": 8, "grape": 1, "mango": 3, "orange": 10},
                },
                {
                    "name": "johnny",
                    "inventory": {"apple": 2, "grape": 3, "orange": 3, "cherry": 2},
                },
            ],
        )
        self.assertEqual(
            result,
            [
                {"owd": {"apple": 1, "grape": 5, "mango": 1}},
                {"mercado": {"apple": 8, "grape": 1, "orange": 5}},
                {"johnny": {"apple": 1, "grape": 2}},
            ],
        )

    def test_zero_order(self):
        result = solution.allocate_inventory(
            {"apple": 10, "grape": 8, "orange": 5, "mango": 0},
            [
                {"name": "owd", "inventory": {"apple": 1, "grape": 5, "mango": 1}},
                {
                    "name": "mercado",
                    "inventory": {"apple": 8, "grape": 1, "mango": 3, "orange": 10},
                },
                {
                    "name": "johnny",
                    "inventory": {"apple": 2, "grape": 3, "orange": 3, "cherry": 2},
                },
            ],
        )
        self.assertEqual(
            result,
            [
                {"owd": {"apple": 1, "grape": 5}},
                {"mercado": {"apple": 8, "grape": 1, "orange": 5}},
                {"johnny": {"apple": 1, "grape": 2}},
            ],
        )

    def test_empty_order(self):
        result = solution.allocate_inventory(
            {},
            [
                {"name": "owd", "inventory": {"apple": 1, "grape": 5, "mango": 1}},
                {
                    "name": "mercado",
                    "inventory": {"apple": 8, "grape": 1, "mango": 3, "orange": 10},
                },
                {
                    "name": "johnny",
                    "inventory": {"apple": 2, "grape": 3, "orange": 3, "cherry": 2},
                },
            ],
        )
        self.assertEqual(result, [])

    def test_negative_order(self):
        result = solution.allocate_inventory(
            {"apple": 10, "grape": 8, "orange": 5, "mango": -3},
            [
                {"name": "owd", "inventory": {"apple": 1, "grape": 5, "mango": 1}},
                {
                    "name": "mercado",
                    "inventory": {"apple": 8, "grape": 1, "mango": 3, "orange": 10},
                },
                {
                    "name": "johnny",
                    "inventory": {"apple": 2, "grape": 3, "orange": 3, "cherry": 2},
                },
            ],
        )
        self.assertEqual(
            result,
            [
                {"owd": {"apple": 1, "grape": 5}},
                {"mercado": {"apple": 8, "grape": 1, "orange": 5}},
                {"johnny": {"apple": 1, "grape": 2}},
            ],
        )

    def test_unshippable_by_one(self):
        result = solution.allocate_inventory(
            {"apple": 10, "grape": 8, "orange": 5, "cherry": 3},
            [
                {"name": "owd", "inventory": {"apple": 1, "grape": 5, "mango": 1}},
                {
                    "name": "mercado",
                    "inventory": {"apple": 8, "grape": 1, "mango": 3, "orange": 10},
                },
                {
                    "name": "johnny",
                    "inventory": {"apple": 2, "grape": 3, "orange": 3, "cherry": 2},
                },
            ],
        )
        self.assertEqual(result, [])

    def test_fulfilled_at_first(self):
        result = solution.allocate_inventory(
            {"pineapple": 5, "cherry": 3, "watermelon": 1},
            [
                {
                    "name": "deliverr",
                    "inventory": {"pineapple": 5, "cherry": 3, "watermelon": 1},
                },
                {"name": "owd", "inventory": {"apple": 2}},
            ],
        )
        self.assertEqual(
            result, [{"deliverr": {"pineapple": 5, "cherry": 3, "watermelon": 1}}]
        )

    def test_skips_first(self):
        result = solution.allocate_inventory(
            {"pineapple": 5, "cherry": 3, "watermelon": 1},
            [
                {"name": "owd", "inventory": {"apple": 2}},
                {
                    "name": "deliverr",
                    "inventory": {"pineapple": 5, "cherry": 3, "watermelon": 1},
                },
            ],
        )
        self.assertEqual(
            result, [{"deliverr": {"pineapple": 5, "cherry": 3, "watermelon": 1}}]
        )


if __name__ == "__main__":
    unittest.main()
