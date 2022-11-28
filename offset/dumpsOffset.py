# https://csgo.dumps.host/offsets


client_state = 0x59f194
client_state_generic_precache_table = 0x52a4
client_state_signon_state = 0x108
entity_list = 0x4dfce74
force_attack = 0x322ac7c
force_attack2 = 0x322ac88
force_backward = 0x322acb8
force_forward = 0x322acac
force_jump = 0x52b8bfc
force_left = 0x322acc4
force_right = 0x322acd0
gamerules_proxy = 0x532c42c
global_vars = 0x59ee58
glow_object_manager = 0x5357948
input = 0x525a448
local_player = 0xde7964
player_resource = 0x3229020
radar_base = 0x523394c
view_matrix = 0x4dedca4
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