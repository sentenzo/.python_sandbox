macro_rules! read_line {
    () => {
      {
        let mut line = String::new();
        std::io::stdin().read_line(&mut line).expect("Failed to read from stdin");
        line.trim().to_string()
      }
    };
  }

macro_rules! echo {
    () => { println!("{}", read_line!()) }
}
  
  fn main() {
    echo!(); 
    echo!(); 
    echo!();
    