// extern crate 11_crates.rs; // May be required for Rust 2015 edition or earlier

fn main() {
    rary::public_function();

    // Error! `private_function` is private
    //rary::private_function();

    rary::indirect_access();
}

// Where library.rlib is the path to the compiled library, assumed that it's
// in the same directory here:
//$ rustc 11_cratesb.rs --extern rary=lib11_crates.rlib --edition=2018 && ./executable 
//called rary's `public_function()`
//called rary's `indirect_access()`, that
//> called rary's `private_function()`