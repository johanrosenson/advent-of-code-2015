// run in browser console on input page

(function (list, pattern, paper, ribbon, result, l, w, h) {
    while((result = pattern.exec(list)) !== null) {
        l = result[1];
        w = result[2];
        h = result[3];
        paper += 2*l*w + 2*w*h + 2*h*l + Math.min(l*w, w*h, h*l);
        ribbon += Math.min(l*2 + w*2, l*2 + h*2, w*2 + h*2) + l*w*h;
    }

    return [paper, ribbon];
})(document.getElementsByTagName('pre')[0].innerText, /^(\d+)x(\d+)x(\d+)$/gm, 0, 0);
