
s1 = 'hi'
s2 = 'ha'
def interleave(s1,s2):
   return ( ''.join( ''.join(pair) for pair in ( zip( (c1 for c1 in s1), (c2 for c2 in s2))) ) )
   

print( interleave(s1, s2) ) 