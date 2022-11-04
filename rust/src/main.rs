use imagesize::blob_size;

fn main() {
    println!("Hello, world!");
    let data: Vec<u8> = magic_partial_download("http://example.com/example.jpg", 0x200);
    let (width, height) = match blob_size(&data) {
    Ok(dim) => (dim.width, dim.height),
    Err(why) => println!("Error getting dimensions: {:?}", why)
}
}
