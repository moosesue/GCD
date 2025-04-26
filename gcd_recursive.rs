fn gcd(a: u32, b: u32) -> u32 {
  if a == 0 {
     b
 }
  else {
     gcd(b % a, a)
     }
}