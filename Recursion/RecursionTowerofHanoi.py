def TowerOfHanoi(n, bat_dau_tu, chuyen_den_cot, cot_trung_gian): 
    if n == 0: 
        return
    TowerOfHanoi(n-1, bat_dau_tu, cot_trung_gian, chuyen_den_cot) 
    print("Chuyen", n, "tu cot", bat_dau_tu, "sang cot", chuyen_den_cot) 
    TowerOfHanoi(n-1, cot_trung_gian, chuyen_den_cot, bat_dau_tu) 
N = 3
TowerOfHanoi(N, 'A', 'C', 'B') 
  