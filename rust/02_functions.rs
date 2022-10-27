fn say_hello (name: &str) -> &str {
    println!("Hello world.");
    println!("Damn {}!", name);
    let x = 10;
    println!("{}", x);
    {
        let x = 15;
        println!("{}", x);
    }
    println!("{}", x);
    "return value"
}

fn say_goodbye() {
    println!("Farewell, friend.");
}

fn main () {
    println!("{}", say_hello("Daniel"));
    say_goodbye();
    say_goodbye();
}

