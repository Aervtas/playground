fn main() {
    println!("Hello, world!");

    // (*mut) name    type    value
    let hello: Vec<i32> = (0..10).collect();

    // 
    fn test_fn(val: &Vec<i32>){
        println!("{}", val.len());
    }

    test_fn(&hello);
}
