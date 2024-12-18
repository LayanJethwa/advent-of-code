#![allow(unused)]
use std::*;
use ::num::pow;

fn main() {
    let mut ro: Vec<i64> = vec![52884621, 0, 0];
    let mut l: Vec<i64> = vec![2,4,1,3,7,5,4,7,0,3,1,5,5,5,3,0];

    let mut r = ro.clone();
    fn co(op: i64, r: &[i64]) -> i64 {
        if op <= 3 {
            return op;
        } else if op == 4 {
            return r[0];
        } else if op == 5 {
            return r[1];
        } else if op == 6 {
            return r[2];
        } else {
            return 0;
        }
    }

    let mut p = 0;
    let mut o = vec![];
    while p < l.len()-1 {
        let mut cp = false;
        let oc = l[p];
        let op = l[p+1];

        if oc == 0 {
            r[0] = r[0]/(pow(2,co(op.try_into().unwrap(),&r).try_into().unwrap()));
        } else if oc == 1 {
            r[1] = op ^ r[1];
        } else if oc == 2 {
            r[1] = co(op,&r)%8;
        } else if oc == 3 {
            if r[0] != 0 {
                p = op as usize;
                cp = true;
            }
        } else if oc == 4 {
            r[1] = r[1] ^ r[2]
        } else if oc == 5 {
            o.push(co(op,&r)%8);
        } else if oc == 6 {
            r[1] = r[0]/(pow(2,co(op,&r).try_into().unwrap()));
        } else if oc == 7 {
            r[2] = r[0]/(pow(2,co(op,&r).try_into().unwrap()));
        }

        if !cp {
            p += 2
        }
    }

    println!("{:?}",o);







    let mut x: i64 = pow(8,15);
    let mut b: i64 = 15;
    let mut nv = vec![];
    let mut v = vec![x];

    while b >= 0 {
        nv = [].to_vec();
        for mut x in v {
            for a in 0..8 {
                let mut p = 0;
                let mut o = vec![];
                r[0] = x;
                while p < l.len()-1 {
                    let mut cp = false;
                    let oc = l[p];
                    let op = l[p+1];

                    if oc == 0 {
                        r[0] = r[0]/(pow(2,co(op,&r).try_into().unwrap()));
                    } else if oc == 1 {
                        r[1] = op ^ r[1];
                    } else if oc == 2 {
                        r[1] = co(op,&r)%8;
                    } else if oc == 3 {
                        if r[0] != 0 {
                            p = op as usize;
                            cp = true;
                        }
                    } else if oc == 4 {
                        r[1] = r[1] ^ r[2]
                    } else if oc == 5 {
                        o.push(co(op,&r)%8);
                    } else if oc == 6 {
                        r[1] = r[0]/(pow(2,co(op,&r).try_into().unwrap()));
                    } else if oc == 7 {
                        r[2] = r[0]/(pow(2,co(op,&r).try_into().unwrap()));
                    }

                    if !cp {
                        p += 2
                    }
                }
                if l[b as usize] == o[b as usize] {
                    nv.push(x);
                }
                x += pow(8,b as usize);
            }
        }
        b -= 1;
        v = nv.clone();
    }
    println!("{:?}",v.iter().min().unwrap());
}
