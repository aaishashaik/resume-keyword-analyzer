resume_skills = ["java", "html", "css", "git"]

job_description_skills = ["java", "spring", "git", "sql"]

missing_skills = []

for skill in job_description_skills:
    if skill not in resume_skills:
        missing_skills.append(skill)

print("Resume Skills:", resume_skills)
print("Job Skills:", job_description_skills)
print("Missing Skills:", missing_skills)
