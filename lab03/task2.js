"use strict"

function checkSpam(text, spamwords) {
    let fl = false;
    text = text.toLowerCase();

    spamwords.forEach(item => {
        if (text.includes(item)) {
            fl = true;
            return fl;
        }
    });

    return fl;
}


let text = 'abcxXxghviagRabc'

console.log(checkSpam('abc def ghi', ['xxx']));
console.log(checkSpam('abc xxx ghi', ['xxx']));
console.log(checkSpam('abc xXx ghi', ['xxx']));
console.log(checkSpam(text, ['xxx', 'viagra']));
console.log(checkSpam('abcghviagRabc', ['xxx', 'viagra']));
