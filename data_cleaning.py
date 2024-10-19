import pandas as pd

def handle_missing_values(data):
    if isinstance(data, pd.DataFrame):
        valid_columns = [col for col in ['Customer ID', 'State', 'Gender', 'Education', 'Income', 'Monthly Premium Auto',
                        'Number of Open Complaints', 'Policy Type', 'Vehicle Class'] if col in data.columns and data[col].notna().any()]
        if valid_columns:
            data = data.dropna(subset=valid_columns)
        else:
            print("No valid columns to drop NA from.")
    return data

def handle_duplicates(data):
    if data is not None and isinstance(data, pd.DataFrame):
        data = data.drop_duplicates(keep='first')
    return data  

def format_date(data):
    if data is not None and isinstance(data, pd.DataFrame):
        if 'Date' in data.columns:
            data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    return data  

def format_gender(data):
    if data is not None and isinstance(data, pd.DataFrame):
        if 'Gender' in data.columns:
            data['Gender'] = data['Gender'].replace({'Female': 'F', 'Male': 'M', 'Femal': 'F', 'female': 'F'})
    return data  

def format_state(data):
    if data is not None and isinstance(data, pd.DataFrame):
        if 'State' in data.columns:
            data['State'] = data['State'].replace({'AZ': 'Arizona', 'Cali': 'California', 'WA': 'Washington'})
    return data  

def format_education(data):
    if data is not None and isinstance(data, pd.DataFrame):
        if 'Education' in data.columns:
            data['Education'] = data['Education'].replace({'Bachelors': 'Bachelor'})
    return data  

def format_vehicle_class(data):
    if data is not None and isinstance(data, pd.DataFrame):
        if 'Vehicle_Class' in data.columns:
            data['Vehicle_Class'] = data['Vehicle_Class'].replace({'Sports Car': 'Luxury', 'Luxury SUV': 'Luxury', 'Luxury Car': 'Luxury'})
    return data  

def format_income(data):
    if data is not None and isinstance(data, pd.DataFrame):
        if 'Income' in data.columns:
            data['Income'] = data['Income'].astype(str).str.replace(',', '').str.replace('$', '', regex=False).astype(float)
        else:
            print("Error: La columna 'Income' no se encuentra en el DataFrame.")
    else:
        print("Error: 'data' es None o no es un DataFrame.")
    return data

def format_column_names(data):
    if data is not None and isinstance(data, pd.DataFrame):
        # Reemplazar espacios por guiones bajos y poner en mayúscula la primera letra de cada palabra
        data.columns = [col.strip().replace(' ', '_').title().replace(' ', '_') for col in data.columns]
    else:
        print("Error: 'data' es None o no es un DataFrame.")
    return data

def format_number_of_complaints(data):
    if data is not None and isinstance(data, pd.DataFrame):
        if 'Number of Open Complaints' in data.columns:
            # Reemplazar palabras por números
            data['Number of Open Complaints'] = data['Number of Open Complaints'].str.replace('One', '1')
            data['Number of Open Complaints'] = data['Number of Open Complaints'].str.replace('Two', '2')
            data['Number of Open Complaints'] = data['Number of Open Complaints'].str.replace('None', '0')
            
            # Separar los valores con "/" y sumar los componentes si existen
            def sum_complaints(complaint):
                if isinstance(complaint, str):
                    parts = complaint.split('/')
                    try:
                        return sum([int(part) for part in parts if part.isdigit()])
                    except ValueError:
                        return 0  # Si hay error, devolver 0
                return complaint  # Devolver tal cual si no es string

            data['Number of Open Complaints'] = data['Number of Open Complaints'].apply(sum_complaints)
    return data

def format_customer_lifetime_value(data):
    if data is not None and isinstance(data, pd.DataFrame):
        if 'Customer-Lifetime-Value' in data.columns:
            # Eliminar el símbolo % y convertir a float
            data['Customer-Lifetime-Value'] = data['Customer-Lifetime-Value'].str.replace('%', '', regex=False).astype(float)
    return data

def clean_data(df):
    df = handle_missing_values(df)
    df = handle_duplicates(df)
    df = format_date(df)
    df = format_gender(df)
    df = format_state(df)
    df = format_education(df)
    df = format_vehicle_class(df)
    df = format_income(df)
    df = format_column_names(df)
    df = format_number_of_complaints(df)
    df = format_customer_lifetime_value(df)
    return df
