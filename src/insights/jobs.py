from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path) -> List[Dict]:
        with open(path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.jobs_list.append(row)

    def get_unique_job_types(self) -> List[str]:
        unique_job = set()
        for job in self.jobs_list:
            unique_job.add(job["job_type"])
        return unique_job

    def filter_by_multiple_criteria(self, jobs, criteria) -> List[dict]:
        filtered_jobs = list()
        for job in jobs:
            job_comparison = job["job_type"] == criteria["job_type"]
            industry_comparison = job["industry"] == criteria["industry"]
            if job_comparison and industry_comparison:
                filtered_jobs.append(job)
        return filtered_jobs
