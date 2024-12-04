use std::fs;

fn main() {
    let contents = fs::read_to_string("../input.txt").expect("");
    let split = contents.split("\n");
    let mut l1 = Vec::new();
    let mut l2 = Vec::new();
    let mut a = 0;
    for line in split {
        if line != "" {
            let num: Vec<i32> = line.split("   ").map(|x| x.parse::<i32>().unwrap()).collect();
            l1.push(num[0]);
            l2.push(num[1]);
        }
    }
    l1.sort();
    l2.sort();
    for i in 0..l1.len() {
        a += (l1[i]-l2[i]).abs();
    }
    println!("{a}");


    a = 0;
    for i in 0..l2.len() {
        if l1.contains(&l2[i]){
            a += l2[i]
        }
    }
    println!("{a}")
}
