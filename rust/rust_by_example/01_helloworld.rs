fn main() {
    // Statements here are executed when the compiled binary is called

    // Print text to the console
    println!("Hello World!");
    act();
    let num = Complex{
        real: 3.3,
        imag: 7.2
    };
    display_complex(num);
    display_list();
    display_color();
}

// print something
fn act() {
    println!("I'm a Rustacean!")
}

// impl trait Display for struct
use std::fmt::{self, Display};
#[derive(Debug)]
struct Complex {
    real: f64,
    imag: f64,
}
impl Display for Complex {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let r = self.real;
        let i = self.imag;
        write!(f, "{r} + {i}i")
    }
}
fn display_complex(num: Complex) {
    println!("{}",num);
    println!("{:?}",num); 
}
// display for seq type
// Define a structure named `List` containing a `Vec`.
struct List(Vec<i32>);
impl fmt::Display for List {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Extract the value using tuple indexing,
        // and create a reference to `vec`.
        let vec = &self.0;
        write!(f, "[")?;
        // Iterate over `v` in `vec` while enumerating the iteration
        // count in `count`.
        for (count, v) in vec.iter().enumerate() {
            // For every element except the first, add a comma.
            // Use the ? operator to return on errors.
            if count != 0 { write!(f, ", ")?; }
            write!(f, "{count}: {v}", )?;
        }
        // Close the opened bracket and return a fmt::Result value.
        write!(f, "]")
    }
}
fn display_list() {
    let v:List = List(vec![1,2,3]);
    println!("{}",v);
}

// display for color
struct Color {
    red: u8,
    green: u8,
    blue: u8,
}
impl Display for Color {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "RGB ({}, {}, {}) {:X}", self.red, self.green, self.blue, self)
    }
}
impl fmt::UpperHex for Color {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "0x{:0>2X}{:0>2X}{:0>2X}",  self.red, self.green, self.blue)
    } 
}
fn display_color(){
    for color in [
        Color { red: 128, green: 255, blue: 90 },
        Color { red: 0, green: 3, blue: 254 },
        Color { red: 0, green: 0, blue: 0 },
    ].iter() {
        // Switch this to use {} once you've added an implementation
        // for fmt::Display.
        println!("{}", *color);
    }
}
