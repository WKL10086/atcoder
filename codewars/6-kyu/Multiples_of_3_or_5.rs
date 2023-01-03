fn solution(num: i32) -> i32 {
    (0..num).filter(|x| x % 3 == 0 || x % 5 == 0).sum()
}
