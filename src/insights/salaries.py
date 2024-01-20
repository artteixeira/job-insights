from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salary = 0
        for job in self.jobs_list:
            salary = job["max_salary"]
            if salary and salary.isdigit():
                salary = int(salary)
                if salary > max_salary:
                    max_salary = salary
        return max_salary

    def get_min_salary(self) -> int:
        min_salary = self.get_max_salary()
        for job in self.jobs_list:
            salary = job["min_salary"]
            if salary and salary.isdigit():
                salary = int(salary)
                if salary < min_salary:
                    min_salary = salary
        return min_salary

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        def is_valid_salary(salary):
            return isinstance(salary, (int, str)) and (isinstance(salary, int) or salary.isdigit())

        if 'min_salary' not in job or 'max_salary' not in job:
            raise ValueError("Min or Max salary is not defined")

        min_salary, max_salary = job["min_salary"], job["max_salary"]

        if not (is_valid_salary(min_salary) and is_valid_salary(max_salary) and is_valid_salary(salary)):
            raise ValueError("Salary must be a number (int or repr of int)")

        if int(max_salary) < int(min_salary):
            raise ValueError("Max salary is less than min salary")

        return int(min_salary) <= int(salary) <= int(max_salary)

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
