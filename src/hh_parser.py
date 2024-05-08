from abc import ABC, abstractmethod
import requests


class JobApi(ABC):
    pass


class Parser(JobApi):
    pass


class HH(Parser):
    pass