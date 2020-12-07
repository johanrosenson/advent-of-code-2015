const fs = require('fs');

let lines = fs.readFileSync('input', {encoding: 'utf8'}).split(/\r?\n/);

let strlen_encoded = 0;
let strlen_decoded = 0;

for (let n in lines) {
    line = lines[n];
    strlen_encoded += line.length;
    decoded = eval(line)
    strlen_decoded += decoded.length
}

console.log('Diff: ' + (strlen_encoded - strlen_decoded));
