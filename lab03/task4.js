"use strict"

function palindrome(text) {

    return text.toLowerCase() === text.split('').reverse().join('').toLowerCase();
}

console.log(palindrome('123'));

console.log(palindrome('AbC cba'));     // По условию "Anna" - палиндром
console.log(palindrome('12321'));  
console.log(palindrome('123 321'));
console.log(palindrome('12 3 3 21'));
console.log(palindrome('-123 321-'));
console.log(palindrome('Abc cbA'));
console.log(palindrome('A!bc,cb!A'));
console.log(palindrome(''));
console.log(palindrome('AAAAAAAAA'));