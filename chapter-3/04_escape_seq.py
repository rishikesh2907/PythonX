a = "Rishikesh is a good boy\nbut not a \tbad \"boy\""
b = "Rishikesh is a good boy but\r not a \bbad boy"  # any characters printed after \r will overwrite the existing text from the start of the line.
print(a)
print(b)