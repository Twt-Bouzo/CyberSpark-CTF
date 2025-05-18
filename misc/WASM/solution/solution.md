![image](https://github.com/user-attachments/assets/4b11a9ed-a5e3-4706-b3bf-6cb40cb0218e)

WebAssembly (WASM) is a fast, low-level code format that runs in web browsers. It lets programs (like games or apps) work at near-native speed, even though they're running safely inside your browser.

The solution required only basic tools (strings, base64), highlighting the importance of proper data handling in compiled web applications. commande : strings index.html


![image](https://github.com/user-attachments/assets/226a7332-5710-4f65-a781-c550023886cd)

We identified a Base64-encoded string within the binary.

![image](https://github.com/user-attachments/assets/c862b24d-363a-40dd-b790-ae389504e5e0)

We decrypte it and we get the flag

FLAG: Spark{Wasm_1s_4ws0m3}

Resources :

WebAssembly : https://webassembly.org/


