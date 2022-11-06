use imagesize::*;

fn main() {
    println!("Hello, world!");
    match size("/Users/marcalph/Projects/learning/random.png") {
        Ok(dim) => {
            // assert_eq!(dim.width, 716);
            // assert_eq!(dim.height, 716);
            println!("{dim:?}");
        }
        Err(why) => println!("Error getting size: {:?}", why)
    }

    // First few bytes of arbitrary data.
    let data = vec![0x89, 0x89, 0x89, 0x89, 0x0D, 0x0A, 0x1A, 0x0A,
                    0x00, 0x00, 0x00, 0x0D, 0x49, 0x48, 0x44, 0x52,
                    0x00, 0x00, 0x00, 0x7B, 0x01, 0x00, 0x01, 0x41,
                    0x08, 0x06, 0x00, 0x00, 0x00, 0x9A, 0x38, 0xC4];

    assert_eq!(blob_size(&data).is_err(), true);
    
}
