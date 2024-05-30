class Vacancy:

    def __init__(self, country: str, name: str, salary: int, url: str, requirement: str, responsibility: str):
        self.country = country
        self.name = name
        self.salary = salary
        self.url = url
        self.requirement = requirement
        self.responsible = responsibility

    @classmethod
    def cast_to_object_list(cls, vacancies):
        """Создаем объект"""
        returned_list = []
        for vacancy in vacancies:
            country = vacancy["area"]["name"]
            name = vacancy["name"]
            if vacancy['salary']:
                salary = Vacancy.validate_int(vacancy.get("salary", {}).get('from', ''))
            else:
                salary = 0
            url = vacancy["alternate_url"]
            requirement = Vacancy.validate_str(vacancy.get('snippet').get('requirement'))
            responsibility = Vacancy.validate_str(vacancy.get('snippet').get('responsibility'))

            vacancy_obj = cls(country, name, salary, url, requirement, responsibility)
            returned_list.append(vacancy_obj)
        return returned_list

    @staticmethod
    def find_by_requirement(list_vacancies, filter_words):
        """Фильтр по ключевым словам"""
        filtered_vacancies = [vacancy for vacancy in list_vacancies if
                              vacancy.requirement and
                              any(word.lower() in vacancy.requirement for word in filter_words)]
        return filtered_vacancies

    @staticmethod
    def validate_int(value):
        """Валидация по int"""
        if value:
            return value
        return 0

    @staticmethod
    def validate_str(word):
        """Валидация по str"""
        if word:
            return word
        return "Не указано"

    @staticmethod
    def find_by_salary(vacancies, min_salary):
        """Фильтр по зарплате"""
        filtered_vacancies_twoo = [vacancy for vacancy in vacancies if
                                   vacancy >= min_salary]
        return filtered_vacancies_twoo

    @staticmethod
    def sorted_by_salary(vacancies):
        """Соритировка по зарплате"""
        return sorted(vacancies, reverse=True)

    @staticmethod
    def get_top_vacancies(count_vacancies, top_n):
        """Количество вакансий для вывода"""
        return count_vacancies[:top_n]

    def __eq__(self, other):
        if type(other) is type(self):
            return self.salary == other.salary
        elif type(other) is not type(self):
            return self.salary == other

    def __ne__(self, other):
        if type(other) is type(self):
            return self.salary != other.salary
        elif type(other) is not type(self):
            return self.salary != other

    def __lt__(self, other):
        if type(other) is type(self):
            return self.salary < other.salary
        elif type(other) is not type(self):
            return self.salary < other

    def __le__(self, other):
        if type(other) is type(self):
            return self.salary <= other.salary
        elif type(other) is not type(self):
            return self.salary <= other

    def __gt__(self, other):
        if type(other) is type(self):
            return self.salary > other.salary
        elif type(other) is not type(self):
            return self.salary > other

    def __ge__(self, other):
        if type(other) is type(self):
            return self.salary >= other.salary
        elif type(other) is not type(self):
            return self.salary >= other

    def __str__(self):
        """Вывод на экран"""
        return (f'\n{self.name}'
                f'\nГород: {self.country}'
                f'\nЗарплата от: {self.salary or "Не указана"}'
                f'\nСайт: {self.url}'
                f'\nТребования: {self.requirement.replace("<highlighttext>", "").replace("</highlighttext>", "")}'
                f'\nОбязанности: {self.responsible.replace("<highlighttext>", "").replace("</highlighttext>", "")}')

    def to_json(self):
        """Преобразование в словарь для JSON"""

        return self.__dict__

