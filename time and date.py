from datetime import datetime
x = '10:04:00'
y = '11:03:11' 
format = '%H:%M:%S'
time = datetime.strptime(y, format) - datetime.strptime(x, format)
print time
