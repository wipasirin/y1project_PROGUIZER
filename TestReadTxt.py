import pandas

data = pandas.read_excel("QuestionText.xlsx")
print(data)
a_data = {}
for i in data['Choice1']:
    a_data.setdefault(i)
print(a_data) 
for i in data['WebKey']:
    a_data.setdefault(i)
print(a_data)
