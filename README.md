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



| Component              | Technology        |

| ---------------------- | ----------------- |

| Programming Language   | Python            |

| AI Processing          | Google Gemini API |

| Database               | SQLite            |

| Reporting              | Microsoft Excel   |

| Excel Processing       | pandas, openpyxl  |

| PDF Processing         | PyMuPDF           |

| Image Processing       | Pillow            |

| Configuration          | YAML              |

| Environment Management | python-dotenv     |

| Version Control        | Git               |

| Repository             | GitHub            |



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



---



# Project Structure



```text

TrackMySpend/



├── app/

│   ├── ai/

│   ├── database/

│   ├── excel/

│   ├── image/

│   ├── pdf/

│   ├── receipt/

│   └── utils/



├── config/

│   ├── config.yaml

│   ├── categories.yaml

│   └── stores.yaml



├── data/

│   └── trackmyspend.db



├── receipts/

│   ├── incoming/

│   ├── processed/

│   ├── archive/

│   └── error/



├── reports/

│   └── Excel/



├── logs/



├── tests/



├── docs/

│   ├── ARCHITECTURE.md

│   └── CHANGELOG.md



├── .env

├── .gitignore

├── requirements.txt

└── README.md

```



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



Prepare the development environment.



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



Initialize Git and create the project structure.



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



Create organized folders for application code, data, receipts, reports, and documentation.



Status:



Completed ✅



---



## Step 4 - Configure Git Protection



Purpose:



Prevent private information from being uploaded.



Protected files:



- API keys

- Receipt images

- Databases

- Excel reports

- Logs



Status:



Completed ✅



---



## Completed Steps

### Step 5 - Create Python Virtual Environment

Status:

Completed ✅


---

### Step 6 - Install Required Libraries

Status:

Completed ✅

## Future Steps

### Step 7 - Build Application Configuration Loader

Purpose:

Load YAML configuration files into the application.

### Step 8 - Create SQLite Database

Purpose:

Store receipt and transaction history.

### Step 9 - Implement Receipt Processing

Purpose:

Extract receipt information from images and PDFs.

### Step 10 - Generate Excel Reports

Purpose:

Create yearly workbooks and monthly worksheets.
---



# Key Takeaways



TrackMySpend demonstrates how modern technologies can solve everyday problems.



Main learning areas:



- Applying AI to real-world documents

- Building secure automation tools

- Designing maintainable Python applications

- Managing structured data

- Creating useful personal analytics



---



# Conclusion



TrackMySpend transforms receipts from forgotten documents into valuable personal spending information.



The project combines:



- Artificial intelligence

- Automation

- Database management

- Data visualization

- Privacy-focused software design



The long-term vision is to create a personal spending assistant that helps users make better financial decisions based on their own purchase history.



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



# Current Status

Version 0.1 - Foundation completed

Completed:
- Project structure
- Python environment
- Dependencies
- Configuration design
- Architecture documentation

---

# License

MIT License (planned)
