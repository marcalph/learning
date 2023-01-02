fn main() {
    // Allocate an integer on the heap
    let _box2 = Box::new(5i32);
    // A nested scope:
    {
        // Allocate an integer on the heap
        let _box3 = Box::new(4i32);
        // `_box3` is destroyed here, and memory gets freed
    }
    // Creating lots of boxes just for fun
    // There's no need to manually free memory!
    for _ in 0u32..1_000 {
        raii();
    }
    // `_box2` is destroyed here, and memory gets freed
    let _x = ToDrop;
    println!("Made a ToDrop!");

    // Create an immutable Book named `immutabook`
    let immutabook = Book {
        // string literals have type `&'static str`
        author: "Douglas Hofstadter",
        title: "Gödel, Escher, Bach",
        year: 1979,
    };
    let mut mutabook = immutabook;
    borrow_book(&immutabook);
    borrow_book(&mutabook);
    new_edition(&mut mutabook);
}

fn raii() {
    // Allocate an integer on the heap
    let _box1 = Box::new(3i32);
    // `_box1` is destroyed here, and memory gets freed
}
struct ToDrop;

impl Drop for ToDrop {
    fn drop(&mut self) {
        println!("ToDrop is being dropped");
    }
}

#[derive(Clone, Copy)]
struct Book {
    // `&'static str` is a reference to a string allocated in read only memory
    author: &'static str,
    title: &'static str,
    year: u32,
}

// This function takes a reference to a book
fn borrow_book(book: &Book) {
    println!("I immutably borrowed {} - {} edition", book.title, book.year);
}

// This function takes a reference to a mutable book and changes `year` to 2014
fn new_edition(book: &mut Book) {
    book.year = 2014;
    println!("I mutably borrowed {} - {} edition", book.title, book.year);
}

