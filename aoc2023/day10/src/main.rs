// THIS IS NOT OPTIMAL CODE, IT IS MY FIRST RUST CODE

use std::fmt;
use std::{fs::File, io::Read, vec};

fn main() -> std::io::Result<()> {

    let mut file = File::open("input.txt")?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;

    let mut map: Vec<Pipe> = vec![];
    
    let mut start_id = 0;
    let mut line_len = 0;
    for (id_x, line) in contents.lines().enumerate() {   
        for (id_y, c) in line.chars().enumerate() {
            map.push(char_to_pipe(&c));
            if c == 'S' { start_id = id_x * line.len() + id_y; line_len = line.len();}
         }
    }

    calc_start(start_id, &mut map, line_len);
    //println!("{:?} s_id:{:?}", map, map[start_id]);

    let path = get_path(start_id, &mut map, line_len);
    println!("p1 result is {}", path.len()/2);

    for (idx, p) in map.iter_mut().enumerate() {
        if !path.contains(&idx) {
            p.n = false;
            p.s = false;
            p.w = false;
            p.e = false;
        }
    }
    /*
    for (idx, p) in map.iter().enumerate() {
        if idx % line_len == 0 {
            println!();
        }
        print!("{}", p);
    }
    */

    let mut count = 0;
    let mut in_loop = false;
    let mut up_vertical = false;
    let mut down_vertical = false;
    for (idx, p) in map.iter().enumerate() {
        
        if idx % line_len == 0 {
            in_loop = false;
        }
        
        if is_vertical(p) {
            in_loop = !in_loop;
        } else if is_up_vertical(p) {
            if up_vertical {
                up_vertical = false;
            } else if down_vertical {
                in_loop = !in_loop;
                down_vertical = false;
            } else {
                up_vertical = true;
            }
        } else if is_down_vertical(p) {
            if down_vertical {
                down_vertical = false;
            } else if up_vertical {
                up_vertical = false;
                in_loop = !in_loop;
            } else {
                down_vertical = true;
            }
        }
        
        if in_loop & is_ground(p) {
            //println!("line: {} {} {}", idx / line_len, idx % line_len, p);
            count += 1;
        }
        
    }

    println!("p2 result is {}", count);

    Ok(())
}

#[derive(Debug)]
#[allow(dead_code)]
struct Pipe {
    n: bool,
    s: bool,
    w: bool,
    e: bool,
}

impl fmt::Display for Pipe {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let mut c = '.';
        match self {
            Pipe {n: false, s: false, w: false, e: false} => {c = '.'},
            Pipe {n: false, s: true, w: false, e: true} => {c = 'F'} ,
            Pipe {n: false, s: true, w: true, e: false} => {c = '7'},
            Pipe {n: true, s: false, w: true, e: false} => {c = 'J'},
            Pipe {n: true, s: true, w: false, e: false} => {c = '|'},
            Pipe {n: false, s: false, w: true, e: true} => {c = '-'},
            Pipe {n: true, s: false, w: false, e: true} => {c = 'L'},
            _ => {},
        }
        write!(f, "{}", c)
    }
}

fn is_ground(p: &Pipe) -> bool {
    !(p.e | p.w | p.s | p.n)
}

fn is_vertical(p: &Pipe) -> bool {
    p.n & p.s
}

fn is_up_vertical(p: &Pipe) -> bool {
    p.n & !p.s
}

fn is_down_vertical(p: &Pipe) -> bool {
    p.s & !p.n
}

fn char_to_pipe(c: &char) -> Pipe {
    match c {
        '.' => Pipe {n: false, s: false, w: false, e: false},
        'F' => Pipe {n: false, s: true, w: false, e: true},
        '7' => Pipe {n: false, s: true, w: true, e: false},
        'J' => Pipe {n: true, s: false, w: true, e: false},
        '|' => Pipe {n: true, s: true, w: false, e: false},
        '-' => Pipe {n: false, s: false, w: true, e: true},
        'L' => Pipe {n: true, s: false, w: false, e: true},
        'S' => Pipe {n: false, s: false, w: false, e: false},
        _ => Pipe { n: true, s: true, w: true, e: true },
    }
}

fn calc_start(id: usize, v: &mut Vec<Pipe>, n: usize) {



    let id_up = id - n;
    let id_down = id + n;
    let id_right = id + 1;
    let id_left = id - 1; 

    let mut new_pipe = Pipe {n: false, s: false, w: false, e: false};

    match v[id_up] {
        Pipe {s: true, ..} => {new_pipe.n = true},
        _ => (),
    }
    match v[id_down] {
        Pipe {n: true, ..} => {new_pipe.s = true},
        _ => (),
    }
    match v[id_left] {
        Pipe {e: true, ..} => {new_pipe.w = true},
        _ => (),
    }
    match v[id_right] {
        Pipe {w: true, ..} => {new_pipe.e = true},
        _ => (),
    }

    v[id] = new_pipe;
}

fn get_path(sid: usize, v: &mut Vec<Pipe>, n: usize) -> Vec<usize> {
    let mut prev = sid as i32;
    let mut curr = sid as i32;
    let mut path: Vec<usize> = vec![prev as usize];

    match v[sid] {
        Pipe {n: true, ..} => {curr = curr - n as i32},
        Pipe {s: true, ..} => {curr = curr + n as i32},
        Pipe {w: true, ..} => {curr = curr - 1},
        Pipe {e: true, ..} => {curr = curr + 1},
        _ => unreachable!()
    }

    while sid != curr as usize {
        let diff = curr - prev;
        match diff {
            1 => {if v[curr as usize].n {
                prev = curr;
                curr = curr - n as i32; 
            } else if v[curr as usize].s {
                prev = curr;
                curr = curr + n as i32;
            } else {
                prev = curr;
                curr = curr + 1;
            }},
            -1 => {if v[curr as usize].n {
                prev = curr;
                curr = curr - n as i32; 
            } else if v[curr as usize].s {
                prev = curr;
                curr = curr + n as i32;
            } else {
                prev = curr;
                curr = curr - 1;
            }},
            _n => {
                if v[curr as usize].w {
                    prev = curr;
                    curr = curr - 1; 
                } else if v[curr as usize].e {
                    prev = curr;
                    curr = curr + 1;
                } else {
                    prev = curr;
                    curr = curr + _n;
                }
     
            },
        }

        path.push(prev as usize);
    }

    path
}