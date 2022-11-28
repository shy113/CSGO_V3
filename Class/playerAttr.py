# 游戏玩家共有属性类
import config as Cfg
import numpy as np
from Class.basePtr import BasePtr

class PlayerAttr:
    def __init__(self, entity_addr):
        self.entity_addr = entity_addr
        self.is_self = self.set_is_self()  # 是否为玩家自己
        self.location = self.set_location()  # 人物位置
        self.headBoneXYZ = self.set_headBoneXYZ()  # 人物骨骼
        self.camp = self.set_camp()  # 阵营
        self.blood = self.set_blood()  # 血量
        self.effective = self.set_effective()  # 判断该人物地址是否有效
        self.glow_index = self.set_glow_index()
        self.aimbot_len = 0  # 自瞄距离 [准心至每个玩家的距离]
        self.armor = 0  # 护甲
        self.helmet = False  # 是否有头盔
        self.recoil = 0  # 后坐力
        self.immunity = False  # 是否是无敌状态(无敌时间)
        self.shot = False  # 是否开枪
        self.flash = 0  # 闪光


    # 设置阵营
    def set_camp(self):
        return Cfg.handle.read_uint(self.entity_addr + Cfg.entity_camp_offset)

    # 设置辉光索引
    def set_glow_index(self):
        return Cfg.handle.read_uint(self.entity_addr + Cfg.entity_glow_index_offset)

    # 设置人物血量
    def set_blood(self):
        return Cfg.handle.read_uint(self.entity_addr + Cfg.entity_blood_offset)

    # 设置人物位置
    def set_location(self):
        location = np.zeros((3), dtype=float)
        tmp = self.entity_addr
        for i in range(3):
            location[i] = Cfg.handle.read_float(tmp + 0xA0)
            tmp += 4
        return location

    # 设置人物头骨
    def set_headBoneXYZ(self):
        headBoneXYZ = np.zeros((3), dtype=float)
        bone_base_address = Cfg.handle.read_uint(self.entity_addr + Cfg.headBoneBase_offset)
        for i in range(3):
            headBoneXYZ[i] = Cfg.handle.read_float(bone_base_address + Cfg.headBoneX_ofsset)
            bone_base_address += 0x10
        return headBoneXYZ

    # 设置玩家是不是我们自身
    def set_is_self(self):
        basePtr = BasePtr()
        if self.entity_addr == basePtr.selfPlayerAddr:
            return True
        return False

    # 设置玩家状态是否正常
    def set_effective(self):
        if self.blood > 0:
            return True
        return False
