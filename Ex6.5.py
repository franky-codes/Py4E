str = 'X-DSPAM-Confidence:0.8475'
col = str.find(':')
#print(col)
slice = str[col + 1 :]
f_slice = float(slice)
print(f_slice)
#print(type(f_slice))
