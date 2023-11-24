mod other_file_same_dir;
mod some_pack;

fn main() {
    println!("Below is a simple example of importing when is in the same file");
    println!("{}", other_file_same_dir::simple_sum(3, 4));

    println!("Below is a simple example from another package");
    some_pack::file_from_other_package::greeting();  // Direct call without println!
}
