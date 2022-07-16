

fid = open('Text')
print(fid)

i = fid.read().strip('/n')
print(i)

print("=" * 30)
print(len(i))
print(type(i))


