macro_rules! read_line {
    () => {{
        let mut line = String::new();
        std::io::stdin()
            .read_line(&mut line)
            .expect("Failed to read from stdin");
        line.trim().to_string()
    }};
}

macro_rules! echo {
    () => {
        println!("{}", read_line!())
    };
}

fn main() {
    let v = vec![1, 2, 3, 4, 5];

    let third: &i32 = &v[2];
    println!("The third element is {third}");

    let third: Option<&i32> = v.get(2);
    match third {
        Some(third) => println!("The third element is {third}"),
        None => println!("There is no third element."),
    }

    let thd = v[2];
    println!("The third element is {thd} {{");
}
