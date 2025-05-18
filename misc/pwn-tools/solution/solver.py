from pwn import *
import re

p = process('./Pwn_tools')  
#or p=remote(host,port)
def solve_sorting_table(line):
    nums = list(map(int, line.strip().split()))
    sorted_nums = sorted(nums, reverse=True)
    return ' '.join(map(str, sorted_nums))

def solve_xor(line):
    nums = list(map(int, re.findall(r'\d+', line)))
    return str(nums[0] ^ nums[1])

while True:
    try:
        line = p.recvline(timeout=1).decode().strip()
        print(f"[DEBUG] Received: {line}")

        if 'Table :' in line:
            nums_line = p.recvline().decode().strip()
            print(f"[DEBUG] Numbers: {nums_line}")
            ans = solve_sorting_table(nums_line)
            print(f"[DEBUG] Sending sorted answer: {ans}")
            p.sendline(ans)

        elif 'XOR' in line:
            ans = solve_xor(line)
            print(f"[DEBUG] Sending XOR answer: {ans}")
            p.sendline(ans)

        else:
            print(line)

    except EOFError:
        break

p.close()
