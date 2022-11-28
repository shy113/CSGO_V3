# 自身玩家属性类
import time

import numpy as np
import config as Cfg
from Class.basePtr import BasePtr


class SelfPlayerAttr:
    def __init__(self, basePtr: BasePtr):
        self.CP = basePtr
        self.locationXYZ = self.set_locationXYZ()  # 人物XYZ
        self.crosshairXY = self.set_crosshairXY()  # 准心
        self.matrix = self.set_matrix()  # 自身矩阵 4*4
        self.jumpState = self.set_jumpState()  # 跳跃状态
        self.squatState = self.set_squatState()  # 下蹲状态
        self.mirrorState = self.set_mirrorState()  # 狙击枪开镜状态
        self.blood = self.set_blood()  # 血量
        self.camp = self.set_camp()  # 阵营
        self.shotState = self.set_ShotState()  # 是否开枪

        # self.immunity = False  # 是否是无敌状态(无敌时间)
        # self.helmet = False                       # 是否有头盔
        # self.recoil = 0                           # 后坐力
        # self.flash = 0  # 闪光

    # 设置位置XYZ
    def set_locationXYZ(self):
        locationXYZ = np.zeros((3), dtype=float)
        tmp_x = self.CP.SPLocationPtr
        for i in range(3):
            locationXYZ[i] = Cfg.handle.read_float(tmp_x)
            tmp_x += 4
        return locationXYZ

    # 设置准心XY
    def set_crosshairXY(self):
        crosshairXY = np.zeros((2), dtype=float)
        crosshairXY[0] = Cfg.handle.read_float(self.CP.SPViewAnglePtr)
        crosshairXY[1] = Cfg.handle.read_float(self.CP.SPViewAnglePtr + 4)
        if crosshairXY[0] and crosshairXY[1]:
            return crosshairXY
        return

    # 设置矩阵信息
    def set_matrix(self):
        matrix = np.zeros((4, 4), dtype=float)  # 构造一个4*4的二维数组 元素类型是 float
        tmp_matrix_addr = self.CP.matrixPtr
        for i in range(4):
            for j in range(4):
                matrix[i][j] = Cfg.handle.read_float(tmp_matrix_addr)
                tmp_matrix_addr += 4
        return matrix

    # 设置自身的跳跃状态
    def set_jumpState(self):
        jump_value = Cfg.handle.read_uint(self.CP.SPJumpPtr)
        if not jump_value:
            return
        if jump_value == 4:
            return False
        return True

    # 设置自身的下蹲状态
    def set_squatState(self):
        squat_value = Cfg.handle.read_float(self.CP.SPSquatPtr)
        if not squat_value:
            return
        if squat_value < float(50.0):
            return True
        return False

    # 设置开镜状态
    def set_mirrorState(self):
        if Cfg.handle.read_bytes(self.CP.SPScopePtr, 1) == b'\x01':
            return True
        return False

    # 设置玩家血量
    def set_blood(self):
        if Cfg.handle.read_uint(self.CP.SPBloodPtr):
            return Cfg.handle.read_uint(self.CP.SPBloodPtr)
        return

    # 设置玩家阵营
    def set_camp(self):
        if Cfg.handle.read_uint(self.CP.SPCampPtr):
            return Cfg.handle.read_uint(self.CP.SPCampPtr)
        return

    # 设置开枪状态
    def set_ShotState(self):
        shot_value = Cfg.handle.read_uint(self.CP.SPShotPtr)
        if not shot_value:
            return
        if shot_value == 4:
            return False
        return True
