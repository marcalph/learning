fn main() {              // Program entry point
    let mut x: i32 = 6;  // Mutable variable binding
    print!("{x} {x} ");       // Macro for printing, like printf
    while x != 1 {       // No parenthesis around expression
        if x % 2 == 0 {  // Math like in other languages
            x = x / 2;
        } else {
            x = 3 * x + 1;
        }
        print!(" -> {x}");
    }
    println!();
}


// Be sure to note the difference between let mut ref_x: &i32 and let ref_x: &mut i32. 
// The first one represents a mutable reference which can be bound to different values, 
// while the second represents a reference to a mutable value.



// In summary, const values are compile-time constants that are always inlined,
// while static variables have a fixed memory location and can be mutable. const values are evaluated at compile-time,
// whereas static variables are lazily initialized at runtime.



// shadowing let us hold onto valeus after unwrap
// fn main() {
//     let a = 1;
//     let b = &a;
//     let a = a + 1;
//     println!("{a} {b}");
// }



// &str an immutable reference to a string slice.
// String a mutable string buffer.
