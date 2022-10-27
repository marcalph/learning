fn main() {
    // inline comment
    /*
    multi
    pass/line
    comment
    */
    let _x: () = (); // unit type close to python None
    let _y: () = println!("something"); 
    assert_eq!(2, 2);
    let z = {5;};  // in blocks i.e. {} if you add ; value of statement is disgarded
    assert_eq!((), z)
}