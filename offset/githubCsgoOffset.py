#  https://github.com/frk1/hazedumper/blob/master/csgo.hpp

timestamp = 1661973720  # 时间戳
#  namespace netvars #  start
cs_gamerules_data = 0x0 # cs游戏规则数据
m_ArmorValue = 0x117CC  # 护甲值 玩家地址 @@
m_Collision = 0x320 # 碰撞
m_CollisionGroup = 0x474    # 碰撞组
m_Local = 0x2FCC    # 本地
m_MoveType = 0x25C  # 移动类型
m_OriginalOwnerXuidHigh = 0x31D4    # 原原所有者 Xuid 高
m_OriginalOwnerXuidLow = 0x31D0 # 原所有者 Xuid 低
m_SurvivalGameRuleDecisionTypes = 0x1328    # 生存游戏规则决策类型
m_SurvivalRules = 0xD00 #  生存规则
m_aimPunchAngle = 0x303C    # 瞄准 打孔角度
m_aimPunchAngleVel = 0x3048 # 瞄准 打孔角度 Vel
m_angEyeAnglesX = 0x117D0   # 视角X
m_angEyeAnglesY = 0x117D4   # 视角Y
m_bBombDefused = 0x29C0 # Bool 是否拆弹
m_bBombPlanted = 0x9A5  # Bool 炸弹是否安放
m_bBombTicking = 0x2990 # Bool 炸弹是否滴答作响
m_bFreezePeriod = 0x20  # Bool 是否是冻结期
m_bGunGameImmunity = 0x9990 # Bool 枪战是否免疫
m_bHasDefuser = 0x117DC # Bool 气体是否扩散 [是否佩戴护目镜]
m_bHasHelmet = 0x117C0  # Bool 是否佩戴头盔
m_bInReload = 0x32B5    # Bool 是否在重新加载
m_bIsDefusing = 0x997C  # Bool 是否在扩散 ?
m_bIsQueuedMatchmaking = 0x74   # Bool 是否 是排队匹配
m_bIsScoped = 0x9974    # Bool 是否作用域的
m_bIsValveDS = 0x7C # Bool 是否阈值 DS
m_bSpotted = 0x93D  # Bool 是否暂停
m_bSpottedByMask = 0x980    # Bool 是否 被面具发现
m_bStartedArming = 0x3400   # Bool 开始布防
m_bUseCustomAutoExposureMax = 0x9D9 # Bool 使用自定义自动曝光最大值
m_bUseCustomAutoExposureMin = 0x9D8 # Bool 使用自定义自动曝光最小值
m_bUseCustomBloomScale = 0x9DA  # Bool 使用自定义 Bloom 比例
m_clrrender = 0x70  # char 渲染
m_dwBoneMatrix = 0x26A8 # 4 bytes 骨头矩阵
m_fAccuracyPenalty = 0x3340 # float 准确性 惩罚
m_fFlags = 0x104    # float 标志
m_flC4Blow = 0x29A0 # C4 要爆炸了
m_flCustomAutoExposureMax = 0x9E0   # 自定义自动曝光最大值
m_flCustomAutoExposureMin = 0x9DC   # 自定义自动曝光最小值
m_flCustomBloomScale = 0x9E4    # 自定义绽放规模
m_flDefuseCountDown = 0x29BC    # 炸弹拆除倒计时
m_flDefuseLength = 0x29B8   # ?
m_flFallbackWear = 0x31E0   # ?
m_flFlashDuration = 0x10470 # 闪光持续时间
m_flFlashMaxAlpha = 0x1046C # 闪光最大 透明
m_flLastBoneSetupTime = 0x2928  # 最后骨骼设置时间
m_flLowerBodyYawTarget = 0x9ADC # 下半身偏航目标
m_flNextAttack = 0x2D80 # 下一次攻击
m_flNextPrimaryAttack = 0x3248  # 下一个主要攻击
m_flSimulationTime = 0x268  # 模拟时间
m_flTimerLength = 0x29A4    # 定时器时长
m_hActiveWeapon = 0x2F08    # 正在使用的武器 ?
m_hBombDefuser = 0x29C4 # 拆弹器
m_hMyWeapons = 0x2E08   # 我的武器
m_hObserverTarget = 0x339C  # 观察者目标
m_hOwner = 0x29DC   # 所有者
m_hOwnerEntity = 0x14C  # 所有者实体
m_hViewModel = 0x3308   # 查看模型
m_iAccountID = 0x2FD8   # 帐户ID
m_iClip1 = 0x3274   # 
m_iCompetitiveRanking = 0x1A84  # 竞争排名
m_iCompetitiveWins = 0x1B88 # 竞争胜利
m_iCrosshairId = 0x11838    # 十字准线 ID
m_iDefaultFOV = 0x333C  # 默认视野
m_iEntityQuality = 0x2FBC   # 实体质量
m_iFOV = 0x31F4 # 游戏视角大小
m_iFOVStart = 0x31F8    # 视场开始
m_iGlowIndex = 0x10488  # 辉光索引
m_iHealth = 0x100   # 血量值
m_iItemDefinitionIndex = 0x2FBA # 项目定义索引
m_iItemIDHigh = 0x2FD0  # 项目 ID 高
m_iMostRecentModelBoneCounter = 0x2690  # 最新模型骨计数器
m_iObserverMode = 0x3388    # 观察者模式
m_iShotsFired = 0x103E0 # 开枪
m_iState = 0x3268   # 状态
m_iTeamNum = 0xF4   # 团队标识
m_lifeState = 0x25F # 生命状态
m_nBombSite = 0x2994    # 炸弹现场
m_nFallbackPaintKit = 0x31D8    # 后备油漆套件
m_nFallbackSeed = 0x31DC    # 后备种子
m_nFallbackStatTrak = 0x31E4    # 后备统计跟踪
m_nForceBone = 0x268C   # 强制骨骼
m_nModelIndex = 0x258   # 模式索引
m_nTickBase = 0x3440    # 刻度线
m_nViewModelIndex = 0x29D0  # 查看模式索引
m_rgflCoordinateFrame = 0x444   # 坐标系
m_szCustomName = 0x304C # 自定义名称
m_szLastPlaceName = 0x35C4  # 最后一个地名
m_thirdPersonViewAngles = 0x31E8    # 第三人称视角
m_vecOrigin = 0x138 # vec 起源?
m_vecVelocity = 0x114   # 矢量速度
m_vecViewOffset = 0x108 # 矢量视图偏移
m_viewPunchAngle = 0x3030   # view Punch Angle
m_zoomLevel = 0x33E0    # 缩放层级
#  namespace netvars #  end


#  namespace signatures  #  start
anim_overlays = 0x2990  # 动画_覆盖
clientstate_choked_commands = 0x4D30    # 客户端状态阻塞命令
clientstate_delta_ticks = 0x174 # 客户端状态_增量_滴答
clientstate_last_outgoing_command = 0x4D2C  # 客户端状态最后一次传出命令
clientstate_net_channel = 0x9C  # 客户端状态_网络_通道
convar_name_hash_table = 0x2F190    # Cvar名称哈希表

# engine.dll + 0x58CFDC [0x180]

dwClientState = 0x58CFDC    # 客户端状态
dwClientState_GetLocalPlayer = 0x180    # 客户端状态获取本地玩家
dwClientState_IsHLTV = 0x4D48   # 客户端状态_是HL TV
dwClientState_Map = 0x28C   # 客户端状态映射
dwClientState_MapDirectory = 0x188  # 客户端状态_映射目录
dwClientState_MaxPlayer = 0x388 # 客户端状态最大玩家
dwClientState_PlayerInfo = 0x52C0   # 客户端状态玩家信息
dwClientState_State = 0x108 # 客户端状态_状态
dwClientState_ViewAngles = 0x4D90   # 客户端状态_视角

# engine.dll + 0x58CFDC [0x4D90]


# client.dll + 0x4DDD91C
dwEntityList = 0x4DDD91C    # 实体列表
dwForceAttack = 0x320DE3C   # 强制攻击
dwForceAttack2 = 0x320DE48  # 强制攻击2
dwForceBackward = 0x320DDE8 # 强制后退
dwForceForward = 0x320DE6C  # 强制前进
dwForceJump = 0x52878FC #  前置跳跃
dwForceLeft = 0x320DDF4 # 强制左移
dwForceRight = 0x320DE00    # 强制右移
dwGameDir = 0x62B900    # 游戏dir
dwGameRulesProxy = 0x52FB12C    # 游戏规则代理
dwGetAllClasses = 0xDEBCAC  # 获取所有类
dwGlobalVars = 0x58CCE0 # 全局变量
dwGlowObjectManager = 0x5326640 # 发光对象管理器
dwInput = 0x522EEF0 # 输入
dwInterfaceLinkList = 0x970754  # 界面链接列表
dwLocalPlayer = 0xDC14CC    # 本地玩家
dwMouseEnable = 0xDC71D8    # 启用鼠标
dwMouseEnablePtr = 0xDC71A8 # 启用鼠标指针
dwPlayerResource = 0x320C180    # 玩家资源
dwRadarBase = 0x5212694 # 雷达基地
dwSensitivity = 0xDC7074    # 灵敏度
dwSensitivityPtr = 0xDC7048 # 灵敏度指针
dwSetClanTag = 0x8A410  # 设置氏族标签
dwViewMatrix = 0x4DCF234    # 自身矩阵
dwWeaponTable = 0x522F9B4   # 武器表
dwWeaponTableIndex = 0x326C # 武器表索引
dwYawPtr = 0xDC6E38 #  偏航指针
dwZoomSensitivityRatioPtr = 0xDCD620    # 变焦敏感度比指针
dwbSendPackets = 0xD85A2    # 发送数据包
dwppDirect3DDevice9 = 0xA6050   # Direct3D设备9
find_hud_element = 0x56F55C30   # 查找HUD元素
force_update_spectator_glow = 0x3BE47A  # 强制更新观众发光
interface_engine_cvar = 0x3EA3C # 接口_引擎_变化量
is_c4_owner = 0x3CB4E0  # IS_C4_Owner 是否持有C4
m_bDormant = 0xED   # 是否休眠
m_bIsLocalPlayer = 0x3628   # 是否是本地玩家
m_flSpawnTime = 0x103C0 # 产生时间
m_pStudioHdr = 0x2950   # 工作室 hdr
m_pitchClassPtr = 0x5212930 # 音高等级指针
m_yawClassPtr = 0xDC6E38    # 偏航类指针
model_ambient_min = 0x590054    # 模型环境平均值
set_abs_angles = 0x1E5AB0   # 设置ABS角度
set_abs_origin = 0x1E58F0   # 设置ABS来源
#  namespace signatures  #  end

