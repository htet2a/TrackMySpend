# TrackMySpend



## AI-powered Personal Spending Intelligence Assistant



TrackMySpend is a privacy-focused application that converts receipt images and PDF receipts into structured purchase data.



It helps users understand their spending habits by automatically extracting purchase information, storing history locally, and generating reports.



The goal is simple:



--Turn everyday receipts into useful personal spending intelligence.--



---



# Table of Contents



1. [Project Overview](#project-overview)

2. [Technology Used](#technology-used)

3. [Technical Concepts](#technical-concepts)

4. [Project Structure](#project-structure)

5. [Project Architecture](#project-architecture)

6. [Implementation Steps](#implementation-steps)

7. [Key Takeaways](#key-takeaways)

8. [Conclusion](#conclusion)

9. [Author](#author)



---



# Project Overview



## Project Description



TrackMySpend processes receipt files provided by the user and extracts useful information using AI.



Supported inputs:


```txt
- Receipt images (JPG, PNG, HEIC)

- PDF receipts from online purchases
```


The application extracts:



### Receipt Information



- Date

- Time

- Store name

- Receipt number

- Currency

- Tax

- Discount amount

- Discount percentage

- Total amount



### Item Information



- Item name

- Brand

- Item code / SKU / UPC (when available)

- Category

- Quantity

- Unit price

- Discount percentage

- Final price



### Reward Information



When available:



- Loyalty program

- Points earned

- Points redeemed

- Reward value



Examples:



- Grocery reward programs

- Store membership points

- Promotional discounts



---



# Technology Used

Programming Language: Python

AI Processing: Google Gemini API

Database: SQLite

Reporting: Microsoft Excel

Excel Processing: pandas, openpyxl

PDF Processing: PyMuPDF

Image Processing: Pillow

Configuration: YAML

Environment Management: python-dotenv

Version Control: Git

Repository: GitHub

---



# Technical Concepts



This project demonstrates:



## Artificial Intelligence



- AI-powered document extraction

- Structured data generation

- Receipt understanding



## Software Development



- Modular application design

- Configuration-driven development

- Error handling

- Logging



## Database Management



- SQLite database design

- Data relationships

- Historical tracking



## Automation



- Automatic receipt processing

- Report generation

- Duplicate detection



## Security Practices



- Local data storage

- Secret management

- Restricted file access

- Privacy-focused design

## Python Module Execution

TrackMySpend is executed using:

python -m app.main

instead of:

python app/main.py


Reason:

Using module execution allows Python to understand the application package structure correctly.

Benefits:

- Consistent imports between modules
- Better package organization
- Easier testing
- Matches standard Python application practices

---



## Project Structure

```text
TrackMySpend/
│
├── app/
│   │
│   ├── main.py
│   │
│   ├── ai/
│   │
│   ├── config/
│   │   └── config_loader.py
│   │
│   ├── database/
│   │   ├── connection.py
│   │   ├── init_db.py
│   │   └── receipt_repository.py
│   │
│   ├── excel/
│   │
│   ├── image/
│   │
│   ├── pdf/
│   │
│   ├── receipt/
│   │   ├── models.py
│   │   └── processor.py
│   │
│   └── utils/
│       ├── logger.py
│       └── paths.py
│
├── config/
│   ├── config.yaml
│   ├── categories.yaml
│   └── stores.yaml
│
├── data/
│   └── trackmyspend.db
│
├── receipts/
│   ├── incoming/
│   ├── processed/
│   ├── archive/
│   └── error/
│
├── reports/
│   └── Excel/
│
├── logs/
│
├── tests/
│   ├── test_database.py
│   ├── test_receipt_model.py
│   └── test_receipt_processor.py
│
├── docs/
│   ├── ARCHITECTURE.md
│   └── CHANGELOG.md
│
├── .env
├── .gitignore
├── requirements.txt
├── requirements-lock.txt
└── README.md
```
Runtime folders such as receipts, reports, logs, and database files are created locally and excluded from Git tracking.

Current implementation status:

- Configuration loading completed
- Application logging completed
- Project path management completed
- SQLite database initialization completed
- Receipt database repository completed
- Receipt data model completed
- Receipt file processor completed

Future modules:

- AI extraction
- Image processing
- PDF processing
- Excel report generation


---



# Project Architecture



High-level workflow:



```text
Receipt Image / PDF
        |
        v
File Validation
        |
        v
AI Extraction
        |
        v
Data Validation
        |
        v
SQLite Database
        |
        v
Excel Reports
```


Design principles:



- SQLite is the main data source.

- Excel is generated as a reporting output.

- Configuration is separated from application code.

- Personal receipt files remain local.

- Only user-selected receipts are processed.



---



# Implementation Steps



## Step 1 - Development Environment Setup



Purpose:

Prepare the development environment for Python application development.

Implementation:

- Verified Python installation.
- Verified Git installation.
- Verified development tools.
- Created project workspace.

Development environment:

- Operating system: Windows
- Python version: 3.13.14
- Virtual environment: Python venv


Commands:



```powershell

python --version

git --version

wsl --version

```



Status:



Completed ✅



---



## Step 2 - Create Project Repository



Purpose:

Create version control for the TrackMySpend project.

Implementation:

- Initialized Git repository.
- Created main branch.
- Connected local repository to GitHub.
- Published project repository.

Repository:

GitHub: https://github.com/htet2a/TrackMySpend



Commands:



```powershell

git init

git branch -M main

```



Status:



Completed ✅



---



## Step 3 - Create Project Folder Structure



Purpose:

Create a modular application structure.

Implementation:

Created separate folders for:

- Application modules
- Configuration files
- Database storage
- Receipt files
- Reports
- Documentation
- Tests

Designed the structure to support future expansion:

- AI extraction
- Image processing
- PDF processing
- Excel reporting

Status:

Completed ✅


---



## Step 4 - Configure Git Protection



Purpose:

Prevent private receipt data and generated files from being uploaded.

Implementation:

Configured .gitignore to exclude:

- Environment variables
- Virtual environments
- Database files
- Receipt files
- Excel reports
- Logs
- Temporary Python files

Privacy protection:

Personal receipt information remains local.

Status:

Completed ✅


---



## Completed Steps

### Step 5 - Create Python Virtual Environment

Purpose:

Create an isolated Python environment for project dependencies.

Implementation:

Created virtual environment:

.venv

Activated environment before development.

Benefits:

- Isolated dependencies
- Reproducible development setup
- Prevents conflicts with system Python

Status:

Completed ✅


---


### Step 6 - Install Required Libraries

Purpose:

Install libraries required for application development.

Implementation:

Installed:

AI:
- google-genai

Data processing:
- pandas
- openpyxl

File processing:
- PyMuPDF
- Pillow

Configuration:
- PyYAML
- python-dotenv

Dependency management:

Created:

- requirements.txt
- requirements-lock.txt

Status:

Completed ✅


---


### Step 7 - Build Application Configuration Loader

Purpose:

Load YAML configuration files into the application instead of hardcoding settings.

Implementation:

- Created YAML configuration files:
  - config.yaml
  - categories.yaml
  - stores.yaml

- Created configuration loader module:
  - app/config/config_loader.py

- Application can now read project settings dynamically.

Status:

Completed ✅



---



### Step 8 - Create SQLite Database

Purpose:

Store receipt and transaction history locally.

Implementation:

- Created SQLite database connection layer:
  - app/database/connection.py

- Created database initialization module:
  - app/database/init_db.py

- Created initial receipts table.

- Created repository layer:
  - app/database/receipt_repository.py

- Database remains the main source of truth.
- Excel will be generated later as a reporting output.

Status:

Completed ✅



---



## Future Steps

### Step 9 - Implement Receipt Processing

Purpose:

Process receipt files and prepare them for AI extraction.

Implementation:

Completed:

- Created receipt data model:
  - app/receipt/models.py

- Created receipt file processor:
  - app/receipt/processor.py

- Added receipt file validation:
  - File existence checking
  - Supported format checking
  - File metadata extraction

Supported formats:

- JPG
- JPEG
- PNG
- PDF

Next:

- Image reading
- PDF text extraction
- AI extraction
- Receipt data validation

Status:

In Progress 🟡

### Step 10 - Generate Excel Reports

Purpose:

Create Excel reports from stored expense data to help users understand spending patterns.

Planned Implementation:

- Create Excel reporting module:
  - app/excel/

- Generate yearly Excel workbooks.

- Create monthly worksheets.

- Use pandas and openpyxl for:
  - Data export
  - Worksheet formatting
  - Summary generation

Reports will include:

- Expense history
- Spending by category
- Monthly totals
- Yearly totals
- Separate currency summaries:
  - CAD totals
  - USD totals

Design principles:

- SQLite remains the main data source.
- Excel is generated only as a reporting output.
- No financial calculations are stored only in Excel.

Status:

Planned 



---



# Conclusion



TrackMySpend demonstrates how modern technologies can solve everyday personal finance problems by transforming receipts from forgotten documents into valuable spending information.

The project combines:

- Artificial intelligence
- Document processing automation
- Database management
- Data visualization
- Privacy-focused software design

Through this project, the main learning areas include:

- Applying AI to real-world documents
- Building secure automation tools
- Designing maintainable Python applications
- Managing structured data
- Creating useful personal analytics

The long-term vision is to create a personal spending assistant that helps users better understand their purchasing behavior and make informed financial decisions based on their own receipt history.



---



# Author



**Htet Htet**



Project creator and maintainer.



TrackMySpend was created as a practical AI automation project focused on solving a real everyday problem while exploring:



- AI application development

- Python software engineering

- Personal finance automation

- Open-source development practices


---


# License

MIT License (planned)
