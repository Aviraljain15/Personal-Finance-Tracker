# Python modules used in this project
import pandas as pd
import matplotlib.pyplot as mlt
import seaborn as sb

# Getting the columns of the main data into lists
expenses = ['Rent','Loan_Repayment','Insurance','Groceries','Transport',
            'Eating_Out','Entertainment','Utilities','Healthcare','Education',
            'Miscellaneous']
savings = ['Potential_Savings_Groceries','Potential_Savings_Transport','Potential_Savings_Eating_Out',
            'Potential_Savings_Entertainment','Potential_Savings_Utilities','Potential_Savings_Healthcare',
            'Potential_Savings_Education','Potential_Savings_Miscellaneous']

# Reading the data from the CSV file
data = pd.read_csv("DataPFT.csv")

# -------- Functions -------- #

def income(dt):
    """Calculate total and average income from the dataset."""
    net_income = dt['Income'].sum()
    average = dt['Income'].mean()
    return net_income, average

def summary_expenses(dt, expenses):
    """Calculate total and average expenses across all categories."""
    net_expense = dt[expenses].sum()
    average = dt[expenses].mean()
    return net_expense, average

def saving(dt, savings):
    """Calculate total and average potential savings across all categories."""
    net_savings = dt[savings].sum()
    average = dt[savings].mean()
    return net_savings, average

def income_spent(df, expense_coloumns):
    """Add net expenses and expense-to-income ratio columns to the dataframe."""
    df['net_Expenses'] = df[expense_coloumns].sum(axis=1)
    df['income_spent'] = df['net_Expenses'] / df['Income']
    return df

def top_spending(df, expense_coloumns):
    """Find the category with the highest total spending and return its name and value."""
    total = df[expense_coloumns].sum()
    highest = total.idxmax()
    top_value = total.max()
    return highest, top_value

def income_distribution(df):
    """Plot a histogram showing the distribution of income."""
    sb.histplot(df['Income'], bins=30)
    mlt.title('Income Distribution')
    mlt.xlabel('Income')
    mlt.ylabel('Count')
    mlt.show()

def category_distribution(df, expense_column):
    """Plot a bar chart showing total spending per expense category."""
    total = df[expense_column].sum()
    sb.barplot(x=total.index, y=total.values)
    mlt.title('Category Distribution')
    mlt.xlabel('Categories')
    mlt.ylabel('Total Amount Spent')
    mlt.show()

def savings_patterns(df, expense_column):
    """Plot a pie chart showing distribution of potential savings."""
    total = df[expense_column].sum()
    mlt.pie(total.values, labels=total.index, autopct='%1.1f%%')
    mlt.title('Savings Distribution')
    mlt.show()

def expense_to_income_ratio(df):
    """Plot a histogram of the expense-to-income ratio."""
    sb.histplot(df['income_spent'], bins=30)
    mlt.title("Distribution of Expense-to-Income Ratio")
    mlt.xlabel("Expense-to-Income Ratio")
    mlt.ylabel("Count")
    mlt.show()

def highlight_top_category(df, expense_columns):
    """Highlight the top spending category in red while others remain blue on a bar chart."""
    total = df[expense_columns].sum()
    highest = total.idxmax()
    top_value = total.max()
    colors = ["red" if cat == highest else "blue" for cat in total.index]
    sb.barplot(x=total.index, y=total.values, palette=colors)
    mlt.title(f"Top Spending Category: {highest} (${top_value:.2f})")
    mlt.xlabel("Categories")
    mlt.ylabel("Total Amount Spent")
    mlt.xticks(rotation=45)
    mlt.show()

# -------- Main Program -------- #
def main():
    """Display the CLI menu and handle user inputs to run specific functions."""
    while True:
        print("--Personal Finance Tracker Menu--")
        print("1. Income Summary")
        print("2. Expense Summary")
        print("3. Savings Summary")
        print("4. Income Distribution Plot")
        print("5. Category Distribution Plot")
        print("6. Savings Patterns Plot")
        print("7. Expense-to-Income Ratio Plot")
        print("8. Top Spending Category")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            net, avg = income(data)
            print(f"Total Income: {net:.2f}, Average Income: {avg:.2f}")
        elif choice == "2":
            total, avg = summary_expenses(data, expenses)
            print("Expense Summary:\n", total)
            print("Average per Category:\n", avg)
        elif choice == "3":
            total, avg = saving(data, savings)
            print("Savings Summary:\n", total)
            print("Average per Category:\n", avg)
        elif choice == "4":
            income_distribution(data)
        elif choice == "5":
            category_distribution(data, expenses)
        elif choice == "6":
            savings_patterns(data, savings)
        elif choice == "7":
            data_with_ratio = income_spent(data, expenses)
            expense_to_income_ratio(data_with_ratio)
        elif choice == "8":
            highlight_top_category(data, expenses)
        elif choice == "9":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()
