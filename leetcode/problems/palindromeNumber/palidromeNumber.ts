function isPalindrome(x: number): boolean {
    const val: string = String(x);

    const m: number = val.length / 2;
    let l: number = 0;
    let r: number = val.length - 1;

    while(l < r){
        if(val[l] !== val[r]){
            return false;
        }

        l += 1;
        r -= 1;
    }

    return true;
}