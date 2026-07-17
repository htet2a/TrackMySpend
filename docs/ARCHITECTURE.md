\# TrackMySpend Architecture



\## Purpose



This document describes the technical design of TrackMySpend.



The goal is to keep the application secure, modular, maintainable, and easy to extend.



\---



\# System Overview



TrackMySpend converts receipt documents into structured spending information.



High-level workflow:



Receipt

|

v

File Processing

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



\---



\# Design Principles



\## Privacy First



\- User selects which receipts are processed.

\- No computer-wide scanning.

\- No email access.

\- Data remains local.



\## Separation of Responsibilities



Each module has a specific purpose:



\- Receipt module handles receipt workflow.

\- AI module extracts information.

\- Database module stores data.

\- Excel module creates reports.



\## Configuration Driven



Settings should be changed through configuration files instead of source code.



Examples:



\- Categories

\- Folder locations

\- AI settings

\- Report settings



\---



\# Main Components



\## Receipt Processing



Responsible for:



\- Reading images

\- Reading PDFs

\- Validating files

\- Moving processed files



\---



\## AI Processing



Responsible for:



\- Sending receipt information to AI

\- Receiving structured output

\- Extracting purchase details



\---



\## Database



SQLite stores:



\- Receipts

\- Stores

\- Items

\- Categories

\- Discounts

\- Loyalty points



\---



\## Reporting



Excel generation provides:



\- Monthly reports

\- Yearly summaries

\- Spending analysis



\---



\# Data Flow



User



|



Receipt File



|



TrackMySpend



|



SQLite Database



|



Excel Report



\---



\# Future Expansion



Possible future modules:



\- Budget tracking

\- Price history

\- Shopping assistant

\- Barcode lookup

\- Mobile application

