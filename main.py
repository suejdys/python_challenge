from extractors.rmt import extract_rmt_jobs
from extractors.wwr import extract_wework_jobs
from file import save_to_file

keyword = input("what do you want to search for? ")

wwr = extract_wework_jobs(keyword)
rmt = extract_rmt_jobs(keyword)
jobs = wwr + rmt

save_to_file(keyword, jobs)

