fn main() {
    let result: bool = 2 + 3 != 5;
    println!("{}", result);
    assert!(4 + 7 == 11);
    println!("If we got here, I guess it worked!");
    assert_ne!(1,2);
    assert!(gets_discount(1));
}


fn gets_discount(age: u32) -> bool {
    age < 18 || age >= 65
}