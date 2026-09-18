"""验证 HTTP 状态码到 API 异常类的映射。"""
import unittest

from src.core.exceptions import ResourceNotFoundError, RateLimitError, raise_for_status_code

class TestAPIErrorMapping(unittest.TestCase):
    def test_404_maps_to_resource_not_found_error(self):
        with self.assertRaises(ResourceNotFoundError):
            raise_for_status_code(
                "https://example.com/items/123",
                404,
                {"detail": "not found"},
            )

    def test_429_maps_to_rate_limit_error(self):
        with self.assertRaises(RateLimitError):
            raise_for_status_code(
                "https://example.com/items",
                429,
                {"detail": "too many requests"},
            )


if __name__ == "__main__":
    unittest.main()
