\ Model games
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  0.25 x0 + 0.3 x1 + x2 + 0.75 x3
Subject To
 c1: 4 x0 - t0 <= 2
 c2: 6 x1 - t1 <= 3
 c3: 13 x2 - t2 <= 10
 c4: 9 x3 - t3 <= 8
 c5: 4 x4 - t4 <= 4
 c6: t0 + t1 + t2 + t3 + t4 <= 100
 c7: 0.01 x0 >= 0
 c8: 0.01 x1 >= 0
 c9: 0.01 x2 >= 0.01
 c10: 0.01 x3 >= 0.01
 c11: 0.01 x4 >= 0.05
 c12: 0.01 x0 <= 0.25
 c13: 0.01 x1 <= 0.1666666666666667
 c14: 0.01 x2 <= 0.0769230769230769
 c15: 0.01 x3 <= 0.1111111111111111
 c16: 0.01 x4 <= 0.25
 c17: 0.03 x0 + 0.07 x1 + 0.08 x2 + 0.1 x3 + 0.07 x4 <= 15
 c18: 0.2 x0 + 0.15 x1 + 0.08 x2 + 0.5 x4 >= 4
 c19: x0 - x2 >= 0
 c20: x1 - x3 >= 0
 c21: x1 - x4 >= 0
Bounds
Generals
 x0 x1 x2 x3 x4
End
