<?php
  $n = $_SERVER['QUERY_STRING'];  //クエリ文字列を取得
  parse_str($n, $str);   //文字列を分解

  //addstock処理開始
  if ( 1 === preg_match('/addstock/', $str['function'])){
    if( ctype_digit($str['amount']) == 0 ) //amountに数字以外が入っていたらERROR
    {
      print('ERROR');
    } else {
      exec("python3 addstock.py"." ".$str['name']." ".$str['amount'], $opt); //addstock.py起動 opt配列をデータとして受け取る
      foreach ($opt as $value) {
        echo $value.'<br>';
      }
    }

  //checkstock処理開始
  } elseif ( 1 === preg_match('/checkstock/', $str['function'])){
    if(1 === preg_match('/name/', $n))
    {
      exec("python3 checkstock1.py"." ".$str['name'], $opt); //checkstock1.py起動
      foreach ($opt as $value) {
        echo $value.'<br>';
      }

    } else if (0 === preg_match('/name/', $n)) {

      exec("python3 checkstockall.py, $opt"); //checkstockall.py起動
      foreach ($opt as $value) {
        echo $value.'<br>';
      }
    }

	//sell処理開始
  } elseif ( 1 === preg_match('/sell/', $str['function'])){
    if ( 0 === preg_match('/amount/', $n)){
      $amount = 0;
      if ( 1 === preg_match('/price/', $n)){
        exec("python3 sellprice.py"." ".$str['name']." ".$amount $str['price'], $opt); //sellprice.py起動
        foreach ($opt as $value) {
          echo $value.'<br>';
        }
      } else if ( 0 === preg_match('/price/', $n)){
        echo $str['name'];
        exec("python3 sell.py"." ".$str['name']." ".$str['amount'], $opt); //sell.py起動
        foreach ($opt as $value) {
          echo $value.'<br>';
        }
      }
    } else {
      if ( 1 === preg_match('/price/', $n)){
        exec("python3 sellprice.py"." ".$str['name']." ".$amount $str['price'], $opt); //sellprice.py起動
        foreach ($opt as $value) {
          echo $value.'<br>';
        }
      } else if ( 0 === preg_match('/price/', $n)){
        exec("python3 sell.py"." ".$str['name']." ".$str['amount'], $opt); //sell.py起動
        foreach ($opt as $value) {
          echo $value.'<br>';
        }
      }
    }
 //checksales処理開始
  } elseif ( 1 === preg_match('/checksales/', $str['function'])){

    exec("python3 checksales.py", $opt); //checksales.py起動
    foreach ($opt as $value) {
      echo $value.'<br>';
    }

  //deleteall処理開始
  } elseif ( 1 === preg_match('/deleteall/', $str['function'])){
    exec("python3 deleteall.py", $opt); //deleteall.py起動
    foreach ($opt as $value) {
      echo $value.'<br>';
    }

  } else {
    print('ERROR');
    echo "<br />";
  }
?>
