import pandas as pd

def separate_by_virus(input_file, virus_list):
    """
    Reads a CSV file and creates a separate CSV file for each virus in the virus list.

    Parameters:
    input_file (str): The path to the input CSV file.
    output_directory (str): The directory where output CSV files will be saved.
    virus_list (list): A list of viruses to separate by.
    """
    output_directory = '/Users/shaunputhuparambil/Desktop'

    try:
        # Load the input CSV file
        df = pd.read_csv(input_file)

        # Loop through each virus in the list
        for virus in virus_list:
            # Filter the DataFrame for the current virus
            virus_df = df[df['DiseaseLevel1'] == virus]

            output_file = f"{output_directory}/{virus.replace(' ', '_')}_data.csv"

            virus_df.to_csv(output_file, index=False)

            print(f"Data for {virus} saved to {output_file}")

    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Virus list
virus_list = ["Buffalopox", "Ebola virus", "Hantavirus", "Influenza A", "Lassa fever", 
              "Lujo mammarenavirus", "Marburg fever", "Monkeypox", "Nipah virus", "Oropouche fever"]

separate_by_virus("filtered_DONdatabase.csv", virus_list)