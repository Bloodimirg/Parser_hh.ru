from abc import ABC, abstractmethod
import requests


class Parser(ABC):

    def __init__(self):
        pass

    def connect(self):
        pass

    def get_vacancies(self):
        pass


class HeadHunterAPI(Parser):
    """Класс для работы с API HeadHunter"""

    def __init__(self):
        super().__init__()
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, search_query):
        self.params['text'] = search_query
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return self.vacancies
