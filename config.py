# 配置文件
import win32con as keymap
import pymem
from   Class.colorRGBA import ColorRGBA
from   Class.moduleInfo import ModuleInfo
import offset.dumpsOffset as dumpsOffset

# 程序开关
switch_exit = keymap.VK_F2
# 自瞄总开关
aimbotSwitch = keymap.VK_F3
# 辉光总开关
glowSwitch = keymap.VK_F4

# 鼠标左键
mouseLeftButton = keymap.VK_LBUTTON
# 鼠标左侧第一个键
mouseLeftMinButton = keymap.VK_XBUTTON2


# 队友 颜色 蓝色
friend_color = ColorRGBA(0, 0, 1, 1)
# 敌人 颜色 绿色
enemy_color = ColorRGBA(0, 1, 0, 1)

# 基于client.dll 进行偏移
local_player_offset = dumpsOffset.local_player  # https://csgo.dumps.host/offsets local_player
glow_object_manager_offset = dumpsOffset.glow_object_manager  # https://csgo.dumps.host/offsets glow_object_manager
entity_list_offset = dumpsOffset.entity_list - 0x10  # 0x4ddd90c + 0x10 为第一个人 # https://csgo.dumps.host/offsets entity_list - 0x10
view_matrix_offset = dumpsOffset.view_matrix  # https://csgo.dumps.host/offsets view_matrix
jump_offset = dumpsOffset.force_jump  # https://csgo.dumps.host/offsets force_jump
force_attack_offset = dumpsOffset.force_attack  # https://csgo.dumps.host/offsets force_attack

# 基于人物地址进行偏移 血量 阵营标识 辉光索引 颜色偏移 位置偏移 下蹲偏移
# 人物地址 *(client.dll + entity_list_offset + n*0x10)
entity_blood_offset = 0x100  # 血量 https://github.com/frk1/hazedumper/blob/master/csgo.hpp m_iHealth
entity_glow_index_offset = 0x10488  # 辉光索引 https://github.com/frk1/hazedumper/blob/master/csgo.hpp m_iGlowIndex
entity_camp_offset = 0xF4  # 阵营标识 https://github.com/frk1/hazedumper/blob/master/csgo.hpp m_iTeamNum
location_x_offset = 0xA0   # 位置XYZ
squat_offset = 0x110       # 下蹲值
headBoneBase_offset = 0x26A8  # 骨骼 https://github.com/frk1/hazedumper/blob/master/csgo.hpp m_dwBoneMatrix
# 基于 *(人物地址 + 0x26A8) 进行偏移
headBoneX_ofsset = 0x18C   #骨骼X

# 基于 glow_manager + entity_glow * 0x38 进行偏移
red_offset = 0x08



# 基于 server.dll 偏移 飞天
# flying_offset1 = 0xA9027C
# flying_offset2 = 0x1E4

# 基于engine.dll 偏移 准心相关偏移
view_angle_offset = dumpsOffset.client_state  # https://csgo.dumps.host/offsets client_state
# 基于 *(engine.dll + client_state_offset) 进行偏移
view_x_offset = 0x4D90  # https://github.com/frk1/hazedumper/blob/master/csgo.hpp dwClientState_ViewAngles


# 自身地址 *(clint.dll + local_player_offset) 相关的偏移
# 开镜偏移 基于*(clint.dll + local_player_offset)进行偏移
scope_offset = 0x9974  # https://github.com/frk1/hazedumper/blob/master/csgo.hpp m_bIsScoped



# 最大自瞄角度[0,360] 值越大 越离谱
max_fov = 360

# 进程模块相关
handle: pymem.Pymem = pymem.Pymem("csgo.exe")
moduleInfo = ModuleInfo(handle)

client_base = moduleInfo.client_base
server_base = moduleInfo.server_base
engine_base = moduleInfo.engine_base

# 常用变量
game_title = "Counter-Strike: Global Offensive - Direct3D 9"
