from rest_framework.pagination import PageNumberPagination


class RunPagination(PageNumberPagination):
    page_size_query_param = 'size'
    max_page_size = 15


class UserPagination(PageNumberPagination):
    page_size_query_param = 'size'
    max_page_size = 12
