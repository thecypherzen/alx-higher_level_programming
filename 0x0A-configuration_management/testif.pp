$arr = [1, 2, 'three',]
each($arr) | $val | {
  notify{"Value: $val":
  message => "this is value $val",
  }
}