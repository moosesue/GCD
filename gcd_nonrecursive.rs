fn gcd(mut a: u32, mut b: u32) -> u32 {
 while a != 0 {
    let temp = a;
    a = b % a;
    b = temp;
  }
 b
}