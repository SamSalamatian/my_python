def to_binary(input_value):
    try:
        binary_representation = bin(input_value)
        return binary_representation
    except Exception as e:
        return f"Error: {e}"

# Test the function
input_value = int(input("what integer?"))
binary_value = to_binary(input_value)
print(f"{binary_value}")
