#!/env/python
import sys

if sys.version_info < (2,7):
  print "\nYou are running Python version: "+sys.version
  print "Please upgrade to 2.7+ / 3.0+"
  exit()

# generate lookups
lookup1a = {i : chr(64+i) for i in range(1,27)}   # 1:A, 2:B, etc
lookupa1 = {chr(64+i):i for i in range(1,27)}     # A:1, B:2, etc
lookup0a = {i : chr(65+i) for i in range(0,26)}   # 0:A, 1:B, etc
lookupa0 = {chr(64+i):i-1 for i in range(1,27)}   # A:0, B:1, etc 


# Common functions
def normalize(text, norm=[]):
  """normalizes input based upon arguments"""
  if 'upper' in norm and text.isupper() == False:
    print "WARN: Converting to uppercase..."
    text=text.upper()
  if 'alpha' in norm and text.isalpha() == False:
    print "WARN: Stripping non-alpha..."
    text=filter(str.isalpha, text)
  return text

def repeat_fill(text_in, length):
  """repeat (or truncate) a string to a new length"""
  a, b = divmod(length, len(text_in))
  return text_in * a + text_in[:b]



# Caeser cipher
def caeser(text, rotate=None):
  """Rotate each character X times.  Brute force rot0-rot26 if rotate arg is not specified."""
  n_text = normalize(text, ['upper','alpha'] ) #Normalize input

  # Rotate once if rotate arg is specified, othersise all combinations
  if rotate != None:
    return ''.join([chr((((ord(i)-65+rotate)%26)+65)) for i in n_text])
  else:
    outdi={}
    for r in range(27):
      outdi[r] = ''.join([chr((((ord(i)-65+r)%26)+65)) for i in n_text])
    return outdi



# OTP and vegenere ciphers  
def otp_encrypt(cleartext, key, lookup_fwd=lookupa0, lookup_rev=lookup0a):
  """sample usage: ciphertext = otp_encrypt('HELLO', 'XMCKL', lookupa1, lookup1a)"""
  
  if len(key) < len(cleartext):
    print "WARN: Your key is shorter than the plaintext.  Falling back to a vigenere cipher..."
    key = repeat_fill(key,len(cleartext))

  ciphertext=''
  for idx, val in enumerate(cleartext):
    msg_key = lookup_fwd[val] + lookup_fwd[key[idx]]
    modded = msg_key % 26
    ciphertext+=lookup_rev[modded]
  return ciphertext

def otp_decrypt(ciphertext, key, lookup_fwd=lookupa0, lookup_rev=lookup0a):
  """sample usage: cleartext = otp_encrypt('EQNVZ','XMCKL', lookupa1, lookup1a)"""

  if len(key) < len(ciphertext):
    print "WARN: Your key is shorter than the plaintext.  Falling back to a vigenere cipher..."
    key = repeat_fill(key,len(ciphertext))

  cleartext=''
  for idx, val in enumerate(ciphertext):
    cipher_key = lookup_fwd[val] - lookup_fwd[key[idx]]
    modded = cipher_key % 26
    cleartext+=lookup_rev[modded]
  return cleartext
  
def otp_brute_force(ciphertext, key_within):
  """Try all possible keys within a block of text based upon the size of the ciphertext"""

  haystack = [otp_decrypt(ciphertext,key_within[i:], lookupa0, lookup0a) for i in range(len(key_within)-len(ciphertext))]
  #with open('otp.txt','w') as f:
  #  f.write('\n'.join(haystack))
  return haystack
  


