const fs = require('fs');

const input = fs.readFileSync('../input.txt', 'utf8');

let index = 0;
let floor = 0;

while (floor >= 0) {
    floor += input.charAt(index) === '('
        ? 1
        : -1;

    index++;
}

console.log(index);
