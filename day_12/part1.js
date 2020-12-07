const fs = require('fs');

const doc = JSON.parse(
    fs.readFileSync('input.txt', 'utf8'),
);

const process = function (doc) {
    let sum = 0;

    for (let [key, value] of Object.entries(doc)) {
        if (Array.isArray(value)) {
            sum += process(value);
        } else if (typeof value === 'string') {
            sum += 0;
        } else if (! isNaN(value)) {
            sum += value;
        } else {
            sum += process(value);
        }
    }

    return sum;
};

let answer = process(doc);

console.log(`Answer: ${answer}`);
