fn main() {
    struct TupleStruct(i32, i32);
    struct NormalStruct {
        a: i32,
        b: i32,
    }

    // we can construct instances of structs and tuple structs as follows

    let ts = TupleStruct(1, 2);
    let ns = NormalStruct { a: 1, b: 2 };

    // shortcut to initialize the fields of a struct using the values of the
    // fields of another struct
    let ns2 = NormalStruct { a: 5, ..ns };
    let ts2 = TupleStruct { 0: 1, ..ts }; // for TupleStruct it needs curly brackets
                                      // and implicit field names

    // destructuring
    let TupleStruct(x, y) = ts;
    println!("x: {}, y: {}", x, y);
    let NormalStruct { a, b } = ns;
    println!("a: {}, b: {}", a, b);


    // A tuple struct's fields have implicit names (0, 1, ...). Hence, accessing fields is performed as follows

    println!("Accessing ns by name - {}{}", ns.a, ns.b);
    println!("accessing ts by name - {}{}", ts.0, ts.1);

    // At least for documentation purposes, it's almost always clearer to assign explicit names to the fields of the struct. That's why in the Rust community I've seen many argue for always using a normal struct.
    // However, there might be cases where the fields of the struct are inherently "anonymous", one notable case being the "newtype" (tuple struct with one field) where you're only wrapping an inner type.
    // In that case, naming the inner field does not arguably provide any additional information.

    struct Inches {
        inner: i32,
    }

    // vs

    struct Inches(i32);
}
