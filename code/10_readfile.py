# Header will be an array of the Header labels
header = []

# Data will be a array of arrays by the time we process the data
data = []

# Open the file within a with block
with open("data/biopsy.csv") as datafile:

    header = datafile.readline()    # Grab the header line of the csv file
    header = header.strip()         # Strip off the whitespace
    header = header.split(',')      # Now the header is an array
    for i in range(0, len(header)): # Clean up the header columns
        # Strip off any quotation marks, modifying the array in place
        header[i] = header[i].strip('"')

    # Since we read one line already (the header),
    # the file read pointer will remember our place
    # and we can iterate through all the remaining data rows
    # The same as calling readline() for all remaining rows
    for row in datafile:    # For the remaining data rows
        row = row.strip().split(',')    # Clean whitespace and convert to an array

        for columnIndex in range(0, len(row)):  # For each column in the row
            # Strip off any quotation marks, modifying the array in place
            row[columnIndex] = row[columnIndex].strip('"')

        data.append(row)   # Add the processed row to data

# Ready to work with Header and Data
print("Header Row: {}".format(header))
print("Data prepared as Python arrays.")
print(data[:2], "... and {} more rows".format(len(data) - 2))
