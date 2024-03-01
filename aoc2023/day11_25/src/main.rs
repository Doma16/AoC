fn main() {
    let mut s = String::from("Aello, World!");
    s.replace_range(0..1, "H");
    println!("{s}");
}
