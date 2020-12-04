// run in browser console on input page

(function (input, grid, callback, h, v) {
    for (var i = 0, imax = input.length, x = 0, y = 0, dir = input[i]; i < imax; i += 2, dir = input[i]) {
        callback(grid, (x = x + (h[dir] || 0)), (y = y + (v[dir] || 0)));
    }

    for (var i = 1, imax = input.length, x = 0, y = 0, dir = input[i]; i < imax; i += 2, dir = input[i]) {
        callback(grid, (x = x + (h[dir] || 0)), (y = y + (v[dir] || 0)));
    }

    return grid;
})('|' + document.getElementsByTagName('pre')[0].innerText, {'_u': 0}, function (grid, x, y, pos) {
    grid['_u'] = grid['_u'] + (grid[(pos = x + ',' + y)] === undefined ? 1 : 0);
    grid[pos] = (grid[pos] || 0) + 1;
}, {'>': 1, '<': -1}, {'^': 1, 'v': -1});
