<?php

$lines = file('../input.txt');

$strlen_original = 0;
$strlen_encoded = 0;

foreach ($lines as $line) {
    $original = trim($line);
    $encoded = '"' . addslashes($original) . '"';

    // var_dump(sprintf('{%1$s} => {%2$s}', $original, $encoded));

    $strlen_original += strlen($original);
    $strlen_encoded += strlen($encoded);
}

$strlen_diff = $strlen_encoded - $strlen_original;

echo sprintf('%1$s', $strlen_diff) . PHP_EOL;
