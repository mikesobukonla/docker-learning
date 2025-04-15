import pandas as pd

# Read the content of the file
with open('piechartselements.txt', 'r') as file:
    lines = file.readlines()

# Create a DataFrame from the lines
df = pd.DataFrame(lines)

# Save the DataFrame to an Excel file
df.to_excel('chartlines_data.xlsx', index=False, header=False)

print("Each line of the content has been successfully saved to lines_data.xlsx.")
