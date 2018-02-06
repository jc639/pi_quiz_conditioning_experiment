# simple script to import the questions and store as .py
# open questions file
with open('questions.txt', 'r', encoding='utf-8') as f:
    q = []
    a = []
    for lines in f.readlines():
        if lines != '\n':
            split_line = lines.split('\t')
            q.append(split_line[0])
            if 'true' in lines.lower():
                a.append('T')
            else:
                a.append('F')

# remove new lines, true/True, false/False from remaining questions
q = [ques.replace('\n', '') for ques in q]
q = [ques.replace('true', '') for ques in q]
q = [ques.replace('True', '') for ques in q]
q = [ques.replace('false', '') for ques in q]
q = [ques.replace('False', '') for ques in q]

# 201 qs and 166 is blank
del q[166]
del a[166]

# remove trailing whitespace
q = [ques.rstrip() for ques in q]
q_a = [i for i in zip(q, a)]

encoding = '''#!/usr/bin/env python
# -*- coding: utf-8 -*-'''
# write to a python file
with open('true_false.py', 'w') as f:
    f.writelines(encoding)
    f.writelines('\n\n')
    f.writelines('q_a = ' + str(q_a))

