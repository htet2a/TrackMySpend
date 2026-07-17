# TrackMySpend Architecture



## 1. Architecture Overview



TrackMySpend is a personal expense tracking application that converts receipt images and PDF files into structured spending records.



The application workflow:



```text

Receipt Image/PDF

        |

        v

Receipt Processing

        |

        v

AI Information Extraction

        |

        v

Standard Expense Data Model

        |

        v

SQLite Database

        |

        v

Excel Report Generator

```



The design goal is:



- Simple to use

- Easy to modify

- Secure

- Low resource usage

- Accurate expense tracking





---



# 2. Technology Architecture



## Programming Language



Python 3.13



## Local Database



SQLite



Purpose:



- Store extracted receipt information

- Track processed receipts

- Prevent duplicate processing



## Data Processing



Libraries:



- pandas

- openpyxl



Purpose:



- Create and update Excel reports

- Calculate summaries



## Receipt Processing



Libraries:



- PyMuPDF



Purpose:



- Read PDF receipts



- Pillow



Purpose:



- Process receipt images





## AI Extraction



Initial provider:



Google Gemini API



Purpose:



- Extract receipt information

- Identify purchased items

- Assist categorization



The AI layer is designed to be replaceable in the future.





---



# 3. Receipt Processing Workflow



Weekly workflow:



## Step 1



User uploads receipts into:



`receipts/incoming`



Supported formats:



- JPG

- JPEG

- PNG

- PDF





## Step 2



Application processes each receipt one at a time.



Information extracted:



- Date

- Time

- Store name

- Receipt number

- Item code

- Item description

- Category

- Quantity

- Unit price

- Discount

- Currency

- Amount

- Loyalty points





If information cannot be found:





N/A





is stored.





## Step 3



Processed information is saved into SQLite.





## Step 4



Excel workbook is updated.





## Step 5



Processed receipts are moved:





`receipts/processed`





Failed receipts are moved:





`receipts/error`







---



# 4. Standard Excel Design



The application uses one Excel workbook per year.



Example:





`TrackMySpend_2026.xlsx`





Workbook sheets:



```text

January

February

March

...

December

Summary

```



Each month contains item-level records.



Example:



| Date | Store | Item | Category | Currency | Amount |

|---|---|---|---|---|---|

|2026-07-17|IKEA|Shelf|Home|CAD|80|





The application appends new receipts instead of recreating the file.





---



# 5. Currency Handling



The application supports multiple currencies.



Rules:



- Keep original receipt currency.

- Do not combine different currencies.

- Calculate totals separately.



Example:





CAD Total: 850.00



USD Total: 120.00





No currency conversion is required.



If a receipt provides both transaction currency and charged currency:



Example:



Receipt:

USD 100



Charged amount:

CAD 142.50





The charged amount can be stored as the reporting amount when it is available in the receipt.



The original receipt currency is kept for reference.



The application avoids double counting.



---



# 6. Summary Calculation



The system only totals meaningful numeric fields.



Included:



- CAD spending

- USD spending

- Discount amount

- Loyalty points earned

- Loyalty points redeemed

- Number of receipts processed





Not summed:



- Item codes

- Unit prices

- Discount percentages





Discount percentage is stored per item.





---



# 7. Resource Efficiency Design



TrackMySpend is designed for normal Windows laptops.



Design principles:



- Process one receipt at a time

- Avoid loading all historical records into memory

- Store history in SQLite

- Generate Excel reports from required data only

- Resize large images before AI processing





Expected impact:



- Low CPU usage

- Low memory usage

- Suitable for weekly receipt processing





---



# 8. Security Design



Security principles:



- User manually selects receipts

- No email integration

- No access to unrelated folders

- No scanning of personal files

- Data stored locally





The application does not collect:



- Passwords

- Credit card numbers

- Banking information





Only receipt information required for expense tracking is processed.





---



# 9. Future Improvements



Possible future features:



- Local AI processing

- Better product recognition

- Product history search

- Loyalty program dashboard

- Secure mobile receipt upload

- Spending analytics dashboard

