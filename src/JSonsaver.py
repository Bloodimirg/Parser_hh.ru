import os
import json
from src.vacancy import Vacancy


class JSONSaver(Vacancy):
    """Класс для сохранения данных в формате JSON."""

    def __init__(self, directory='data'):
        self.directory = directory
        # Создаем папку, если ее еще нет
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def dump_to_file(self, vacancies):
        """Сохраняет список вакансий в файл JSON."""

        file_path = os.path.join(self.directory, 'base.json')
        with open(file_path, mode='w', encoding='utf-8') as file:
            json.dump([vac.to_json() for vac in vacancies], file, ensure_ascii=False, indent=4)
