key_to_cn={
    "Difficulty" : "难度, None 或 Difficulty",
    "DayTimeSpeedRate" : "白天流逝速度倍率",
    "NightTimeSpeedRate" : "夜晚流逝速度倍率",
    "ExpRate" : "经验值倍率",
    "PalCaptureRate" : "捕捉概率倍率",
    "PalSpawnNumRate" : "帕鲁出现数量倍率",
    "PalDamageRateAttack" : "帕鲁攻击伤害倍率",
    "PalDamageRateDefense" : "帕鲁承受伤害倍率",
    "PlayerDamageRateAttack" : "玩家攻击伤害倍率",
    "PlayerDamageRateDefense" : "玩家承受伤害倍率",
    "PlayerStomachDecreaceRate" : "玩家饱食度降低倍率",
    "PlayerStaminaDecreaceRate" : "玩家耐力降低倍率",
    "PlayerAutoHPRegeneRate" : "玩家生命值自然恢复倍率",
    "PlayerAutoHpRegeneRateInSleep" : "玩家睡眠时生命恢复倍率",
    "PalStomachDecreaceRate" : "帕鲁饱食度降低倍率",
    "PalStaminaDecreaceRate" : "帕鲁耐力降低倍率",
    "PalAutoHPRegeneRate" : "帕鲁生命值自然恢复倍率",
    "PalAutoHpRegeneRateInSleep" : "帕鲁睡眠时生命恢复倍率",
    "BuildObjectDamageRate" : "对建筑物伤害倍率",
    "BuildObjectDeteriorationDamageRate" : "建筑物劣化速度倍率",
    "CollectionDropRate" : "可采集物品掉落倍率",
    "CollectionObjectHpRate" : "可采集物品生命值倍率",
    "CollectionObjectRespawnSpeedRate" : "可采集物品生成速率",
    "EnemyDropItemRate" : "敌方掉落物品倍率",
    "DeathPenalty" : "死亡惩罚，None 不掉落，Item 只掉物品不掉装备，ItemAndEquipment 掉物品和装备，All 全都掉",
    "bEnablePlayerToPlayerDamage" : "启用玩家对玩家伤害功能",
    "bEnableFriendlyFire" : "启用友军伤害功能",
    "bEnableInvaderEnemy" : "启用袭击事件功能",
    "bActiveUNKO" : "启用 UNKO 功能",
    "bEnableAimAssistPad" : "启用手柄瞄准辅助功能",
    "bEnableAimAssistKeyboard" : "启用键盘瞄准辅助功能",
    "DropItemMaxNum" : "掉落物品最大数量",
    "DropItemMaxNum_UNKO" : "掉落物品最大数量_UNKO",
    "BaseCampMaxNum" : "大本营最大数量",
    "BaseCampWorkerMaxNum" : "大本营工人最大数量",
    "DropItemAliveMaxHours" : "掉落物品存在最大时长（小时）",
    "bAutoResetGuildNoOnlinePlayers" : "自动重置没有在线玩家的公会",
    "AutoResetGuildTimeNoOnlinePlayers" : "无在线玩家时自动重置公会的时间（小时）",
    "GuildPlayerMaxNum" : "公会玩家最大数量",
    "PalEggDefaultHatchingTime" : "帕鲁蛋默认孵化时间（小时）",
    "WorkSpeedRate" : "工作速度倍率",
    "bIsMultiplay" : "是否为多人游戏",
    "bIsPvP" : "是否为 PvP 游戏",
    "bCanPickupOtherGuildDeathPenaltyDrop" : "是否可以拾取其他公会的死亡掉落物",
    "bEnableNonLoginPenalty" : "是否启用不登录惩罚",
    "bEnableFastTravel" : "是否启用快速旅行",
    "bIsStartLocationSelectByMap" : "是否通过地图选择起始位置",
    "bExistPlayerAfterLogout" : "是否在登出后保留玩家",
    "bEnableDefenseOtherGuildPlayer" : "是否启用对其他公会玩家的防御",
    "CoopPlayerMaxNum" : "合作玩家最大数量",
    "ServerPlayerMaxNum" : "服务器玩家最大数量",
    "ServerName" : "服务器名称",
    "ServerDescription" : "服务器描述",
    "AdminPassword" : "管理员密码",
    "ServerPassword" : "服务器密码",
    "PublicPort" : "公共端口",
    "PublicIP" : "服务器IP",
    "RCONEnabled" : "是否启用RCON",
    "RCONPort" : "RCON端口",
    "Region" : "地区",
    "bUseAuth" : "使用授权",
    "BanListURL" : "封禁玩家名单"
}

cn_to_key = {v: k for k, v in key_to_cn.items()}

key_to_cn = dict(key_to_cn)
cn_to_key = dict(cn_to_key)

