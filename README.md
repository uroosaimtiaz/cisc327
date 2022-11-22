# cisc327
![GitHub Workflow Status](https://github.com/uroosaimtiaz/cisc327/actions/workflows/pytest.yml/badge.svg)
![GitHub Workflow Status](https://github.com/uroosaimtiaz/cisc327/actions/workflows/style_check.yml/badge.svg)

# Information 

Folder structure:

```
├── .github
│   └── pull_request_template.md
│   └── workflows
│       ├── pytest.yml       ======> CI settings for running test           automatically (trigger test for commits/pull-requests)
│       └── style_check.yml  ======> CI settings for checking PEP8 automatically (trigger test for commits/pull-requests)
├── qbay                 ======> Application source code
│   ├── __init__.py      
│   ├── __main__.py      ======> Program entry point
│   ├── cli.py           ======> Frontend screens
│   └── models.py        ======> Data models
├── qbay_test            ======> Testing code
│   ├── __init__.py      
│   ├── conftest.py      ======> Code to run before/after all the testing
│   ├── frontend         ======> Integration testing
│       ├── __init__.py
│       ├── test_create_listing     ======> Integration tests for create listing in cli.py
│       ├── test_login              ======> Integration tests for login in cli.py
│       ├── test_register           ======> Integration tests for register in cli.py
│       ├── test_update_listing     ======> Integration tests for update listing in cli.py
│       └── test_update_user_profile======> Integration tests for update user profile in cli.py
│   └── test-backend     ======> Backend testing
│       ├── __init__.py
│       └── test_models.py  ======> Backend testing for models.py
├── .gitignore
├── A0-contract.md
├── LICENSE
├── README.md
├── requirements.txt     ======> Dependencies
└── scrumboard.png       ======> Scrum board screenshot
```

# Scrum Board

Current SCRUM Board Screenshot after sprint kickoff meeting in scrumboard.png.

<img src="https://github.com/uroosaimtiaz/cisc327/blob/testing_update_user3/scrumboard.png?raw=true" width="800" />
