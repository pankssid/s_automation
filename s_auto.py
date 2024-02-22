import streamlit as st
import pandas as pd
from datetime import datetime
import base64

def main():
    st.title("File Upload and Column Selection App")

    # Upload file through Streamlit
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file is not None:
        st.success("File uploaded successfully!")

        # Read the uploaded CSV file into a DataFrame
        df = pd.read_csv(uploaded_file)

        # Display the original DataFrame
        st.write("Original DataFrame:")
        st.write(df)
        predefined_columns = [
            "Order ID", "Shiprocket Created At", "Status", "Customer Name",
            "Customer Mobile", "Payment Method", "Order Total", "AWB Code",
            "EDD", "Delayed Reason", "Order Delivered Date"
        ]

        
        # Allow users to select columns to keep
        # selected_columns = st.multiselect("Select columns to keep", predefined_columns)

        # Create a new DataFrame with selected columns
        selected_df = df[predefined_columns]

        selected_df.colums = [
            "Order ID",  "Created At", "Status", "Customer Name",
            "Customer Mobile", "Payment Method", "Order Total", "AWB Code",
            "EDD", "Delayed Reason", "Order Delivered Date"
        ]

        selected_df=selected_df[~selected_df.Status.isin(['CANCELED'])].reset_index(drop=True)
        
        # Display the modified DataFrame
        st.write("DataFrame with selected columns:")
        st.write(selected_df)

        # Provide a link to download the modified DataFrame as a CSV file
        st.markdown(get_csv_download_link(selected_df), unsafe_allow_html=True)
def get_csv_download_link(df):
    # Generate a link to download the DataFrame as a CSV file with today's date
    today_date = datetime.today().strftime('%Y-%m-%d')
    filename = f"selected_data_{today_date}_orders.csv"
    
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">Download CSV</a>'
    return href

if __name__ == "__main__":
    main()
