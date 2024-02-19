#[derive(Debug, Clone)]
struct Point(usize, usize);

fn main() {

    let input = include_str!("../../inputs/11.in");
    let lines = input.lines()
                     .map(|l| l.as_bytes()).collect::<Vec<_>>();
    
    let mut pts: Vec<Point> = vec![];
    for (idy, &line) in lines.iter().enumerate() {
        for (idx, &c) in line.iter().enumerate() {
            if c == b'#' {
                pts.push(Point(idx, idy));
            }
        }
    }

    let mut xs: Vec<_> = pts.iter().map(|p| p.0).collect();
    xs.sort();
    let &minx = xs.first().unwrap();
    let &maxx = xs.last().unwrap();

    let mut not_x: Vec<usize> = vec![];
    for i in minx..=maxx {
        if !xs.contains(&i) {
            not_x.push(i);
        }
    }
    
    let mut ys: Vec<_> = pts.iter().map(|p| p.1).collect();
    ys.sort();
    let &miny = ys.first().unwrap();
    let &maxy = ys.last().unwrap();

    let mut not_y: Vec<usize> = vec![];
    for i in miny..=maxy {
        if !ys.contains(&i) {
            not_y.push(i);
        }
    }

    let mut pts_p2 = pts.clone();
    
    for pt in pts.iter_mut() {
        pt.0 = pt.0 + count_larger(pt.0, &not_x);
        pt.1 = pt.1 + count_larger(pt.1, &not_y);
    }

    let mut ds: Vec<i32> = vec![];
    let n = pts.len();
    for i in 0..n {
        for j in i..n {
            let diff_x = pts[i].0 as i32 - pts[j].0 as i32;
            let diff_y = pts[i].1 as i32 - pts[j].1 as i32;
            ds.push(diff_x.abs() + diff_y.abs())
        }
    }

    println!("P1: {}", ds.iter().sum::<i32>());

    let times = 1_000_000;
    for pt in pts_p2.iter_mut() {
        pt.0 = pt.0 + count_larger(pt.0, &not_x) * (times-1);
        pt.1 = pt.1 + count_larger(pt.1, &not_y) * (times-1);
    }

    let mut ds: Vec<i128> = vec![];
    for i in 0..n {
        for j in i..n {
            let diff_x = pts_p2[i].0 as i128 - pts_p2[j].0 as i128;
            let diff_y = pts_p2[i].1 as i128 - pts_p2[j].1 as i128;
            ds.push(diff_x.abs() + diff_y.abs())
        }
    }

    //println!("{:?}", ds);
    println!("P2: {}", ds.iter().map(|&x| x as i128).sum::<i128>());

}

fn count_larger(val: usize, v: &Vec<usize>) -> usize {
    v.iter()
     .filter(|&&e| e < val)
     .map(|_| 1)
     .sum()
}