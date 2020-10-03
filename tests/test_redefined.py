import pytest

from sa_lint.sa_lint import find_duplicate_definitions, DuplicateFinder

data = """
from sqlalchemy import Boolean, Column, Integer

class RedefinedColumnsModel:
    __table_name__ = 'redefined_columns_model'
    duplicate = Column(Integer)
    col_1 = Column()
    col_2 = Column()
    duplicate = Column(Boolean)

false_positive = True
false_positive = False
"""


@pytest.mark.asyncio
async def test_find_duplicate_definitions():
    res = await find_duplicate_definitions(data)
    assert len(res) == 1
    assert "duplicate" in res
    assert res["duplicate"][0] == (6, "Column(Integer)")
    assert res["duplicate"][1] == (9, "Column(Boolean)")
    assert "false_positive" not in res


def test_duplicate_finder():
    nums = [1, 2, 3, 1, 2, 3, 4, 5, 6]
    df = DuplicateFinder()
    for i, n in enumerate(nums):
        df[n] = i
    assert 4 not in df.duplicates
    assert 5 not in df.duplicates
    assert 6 not in df.duplicates
    assert 1 in df.duplicates
    assert 2 in df.duplicates
    assert 3 in df.duplicates

    for n in nums:
        assert n in df.items
