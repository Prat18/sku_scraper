# Project Name

A web scraper app which scrapes all the SKU listed on the configured web page. At the moment it only scrapes the webpage provided.
It uses celery to process the webpage asynchronously.

## Table of Contents

- [SKU SCRAPER](#project-name)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Configuration](#configuration)
  - [Running the Application](#running-the-application)
  - [Testing](#testing)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)

## Features

- List of features of your project.
  - Background task
  - check status of the task
  - Retry after N seconds

## Requirements

- Python 3.x
- Redis
- FastAPI
- Celery

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```
### start celery worker
```commandline
celery -A celery_app worker --pool solo --loglevel info
```

### install requirements
```commandline
pip install -r requirements.txt
```

### start fast api server using uvicorn
```commandline
uvicorn app.main:app
```

### test the api using swagger docs
