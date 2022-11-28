# Author     : 蜉蝣
# Date       : 2022/9/27
# Description: CSGO自瞄 透视 游戏更新的话将CSGO_V3/offset/dumpsOffset.py更新一下就行

# 基于 C++项目 Python项目 的二次开发
# C++ Bili 作者 大会员也没积分 GitHub https://github.com/245950258/How-to-create-a-csgo-cheating-program
# Python glow CSDN链接 https://blog.csdn.net/qq_44803739/article/details/115245870
# 参考偏移网址:
# https://csgo.dumps.host/offsets
# https://github.com/frk1/hazedumper/blob/master/csgo.hpp

# 关于矩阵的知识
# https://blog.csdn.net/qq_27161673/article/details/103436678

import threading
import config as Cfg
import func.commonFunc as commonF
import func.glowFunc as glowF
import func.aimbotFunc as aimbotF
def main():
    commonF.help_msg()                  #帮助信息
    try:
        bswitchFlag = False
        while True:
            if commonF.key_pressed(Cfg.switch_exit):bswitchFlag = not bswitchFlag
            if bswitchFlag:
                threading.Thread(aimbotF.aimbot_mian()).start()
                threading.Thread(glowF.glow_main()).start()
    finally:
        Cfg.handle.close_process()

# 入口函数
if __name__ == '__main__':
    main()

