# core/latex_editor.py
import re

class LaTeXEditor:
    def __init__(self, latex_path: str):
        with open(latex_path, 'r') as f:
            self.content = f.read()

    def replace_section(self, section_name: str, new_content: str) -> None:
        pattern = rf"(\\section\*\{{{section_name}\}}\n)(.*?)(?=\\section\*|\\end\{{document\}})"
        match = re.search(pattern, self.content, re.DOTALL)
        if match:
            self.content = self.content.replace(match.group(0), match.group(1) + new_content + '\n')
        else:
            print(f"Warning: Section '{section_name}' not found.")

    def save(self, output_path: str):
        with open(output_path, 'w') as f:
            f.write(self.content)

