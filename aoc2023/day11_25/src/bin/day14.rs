use std::{fs::read_to_string, ops::Index};

fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename)
    .unwrap()
    .trim()
    .split("\n")
    .map(String::from)
    .collect()
}

#[derive(Debug)]
struct Point(usize, usize);

fn main() {

    let map = read_lines("./inputs/14.in");
    
    let mut balls: Vec<Point> = vec![];
    let mut rocks: Vec<Point> = vec![];

    for (idy, row) in map.iter().enumerate() {
        for (idx, b) in row.chars().enumerate() {
            match b {
                '#' => {rocks.push(Point(idx,idy));},
                'O' => {balls.push(Point(idx,idy));},
                _ => {},
            }
            
        }
    }    

    println!("{:?}", balls);
    println!("{:?}", rocks);

}