students = {'shivam':{'class':'V',
        'rolld_id':2},
        'hero':{'class':'V',
        'roll_id':3}}
for a in students:
    print(a)
    for b in students[a]:
        print (b,':',students[a][b])
