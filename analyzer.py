# Resume Keyword Analyzer

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read().lower()

resume = read_file("sample_resume.txt")
job_description = read_file("job_description.txt")

resume_words = set(resume.split())
job_words = set(job_description.split())

matched_skills = resume_words.intersection(job_words)
missing_skills = job_words - resume_words

print("Matched Skills:", matched_skills)
print("Missing Skills:", missing_skills)
