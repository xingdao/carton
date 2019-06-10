# _*_ coding:utf-8 _*_

from django.utils.functional import cached_property
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    """每页最大显示数"""

    page_size = 15
    page_query_param = 'index'
    max_page_size = 120
