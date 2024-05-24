import pandas as pd
from pyproj import Transformer
from tkinter import filedialog
from tkinter import Tk

def convert_coordinates(input_file, output_file):
    # Load the data
    df = pd.read_csv(input_file)

    # Convert 'x' and 'y' columns to numeric
    df['x'] = pd.to_numeric(df['x'], errors='coerce')
    df['y'] = pd.to_numeric(df['y'], errors='coerce')

    # Create a transformer
    transformer = Transformer.from_crs("EPSG:4326", "EPSG:25832", always_xy=True)

    # Apply the transformation
    df['x'], df['y'] = zip(*df.apply(lambda row: transformer.transform(row['y'], row['x']), axis=1))

    # Save the transformed data to a new CSV file
    df[['prove','x', 'y']].to_csv(output_file, index=False)

def select_input_file():
    filename = filedialog.askopenfilename(filetypes = (("CSV files","*.csv"),("all files","*.*")))
    return filename

def select_output_file():
    filename = filedialog.asksaveasfilename(defaultextension=".csv")
    return filename

def main():
    root = Tk()
    root.withdraw() # Hide the main window
    print("Format: proeve,x,y")
    input_file = select_input_file()
    output_file = select_output_file()
    convert_coordinates(input_file, output_file)

if __name__ == "__main__":
    main()