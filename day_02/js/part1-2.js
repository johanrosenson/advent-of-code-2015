const fs = require('fs');

const input = fs.readFileSync('../input.txt', 'utf8')
    .split('\n');

let paper = 0;
let ribbon = 0;

input.forEach(function (input) {
    const [l, w, h] = input.split('x').map(v=>parseInt(v));

    paper += (2*l*w) + (2*w*h) + (2*h*l) + Math.min(l*w, w*h, h*l);
    ribbon += l*w*h + Math.min(...[
        l*2 + w*2,
        w*2 + h*2,
        h*2 + l*2,
    ]);
});

console.log({
    paper,
    ribbon,
});
