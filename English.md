# BufferOverflowKiller v1.0

A tool for buffer overflow attacks


# run
```
./BufferOverflowKiller.py
```
![image](https://user-images.githubusercontent.com/52622597/187816563-d2611b8e-8003-4e87-89fa-47c2a8b350a9.png)

# Module explanation
```
1. Change the destination ip address and port
2. Target program buffer overflow test
3. Get the program overflow boundary value
4. Exclude bad characters
5. Pwn the program and get the connection back shell
```

# Actual demonstration
## 1. Set the destination IP and port
![image](https://user-images.githubusercontent.com/52622597/178109492-fa2ca80b-e7b4-4644-8b1f-c6e732916ddc.png)
![image](https://user-images.githubusercontent.com/52622597/178109495-958ac298-1aa4-4057-97a2-3ccec5a88446.png)

## 2. Fuzz test the parameters of the target program to see if there is a buffer overflow vulnerability
![image](https://user-images.githubusercontent.com/52622597/178109637-c8df4c89-24b8-4c16-b954-ee9649088bbc.png)
```
It is found that the range of program overflow is within 2000 characters, and then the detailed overflow boundary value of the program is tested.
```
## 3. Test program detailed overflow boundary value

![image](https://user-images.githubusercontent.com/52622597/178109694-5c7b2b41-2f7d-46df-80f9-2b4dca82bfc7.png)
```
Then we go to the Immunity Debugger tool to view the value of the eip register of the program and record it, here is 6F43396E
```
![image](https://user-images.githubusercontent.com/52622597/178109740-fd492a9f-7c37-4476-9914-df72fd80985f.png)
```
Then enter the value of the eip address
```
![image](https://user-images.githubusercontent.com/52622597/178109798-4dc13dd6-bbd4-4a57-9001-a20ab08a3a2c.png)

The program concludes that the verbose overflow boundary is 1978 characters

# exclude bad characters
```
We just ran the fourth module, here we go directly to the Immunity Debugger tool to exclude bad characters
```
![image](https://user-images.githubusercontent.com/52622597/178109900-ac8fb380-7115-4884-92ab-4d6b025b2f25.png)
```
Here we can see what the bad characters of the program are, and then we can easily rule them out
```
# pwn

Run the fifth module, enter the local ip, port, bad characters, return address of the program

![image](https://user-images.githubusercontent.com/52622597/178109987-49ffbf6b-3478-4a89-ab7b-c986feee8298.png)
![image](https://user-images.githubusercontent.com/52622597/178110000-6cf8db91-5db0-4690-8d1b-ca98fe650429.png)
```
Then we open another script and follow the supplementary script prompted by the program
```
![image](https://user-images.githubusercontent.com/52622597/178110028-fb17b9b1-c0a5-455f-b6f3-0eeb647c7a9a.png)
![image](https://user-images.githubusercontent.com/52622597/178110109-79a3bb68-84ee-4315-b397-7e20eb25a746.png)
```
Listen to the set port, then run the program to get the shell
```
![image](https://user-images.githubusercontent.com/52622597/178110133-fd8e25cd-eca0-4e7a-838e-19223792f6bc.png)
# 其他
```
The tool can execute linux commands normally when running
```
![image](https://user-images.githubusercontent.com/52622597/178110205-62d00f69-ecf7-4668-977d-5f9ad1affe06.png)
```
When testing the bad characters of the program, if there are many bad characters in the program, the test can be repeated, which is very convenient
```
