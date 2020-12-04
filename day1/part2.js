// run in browser console on input page

(function (input) {
    var floor = 0;
    for (var i = 0, imax = input.length; i < imax; i++) {
        floor += input[i] == '(' ? 1 : -1;
        if (floor == -1) {
            console.log('basement: ' + (i+1));
            break;
        }
    }
})(document.getElementsByTagName('pre')[0].innerText);
