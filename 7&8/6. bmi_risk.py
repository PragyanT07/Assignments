'''a program that reads weight and height data from a csv file, calculates body mass index (bmi) 
and assigns a health risk category based on bmi values. it then displays the updated dataframe.'''

import pandas as pd # import pandas for data manipulation
import numpy as np # import numpy for numerical operations

# determines health risk category based on bmi value
def calculate_risk(bmi):
    if bmi < 18.5:
        return "nutrient deficient"
    elif 18.5 <= bmi <= 24.9:
        return "lower risk"
    elif 25 <= bmi <= 29.9:
        return "heart disease risk"
    elif 30 <= bmi <= 34.9:
        return "higher risk of diabetes, heart disease"
    elif bmi >= 40: # condition for 40 or higher
        return "serious health condition risk"
    else:
        return "moderate risk" # fallback for any unhandled range

# reads health data, calculates bmi and risk, and displays the updated dataframe
def process_health_data(filename="weight_height.csv"):

    try:
        df = pd.read_csv(filename) # read csv into dataframe
        if df.empty:
            print(f"the file '{filename}' is empty or contains no data. no bmi or risk to calculate.")
            return
        
        # ensure columns are numeric, coerce errors to nan
        df['height'] = pd.to_numeric(df['height'], errors='coerce')
        df['weight'] = pd.to_numeric(df['weight'], errors='coerce')
        
        # drop rows where critical data might be missing after coercion
        df.dropna(subset=['height', 'weight'], inplace=True)

        if df.empty:
            print(f"no valid numeric height/weight data found in '{filename}' after cleaning.")
            return

    except FileNotFoundError:
        print(f"error: the file '{filename}' was not found. please ensure it exists in the same directory.") # clearer error message
        return
    except Exception as e:
        print(f"an error occurred while reading the file: {e}") # general read error
        return

    # calculate bmi: convert height to meters, then weight / (height_m ** 2)
    df['height_m'] = df['height'] / 100 # convert height from cm to meters
    df['bmi'] = df['weight'] / (df['height_m'] ** 2) # calculate bmi
    
    # apply the calculate_risk function to the bmi column to create the 'risk' column
    df['risk'] = df['bmi'].apply(calculate_risk)
    
    df = df.drop(columns=['height_m']) # drop the temporary 'height_m' column

    print("\n--- health data with bmi and risk analysis ---")
    print(df.to_string()) # print the entire dataframe without truncation
    print("\n----------------------------------------------")

# main execution block
if __name__ == "__main__":
    process_health_data() 
