fn main() {
    println!("Hello whole world");
    let name: &str = "Marc";
    println!("My name is {}", name);
    let apples = 10 + 3;
    println!("I have {}", apples);
    // let error = "fds" + "e";
    let x = 5 + 3;
    let x = x * 2;
    let x = x - 6;
    let x: i32 = x / 2;
    println!("The answer is {}", x); // but x gets recreated each time >> shadowing
}
