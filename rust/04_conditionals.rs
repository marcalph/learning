fn main() {
    let is_hot = false; // semicolon needed to end let expr
    if is_hot {
        println!("It's hot!");
    } else {
        println!("It's not hot!");
    }
}

fn tell_temperature(temp: i32) {
    if temp <= 10 {
        println!("It's cold!");
    } else if temp <= 25 {
        println!("It's nice");
    } else if temp <= 30 {
        println!("It's warm");
    } else {
        println!("It's hot!")
    }
}
