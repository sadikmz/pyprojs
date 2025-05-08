data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
word = data.split()
email = word[1]
pieces  = email.split('@')
print(pieces[1])

