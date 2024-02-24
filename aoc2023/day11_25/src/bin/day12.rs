use std::{collections::HashMap, fs::read_to_string, iter::zip, vec};

fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename)
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}

fn main() {
    let lines = read_lines("./inputs/12.in");

    let mut targets: Vec<Vec<char>> = vec![];
    let mut labels: Vec<Vec<u32>> = vec![];

    for line in lines {
        let sline: Vec<&str> = line.split_whitespace().collect();

        targets.push(parse_target(sline[0]));
        labels.push(parse_labels(sline[1]))
    }
    
    let mut p1_sum = 0;
    for (_ ,(target, label)) in zip(targets.clone(), labels.clone()).enumerate() {
        let mut hmap = HashMap::new();
        let score = count_valid(&target, &label, 0, 0, 0, &mut hmap);
        p1_sum += score;
    }
    println!("P1: {}", p1_sum);
    
    let mut p2_sum = 0;
    for (target, label) in zip(targets, labels) {
        let (unfold_t, unfold_l) = unfold(target, label);
        let mut hmap = HashMap::new();
        let score = count_valid(&unfold_t, &unfold_l, 0, 0, 0, &mut hmap);
        p2_sum += score;
    }
    println!("P2: {}", p2_sum);

}

fn parse_target(s: &str) -> Vec<char> {
    s.bytes()
     .map(|x| x as char)
     .collect()
}

fn parse_labels(s: &str) -> Vec<u32> {
    s.split(',')
     .map(|x| x.parse::<u32>().unwrap())
     .collect()
}

fn count_valid(target: &Vec<char>, label: &Vec<u32>, i: usize, bi: usize, current: u32, hmap: &mut HashMap<(usize, usize, u32), u64>) -> u64 {
    let key = (i, bi, current);
    if let Some(&val) = hmap.get(&key) { return val; }
    if target.len() == i {
        if bi == label.len() && current == 0 {
            return 1;
        } else if bi == label.len() - 1 && current == label[bi] {
            return 1;
        } else {
            return 0;
        }
    }
    let mut sum: u64 = 0;

    for c in vec!['.', '#'] {
        match target[i] == c || target[i] == '?' {
            true => {
                if c == '.' && current == 0 {
                    sum += count_valid(&target, label, i+1, bi, 0, hmap);
                } else if c == '.' && current > 0 && bi<label.len() && label[bi]==current{
                    sum += count_valid(&target, label, i+1, bi+1, 0, hmap);
                } else if c == '#' {
                    let saved = count_valid(&target, label, i+1, bi, current+1, hmap);
                    sum += saved;
                }
            },
            _ => {}
        }
    }
    hmap.insert((i, bi, current), sum);
    return sum;
}

fn _check_valid(target: &Vec<char>, label: &Vec<i32>) -> bool {
    let mut check_label: Vec<i32> = vec![];
    let mut counter = 0;
    for c in target.iter() {
        match c {
            '#' => counter += 1,
            '.' => {
                if counter != 0 {
                    check_label.push(counter);
                    counter = 0;
                }
            },
            _ => return false,
        }
    }
    if counter != 0 {check_label.push(counter)};
    &check_label == label
}

fn unfold(t: Vec<char>, l: Vec<u32>) -> (Vec<char>, Vec<u32>){
    let mut tt = t.clone();
    let mut ll = l.clone();

    for _ in 0..4 {
        tt.push('?');
        tt.extend(t.clone());
        ll.extend(l.clone());
    }

    (tt, ll)
}