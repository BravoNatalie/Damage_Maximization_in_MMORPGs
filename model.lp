\ Model games
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  0.5 x0 + x1
Subject To
 c1: 4 x0 + 5 x1 <= 30
 c2: 0.0333333333333333 x0 >= 0
 c3: 0.0333333333333333 x1 >= 0
 c4: 0.0333333333333333 x0 <= 0.25
 c5: 0.0333333333333333 x1 <= 0.2
 c6: 0.1666666666666667 x0 + 0.2333333333333333 x1 <= 10
 c7: x0 + 0.1 x1 >= 2
 c8: x0 - x1 >= 0
Bounds
Generals
 x0 x1
End
