from abc import ABC, abstractmethod
import requests


class Parser(ABC):
    """Абстрактный класс работы с API"""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def _connect(self):
        pass

    @abstractmethod
    def load_vacancies(self, search_query):
        pass


class HeadHunterAPI(Parser):
    """Класс для работы с API HeadHunter"""
    def __init__(self):
        self._url = "https://api.hh.ru/vacancies"
        self._headers = {'User-Agent': 'HH-User-Agent'}
        self._params = {'text': '', 'page': 0, 'per_page': 100}
        self._vacancies = []

    def _connect(self):
        response = requests.get(self._url, headers=self._headers, params=self._params)
        returned_response = response.json()
        return returned_response

    def load_vacancies(self, search_query):
        self._params['text'] = search_query
        while self._params.get('page') != 5:
            vacancies = self._connect()['items']
            self._vacancies.extend(vacancies)
            self._params['page'] += 1
        return self._vacancies
