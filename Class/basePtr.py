import config as Cfg
# 常用地址类
class BasePtr:
    def __init__(self):
        # SP = selfPlayer 自定义简称
        self.selfPlayerAddr = Cfg.handle.read_uint(Cfg.client_base + Cfg.local_player_offset)
        self.matrixPtr = Cfg.client_base + Cfg.view_matrix_offset
        self.SPLocationPtr = self.selfPlayerAddr + Cfg.location_x_offset
        self.SPJumpPtr = Cfg.client_base + Cfg.jump_offset
        self.SPSquatPtr = self.selfPlayerAddr + Cfg.squat_offset
        self.SPViewAnglePtr = Cfg.handle.read_uint(Cfg.engine_base + Cfg.view_angle_offset) + Cfg.view_x_offset
        self.SPBloodPtr = self.selfPlayerAddr + Cfg.entity_blood_offset
        self.SPCampPtr = self.selfPlayerAddr + Cfg.entity_camp_offset
        self.SPShotPtr = Cfg.client_base + Cfg.force_attack_offset
        self.SPScopePtr = self.selfPlayerAddr + Cfg.scope_offset
