def towerofhanoi (n,a,b,c):
    if n == 1:
        print(f"move 1st disk from rod {a} to rod {c}\n")
        return
    towerofhanoi(n-1,a,c,b)
    print(f"move disk {n} from rod {a} to rod {c}\n")
    towerofhanoi(n-1,b,a,c)
    
towerofhanoi(3,"a","b","c") 