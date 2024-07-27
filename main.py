def towerofhanoi (n,sa,sb,sc):
    if n == 0:
        return
    towerofhanoi(n-1,sa,sc,sb)
    print(f"move disk {n} from rod {sa} to rod {sc}\n")
    towerofhanoi(n-1,sc,sb,sa)
    
towerofhanoi(3,"a","b","c")