<?php

// https://adventofcode.com/2015/day/8

$lines = file('input');
// $lines = file('example');

$strlen_encoded = 0;
$strlen_decoded = 0;

foreach ($lines as $line) {
    $encoded = trim($line);
    $decoded = eval('return ' . $encoded . ';');

    // var_dump(sprintf('{%1$s} => {%2$s}', $encoded, $decoded));

    $strlen_encoded += strlen($encoded);
    $strlen_decoded += strlen($decoded);
}

$strlen_diff = $strlen_encoded - $strlen_decoded;

echo sprintf('%1$s', $strlen_diff) . PHP_EOL;
