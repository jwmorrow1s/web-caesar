import string

def alpha_placement(char):
  """takes a character and gives its case: 0 for lower, 1 for upper, or -1 if other character, and placement 0-25 (a/A-z/Z)"""
  if char in string.ascii_lowercase:
    return (0, ord(char) % ord('a'))
  elif char in string.ascii_uppercase:
    return (1, ord(char) % (ord('A')))
  else: return (-1, char)
  
def rotate_char(alpha_tuple, offset):
  """takes result of alpha_placement(char) and an offset to rotate the character by that offset"""
  if alpha_tuple[0] == 0:
    return chr(ord('a') + ((alpha_tuple[1]) + offset) % 26)
  elif alpha_tuple[0] == 1:
    return chr(ord('A') + ((alpha_tuple[1]) + offset) % 26)
  else:
    return alpha_tuple[1]


def encrypt_caesar(string_, offset):
  ret = ""
  for char in string_:
    ret += (rotate_char(alpha_placement(char), offset))
  return ret
  
def main():
  text = input("Type a message:")
  rot = int(input("Rotate by:"))
  print(encrypt_caesar(text,rot))
  
if __name__ == "__main__":
  main()
