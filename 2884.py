hour, min = map(int, input().split())
mount = hour*60 + min -45
if(mount<0): print(f"23 {mount%60}")
else: print(f"{int(mount/60)} {mount%60}")