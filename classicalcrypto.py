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



def get_alpha(everything):
  'returns alpha only'
  return filter(str.isalpha, everything)



  
def otp_encrypt(cleartext, key, lookup_fwd, lookup_rev):
  "sample usage: ciphertext = otp_encrypt('HELLO', 'XMCKL', lookupa0, lookup0a)"
  ciphertext=''
  for idx, val in enumerate(cleartext):
    msg_key = lookup_fwd[val] + lookup_fwd[key[idx]]
    modded = msg_key % 26
    ciphertext+=lookup_rev[modded]
  return ciphertext

def otp_decrypt(ciphertext, key, lookup_fwd, lookup_rev):
  """sample usage: cleartext = otp_encrypt('EQNVZ','XMCKL', lookupa0, lookup0a)
  key must be >= len(ciphertext)"""
  cleartext=''
  for idx, val in enumerate(ciphertext):
    cipher_key = lookupa0[val] - lookupa0[key[idx]]
    modded = cipher_key % 26
    cleartext+=lookup0a[modded]
  return cleartext
  
  
  
####BRUTE FORCE OTP
#key = """ISOLVEMYPROBLEMSANDISEETHELIGHTWEGOTTAPLUGANDTHINKWEGOTTAFEEDITRIGHTTHEREAINTNODANGERWECANGOTOFARWESTARTBELIEVINGNOWTHATWECANBEWHOWEAREGREASEISTHEWORDTHEYTHINKOURLOVEISJUSTAGROWINGPAINWHYDONTTHEYUNDERSTANDITSJUSTACRYINGSHAMETHEIRLIPSARELYINGONLYREALISREALWESTARTTOFINDRIGHTNOWWEGOTTOBEWHATWEFEELGREASEISTHEWORDGREASEISTHEWORDISTHEWORDTHATYOUHEARDITSGOTGROOVEITSGOTMEANINGGREASEISTHETIMEISTHEPLACEISTHEMOTIONGREASEISTHEWAYWEAREFEELINGWETAKETHEPRESSUREANDWETHROWAWAYCONVENTIONALITYBELONGSTOYESTERDAYTHEREISACHANCETHATWECANMAKEITSOFARWESTARTBELIEVINGNOWTHATWECANBEWOWEAREGREASEISTHEWORDGREASEISTHEWORDISTHEWORDTHATYOUHEARDITSGOTGROOVEITSGOTMEANINGGREASEISTHETIMEISTHEPLACEISTHEMOTIONGREASEISTHEWAYWEAREFEELINGTHISISTHELIFEOFILLUSIONWRAPPEDUPINTROUBLELACEDWITHCONFUSIONWHATWEDOINGHEREWETAKETHEPRESSUREANDWETHROWAWAYCONVENTIONALITYBELONGSTOYESTERDAYTHEREISACHANCETHATWECANMAKEITSOFARWESTARTBELIEVINGNOWTHATWECANBEWHOWEAREGREASEISTHEWORDGREASEISTHEWORDISTHEWORDTHATYOUHEARDITSGOTGROOVEITSGOTMEANINGGREASEISTHETIMEISTHEPLACEISTHEMOTIONGREASEISTHEWAYWEAREFEELINGGREASEISTHEWORDISTHEWORDTHATYOUHEARDITSGOTGROOVEITSGOTMEANINGGREASEISTHETIMEISTHEPLACEISTHEMOTIONGREASEISTHEWAYWEAREFEELING"""
#ciphertext = "XTEZPTPRPBFGTBOJPKYEAAZPXOBFTYAPWMERMMSDBFJGQUGBAMHNWSEKTSPVIVFAXFJ"

#chaff=''
#for i in range(len(key)-len(ciphertext)):
#  chaff+= otp_decrypt(ciphertext,key[i:], lookupa0, lookup0a)+'\n'

#write each decryption attempt to a line & output to a file for easy viewing/searching/grepping
#ofp = open('out.txt','w')   
#ofp.write(chaff)


def caeser_brute(text):
  'this function rot1-rot25s the input text (& converts to uppercase)'
  for r in range(27):
    print "\n %s - " % r,
    for i in text.upper(): print chr((((ord(i)-65+r)%26)+65)),