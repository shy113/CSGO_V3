# class Hello:
#     def __init__(self):
#         self.w = 0
#         self.set_w()
#
#     def set_w(self):
#         self.w = 100
#
#
# hello = Hello()
#
# print(f"{hello.w}")


# import requests
#
# api = 'https://csgo.dumps.host/api/offset'
#
# proxies = {
#     'http': '120.236.128.201:8060',
#     'https': '120.236.128.201:8060'
# }
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50'
# }
#
# params = {'key': 'd41d8cd98f00b204e9800998ecf8427e',
#           'name': 'local_player'}
# tmp = requests.get('https://csgo.dumps.host/api/offset', params=params, headers=headers,verify=False)
#
# print()
# import pyautogui
# import win32con as keymap
# from win32api import GetAsyncKeyState
# import time,datetime
# def key_pressed(key):
#     state = GetAsyncKeyState(key)
#     if state == -32768:
#         return True
#
# def key_down(key):
#     state = GetAsyncKeyState(key)
#     if state == -32768:
#         print("按下且未抬起"+datetime.datetime.now())
#
#
#
# # t = keymap.VK_XBUTTON2
# t = keymap.VK_XBUTTON2
#
# while True:
#     if key_pressed(t):
#         pyautogui.click()
#
#     # key_down(t)


# !/bin/python
# from pymouse import PyMouse
import time

# k = ('左', '右', '中')
# m = PyMouse()
# t = int(input('输入点击总次数（0=不限制，慎用！）：'))
# if (t == 0):
#     print('[W]您设定了不限制，您需要考虑您是否有办法关闭它！')
# d = float(input('输入两次点击之间的间隔（单位为秒，可以为0）：'))
# if (d < 0.005):
#     print('[W]您设定的间隔很小，您需要考虑您的计算机或要点击的东西是否可以承受它。')
# p = int(input('点击的键（1=左键，2=右键，3=中键）：'))
# print('[I]全部设置完毕！')
# print('[I]你有5秒的时间移动鼠标到想要连点的地方或关闭点击器。')
# for i in range(5):
#     print('[I]剩余', 5 - i, 'S')
#     time.sleep(1)
# print('[I]Start to click.')
# s = time.time()
# i = 0
# while (i < t or t == 0):
#     m.click(m.position()[0], m.position()[1], p)
#     i = i + 1
#     # print('[D]TIME =',time.asctime(time.localtime(time.time())),' ','POSITION =',m.position(),' ','TOTAL =',i) #中二装B疯狂输出模式。
#     time.sleep(d)
# e = time.time()
# print('[S]点击', k[p - 1], '键', t, '次，点击间隔为', d, '的任务成功结束，共用时约', round(e - s, 2), '秒，平均每秒约点击', round(t / (e - s), 2),
#       '次。')


import pymem.process
import win32con as keymap
import re
from pymem import Pymem
from win32api import GetAsyncKeyState


class ColorRGBA:
    def __init__(self, r, g, b, a):
        self.Red = r
        self.Green = g
        self.Blue = b
        self.Alpha = a


exit_hack = keymap.VK_END
show_teammate = keymap.VK_F2
glow_toggle = keymap.VK_F3
enemy_color = ColorRGBA(0, 1, 0, 1)
teammate_color = ColorRGBA(0, 0, 1, 1)


def key_pressed(key):
    return GetAsyncKeyState(key) & 1 == 1


def glow(h_game: pymem, red_offset, glow_manager, entity_glow, color: ColorRGBA):
    w_glow = glow_manager + entity_glow * 0x38 + red_offset
    h_game.write_float(w_glow, float(color.Red))
    h_game.write_float(w_glow + 0x4, float(color.Green))
    h_game.write_float(w_glow + 0x8, float(color.Blue))
    h_game.write_float(w_glow + 0xc, float(color.Alpha))
    h_game.write_uchar(w_glow + 0x20, 1)
    h_game.write_uchar(w_glow + 0x21, 0)


def main():
    b_glow_teammate = False
    b_glow = True

    handle: Pymem = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(handle.process_handle, "client.dll")
    client_base = client.lpBaseOfDll
    client_module = handle.read_bytes(client_base, client.SizeOfImage)

    # If this part failed, please remind me to update the pattern.
    # ----------------------------------------------------------------------------------------------
    loc_entity_list_pattern = re.search(rb'\x42\x56\x8d\x34\x85.{4}', client_module).start()
    local_ptr_4 = client_base + loc_entity_list_pattern + 5
    local_addr = handle.read_uint(local_ptr_4) + 4
    entity_list_addr = client_base + loc_entity_list_pattern + 0x20 + 1

    glow_manger_addr = client_base + re.search(rb'\x0f\x11\x05.{4}\x83\xc8\x01', client_module).start() + 3
    glow_index_addr = client_base + re.search(rb'\x8B\x7d\xec\x8b\xb3.{4}', client_module).start() + 5
    glow_red_addr = client_base + re.search(rb'\x8b\x00\xf3\x0f\x11\x44\xc8.\xf3\x0f\x10\x44\x24', client_module).start() + 7

    health_addr = client_base + re.search(rb'\x83\xb9.{4}\x00\x7f\x2d\x8b\x01', client_module).start() + 2
    team_addr = client_base + re.search(rb'\xcc\x8b\x89.{4}\xe9.{4}\xcc', client_module).start() + 3
    # ----------------------------------------------------------------------------------------------

    glow_manager_ptr = handle.read_uint(glow_manger_addr)
    entity_list_ptr = handle.read_uint(entity_list_addr)
    m_glow_index = handle.read_uint(glow_index_addr)
    m_health = handle.read_uint(health_addr)
    m_team = handle.read_uint(team_addr)
    red_offset = handle.read_uchar(glow_red_addr)
    print("Glow has launched.")
    print("Press F1 to show teammates.")
    print("Press F2 to turn the glow on/off.")
    print("Press END to quit.")
    try:
        while True:
            glow_manager = handle.read_uint(glow_manager_ptr)
            if key_pressed(exit_hack):
                break
            if key_pressed(show_teammate):
                b_glow_teammate = not b_glow_teammate
                print("Team glow is " + ("on" if b_glow_teammate is True else "off"))
            if key_pressed(glow_toggle):
                b_glow = not b_glow
                print("Glow is " + ("on" if b_glow is True else "off"))

            local_player_ent = handle.read_uint(local_addr)
            if local_player_ent:
                local_team = handle.read_uint(local_player_ent + m_team)
                if b_glow:
                    for i in range(1, 32):
                        entity = handle.read_uint(entity_list_ptr + i * 0x10)
                        if entity:
                            entity_team = handle.read_uint(entity + m_team)
                            if not b_glow_teammate:
                                if entity_team == local_team:
                                    continue
                            entity_glow = handle.read_uint(entity + m_glow_index)

                            if entity_team == local_team:
                                glow(handle, red_offset, glow_manager, entity_glow, teammate_color)
                            else:
                                ent_health = handle.read_uint(entity + m_health)
                                enemy_color.Green = 0.006 * ent_health
                                if ent_health == 0x64:
                                    enemy_color.Green = 1
                                enemy_color.Red = 1.0 - enemy_color.Green
                                glow(handle, red_offset, glow_manager, entity_glow, enemy_color)

    finally:
        handle.close_process()


if __name__ == '__main__':
    main()