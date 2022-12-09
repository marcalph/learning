#![crate_type = "bin"] // crate level attribute #! (but only useful with rustc and not cargo)

fn main() {
    // `#[allow(dead_code)]` is an attribute that disables the `dead_code` lint
    used_function();
    // cfg attribut for condition compilation cfg! macro for conditionnal runs
    cfg_attribute_and_cfg_macro(); 
    //$ rustc --cfg flag needed to allow compilation of conditional_function
    conditional_function();
}



fn used_function() {}

#[allow(dead_code)]
fn unused_function() {}

#[allow(dead_code)]
fn noisy_unused_function() {}

#[cfg(target_os = "linux")]
fn are_you_on_linux() {
    println!("You are running linux!");
}

// And this function only gets compiled if the target OS is *not* linux
#[cfg(not(target_os = "linux"))]
fn are_you_on_linux() {
    println!("You are *not* compiling on linux!");
}

fn cfg_attribute_and_cfg_macro() {
    are_you_on_linux();

    println!("Are you sure?");
    if cfg!(target_os = "linux") {
        println!("Yes. It's definitely linux!");
    } else {
        println!("Yes. It's definitely *not* running on linux!");
    }
}



#[cfg(some_condition)]
fn conditional_function() {
    println!("condition met!");
}
