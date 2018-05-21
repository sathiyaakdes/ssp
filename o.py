from datetime import datetime
a = '10:04:00'
b = '11:03:11' 
format = '%H:%M:%S'
time = datetime.strptime(b, format) - datetime.strptime(a, format)
print time
