# BufferOverflowKiller v1.0
### [English](https://github.com/baimao-box/BufferOverflowKiller/edit/main/English.md)


一个用于缓冲区溢出攻击的工具

# 运行
```
./BufferOverflowKiller.py
```
![image](https://user-images.githubusercontent.com/52622597/187816563-d2611b8e-8003-4e87-89fa-47c2a8b350a9.png)

# 模块解释
```
1. 更改目标ip地址和端口
2. 目标程序缓冲区溢出测试
3. 获取程序溢出边界数值
4. 排除坏字符
5. pwn掉程序，获取回连shell
```

# 实战演示
## 1. 设置目标IP和端口
![image](https://user-images.githubusercontent.com/52622597/178109492-fa2ca80b-e7b4-4644-8b1f-c6e732916ddc.png)
![image](https://user-images.githubusercontent.com/52622597/178109495-958ac298-1aa4-4057-97a2-3ccec5a88446.png)

## 2. 模糊测试目标程序的参数，看是否有缓冲区溢出漏洞
![image](https://user-images.githubusercontent.com/52622597/178109637-c8df4c89-24b8-4c16-b954-ee9649088bbc.png)
```
发现程序溢出的区间在2000个字符内，接下来测试程序详细的溢出边界数值
```
## 3. 测试程序详细的溢出边界数值

![image](https://user-images.githubusercontent.com/52622597/178109694-5c7b2b41-2f7d-46df-80f9-2b4dca82bfc7.png)
```
然后我们去到Immunity Debugger工具中查看程序的eip寄存器的值并记录，这里是6F43396E
```
![image](https://user-images.githubusercontent.com/52622597/178109740-fd492a9f-7c37-4476-9914-df72fd80985f.png)
```
然后输入eip地址的值
```
![image](https://user-images.githubusercontent.com/52622597/178109798-4dc13dd6-bbd4-4a57-9001-a20ab08a3a2c.png)

程序得出详细的溢出边界是1978个字符

# 排除坏字符
```
刚刚我们运行了第四个模块，这里我们直接去Immunity Debugger工具里排除坏字符
```
![image](https://user-images.githubusercontent.com/52622597/178109900-ac8fb380-7115-4884-92ab-4d6b025b2f25.png)
```
这里我们可以看到程序的坏字符是什么，之后我们方便排除
```
# pwn

运行第五个模块，输入本地ip，端口，坏字符，程序的返回地址

![image](https://user-images.githubusercontent.com/52622597/178109987-49ffbf6b-3478-4a89-ab7b-c986feee8298.png)
![image](https://user-images.githubusercontent.com/52622597/178110000-6cf8db91-5db0-4690-8d1b-ca98fe650429.png)
```
然后我们打开另一个脚本，按照程序提示的补充脚本
```
![image](https://user-images.githubusercontent.com/52622597/178110028-fb17b9b1-c0a5-455f-b6f3-0eeb647c7a9a.png)
![image](https://user-images.githubusercontent.com/52622597/178110109-79a3bb68-84ee-4315-b397-7e20eb25a746.png)
```
监听设置的端口，然后运行程序，得到shell
```
![image](https://user-images.githubusercontent.com/52622597/178110133-fd8e25cd-eca0-4e7a-838e-19223792f6bc.png)
# 其他
```
工具在运行时可以正常执行linux命令
```
![image](https://user-images.githubusercontent.com/52622597/178110205-62d00f69-ecf7-4668-977d-5f9ad1affe06.png)
```
在测试程序坏字符时，如果程序坏字符很多，可以重复测试，很方便
```
