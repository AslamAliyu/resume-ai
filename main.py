# main.py
from core.resume_builder import generate_resume

if __name__ == "__main__":
    job_desc_path = input("Enter path to job description text file: ")
    target_sections = input("Enter sections to update (comma-separated, e.g. summary,skills): ").split(',')
    generate_resume(job_desc_path, target_sections)

