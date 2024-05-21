class Vacancy:

    def __init__(self, country, name, salary, url, requirement, responsibility):
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
            if vacancy['salary']:
                country = vacancy["area"]["name"]
                name = vacancy["name"]
                salary = vacancy.get("salary", {}).get('from', '')
                url = vacancy["alternate_url"]
                requirement = vacancy.get('snippet', {}).get('requirement')
                responsibility = vacancy.get('snippet', {}).get('responsibility')

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
    def find_by_salary(vacancies, min_salary):
        """Фильтр по зарплате"""
        filtered_vacancies_twoo = [vacancy for vacancy in vacancies if
                                   vacancy.salary and vacancy.salary >= min_salary]
        return filtered_vacancies_twoo

    @staticmethod
    def get_top_vacancies(count_vacancies, top_n):
        """Количество вакансий"""
        return count_vacancies[:top_n]

    def __str__(self):
        """Вывод на экран"""
        return (f'\n{self.name}'
                f'\nГород: {self.country or "не указан"}'
                f'\nЗарплата от: {self.salary or "не указана"}'
                f'\nСайт: {self.url or "не указан"}'
                f'\nТребования: {self.requirement or "не указаны"}'
                f'\nОбязанности: {self.responsible or "не указаны"}')

    def to_json(self):
        """Преобразование в словарь для JSON"""
        return {
            "country": self.country,
            "name": self.name,
            "salary": self.salary,
            "url": self.url,
            "requirement": self.requirement,
            "responsibility": self.responsible
        }


