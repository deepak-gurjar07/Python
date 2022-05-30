def sum_math_I_II_average(list_of_dicts):
    for d in list_of_dicts:
        n1 = d.pop('I')
        n2 = d.pop('II')
        d['I+II'] = (n1 + n2)/2
    return list_of_dicts 

student_details= [
  {'id' : 1, 'subject' : 'math', 'I' : 70, 'II' : 82},
  {'id' : 2, 'subject' : 'math', 'I' : 73, 'II' : 74},
  {'id' : 3, 'subject' : 'math', 'I' : 75, 'II' : 86}
]

print(sum_math_I_II_average(student_details))
