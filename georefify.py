import pandas as pd

def georef_csv(input_file, output_file):
    """
    Creates a new CSV file with specified columns and copies data from the input CSV file to the new CSV file.

    Parameters:
    input_file (str): The path to the input CSV file.
    output_file (str): The path to the output CSV file.
    """
    try:
        # Load the input CSV file
        df = pd.read_csv(input_file)

        # Initialize a new DataFrame with the required columns
        new_df = pd.DataFrame(columns=["locality string", "country", "state", "county", 
                                       "latitude", "longitude", "correction status", 
                                       "precision error polygon", "multiple results", 
                                       "DONid", "Locality String Present"])

        # Copy data from the input DataFrame to the new DataFrame
        new_df["DONid"] = df["DONid"]
        new_df["country"] = df["Country"]
        new_df["locality string"] = df["OutbreakEpicenter"]
        new_df["Locality String Present"] = df["OutbreakEpicenter"].notnull()

        # Set 'locality string' to 'country' where 'OutbreakEpicenter' is missing
        # Replace NaN in 'locality string' with False in 'Locality String Present'
        new_df.loc[new_df["locality string"].isnull(), "locality string"] = new_df["country"]
        new_df.loc[new_df["locality string"].isnull(), "Locality String Present"] = False

        # Save the new DataFrame to a CSV file
        new_df.to_csv(output_file, index=False)

        print(f"New CSV saved to {output_file}")

    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with the appropriate file paths
georef_csv("filtered_DONdatabase.csv", "new_DONdatabase.csv")