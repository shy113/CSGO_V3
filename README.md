## CSGO自瞄+透视

### 0x01 声明：

>   - 本项目仅限于学习交流不可商用，不可用于非法用途（包括但不限于：用于制作游戏外挂等）
>   - 使用本项目产生的任何后果与本人无关！！！！
>   - 使用本项目则默认同意本声明！
>

### 0x02 项目信息

> * Author : 蜉蝣
> * Date   : 2022/9/27
> * 基于 C++项目 python项目 的二次开发
> * 进入对局后运行python脚本按F2开启自瞄透视


### 0x03 偏移网站

> 1. https://csgo.dumps.host/offsets
>
> 2. https://github.com/frk1/hazedumper/blob/master/csgo.hpp
>


### 0x04 Python特性
- 01 A B 不能互导 容易导致死循环
- 02 配置文件中的 变量 在哪个文件中被修改 则就在哪个文件中有效 并且谁引入这个文件中生效

	
	- config.py  A.py B.py C.py 在config存放着变量
	- A B C 三者都导入了 config.py
	- 现config.py中的值在 B中被修改了 则 B 能访问这些修改后的数据 A里面访问不了
	- 若 C 导入了 B 则 C也能访问被B修改的数据

### 0x05 致谢

***前身:***

- C++ Bili 作者 大会员也没积分 GitHub https://github.com/245950258/How-to-create-a-csgo-cheating-program
- python glow CSDN链接 https://blog.csdn.net/qq_44803739/article/details/115245870

***参考偏移网址:***

- https://csgo.dumps.host/offsets
- https://github.com/frk1/hazedumper/blob/master/csgo.hpp
