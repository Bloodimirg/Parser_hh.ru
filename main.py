from src.hh_parser import HeadHunterAPI
from src.vacancy import Vacancy
from src.JSonsaver import JSONSaver


def main():
    search_query = input("Введите поисковый запрос: ")
    salary_range = int(input("Введите минимальную зарплату: "))
    filter_words = input("Введите ключевое слово для фильтрации вакансий: ")
    top_vacancies = int(input("Сколько вакансий показать?: "))

    hh_api = HeadHunterAPI()

    hh_vacancies = hh_api.load_vacancies(search_query)  # запрос на сайт с вводимой должностью

    objects_vacancies = Vacancy.cast_to_object_list(hh_vacancies)  # создаем объект

    get_search_word = Vacancy.find_by_requirement(objects_vacancies, filter_words)  # фильтруем по требованиям

    salary_vacancies = Vacancy.find_by_salary(get_search_word, salary_range)  # фильтруем по зарплате

    get_top_vacancies = Vacancy.get_top_vacancies(salary_vacancies, top_vacancies)  # количество вакансий

    if salary_vacancies is not None:
        for vacancy in get_top_vacancies:
            print(vacancy)
    else:
        print("Ничего не найдено")

    # сохраняем в JSON
    json_saver = JSONSaver()
    json_saver.dump_to_file(get_top_vacancies)


if __name__ == "__main__":
    main()
