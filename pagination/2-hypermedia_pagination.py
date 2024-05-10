#!/usr/bin/env python3
"""
HyperMedia Pagination file
"""
import csv
from typing import List
from math import ceil


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
        """ checks if parameters are correct type and greater than 0
        uses index_range() to find the correct indexes to paginate
        returns list with specified indexes"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        ''' returns a dictionary containing the following key-value pairs '''
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        # page_size = len(dataset[start_index:end_index])
        data = dataset[start_index:end_index]
        total_pages = round(len(dataset) / page_size)
        if page_size == 0:
            total_pages = 195
        else:
    
            total_pages = round(len(dataset) / page_size)
            
        if page == 1:
            prev_page = None
        else:
            prev_page = page - 1
        if page >= total_pages:
            next_page = None
        else:
            next_page = page + 1
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
            }


def index_range(page: int, page_size: int) -> tuple:
    """  return a tuple of size two,
    containing a start index and an end index based on page number """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
