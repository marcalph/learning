fn main() {
    let mut i = 0;

    while i < 10 {
        println!("Hello, world!");
        i += 1;
    }

    shadow_and_mutate()
}


fn shadow_and_mutate() {
    let x = 5;
    {
        let mut x = 6;
        assert_eq!(x, 6);
        x += 1;
        assert_eq!(x, 7);
        x = 8;
        assert_eq!(x, 8);
    }
    assert_eq!(x, 5);
}