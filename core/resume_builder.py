import os
from core.latex_editor import LaTeXEditor
from core.model_interface import ResumeModel


def generate_resume(job_desc_path: str, sections_to_update: list):
    # Load job description
    with open(job_desc_path, 'r') as f:
        job_description = f.read()

    # Set paths
    template_path = "templates/master_resume.tex"
    output_dir = "data/resumes"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "resume_output.tex")

    # Initialize helpers
    editor = LaTeXEditor(template_path)
    model = ResumeModel()

    # Replace each section with updated content
    for section in sections_to_update:
        print(f"Updating section: {section}")
        # Optional: extract current content from the LaTeX file before update
        original_text = f"[Original {section} content here]"
        rewritten = model.rewrite_section(original_text, job_description, section)
        editor.replace_section(section, rewritten)

    # Save output
    editor.save(output_path)
    print(f"Updated resume saved to {output_path}")
