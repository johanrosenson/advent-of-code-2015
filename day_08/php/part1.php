<?php

$lines = file('../input.txt');

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
