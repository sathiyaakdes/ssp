def camelCase(st):
    output = ''.join(x for x in st.title() if x.isalpha())
    return output[0].upper() + output[1:]
s=str(input('enter the string'))
r=camelCase(s)
print (r)
