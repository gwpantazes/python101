import csv
import statistics

# There is a bug in this program. Can you catch it? Hint: It's an important piece of the data crunching algorithm.

# Header will be an array of the Header labels
header = []

# Data will be a array of arrays by the time we process the data
data = []

# Initialize the Average values to zero
# Since our mean algorithm will compute a sum
# And calculate the average at the end
average_v = [0] * 9     # Creates a list of 9 elements of the value 0

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
print("Computing averages for fields v1 through v9")

v_slice = slice(2,11)   # Slices can be predefined for reusability
average_headers = header[v_slice]
print("Confirming V Field header labels and indices:", average_headers)

# We will use a simple algorithm to compute averages for each V field
# Average = Sum / Total #
# But first we need to compute the sum for each field
for row in data:
    v_fields = row[v_slice] # Reuse the slice object to get the right fields out of the row
    print(v_fields)

    for i in range(0,len(v_fields)):

        try:        # Error check in case value is "NA" or invalid
            value = int(v_fields[i])    # Convert to number
        except ValueError:
            print("ERROR invalid value at V{}: {}".format(i+1, v_fields[i]))
            # It failed to convert to number, so skip back to the beginning of the for loop without summing
            continue

        # value = int(v_fields[i])  # Convert to a number
        # Sum on average_v in place. Notice we are converting to a number
        average_v[i] = average_v[i] + value

print("V Field computed sums:", average_v)

for i in range(0, len(average_v)):
    # Indentation matters, but in open parentheses we can do multiline code for clarity
    print("{label} average = {value}".format(
            label = average_headers[i],
            value = average_v[i]/len(data)
        )
    )
