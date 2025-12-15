text=" welcome to sunbeam  "
print("text1:",text)
print("upper:",text.upper())
print("lower:",text.lower())
print("Capitalize:",text.capitalize())
print("Title:",text.title())

print("strip:",text.strip())
print("lstrip:",text.lstrip())
print("rstrip:",text.rstrip())


print("find(to):",text.find("to"))
print("count(e):",text.count("o"))

print("Replace(sunbeam, pune):",text.replace("sunbeam","pune"))



split=text.split()
print("Split text:",split)

print("join text:"," ".join(split))


print("starts with:",text.startswith("welcome"))
print("ends with:",text.endswith("sunbeam"))

text2="sunbeam123"
print("text2:",text2)
print("is alphabets:",text2.isalpha())
print("is digits:",text2.isdigit())
print("is alnum:",text2.isalnum())

print("len text1:",len(text))
print("len text2:",len(text2))

