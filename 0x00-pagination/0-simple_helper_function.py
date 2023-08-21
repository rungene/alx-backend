#!/usr/bin/env python3
"""
0-simple_helper_function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Get index rane for a given page number and page_size
    Args:
        page(int): page number
        page_size(int): page size

    Return:
        tuple of size two containing a start index and an end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
