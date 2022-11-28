# https://csgo.dumps.host/offsets

client_state = 0x59f194
client_state_generic_precache_table = 0x52a4
client_state_signon_state = 0x108
entity_list = 0x4dfbe54
force_attack = 0x3229cbc
force_attack2 = 0x3229cc8
force_backward = 0x3229c68
force_forward = 0x3229cec
force_jump = 0x52b7bdc
force_left = 0x3229c74
force_right = 0x3229c80
gamerules_proxy = 0x532b40c
global_vars = 0x59ee58
glow_object_manager = 0x5356910
input = 0x5259428
local_player = 0xde6964
player_resource = 0x3228000
radar_base = 0x523292c
view_matrix = 0x4decc84
send_packets = 0xdcf92
direct3d_device9 = 0xa62c0
studio_hdr = 0x2950
dormant = 0xed
engine_build_number = 0x38eb054



'''
view_matrix # 矩阵 client.dll + view_matrix
radar_base # 小地图 client.dll + radar_base
studio_hdr # 高动态渲染 视觉更好
dormant # 休眠标志位 基于人物地址 偏移 休眠是人物的位置信息不会更新
'''