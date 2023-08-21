#!/usr/bin/env python3
"""
1-simple_pagination
"""
import csv
import math
from typing import Dict, List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ calculates the start and end indexes for the requested page,
        and returns the corresponding page of data from the dataset."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)

        if not self.__dataset:
            self.dataset()
        return self.__dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Implements hypermedia pagination"""
        data: List[List] = self.get_page(page, page_size)
        start_index, end_index = index_range(page, page_size)
        prev_page: int = page - 1 if page > 1 else None
        next_page: int = page + 1 if end_index < len(self.__dataset) else None
        total_records: int = len(self.__dataset)
        tota_pages: int = ceil(total_records / page_size)
        dict_hyper = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

        return dict_hyper
