resume-tailor/
│
├── main.py                       # Entry point
├── config.yaml                   # Configs (page length, formatting, etc.)
├── requirements.txt              # Dependencies
├── README.md                     # Project overview
│
├── /templates/                   # LaTeX templates
│   └── master_resume.tex
│
├── /data/
│   ├── projects.yaml             # All possible project descriptions
│   ├── skills.yaml               # All possible skills
│   └── resumes/                  # Generated .tex/.pdf resumes
│
├── /core/                        # Main logic
│   ├── latex_editor.py           # Safely edit LaTeX sections
│   ├── job_parser.py             # NLP + keyword matcher
│   ├── resume_builder.py         # Assembles final resume
│   ├── model_interface.py        # Interact with Hugging Face models
│   └── db_manager.py             # Save resume metadata (category, job title)
│
├── /cli/                         # Optional CLI tool
│   └── generate.py
│
└── .git/                         # For version control
