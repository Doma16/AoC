use std::{collections::HashSet, fs::read_to_string};

fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename)
        .unwrap()
        .trim()
        .split("\n\n")
        .map(String::from)
        .collect()
}
fn main() {
    let note = read_lines("./inputs/13.in");

    let mut notes: Vec<Vec<String>> = vec![];
    for n in note {
        let tmp: Vec<String> = n
        .split('\n')
        .map(String::from)
        .collect();
        notes.push(tmp);
    }

    let mut p1: Vec<usize> = vec![]; 
    let mut p2: Vec<usize> = vec![];
    for (_idx, note) in notes.iter_mut().enumerate() {
        let n_s = note[0].len();
        let mut test: HashSet<usize> = get_sym(&note[0]);
        let mut test2: HashSet<usize> = HashSet::new();

        for row in note.iter().skip(1) {
            let tmp = get_sym(row);
            let c: HashSet<usize> = test.intersection(&tmp).cloned().collect();
            test = c;
            if test.len() == 0 {
                break;
            }
        }
        if test.len() == 0 {
            // do horizontal test
            let mut first = true;
            for i in 0..n_s {
                let mut hor = String::new();
                for n in note.iter() {
                    let x = n.chars().collect::<Vec<char>>();
                    hor.push(x[i]);
                }

                if first {
                    test2 = get_sym(&hor);
                    first = false;
                }

                let tmp = get_sym(&hor);
                let c: HashSet<usize> = test2.intersection(&tmp).cloned().collect();
                test2 = c;
                if test2.len() == 0 {
                    break;
                }
            }

            if test2.len() != 0 {
                p1.push(100 * test2.iter().next().unwrap().clone());
            }
        } else {
            p1.push(test.iter().next().unwrap().clone());
        }

        if test.len() == 1 {
            let id = test.iter().next().unwrap().clone();
            //let min_d = (n_s-id).min(id);

            let tmp: HashSet<usize>;
            let tmp2: HashSet<usize>;

            if id > n_s / 2 {
                //let x = n_s - 2 * min_d;
                (tmp, tmp2) = calc_sym(note, 0, n_s, 0, note.len());
            } else {
                //let x = 2 * min_d;
                (tmp, tmp2) = calc_sym(note, 0, n_s, 0, note.len());
            }

            if tmp2.len() > 0 {
                p2.push(100 * tmp2.iter().next().unwrap().clone());
            } else {
                if tmp.len() == 1 {
                    p2.push(tmp.iter().next().unwrap().clone());
                } else {
                    for el in tmp {
                        if el != id {p2.push(el)}
                    }
                }
            }
            
        } else if test2.len() == 1 {
            let &id = test2.iter().next().unwrap();
            //let min_id = (note.len() - id).min(id);
            
            let tmp: HashSet<usize>;
            let tmp2: HashSet<usize>;
            
            if id > note.len() / 2 {
                //let y = note.len() - 2 * min_id;
                (tmp, tmp2) = calc_sym(note, 0, n_s, 0, note.len());
            } else {
                //let y = 2 * min_id;
                (tmp, tmp2) = calc_sym(note, 0, n_s, 0, note.len());
            }

            if tmp.len() == 1 {
                p2.push(tmp.iter().next().unwrap().clone());
            } else {
                if tmp2.len() == 1 {
                    p2.push(100 * tmp2.iter().next().unwrap().clone());
                } else {
                    for el in tmp2 {
                        if el != id { p2.push(100 * el); }
                    }
                }
            }

        } else {
            unreachable!();
        }
    }

    // println!("{:?}", p1);
    // println!("{:?}", p2);
    println!("P1: {}", p1.iter().map(|&x| x as u128).sum::<u128>());
    println!("P2: {}", p2.iter().map(|&x| x as u128).sum::<u128>());

}

fn calc_sym(s: &mut Vec<String>, x1: usize, x2: usize, y1: usize, y2: usize) -> (HashSet<usize>, HashSet<usize>) {
    assert!( x2 > x1 );
    assert!( y2 > y1 );

    let mut t1: HashSet<usize> = HashSet::new();
    let mut t2: HashSet<usize> = HashSet::new();

    'outer: for idy in y1..y2 {
        for idx in x1..x2 {
            match s[idy].get(idx..idx+1) {
                Some("#") => {s[idy].replace_range(idx..idx+1, ".");},
                Some(".") => {s[idy].replace_range(idx..idx+1, "#");},
                _ => {unreachable!();},
            }

            let n_s = s[0].len();
            let mut test: HashSet<usize> = get_sym(&s[0]);
            let mut test2: HashSet<usize> = HashSet::new();

            for row in s.iter().skip(1) {
                let tmp = get_sym(row);
                let c: HashSet<usize> = test.intersection(&tmp).cloned().collect();
                test = c;
                if test.len() == 0 {
                    break;
                }
            }
            if test.len() == 1 || test.len() == 0 {
                // do horizontal test
                let mut first = true;
                for i in 0..n_s {
                    let mut hor = String::new();
                    for n in s.iter() {
                        let x = n.chars().collect::<Vec<char>>();
                        hor.push(x[i]);
                    }
                    
                    if first {
                        test2 = get_sym(&hor);
                        first = false;
                    }
                    
                    let tmp = get_sym(&hor);
                    let c: HashSet<usize> = test2.intersection(&tmp).cloned().collect();
                    test2 = c;
                    if test2.len() == 0 {
                        break;
                    }
                }
                
                if test2.len() != 0 {
                    //p1.push(100 * test2.iter().next().unwrap().clone());
                }
            } else {
                //p1.push(test.iter().next().unwrap().clone());
            }
            
            t1 = t1.union(&test).cloned().collect();
            t2 = t2.union(&test2).cloned().collect();
            if test.len() + test2.len() > 1 {break 'outer;}
            
            match s[idy].get(idx..idx+1) {
                Some("#") => {s[idy].replace_range(idx..idx+1, ".");},
                Some(".") => {s[idy].replace_range(idx..idx+1, "#");},
                _ => {unreachable!();},
            }
        }
    }
    (t1, t2)
}

fn get_sym(s: &String) -> HashSet<usize> {
    let mut syms = HashSet::new();
    let n = s.len();
 
    for id in 0..n-1 {
        let s1 = String::from(&s[..id+1]).chars().rev().collect::<String>();
        let s2 = String::from(&s[id+1..]);

        let min = s1.len().min(s2.len());

        if &s1[..min] == &s2[..min] {
            syms.insert(id+1);
        }
    }
    syms
}