# cisc327
![GitHub Workflow Status](https://github.com/uroosaimtiaz/cisc327/actions/workflows/pytest.yml/badge.svg)
![GitHub Workflow Status](https://github.com/uroosaimtiaz/cisc327/actions/workflows/style_check.yml/badge.svg)

# Information 

Folder structure:

```
├── .github
    └── pull_request_template.md
│   └── workflows
│       ├── pytest.yml       ======> CI settings for running test automatically (trigger test for commits/pull-requests)
│       └── style_check.yml  ======> CI settings for checking PEP8 automatically (trigger test for commits/pull-requests)
├── qbay                 ======> Application source code
│   ├── __init__.py      ======> Required for a python module (can be empty)
│   ├── __main__.py      ======> Program entry point
│   ├── cli.py           ======> Frontend screens
│   └── models.py        ======> Data models
├── qbay_test            ======> Testing code
│   ├── __init__.py      ======> Required for a python module (can be empty)
│   ├── conftest.py      ======> Code to run before/after all the testing
│   ├── test_cli.py      ======> Testing code for cli.py
│   └── test_models.py   ======> Testing code for models.py
├── .gitignore
├── A0-contract.md
├── LICENSE
├── README.md
├── requirements.txt     ======> Dependencies
└── scrumboard.png       ======> Scrum board screenshot
```

# Scrum Board

Current SCRUM Board Screenshot after sprint kickoff meeting in scrumboard.png.

<img src="https://github.com/uroosaimtiaz/cisc327/blob/build-badge/scrumboard.png" width="800" />
