def gcd(a: int, b: int)->int:
  #check if either of the numbers passed in is zero
  if (a !=0) and (b!=0) :
    #check if a is bigger than b
    if a > b:
       #if it is then set new_number_a to be the remainder of a #divided by b and set new_number_b to be b.
       new_number_a = a%b
       new_number_b = b
    else:
        #if it isn’t then set new_number_a to be the remainder of b #divided by a and set new_number_b to be a.
        if a < b:
           new_number_a = b%a
           new_number_b = a
  #check if new_number_a is the same as new_number_b and that
  #new_number_b is not zero. If so, call the function again 
  #with the new numbers.
  if (new_number_a != new_number_b) and (new_number_b!=0):
     return gcd(new_number_a, new_number_b)
  else:
     #if not then we must be finished and so the result is 
     #new_number_a
     return new_number_a