# 自瞄相关方法
import win32gui, win32con, math, time, numpy as np
from sympy import *
import config as Cfg
import func.commonFunc as commonF
from Class.selfPlayerAttr import SelfPlayerAttr
from Class.playerAttr import PlayerAttr
from Class.basePtr import BasePtr


# 利用矩阵 和 玩家位置坐标 和 准心至游戏左边框上边框的距离 得到 玩家距离游戏左边框上边框的距离
def get_playerBorder_distance(matrix, playerAttr: PlayerAttr, crosshair_w, crosshair_h):
    '''
    :param matrix               : 矩阵信息 4*4数组
    :param playerAttr           : 玩家属性 可拿到 玩家的位置坐标
    :param crosshair_w          : 准心至游戏左边框的距离
    :param crosshair_h          : 准心至游戏上边框的距离
    :return:player_w,player_h   : 游戏玩家至游戏左边框的距离,游戏玩家至游戏上边框的距离
    '''
    # 不太理解
    location = playerAttr.location
    to_target = float(
        matrix[2][0] * location[0] + matrix[2][1] * location[1] + matrix[2][2] * location[2] + matrix[2][3])
    if to_target < float(0.01):
        player_w = player_h = 0
        return player_w, player_h
    to_target = float(1.0 / to_target)
    tmp = float(matrix[0][0] * location[0] + matrix[0][1] * location[1] + matrix[0][2] * location[2] + matrix[0][3])
    to_width = float(crosshair_w + tmp * to_target * crosshair_w)

    tmp = float(
        matrix[1][0] * location[0] + matrix[1][1] * location[1] + matrix[1][2] * (location[2] + 75.0) + matrix[1][3])
    to_height_h = float(crosshair_h - tmp * to_target * crosshair_h)

    tmp = float(
        matrix[1][0] * location[0] + matrix[1][1] * location[1] + matrix[1][2] * (location[2] - 5.0) + matrix[1][3])
    to_height_w = float(crosshair_h - tmp * to_target * crosshair_h)

    x = (int)(to_width - (to_height_w - to_height_h) / float(4.0))
    y = (int)(to_height_h)
    w = (int)((to_height_w - to_height_h) / float(2.0))
    h = (int)(to_height_w - to_height_h)

    player_w = x + (w / 2)
    player_h = y + (h / 2)
    return player_w, player_h


# 获取准心至游戏左边框 上边框的距离
def get_crosshairBorder_distance(game_title):
    '''
    获取准心至游戏左边框 上边框的距离
    :param game_title:  进程名称 "Counter-Strike: Global Offensive - Direct3D 9"
    :return:crosshair_w 准心至游戏左边框的距离 crosshair_h 准心至游戏上边框的距离
    '''
    hwnd = win32gui.FindWindow(None, game_title)
    l, t, r, b = win32gui.GetWindowRect(hwnd)  # 返回左上右下
    window_x = l
    window_y = t
    window_w = r - l
    window_h = b - t
    if (win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE) & win32con.WS_CAPTION):
        window_x += 8
        window_y += 30
        window_w -= 8
        window_h -= 30
    crosshair_w = window_w / 2
    crosshair_h = window_h / 2
    return crosshair_w, crosshair_h


# 利用准心至左、上边框的距离 和玩家至左、上的距离 得到 "自瞄长度"
def calc_crosshairPlayer_len(crosshair_w, crosshair_h, player_w, player_h):
    '''
    计算自瞄长度
    :param crosshair_w: 准心至左边框的距离
    :param crosshair_h: 准心至上边框的距离
    :param player_w:    玩家至左边框的距离
    :param player_h:    玩家至上边框的距离
    :return: aimbot_len :准心至每个玩家的距离
    '''
    tmp_w = math.fabs(crosshair_w - player_w)
    tmp_h = math.fabs(crosshair_h - player_h)
    aimbot_len = int(math.sqrt((tmp_w * tmp_w) + (tmp_h * tmp_h)))

    return aimbot_len


# 设置准心至每个玩家的距离
def setup_aimbot_len(selfPlayerAttr, playerArrt: PlayerAttr):
    crosshair_w, crosshair_h = get_crosshairBorder_distance(Cfg.game_title)
    matrix = selfPlayerAttr.matrix
    if (not playerArrt.is_self) and playerArrt.effective:
        player_w, player_h = get_playerBorder_distance(matrix, playerArrt, crosshair_w, crosshair_h)
        return calc_crosshairPlayer_len(crosshair_w, crosshair_h, player_w, player_h)


# 获取离准心最近的人物在列表中的索引
def get_minAimbotLen_index(selfPlayerAttr, playerArrtList):
    aimIndex = -1
    count = 0
    min_aimbot_len = float(100000)  # 假定最小为100000
    for playerAttr in playerArrtList:
        playerAttr: PlayerAttr = playerAttr
        # 不是队友 不是自己 距离最近 没挂掉
        if playerAttr.aimbot_len and playerAttr.effective and \
                not playerAttr.is_self and \
                not playerAttr.camp == selfPlayerAttr.camp:
            if playerAttr.aimbot_len < min_aimbot_len:
                min_aimbot_len = playerAttr.aimbot_len
                aimIndex = count
        count += 1
    return aimIndex


#  利用我们XYZ、敌人头骨XYZ , 获取自瞄角度x y --> 最终要写入内存的数据
def get_aimbot_angle(selfPlayerAttr, playerArrtList, aimIndex, recoil):
    playAttr: PlayerAttr = playerArrtList[aimIndex]
    headBoneXYZ = playAttr.headBoneXYZ
    self_location = selfPlayerAttr.locationXYZ

    squat_state = selfPlayerAttr.squatState

    # headBoneXYZ 准心要去的位置
    x = float(self_location[0] - headBoneXYZ[0])
    y = float(self_location[1] - headBoneXYZ[1])
    z = float(self_location[2] - headBoneXYZ[2] + float(62.0))  # 值越小离头部越近
    # z = float(self_location[2] - head_bone_z + float(0.0) + float(65.0) + float(15.0))  # 脚部 头部 身子
    if squat_state:
        z -= float(15.0)
    z += recoil
    pi = float(3.1415)
    aim_angle = np.zeros((2), dtype=float)  # 构造 需要写入 内存的 角度
    # 不太理解
    aim_angle[0] = float(atan(z / math.sqrt(x * x + y * y)) / pi * float(180))
    aim_angle[1] = float(atan(y / x) / pi * float(180.0))

    if x >= 0:
        if y >= 0:
            aim_angle[1] = aim_angle[1] - float(180.0)
        else:
            aim_angle[1] = aim_angle[1] + float(180.0)

    return aim_angle


# 将算好的角度写入内存
def write_current_angle(aim_angle, selfPlayerAttr):
    view_angle_base = Cfg.handle.read_uint(Cfg.engine_base + Cfg.view_angle_offset)
    Cfg.handle.write_float(view_angle_base + Cfg.view_x_offset, aim_angle[0])
    Cfg.handle.write_float(view_angle_base + Cfg.view_x_offset + 4, aim_angle[1])


# 自瞄主要逻辑
def aimbot_players(selfPlayerAttr, playerArrtList, max_fov=Cfg.max_fov):  # max_fov 值越大越浮夸
    if selfPlayerAttr.jumpState:  # 跳起来是打不到人的 无需自瞄
        return

    aimIndex = get_minAimbotLen_index(selfPlayerAttr, playerArrtList)
    if aimIndex == -1:  # 没有可以自瞄的目标
        return

    aim_angle = get_aimbot_angle(selfPlayerAttr, playerArrtList, aimIndex, float(0.0))
    current_angle = selfPlayerAttr.crosshairXY
    if math.fabs(aim_angle[0] - current_angle[0]) > max_fov / 2 or math.fabs(aim_angle[1] - current_angle[1]) > max_fov:
        return
    write_current_angle(aim_angle, selfPlayerAttr)


# 获得所有玩家属性
def get_playerArrtList(selfPlayerAttr):
    playerArrtList = []
    for i in range(1, 32):
        single_addr_container = Cfg.client_base + Cfg.entity_list_offset + i * (0x10)
        entity_addr = Cfg.handle.read_uint(single_addr_container)  # 注意判空
        if entity_addr:
            playerArrt: PlayerAttr = PlayerAttr(entity_addr)
            # 设置准心至每个2d玩家的距离
            playerArrt.aimbot_len = setup_aimbot_len(selfPlayerAttr, playerArrt)
            playerArrtList.append(playerArrt)
    return playerArrtList


# 自瞄入口
def aimbot_mian():
    basePtr = BasePtr()
    selfPlayerAttr = SelfPlayerAttr(basePtr)  # 初始化自身玩家属性
    playerArrtList = get_playerArrtList(selfPlayerAttr)  # 初始化所有玩家属性 放在一个列表里面
    if commonF.key_pressed(Cfg.mouseLeftMinButton) or selfPlayerAttr.mirrorState \
            or selfPlayerAttr.shotState or selfPlayerAttr.squatState:  # 如果左侧小键点击 或者开镜
        aimbot_players(selfPlayerAttr, playerArrtList)
