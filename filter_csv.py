import pandas as pd

def filter_csv(input_file, output_file, disease_list):
    """
    Filters a CSV file based on specified diseases and writes the result to a new CSV file.

    Parameters:
    input_file (str): The path to the input CSV file.
    output_file (str): The path to the output CSV file.
    disease_list (list): A list of diseases to filter by.
    """
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(input_file)

        # Filter the DataFrame based on the DiseaseLevel1 column
        filtered_df = df[df['DiseaseLevel1'].isin(disease_list)]

        # Save the filtered DataFrame to a new CSV file
        filtered_df.to_csv(output_file, index=False)

        print(f"Filtered CSV saved to {output_file}")

    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

virus_list = ["Buffalopox", "Ebola virus", "Hantavirus", "Influenza A", "Lassa fever", 
              "Lujo mammarenavirus", "Marburg fever", "Monkeypox", "Nipah virus", "Oropouche fever"]

# Call the function with the appropriate file paths and the disease list
filter_csv("DONdatabase.csv", "filtered_DONdatabase.csv", virus_list)
