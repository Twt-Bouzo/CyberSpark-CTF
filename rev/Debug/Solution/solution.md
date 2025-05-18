![image](https://github.com/user-attachments/assets/50589d24-d4d5-4582-adbc-7610175296a2)


🐛 Debugging with GDB – Secret Value Extraction

When you connect, the binary starts running with gdb already attached on the server side.

Our goal is to break after the program generates a random secret, inspect it using gdb, and input it correctly. If your input matches the secret, the server will give you the flag.

1/

![image](https://github.com/user-attachments/assets/700fb12b-aaa0-45c8-a2f7-f5ba0d1f5385)

2/

disassemble main

layout asm


![image](https://github.com/user-attachments/assets/dc54e30d-9fcc-4760-8082-e5af46e72e50)

3/Set a breakpoint just after the value is stored:


![image](https://github.com/user-attachments/assets/2e22e864-c78b-4ce2-b018-444415b7f171)

4/Check the secret value: It might be in a register like eax/rax, or stored in memory.


![image](https://github.com/user-attachments/assets/53b4710c-a9de-43ed-9ee5-1915f24fcb8d)


5/Continue and write the value


![image](https://github.com/user-attachments/assets/66454a7e-828c-451d-ba1f-ec6c8bd660e1)

FLAG : Spark{Gdb_1s_4_H4ck3rs_Fr13nd}

Resources :

GDB : https://sternumiot.com/iot-blog/learn-gdb-debugger-key-features-and-tutorial/

Debugging : https://www.baeldung.com/linux/gdb-debug

Assembly : https://pwn.college/



