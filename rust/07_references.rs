fn main() {
    let x: i32 = 5;
    println!("x == {}, located at {:p}", x, &x);
}




// An immutable variable holding a value directly, e.g., let fruit: Fruit = Fruit { …​ };
// A mutable variable holding a value directly, e.g., let mut fruit: Fruit = Fruit { …​ };
// An immutable variable holding an immutable reference, e.g., let fruit_ref: &Fruit = &fruit;
// An immutable variable holding a mutable reference, e.g., let fruit_ref: &mut Fruit = &mut fruit;

// The other two possibilities, which we almost never want, are:

// A mutable variable holding an immutable reference, e.g., let mut fruit_ref: &Fruit = &fruit;
// A mutable variable holding a mutable reference, e.g., let mut fruit_ref: &mut Fruit = &mut fruit;





// You are allowed to borrow references to values
// Borrowing a reference does not move ownership
// Borrowing is the preferred way to solve the “move in move out” problem we encountered previously
// References have their own type, and i32 is different than &i32
// We also have mutable references such as &mut i32, which allow the values behind the reference to be changed
// Mutable references can only be borrowed from mutable values
// References are, essentially, addresses for where the original value lives in memory
// If you want to operate directly on the value behind a reference, you can dereference using the * operator
// A reference cannot outlive the value it refers to
// To avoid confusion around mutation and references, Rust has some rules you need to abide by
//     You cannot mutate a value if there is a reference to it
//     You can have multiple immutable references to a value
//     You can only have one mutable reference to a value, and then no other immutable references to it, or access the value directly
// You can create an immutable reference from a mutable reference, but not the other way around.

