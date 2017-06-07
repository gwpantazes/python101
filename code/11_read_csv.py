import csv

# Header will be an array of the Header labels
header = []

# Data will be a array of arrays by the time we process the data
data = []

# Open the file within a with block, the same way as with regular file reading
with open("data/biopsy.csv") as csvfile:
    reader = csv.reader(csvfile)    # Create a magic csv reader here
    for row in reader:     # For each line computed by the csv reader
        data.append(row)   # Add the processed row to data

# The csv reader lumped the header row in to the data
# Let's just slice that out
header = data[0]
data = data[1:]

# Ready to work with Header and Data
print("Header Row: {}".format(header))
print("Data prepared as Python arrays.")
print(data[:2], "... and {} more rows".format(len(data) - 2))

"""
Note: It's a better idea to do a simple math expression with length
than to create a whole new sliced array of data and take the length of it.
We could have used len(data[2:]), but what's actually happening
is a whole new array is created just for that slice, which is wasteful :(
Instead, we save resources by being clever and using math :) !
This is a good thing to remember as often as possible when programming,
but don't worry about it too much unless performance becomes a problem.
"""
