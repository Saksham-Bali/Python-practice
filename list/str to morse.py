code = ['._', '_...', '_._.', '_..', '.', '.._.', '__.', '....', '..', '.___']
text = input('Enter the text to be converted to morse (all in lowercase):')
morse = ''
for x in text:
    i = ord(x) - ord('a')
    morse += code[i] + ' '
print("The telegram in morse is: ", morse)
