"use strict"


// for strong
function FizzBuzzMap(start, end, dict) {

    let out = ''

    for (let i = start; i <= end; i++) {
        let check = false;
        dict.forEach((value, key, map) => {
            if (i % key == 0) {
                out += value;
                check = true;
            }
        });

        if (!check) {
            out += i;
        }
        out += '\n';
    }

    console.log(out)
}


// for weak
function Fizzbuzz(start, end) {
    for (let i = start; i <= end; i++) {
        
        let output = '';

        if (i % 3 == 0) {
            output += 'fizz';
        }
        if (i % 5 == 0) {
            output += 'buzz'
        }
        if (output === '')
            console.log(i);
        else
            console.log(output)
    }
}

// Fizzbuzz(1, 30);

let map = new Map();
map.set("3", "fizz");
map.set("5", "buzz");
// map.set("2", "haha")

FizzBuzzMap(1, 30, map)
FizzBuzzMap(1, 1, map)
FizzBuzzMap(1, 3, map)
FizzBuzzMap(1, 5, map)
FizzBuzzMap(1, 15, map)
