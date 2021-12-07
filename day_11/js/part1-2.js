const fs = require('fs');

const input = 'cqjxjnds';

console.log(`Old password: ${input}`);

const incrementLetter = function (letter) {
    return String.fromCharCode(
        'a'.charCodeAt(0) +
        (letter.charCodeAt(0) - 'a'.charCodeAt(0) + 1) % ('z'.charCodeAt(0) - 'a'.charCodeAt(0) + 1)
    );
}

const incrementPassword = function (password) {
    let newPassword = password;

    let pos = password.length - 1;

    let wrapped = false;

    do {
        const newLetter = pos < 0
            ? 'a'
            : incrementLetter(newPassword.substr(pos));
        newPassword = newPassword.substr(0, pos) + newLetter + newPassword.substr(pos + 1);

        wrapped = pos >= 0 && newLetter === 'a';

        if (wrapped) {
            pos--;
        }
    } while (wrapped);

    return newPassword;
}

const validatePassword = function (password) {
    if (password.match(/[iol]/) !== null) {
        return false;
    }

    const pairs = Array.from(password.match(/(?<group>(.)\2)/g) || []).filter(function (value, index, self) {
        return self.indexOf(value) === index;
    });

    if (pairs.length < 2) {
        return false;
    }

    let containsStraight = false;

    for (i = 0, imax = password.length - 2; i < imax; i++) {
        const charCode = password.substr(i, 1).charCodeAt(0);

        if (password.substr(i+1, 1).charCodeAt(0) !== charCode + 1) {
            continue;
        }

        if (password.substr(i+2, 1).charCodeAt(0) !== charCode + 2) {
            continue;
        }

        containsStraight = true;
        break;
    }

    if (! containsStraight) {
        return false;
    }

    return true;
}

const calculateNextPassword = function (currentPassword) {
    let newPassword = incrementPassword(currentPassword);

    while (! validatePassword(newPassword)) {
        newPassword = incrementPassword(newPassword);
    }

    return newPassword;
}

let newPassword = calculateNextPassword(input);
let nextPassword = calculateNextPassword(newPassword);

console.log(`New password: ${newPassword}`);
console.log(`Next password: ${nextPassword}`);
