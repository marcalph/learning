fn main() {
    let _a_float: f64 = 1.0;  // Regular annotation
    let _an_integer   = 5i32; // Suffix annotation
    
        // Integer subtraction
    println!("1 - 2 = {}", 1i32 - 2);
    // TODO ^ Try changing `1i32` to `1u32` to see why the type is important

    // Short-circuiting boolean logic
    println!("true AND false is {}", true && false);
    println!("true OR false is {}", true || false);
    println!("NOT true is {}", !true);

    // Bitwise operations
    println!("0011 AND 0101 is {:04b}", 0b0011u32 & 0b0101);
    println!("0011 OR 0101 is {:04b}", 0b0011u32 | 0b0101);
    println!("0011 XOR 0101 is {:04b}", 0b0011u32 ^ 0b0101);
    println!("1 << 5 is {}", 1u32 << 5);
    println!("0x80 >> 2 is 0x{:x}", 0x80u32 >>2);

    // Use underscores to improve readability!
    println!("One million is written as {}", 1_000_000u32);
    let a = reverse((1, true));
    println!("{a:?}");

    let tuple_of_tuples = ((1u8, 2u16, 2u32), (4u64, -1i8), -2i16);

    // Tuples are printable
    println!("tuple of tuples: {:?}", tuple_of_tuples);
    // But long Tuples (more than 12 elements) cannot be printed
    // let too_long_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13);
    // println!("too long tuple: {:?}", too_long_tuple);
    // TODO ^ Uncomment the above 2 lines to see the compiler error
    println!("one element tuple: {:?}", (5u32,));
    println!("just an integer: {:?}", (5u32));
    let tuple = (1, "hello", 4.5, true);
    let (a, b, c, d) = tuple;
    println!("{:?}, {:?}, {:?}, {:?}", a, b, c, d);

    display_matrix();
    array_n_slice()
}

fn reverse(pair: (i32, bool)) -> (bool, i32) {
    // `let` can be used to bind the members of a tuple to variables
    let (int_param, bool_param) = pair;
    (bool_param, int_param)
}
//display and trasnpose tuple matrix
use std::fmt::{self};
#[derive(Debug)]
struct Matrix ((f32, f32, f32, f32));
fn display_matrix() {
    let mat: Matrix = Matrix((1.1, 1.2, 2.1, 2.2));
    println!("{:?}",mat);
    println!("Matrix:\n{}", mat);
    println!("Transpose:\n{}", transpose(mat));
}
impl fmt::Display for Matrix{
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        writeln!(f, "( {} {} )", self.0.0, self.0.1)?;
        write!(f, "( {} {} )", self.0.2, self.0.3)

    }
}
fn transpose(mat: Matrix) -> Matrix{
    let (u, v, x, y) = mat.0;
    Matrix((u, x, v, y))
}
// arrays and slices
use std::mem;
fn array_n_slice() {
    // array (type signature is superfluous)
    let xs: [i32; 5] = [1, 2, 3, 4, 5];

    // All elements can be initialized to the same value
    let ys: [i32; 500] = [0; 500];

    // Indexing starts at 0
    println!("first element of the xs array: {}", xs[0]);
    println!("second element of the xs array: {}", xs[1]);
    println!("last element of the xs array: {}", xs[xs.len()-1]);
    println!("first element of the ys array: {}", ys[0]);
    println!("second element of the ys array: {}", ys[1]);
    println!("last element of the ys array: {}", ys[ys.len()-1]);
    
    // `len` returns the count of elements in the array
    println!("number of elements in xs array: {}", xs.len());

    // Arrays are stack allocated
    println!("xs array occupies {} bytes", mem::size_of_val(&xs));

    // Arrays can be automatically borrowed as slices
    println!("borrow the whole xs array as a slice");
    analyze_slice(&xs);

    // Slices can point to a section of an array
    // They are of the form [starting_index..ending_index]
    // starting_index is the first position in the slice
    // ending_index is one more than the last position in the slice
    println!("borrow a section of the ys array as a slice");
    analyze_slice(&ys[1 .. 10]);

    // Example of empty slice `&[]`
    let empty_array: [u32; 0] = [];
    assert_eq!(&empty_array, &[]);
    assert_eq!(&empty_array, &[][..]); // same but more verbose

    // Arrays can be safely accessed using `.get`, which returns an
    // `Option`. This can be matched as shown below, or used with
    // `.expect()` if you would like the program to exit with a nice
    // message instead of happily continue.
    for i in 0..xs.len() + 1 { // OOOPS, one element too far
        match xs.get(i) {
            Some(xval) => println!("xs.get() gives val {}@index {}", xval, i),
            None => println!("Slow down! {} is too far!", i),
        }
    }

    // Out of bound indexing causes compile error
    //println!("{}", xs[5]);
}
fn analyze_slice(slice: &[i32]) {
    println!("\\_> first element of the slice: {}", slice[0]);
    println!("\\_> the slice has {} elements", slice.len());
}