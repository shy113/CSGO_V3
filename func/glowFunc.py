# 透视相关方法
import func.commonFunc as commonF

Cfg = commonF.Cfg
ColorRGBA = Cfg.ColorRGBA

from Class.selfPlayerAttr import SelfPlayerAttr
from Class.playerAttr import PlayerAttr
from Class.basePtr import BasePtr


# 修改内存 设置辉光值
def glow(entity_glow, color: ColorRGBA):
    glow_manager = Cfg.handle.read_uint(Cfg.client_base + Cfg.glow_object_manager_offset)
    final_addr = glow_manager + entity_glow * 0x38 + Cfg.red_offset  # 辉光红色所在地地址
    Cfg.handle.write_float(final_addr, float(color.Red))
    Cfg.handle.write_float(final_addr + 0x4, float(color.Green))
    Cfg.handle.write_float(final_addr + 0x8, float(color.Blue))
    Cfg.handle.write_float(final_addr + 0xC, float(color.Alpha))
    Cfg.handle.write_uchar(final_addr + 0x20, 1)
    Cfg.handle.write_uchar(final_addr + 0x21, 0)


# # 获得所有玩家属性
# def get_playerArrtList():
#     playerArrtList = []
#     for i in range(1, 32):
#         single_addr_container = Cfg.client_base + Cfg.entity_list_offset + i * (0x10)
#         entity_addr = Cfg.handle.read_uint(single_addr_container)  # 注意判空
#         if entity_addr:
#             playerArrt: PlayerAttr = PlayerAttr(entity_addr)
#             playerArrtList.append(playerArrt)
#     return playerArrtList

# 获得所有玩家属性 试试迭代器 哈哈
def get_playerArrtList():
    for i in range(1, 32):
        single_addr_container = Cfg.client_base + Cfg.entity_list_offset + i * (0x10)
        entity_addr = Cfg.handle.read_uint(single_addr_container)  # 注意判空
        if entity_addr:
            playerArrt: PlayerAttr = PlayerAttr(entity_addr)
            yield playerArrt


# 辉光主逻辑
def glow_main():
    basePtr = BasePtr()
    selfPlayerAttr = SelfPlayerAttr(basePtr)  # 初始化自身玩家属性
    playerArrtList = get_playerArrtList()  # 初始化所有玩家属性 放在一个列表里面
    if not commonF.key_pressed(Cfg.glowSwitch):
        for playerArrt in playerArrtList:
            if not playerArrt.camp == selfPlayerAttr.camp:
                # 敌人
                Cfg.enemy_color.Green = 0.006 * playerArrt.blood
                if playerArrt.blood == 0x64:
                    Cfg.enemy_color.Green = 1
                Cfg.enemy_color.Red = 1.0 - Cfg.enemy_color.Green
                glow(playerArrt.glow_index, Cfg.enemy_color)
            else:  # glow(playerArrt.glow_index, Cfg.friend_color) # 队友
                pass
