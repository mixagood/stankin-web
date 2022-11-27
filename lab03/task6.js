"use strict"

function findVowels(text, vowels) {
    let ctr = 0;
    vowels.forEach(item => {
        let x = -1;
        while((x = text.indexOf(item, x + 1)) !== -1) {
            ctr += 1;
        }
    });
    return ctr;
}


let s = new Set()
s.add('a');
s.add('e');
s.add('i');
s.add('o');
s.add('u');

console.log(findVowels('hello', s));        
console.log(findVowels('aaaaa', s));
console.log(findVowels('uaeaio', s));
console.log(findVowels('bbbbb', s));
console.log(findVowels('', s));
console.log(findVowels('123', s));
console.log(findVowels('bbbbbbbocccc', s));
