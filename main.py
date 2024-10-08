import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'C:/Users/Michael Ajayi/PycharmProjects/pythonProject4/bank.csv'

try:
    df = pd.read_csv(file_path)
    print("File loaded successfully!")
except Exception as e:
    print("Error loading file:", e)
    df = None

if df is not None:
    # Display basic information about the dataset
    print("Data Overview:")
    print(df.info())

    # Display the first few rows of the dataset
    print("\nFirst 5 Rows:")
    print(df.head())

    # Check for missing values
    print("Missing Values:\n", df.isnull().sum())

    # Handle missing values (e.g., drop rows with missing values)
    df_cleaned = df.dropna()

    # Remove duplicates
    df_cleaned = df_cleaned.drop_duplicates()

    # Convert data types if necessary (example: converting a 'Date' column to datetime)
    # df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date'])

    # Display the cleaned data info
    print("Cleaned Data Overview:")
    print(df_cleaned.info())

    # Summary statistics for numerical columns
    print("Summary Statistics:\n", df_cleaned.describe())

    # Count of unique values in categorical columns
    categorical_columns = df_cleaned.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        print(f"Unique values in {col}: {df_cleaned[col].nunique()}")

    # ---- Additional Data Analysis Methods ----

    # Visualize the distribution of the 'balance' column
    if 'balance' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df['balance'], kde=True)
        plt.title('Distribution of balance')
        plt.xlabel('balance')
        plt.ylabel('Frequency')
        plt.show()
    else:
        print("Column 'balance' not found in the dataset.")

    # 2. Correlation Analysis: Correlation matrix of numerical columns
    df_numeric = df_cleaned.select_dtypes(include=['number'])
    if not df_numeric.empty:
        correlation_matrix = df_numeric.corr()
        plt.figure(figsize=(12, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
        plt.title('Correlation Matrix')
        plt.show()
    else:
        print("No numeric columns found for correlation analysis.")

    # 3. Group By and Aggregation: Summarize data by categories
    if 'Category' in df_cleaned.columns:
        category_summary = df_cleaned.groupby('Category').agg({
            'Sales': 'sum',
            'Revenue': 'sum',
            'Profit': 'mean'
        }).reset_index()
        print("\nCategory Summary:")
        print(category_summary)
    else:
        print("Column 'Category' not found in the dataset.")

    # 4. Feature Engineering: Creating new features
    if 'Profit' in df_cleaned.columns and 'Revenue' in df_cleaned.columns:
        df_cleaned['Profit Margin'] = df_cleaned['Profit'] / df_cleaned['Revenue'] * 100
        print("\nFeature Engineering - First 5 Rows with New Feature:")
        print(df_cleaned.head())
    else:
        print("Columns 'Profit' and/or 'Revenue' not found in the dataset.")

    # Optional: Save the cleaned and processed dataset
    df_cleaned.to_csv('C:/Users/Michael Ajayi/PycharmProjects/pythonProject4/bank_cleaned.csv', index=False)
    print("Cleaned dataset saved to 'bank_cleaned.csv'.")
