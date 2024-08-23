import re 

string='abdul'
pattern = 'a'

if re.match(pattern,string):
    print('Match Found')
else: 
    print('Match not found!')
    
if re.search(pattern,string):
    print('Match found')
else:
    print('match not found !')