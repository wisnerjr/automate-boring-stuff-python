def comma_code(words):
  if len(words) == 1:
    return words[0]
  return '{}, and {}'.format(', '.join(words[:-1]), words[-1])

try:
  str = input()  
  print(comma_code(str))
except:
  print('Empty input!')