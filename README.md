Personal Finance Tracker
A simple, beginner-friendly Python project to help you manage your income and expenses from the command line. This tracker lets you log transactions, view summaries, and save or load your financial data for easy tracking and analysis.

Features
Add Income & Expenses: Record income and expense transactions with categories.

View Summary: Instantly see total income, total expenses, and net savings.

Persistent Storage: Save and load your data using JSON files.

Simple CLI Interface: Easy-to-use command-line prompts for all operations.

Extensible: Easily add new features such as CSV export, date filtering, or data visualization.

Getting Started
Prerequisites
Python 3.6 or higher installed on your system.

Installation
Clone the Repository

bash
git clone https://github.com/YOUR-USERNAME/personal-finance-tracker.git
cd personal-finance-tracker
(Optional) Create a Virtual Environment

bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install Dependencies

No external dependencies are required for the basic version.

For advanced features (CSV, plots), you may need pandas or matplotlib.

Usage
Run the Application

bash
python finance_tracker.py
Follow the Prompts

Add income or expense with category and amount.

View a summary of your finances.

Save or load your data for future use.

Example
text
Welcome to the Personal Finance Tracker!

Options: Add Income, Add Expense, Save, Load, Summary, Exit
What would you like to do? add income
Enter amount: 5000
Enter category: Salary
Income added.

Options: Add Income, Add Expense, Save, Load, Summary, Exit
What would you like to do? summary

Income Summary:
  Salary: $5000
Total Income: 5000
Expenses Summary:
Total Expenses: 0
Net Savings: 5000
File Structure
File	Description
finance_tracker.py	Main Python script for the tracker
data.json	(Optional) Saved data file
README.md	Project documentation
Customization Ideas
Add CSV export/import.

Integrate data visualization with matplotlib.

Add date support for transactions.

Build a simple GUI using Tkinter or PyQt.