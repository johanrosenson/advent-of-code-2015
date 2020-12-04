const fs = require('fs');

let lines = fs.readFileSync('input', {encoding: 'utf8'}).split(/\r?\n/);

let strlen_original = 0;
let strlen_encoded = 0;

for (let n in lines) {
    line = lines[n];
    strlen_original += line.length;
    encoded = '"' + line.replace(/(["\\])/g, '\\$1') + '"';
    strlen_encoded += encoded.length
}

console.log('Diff: ' + (strlen_encoded - strlen_original));
