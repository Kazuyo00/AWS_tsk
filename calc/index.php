<?php
$number = "(\\d+(\\.\\d+)?)";
$pow = "(pow\\((?R),(?R)\\))";
$func = "{$pow}";
$factor = "(-?({$number}|\(\\s*(?R)\\s*\)|{$func}))";
$expression = "(?>\\s*{$factor}(\\s*[\\+\\-\\*\\/\\%]\\s*{$factor})*\\s*)";
$pattern = "/{$expression}/";
$input = $_SERVER['QUERY_STRING'];
if (preg_match($pattern, $input, $match) == 1 && $match[0] === $input)
{
  $result= eval("return {$input};");
  echo "$result\n";
}
else
{
    echo "ERROR\n";
}
?>
