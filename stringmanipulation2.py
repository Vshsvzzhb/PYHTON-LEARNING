string = "Hello, World!"
vowels = "aeiouAEIOU"
count = sum(1 for char in string if char in vowels)
print("Jumlah vokal dalam string:", count)