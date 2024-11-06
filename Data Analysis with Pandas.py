import pandas as pd


# Load the CSV file into a DataFrame
def load_sales_data(file_path):
    try:
        # Reading the CSV file and handling missing or corrupt data with 'na_filter'
        data = pd.read_csv(file_path, na_filter=True)
        print("Data loaded successfully.\n")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None


# Function to calculate total and average sales
def calculate_sales(data):
    # Dropping rows where sales are missing or not valid (NaN or non-numeric values)
    valid_sales = pd.to_numeric(data['Sales'], errors='coerce')
    total_sales = valid_sales.sum()
    average_sales = valid_sales.mean()
    print(f"Total Sales: {total_sales}")
    print(f"Average Sales: {average_sales}\n")


# Function to filter data by a specific month
def filter_by_month(data, month):
    filtered_data = data[data['Month'] == month]
    print(f"Filtered Data for Month: {month}")
    print(filtered_data)
    return filtered_data


# Function to group sales by product category and calculate total sales for each category
def group_by_category(data):
    grouped_data = data.groupby('Product Category')['Sales'].sum()
    print("Total Sales by Product Category:")
    print(grouped_data)
    return grouped_data


# Main function to perform the analysis
def main():
    file_path = 'sales_data.csv'  # Path to the CSV file
    data = load_sales_data(file_path)

    if data is not None:
        # Handle missing or corrupt data by dropping rows with missing sales values
        data = data.dropna(subset=['Sales'])

        # Calculate total and average sales
        calculate_sales(data)

        # Filter data by a specific month (e.g., "January")
        filter_by_month(data, 'January')

        # Group data by product category and calculate total sales
        group_by_category(data)


# Run the analysis
if __name__ == "__main__":
    main()
