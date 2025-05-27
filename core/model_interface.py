# core/model_interface.py
from transformers import pipeline

class ResumeModel:
    def __init__(self, model_name="google/flan-t5-xl"):
        self.generator = pipeline("text2text-generation", model=model_name)

    def rewrite_section(self, original_text: str, job_description: str, section_name: str) -> str:
        prompt = f"""
        You are updating a LaTeX resume. Rewrite the following section titled '{section_name}'
        so that it matches the job description. Preserve LaTeX formatting.

        Job Description:
        {job_description}

        Original Section:
        {original_text}

        Updated Section:
        """
        result = self.generator(prompt, max_length=250)[0]['generated_text']
        return result

