# 公共方法
import re, win32gui, win32con, time
from win32api import GetAsyncKeyState
import config as Cfg


# 帮助信息
def help_msg():
    print("*******     F2 ON/OFF(默认关闭状态,请在对局中按F2开启,对局结束前记得按F2关闭)     *******")
    print("*******     人物透视 开枪自瞄 开镜自瞄      *******")
    print("注意事项: 不适用连点 [未考虑后坐力对准度的影响]")


# 返回按键状态
def key_pressed(key):
    return GetAsyncKeyState(key) & 1 == 1


# 特征查找 没用上
def find_by_Character():
    # Cfg.local_player_offset = re.search(rb'\x7C\xD0..\x97\x72..\x08\x20\x08\x00\xF8\x17..\x70\x14..\xA8\xD0',
    #                                     Cfg.client_module).start() + 0x50
    # Cfg.glow_object_manager_offset = re.search(rb'\x8C\x0C..\x00{28}\x20\xB3..\x00{12}\xFF{4}\x01\x00{23}\x01',
    #                                            Cfg.client_module).start() + 0x50

    noPlayerAddrContainer = Cfg.client_base + re.search(rb'\x42\x56\x8d\x34\x85.{4}', Cfg.client_module).start() + 0x21
    entity_list = Cfg.handle.read_uint(noPlayerAddrContainer)
    Cfg.entity_list_offset = entity_list - Cfg.client_base
    pass
