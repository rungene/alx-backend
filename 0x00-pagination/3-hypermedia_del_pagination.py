#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Get index rane for a given page number and page_size
    Args:
        page(int): page number
        page_size(int): page size

    Return:
        tuple of size two containing a start index and an end index
    """
    start_index = (page) * page_size
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """implementing deletion-resilient hypermedia pagination.
        Args:
            index(int): current start index of the return page
            page_size(int): the current page size

        Return:
            a dictionary with the key-value pairs"""

        start_index, end_index = index_range(index, page_size)
        data = []
        for i in range(start_index, end_index):
            assert 0 <= i < len(self.__indexed_dataset)
            if i in self.__indexed_dataset:
                data.append(self.__indexed_dataset[i])
            else:
                # Append None only when index is not in self.__indexed_dataset
                data.append(None)

        hyper_dict = {
            'index': start_index,
            'next_index': end_index,
            'page_size': page_size,
            'data': data
        }

        return hyper_dict
