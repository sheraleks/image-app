from aiohttp.test_utils import unittest_run_loop
from tests import AppTestCase


class UserListTestCase(AppTestCase):

    @unittest_run_loop
    async def test_list_users(self):
        pass