const fs = require('fs');

const input = fs.readFileSync('input.txt', 'utf8');

const floor = Math.abs(input.split(')').length - input.split('(').length);

console.log(floor);
