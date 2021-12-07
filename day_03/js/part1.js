// run in browser console on input page

(function (input, grid, x, y, dir, callback, h, v) {
    for (var i = 0, imax = input.length, dir = input[i]; i < imax; i++, dir = input[i]) {
        callback(grid, (x = x + (h[dir] || 0)), (y = y + (v[dir] || 0)));
    }

    return grid;
})('|' + document.getElementsByTagName('pre')[0].innerText, {'_u': 0}, 0, 0, '', function (grid, x, y, pos) {
    grid['_u'] = grid['_u'] + (grid[(pos = x + ',' + y)] === undefined ? 1 : 0);
    grid[pos] = (grid[pos] || 0) + 1;
}, {'>': 1, '<': -1}, {'^': 1, 'v': -1});
