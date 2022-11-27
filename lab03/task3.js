"use strict"

function random(min, max) {
    let number = Math.random();
    let range = max - min;

    return number * range + min;
}

console.log(random(1, 5));
console.log(random(10, 20));
console.log(random(100, 250));
console.log(random(123, 125));
console.log(random(123, 124));
console.log(random(-124, -123));
console.log(random(-124, 125));
console.log(random(0, 0));
