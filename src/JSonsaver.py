import os
import json
from abc import ABC, abstractmethod


class WorkWithFiles(ABC):
    """Абстрактный класс работы с файлами"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_vacancies(self):
        pass

    @abstractmethod
    def write_vacancies(self, vacancies):
        pass

    @abstractmethod
    def add_vacancies(self, vacancies):
        pass

    @abstractmethod
    def del_vacancy_full(self, vacancies):
        pass

    @abstractmethod
    def del_vacancy_one(self, vacancy):
        pass


class JSONSaver(WorkWithFiles):
    """Класс для сохранения данных в формате JSON."""

    def __init__(self, file_name='base.json'):
        project_root = os.path.dirname(os.path.dirname(__file__))
        self._directory = os.path.join(project_root, 'data')
        self.__file_path = os.path.join(self._directory, file_name)
        self.__file_name = file_name

        # Создаем деррикторию data если её еще нет
        if not os.path.exists(self._directory):
            os.makedirs(self._directory, exist_ok=True)
            # Создаем файл __init__.py в директории, чтобы сделать ее пакетом
            with open(os.path.join(self._directory, '__init__.py'), 'w') as init_file:
                init_file.write('# Initializer\n')

    def load_vacancies(self):
        """Чтение файла"""
        with open(self.__file_path, 'r', encoding='utf-8') as file:
            new_list = json.load(file)
            return new_list

    def write_vacancies(self, vacancies):
        """Запись в файл"""
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            for_add = []
            for vacancy in vacancies:
                for_add.append(vacancy.__dict__)
            json.dump(for_add, file, ensure_ascii=False, indent=4)

    def add_vacancies(self, vacancies):
        """Добавление вакансий"""
        with open(self.__file_path, 'r', encoding='utf-8') as file:
            old_data = json.load(file)
            for vacancy in vacancies:
                old_data.append(vacancy.__dict__)
        with open(self._directory, 'w', encoding='utf-8') as file:
            json.dump(old_data, file, ensure_ascii=False, indent=4)

    def del_vacancy_full(self, vacancy):
        """Удаление всех вакансий"""
        with open(self.__file_path, 'r', encoding='utf-8') as file:
            old_data = json.load(file)
            while vacancy in old_data:
                old_data.remove(vacancy)
        with open(self._directory, 'w', encoding='utf-8') as file:
            json.dump(old_data, file, ensure_ascii=False, indent=4)

    def del_vacancy_one(self, vacancy):
        """Удаление одной вакансии"""
        with open(self.__file_path, 'r', encoding='utf-8') as file:
            old_data = json.load(file)
            if vacancy in old_data:
                old_data.remove(vacancy)
        with open(self._directory, 'w', encoding='utf-8') as file:
            json.dump(old_data, file, ensure_ascii=False, indent=4)
