// Josh's Joltin' Giants
// SoftDev pd08
// K27 -- Basic functions in JavaScript
// 2023-04-03t
// --------------------------------------------------

function fact(a) {
    if(a <= 1){
        return 1
    } else{
        return fact(a - 1) * a
    }
}

function fib(a){
    if(a == 0 || a == 1){
        return a
    }
    var count = 2
    var kot1 = 1
    var kot2 = 1
    var kot3 = 1

    while(count < a){
        var temp = kot3
        kot3 = kot3 + kot2
        kot1 = kot2
        kot2 = temp
        count++
    }
    return kot3
 }