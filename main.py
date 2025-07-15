from mean_var_std import calculate

# Test input with 9 numbers
test_input = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Call the function and print the results
output = calculate(test_input)

# Display the result in a readable format
for key, value in output.items():
    print(f"{key.capitalize()}: {value}")