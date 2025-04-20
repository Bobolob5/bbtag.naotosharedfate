@Subroutine
def PreInit():
    CharacterID('pna')


@Subroutine
def MatchInit():
    Health(16000)
    AirBDashDuration(13)
    AirBDashGravity(-1800)
    FootstepType(1)
    FootstepSE(1)
    CreateDecalOn(1)
    Unknown30093(1, 5, 36, 0, 0)
    Unknown3060(0, 'vr_layer1')
    Unknown3061(0, 5)
    Unknown3063(0, 65000)
    Unknown3062(0, 100000)

    @StateRegister
    def AutoFDash(INPUT_0x0):
        Unknown14009(6)
        Move_AirGround_(0x2000)
        Move_Input_(INPUT_0x78)
        StateCall('CmnActFDash')

    @StateRegister
    def KamaeCancel(INPUT_SPECIALMOVE):
        FollowupOnly(1)
        Move_Input_(INPUT_0x5f)

    @StateRegister
    def KamaeEX(INPUT_SPECIALMOVE):
        FollowupOnly(1)
        Move_Input_(INPUT_66)

    @StateRegister
    def NmlAtk5A(INPUT_0x7):
        MoveMaxChainRepeat(3)
        DamageStunPriority(2000)
        SkillEstimateRange(0, 400000, -117000, 143000, 1000, 50)

    @StateRegister
    def NmlAtk4A(INPUT_0x6):
        MoveMaxChainRepeat(3)
        SkillEstimateRange(-3000, 250000, -200000, 127000, 1000, 50)

    @StateRegister
    def NmlAtk4A2nd(INPUT_0x6):
        MoveMaxChainRepeat(1)
        FollowupOnly(1)
        GuardStunPriority(2000)
        DamageStunPriority(2000)
        SkillEstimateRange(0, 350000, -200000, 150000, 1000, 50)

    @StateRegister
    def NmlAtk4A3rd(INPUT_0x6):
        MoveMaxChainRepeat(1)
        FollowupOnly(1)
        GuardStunPriority(2000)
        DamageStunPriority(2000)
        SkillEstimateRange(0, 350000, -200000, 150000, 1000, 50)

    @StateRegister
    def NmlAtk4A4th(INPUT_0x1):
        FollowupOnly(1)
        MoveMaxChainRepeat(1)
        Move_Input_(INPUT_0x5e)
        Move_Input_(INPUT_PRESS_A)
        StateCall('NmlAtk5A4th')
        SkillEstimateRange(0, 350000, -200000, 250000, 1000, 50)

    @StateRegister
    def NmlAtk5A2nd(INPUT_0x7):
        FollowupOnly(1)
        MoveMaxChainRepeat(1)
        GuardStunPriority(2000)
        DamageStunPriority(2000)
        SkillEstimateRange(0, 450000, -200000, 150000, 1000, 50)

    @StateRegister
    def NmlAtk5A3rd(INPUT_0x7):
        FollowupOnly(1)
        MoveMaxChainRepeat(1)
        GuardStunPriority(2000)
        DamageStunPriority(2000)
        SkillEstimateRange(0, 450000, -200000, 150000, 1000, 50)

    @StateRegister
    def NmlAtk5A4th(INPUT_0x7):
        FollowupOnly(1)
        MoveMaxChainRepeat(1)
        GuardStunPriority(100)
        DamageStunPriority(2000)
        SkillEstimateRange(0, 450000, -200000, 150000, 1000, 50)

    @StateRegister
    def NmlAtk2A(INPUT_0x4):
        SharedGatling('NmlAtk4A')
        MoveLow()
        SkillEstimateRange(6000, 213000, -100000, 100000, 1000, 50)

    @StateRegister
    def NmlAtk5B(INPUT_0x19):
        MoveMaxChainRepeat(1)
        SkillEstimateRange(-67000, 467000, -81000, 212000, 1000, 50)

    @StateRegister
    def NmlAtk5B2nd(INPUT_0x19):
        FollowupOnly(1)
        MoveMaxChainRepeat(1)
        GuardStunPriority(2000)
        DamageStunPriority(2000)
        SkillEstimateRange(-67000, 550000, -81000, 212000, 1000, 50)

    @StateRegister
    def NmlAtk5B3rd(INPUT_0x19):
        FollowupOnly(1)
        MoveMaxChainRepeat(1)
        SkillEstimateRange(-67000, 650000, -81000, 212000, 1000, 50)

    @StateRegister
    def NmlAtk2B(INPUT_0x16):
        MoveMaxChainRepeat(1)
        SkillEstimateRange(0, 400000, -58000, 450000, 500, 50)

    @StateRegister
    def CmnActCrushAttack(INPUT_0x66):
        MoveMid()
        SkillEstimateRange(20000, 430000, -219000, -66000, 1000, 10)
        OpponentAttackPriority(0)

    @StateRegister
    def NmlAtk2C(INPUT_0x28):
        MoveLow()
        AirborneOpponentPriority(1)
        SkillEstimateRange(-10000, 400000, -100000, 100000, 1000, 50)

    @StateRegister
    def CmnActChangePartnerQuickOut(INPUT_0x63):
        pass

    @StateRegister
    def NmlAtkAIR5A(INPUT_0x10):
        SkillEstimateRange(0, 300000, -200000, 200000, 1000, 50)

    @StateRegister
    def NmlAtkAIR5A2nd(INPUT_0x10):
        FollowupOnly(1)
        MoveMaxChainRepeat(3)

    @StateRegister
    def NmlAtkAIR5A2ndex(INPUT_0x22):
        FollowupOnly(1)
        MoveMaxChainRepeat(3)
        StateCall('NmlAtkAIR5A2nd')

    @StateRegister
    def NmlAtkAIR5B(INPUT_0x22):
        SkillEstimateRange(-1000, 446000, -250000, 350000, 1000, 50)

    @StateRegister
    def NmlAtkAIR5C(INPUT_0x34):
        DamageStunPriority(2000)
        SkillEstimateRange(233000, 1000000, -143000, 150000, 750, 50)

    @StateRegister
    def NmlAtkThrow(INPUT_0x5d):
        MoveThrow()
        AirborneOpponentPriority(1)
        DamageStunPriority(1)
        SkillEstimateRange(0, 350000, -200000, 200000, 1000, 0)

    @StateRegister
    def NmlAtkBackThrow(INPUT_0x61):
        MoveThrow()
        AirborneOpponentPriority(1)
        DamageStunPriority(1)
        SkillEstimateRange(0, 350000, -200000, 200000, 1000, 0)

    @StateRegister
    def NmlAtk5A3rdEx(INPUT_0x1):
        FollowupOnly(1)
        Move_Input_(INPUT_PRESS_A)
        StateCall('NmlAtk5A3rd')
        SharedGatling('NmlAtk5A3rd')
        Unknown15000(0)

    @StateRegister
    def NmlAtk5A4thEx(INPUT_0x1):
        FollowupOnly(1)
        Move_Input_(INPUT_PRESS_A)
        StateCall('NmlAtk5A4th')
        SharedGatling('NmlAtk5A4th')
        Unknown15000(0)

    @StateRegister
    def NmlAtk5BEx(INPUT_0x1):
        FollowupOnly(1)
        Move_Input_(INPUT_PRESS_B)
        StateCall('NmlAtk5B')
        SharedGatling('NmlAtk5B')
        Unknown15000(0)

    @StateRegister
    def NmlAtk2BEx(INPUT_0x1):
        FollowupOnly(1)
        Move_Input_(INPUT_PRESS_B)
        Move_Input_(INPUT_0x45)
        StateCall('NmlAtk2B')
        SharedGatling('NmlAtk2B')
        Unknown15000(0)

    @StateRegister
    def CmnActCrushAttackEx(INPUT_0x1):
        FollowupOnly(1)
        Move_Input_(INPUT_PRESS_C)
        StateCall('CmnActCrushAttack')
        SharedGatling('CmnActCrushAttack')
        Unknown15000(0)

    @StateRegister
    def NmlAtk2CEx(INPUT_0x1):
        FollowupOnly(1)
        Move_Input_(INPUT_PRESS_C)
        Move_Input_(INPUT_0x45)
        StateCall('NmlAtk2C')
        SharedGatling('NmlAtk2C')
        Unknown15000(0)

    @StateRegister
    def AN_NmlAtkThrowEX(INPUT_0x1):
        Move_Input_(INPUT_0xd3)
        FollowupOnly(1)
        StateCall('NmlAtkThrow')
        SharedGatling('NmlAtkThrow')
        Unknown15000(0)

    @StateRegister
    def AN_NmlAtkBackThrowEX(INPUT_0x1):
        Move_Input_(INPUT_0xd3)
        FollowupOnly(1)
        StateCall('NmlAtkBackThrow')
        SharedGatling('NmlAtkBackThrow')
        Unknown15000(0)

    @StateRegister
    def KamaeA(INPUT_SPECIALMOVE):
        Move_AirGround_(0x2000)
        Move_Input_(INPUT_236)
        Move_Input_(INPUT_PRESS_A)
        SkillEstimateRange(707000, 1466000, -223000, 355000, 10, 10)

    @StateRegister
    def KamaeCancelA_EX(INPUT_SPECIALMOVE):
        FollowupOnly(1)
        Move_AirGround_(0x2000)
        Move_Input_(INPUT_236)
        Move_Input_(INPUT_PRESS_A)
        Unknown14024('KamaeCancelcheck')
        Unknown15000(0)
        Unknown15003(0)

    @StateRegister
    def ShagekiA(INPUT_SPECIALMOVE):
        FollowupOnly(1)
        Move_AirGround_(0x2000)
        Move_Input_(INPUT_HOLD_A)
        SkillEstimateRange(507000, 1466000, -223000, 355000, 2000, 50)
        Unknown15016(0, 100, 1000)

    @StateRegister
    def ShagekiB(INPUT_SPECIALMOVE):
        FollowupOnly(1)
        Move_AirGround_(0x2000)
        Move_Input_(INPUT_HOLD_B)
        SkillEstimateRange(507000, 1466000, 77000, 655000, 100, 50)
        Unknown15016(1, 100, 1000)

    @StateRegister
    def ShagekiC(INPUT_SPECIALMOVE):
        FollowupOnly(1)
        Move_AirGround_(0x2000)
        Move_Input_(INPUT_HOLD_C)
        SkillEstimateRange(507000, 1466000, 77000, 655000, 100, 50)
        Unknown15016(2, 100, 1000)

    @StateRegister
    def BanditRevolverB(INPUT_SPECIALMOVE):
        Move_AirGround_(0x2000)
        Move_Input_(INPUT_236)
        Move_Input_(INPUT_PRESS_B)
        SkillEstimateRange(-90000, 666000, -207000, 285000, 100, 50)

    @StateRegister
    def WalkingShotEX(INPUT_SPECIALMOVE):
        Move_AirGround_(0x2000)
        Move_Input_(INPUT_236)
        Move_Input_(INPUT_PRESS_C)
        Move_AirGround_(0x3086)
        SkillEstimateRange(7000, 1466000, -123000, 255000, 1000, 50)
        Unknown15000(0)

    @StateRegister
    def WalkingShotKickEX(INPUT_SPECIALMOVE):
        FollowupOnly(1)
        Move_AirGround_(0x2000)
        Move_Input_(INPUT_PRESS_C)
        SkillEstimateRange(-173000, 286000, -123000, 255000, 1000, 50)
        OpponentAttackPriority(3000)

    @StateRegister
    def TrapA(INPUT_SPECIALMOVE):
        Move_AirGround_(0x2000)
        Move_Input_(INPUT_214)
        Move_Input_(INPUT_PRESS_A)
        SkillEstimateRange(707000, 1466000, -223000, 355000, 10, 10)

    @StateRegister
    def TrapB(INPUT_SPECIALMOVE):
        Move_AirGround_(0x2000)
        Move_Input_(INPUT_214)
        Move_Input_(INPUT_PRESS_B)
        SkillEstimateRange(707000, 1466000, -223000, 355000, 10, 10)

    @StateRegister
    def TrapEX(INPUT_SPECIALMOVE):
        Move_AirGround_(0x2000)
        Move_Input_(INPUT_214)
        Move_Input_(INPUT_PRESS_C)
        Move_AirGround_(0x3086)
        SkillEstimateRange(707000, 1466000, -223000, 355000, 10, 10)

    @StateRegister
    def AirBanditRevolverA(INPUT_SPECIALMOVE):
        Move_AirGround_(0x2001)
        Move_Input_(INPUT_236)
        Move_Input_(INPUT_PRESS_A)
        SkillEstimateRange(-3000, 560000, -158000, 170000, 100, 50)

    @StateRegister
    def AirBanditRevolverB(INPUT_SPECIALMOVE):
        Move_AirGround_(0x2001)
        Move_Input_(INPUT_236)
        Move_Input_(INPUT_PRESS_B)
        SkillEstimateRange(-90000, 666000, -207000, 285000, 100, 50)

    @StateRegister
    def AirBanditRevolverEX(INPUT_SPECIALMOVE):
        Move_AirGround_(0x2001)
        Move_Input_(INPUT_236)
        Move_Input_(INPUT_PRESS_C)
        Move_AirGround_(0x3086)
        SkillEstimateRange(310000, 1066000, -207000, 285000, 100, 50)

    @StateRegister
    def AirTrapA(INPUT_SPECIALMOVE):
        Move_AirGround_(0x2001)
        Move_Input_(INPUT_214)
        Move_Input_(INPUT_PRESS_A)
        SkillEstimateRange(707000, 1466000, -223000, 355000, 10, 10)

    @StateRegister
    def AirTrapB(INPUT_SPECIALMOVE):
        Move_AirGround_(0x2001)
        Move_Input_(INPUT_214)
        Move_Input_(INPUT_PRESS_B)
        SkillEstimateRange(707000, 1466000, -223000, 355000, 10, 10)

    @StateRegister
    def AirTrapEX(INPUT_SPECIALMOVE):
        Move_AirGround_(0x2001)
        Move_Input_(INPUT_214)
        Move_Input_(INPUT_PRESS_C)
        Move_AirGround_(0x3086)
        SkillEstimateRange(707000, 1466000, -223000, 355000, 10, 10)

    @StateRegister
    def BanditRevolverB_EX(INPUT_SPECIALMOVE):
        Move_Input_(INPUT_236)
        Move_Input_(INPUT_PRESS_B)
        FollowupOnly(1)
        StateCall('BanditRevolverB')
        Unknown15000(0)

    @StateRegister
    def WalkingShotEX_EX(INPUT_SPECIALMOVE):
        Move_Input_(INPUT_236)
        Move_Input_(INPUT_PRESS_C)
        Move_AirGround_(0x3086)
        FollowupOnly(1)
        StateCall('WalkingShotEX')
        Unknown15000(0)

    @StateRegister
    def TrapA_EX(INPUT_SPECIALMOVE):
        Move_Input_(INPUT_214)
        Move_Input_(INPUT_PRESS_A)
        FollowupOnly(1)
        StateCall('TrapA')
        Unknown15000(0)

    @StateRegister
    def TrapB_EX(INPUT_SPECIALMOVE):
        Move_Input_(INPUT_214)
        Move_Input_(INPUT_PRESS_B)
        FollowupOnly(1)
        StateCall('TrapB')
        Unknown15000(0)

    @StateRegister
    def TrapEX_EX(INPUT_SPECIALMOVE):
        Move_Input_(INPUT_214)
        Move_Input_(INPUT_PRESS_C)
        Move_AirGround_(0x3086)
        FollowupOnly(1)
        StateCall('TrapEX')
        Unknown15000(0)

    @StateRegister
    def CmnActInvincibleAttack(INPUT_0x64):
        Unknown15006(0)
        DamageStunPriority(0)
        GuardStunPriority(0)
        OpponentAttackPriority(6000)
        Unknown15020(500, 1000, 100, 1000)
        SkillEstimateRange(-3000, 204000, -91000, 127000, 250, 5)

    @StateRegister
    def SecretGunA(INPUT_0x68):
        Move_AirGround_(0x2000)
        Move_AirGround_(0x3089)
        Move_Input_(INPUT_236)
        Move_Input_(INPUT_0xde)
        SkillEstimateRange(307000, 1466000, -223000, 355000, 200, 50)
        Unknown15022(3, 5, 50, 1000)

    @StateRegister
    def SecretGunB(INPUT_0x68):
        Move_AirGround_(0x2001)
        Move_AirGround_(0x3089)
        Move_Input_(INPUT_236)
        Move_Input_(INPUT_0xde)
        SkillEstimateRange(307000, 1466000, -223000, 355000, 10, 10)
        Unknown15022(3, 5, 50, 1000)

    @StateRegister
    def SecretGunOD(INPUT_0x68):
        Move_AirGround_(0x3089)
        Move_AirGround_(0x3081)
        Move_Input_(INPUT_236)
        Move_Input_(INPUT_0xde)
        SkillEstimateRange(307000, 1466000, -223000, 355000, 10, 10)
        Unknown15022(3, 5, 50, 1000)

    @StateRegister
    def UltimateKill(INPUT_0x68):
        Move_AirGround_(0x2000)
        Move_AirGround_(0x3089)
        Move_Input_(INPUT_214)
        Move_Input_(INPUT_0xde)
        Unknown15000(0)
        SkillEstimateRange(342000, 861000, -198000, 116000, 10, 10)
        Unknown15022(3, 5, 50, 1000)

    @StateRegister
    def UltimateKillOD(INPUT_0x68):
        Move_AirGround_(0x2000)
        Move_AirGround_(0x3089)
        Move_AirGround_(0x3081)
        Move_Input_(INPUT_214)
        Move_Input_(INPUT_0xde)
        Unknown15000(0)
        SkillEstimateRange(342000, 861000, -198000, 116000, 10, 10)
        Unknown15022(3, 5, 50, 1000)

    @StateRegister
    def UltimateKillAir(INPUT_0x68):
        Move_AirGround_(0x2001)
        Move_AirGround_(0x3089)
        Move_Input_(INPUT_214)
        Move_Input_(INPUT_0xde)
        Unknown15000(0)
        SkillEstimateRange(233000, 1007000, -143000, 150000, 100, 50)
        Unknown15022(3, 5, 50, 1000)

    @StateRegister
    def UltimateKillAirOD(INPUT_0x68):
        Move_AirGround_(0x2001)
        Move_AirGround_(0x3089)
        Move_AirGround_(0x3081)
        Move_Input_(INPUT_214)
        Move_Input_(INPUT_0xde)
        Unknown15000(0)
        SkillEstimateRange(233000, 1007000, -143000, 150000, 100, 50)
        Unknown15022(3, 5, 50, 1000)

    @StateRegister
    def SecretGunB_EX(INPUT_0x68):
        Move_AirGround_(0x3089)
        Move_Input_(INPUT_236)
        Move_Input_(INPUT_0xde)
        FollowupOnly(1)
        StateCall('SecretGunB')
        Unknown15000(0)

    @StateRegister
    def SecretGunOD_EX(INPUT_0x68):
        Move_AirGround_(0x3089)
        Move_AirGround_(0x3081)
        Move_Input_(INPUT_236)
        Move_Input_(INPUT_0xde)
        FollowupOnly(1)
        StateCall('SecretGunOD')
        Unknown15000(0)

    @StateRegister
    def UltimateKill_EX(INPUT_0x68):
        Move_AirGround_(0x3089)
        Move_Input_(INPUT_214)
        Move_Input_(INPUT_0xde)
        FollowupOnly(1)
        StateCall('UltimateKill')
        Unknown15000(0)

    @StateRegister
    def UltimateKillOD_EX(INPUT_0x68):
        Move_AirGround_(0x3089)
        Move_AirGround_(0x3081)
        Move_Input_(INPUT_214)
        Move_Input_(INPUT_0xde)
        FollowupOnly(1)
        StateCall('UltimateKillOD')
        Unknown15000(0)

    @StateRegister
    def AstralHeat(INPUT_0x69):
        Move_AirGround_(0x304a)
        Move_AirGround_(0x2000)
        Move_Input_(INPUT_222)
        Move_Input_(INPUT_0xde)
        OpponentAttackPriority(3000)
        DamageStunPriority(3000)
        SkillEstimateRange(-350000, 850000, -200000, 100000, 1000, 50)
    TempPriorityMultiplier('NmlAtk5A', 'NmlAtk5A2nd', 10000000)
    TempPriorityMultiplier('NmlAtk5A2nd', 'NmlAtk5A3rd', 10000000)
    TempPriorityMultiplier('NmlAtk5A3rd', 'NmlAtk5A4th', 10000000)
    TempPriorityMultiplier('NmlAtk4A', 'NmlAtk4A2nd', 10000000)
    TempPriorityMultiplier('NmlAtk4A2nd', 'NmlAtk4A3rd', 10000000)
    TempPriorityMultiplier('NmlAtk4A3rd', 'NmlAtk5A3rd', 10000000)
    TempPriorityMultiplier('NmlAtk2A', 'NmlAtk5A', 10000000)
    TempPriorityMultiplier('NmlAtk2A', 'NmlAtk2C', 10000000)
    TempPriorityMultiplier('NmlAtk2B', 'FJump', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk5B2nd', 10000000)
    TempPriorityMultiplier('NmlAtk5B2nd', 'NmlAtk5B3rd', 10000000)
    TempPriorityMultiplier('NmlAtk5B3rd', 'NmlAtk2B', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5A', 'NmlAtkAIR5A2nd', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5B', 'FJump', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5C', 'FJump', 10000000)
    CommonVoicelines(0, 'pna000')
    CommonVoicelines(1, 'pna001')
    CommonVoicelines(2, 'pna002')
    CommonVoicelines(3, 'pna003')
    CommonVoicelines(4, 'pna004')
    CommonVoicelines(5, 'pna005')
    CommonVoicelines(6, 'pna006')
    CommonVoicelines(7, 'pna007')
    CommonVoicelines(8, 'pna008')
    CommonVoicelines(9, 'pna009')
    CommonVoicelines(10, 'pna010')
    CommonVoicelines(15, 'pna015')
    CommonVoicelines(16, 'pna016')
    CommonVoicelines(17, 'pna017')
    CommonVoicelines(18, 'pna018')
    CommonVoicelines(19, 'pna019')
    CommonVoicelines(20, 'pna020')
    CommonVoicelines(21, 'pna021')
    CommonVoicelines(22, 'pna022')
    CommonVoicelines(23, 'pna023')
    CommonVoicelines(24, 'pna024')
    CommonVoicelines(25, 'pna025')
    CommonVoicelines(28, 'pna028')
    CommonVoicelines(29, 'pna029')
    CommonVoicelines(30, 'pna030')
    CommonVoicelines(31, 'pna031')
    CommonVoicelines(32, 'pna032')
    CommonVoicelines(33, 'pna033')
    CommonVoicelines(34, 'pna034')
    CommonVoicelines(35, 'pna035')
    CommonVoicelines(36, 'pna036')
    CommonVoicelines(37, 'pna037')
    CommonVoicelines(39, 'pna039')
    CommonVoicelines(42, 'pna042')
    CommonVoicelines(43, 'pna043')
    CommonVoicelines(44, 'pna044')
    CommonVoicelines(45, 'pna045')
    CommonVoicelines(46, 'pna046')
    CommonVoicelines(47, 'pna047')
    CommonVoicelines(48, 'pna048')
    CommonVoicelines(49, 'pna049')
    CommonVoicelines(50, 'pna050')
    CommonVoicelines(52, 'pna052')
    CommonVoicelines(53, 'pna053')
    CommonVoicelines(54, 'pna100_0')
    CommonVoicelines(55, 'pna100_1')
    CommonVoicelines(56, 'pna100_2')
    CommonVoicelines(63, 'pna101_0')
    CommonVoicelines(64, 'pna101_1')
    CommonVoicelines(65, 'pna101_2')
    CommonVoicelines(57, 'pna102_0')
    CommonVoicelines(58, 'pna102_1')
    CommonVoicelines(59, 'pna102_2')
    CommonVoicelines(66, 'pna103_0')
    CommonVoicelines(67, 'pna103_1')
    CommonVoicelines(68, 'pna103_2')
    CommonVoicelines(60, 'pna104_0')
    CommonVoicelines(61, 'pna104_1')
    CommonVoicelines(62, 'pna104_2')
    CommonVoicelines(69, 'pna105_0')
    CommonVoicelines(70, 'pna105_1')
    CommonVoicelines(71, 'pna105_2')
    CommonVoicelines(72, 'pna150')
    CommonVoicelines(73, 'pna151')
    CommonVoicelines(74, 'pna152')
    CommonVoicelines(85, 'pna153')
    CommonVoicelines(87, 'pna154')
    CommonVoicelines(88, 'pna155')
    CommonVoicelines(96, 'pna161_0')
    CommonVoicelines(97, 'pna161_1')
    CommonVoicelines(92, 'pna162_0')
    CommonVoicelines(93, 'pna162_1')
    CommonVoicelines(98, 'pna163_0')
    CommonVoicelines(99, 'pna163_1')
    CommonVoicelines(100, 'pna164_0')
    CommonVoicelines(101, 'pna164_1')
    CommonVoicelines(105, 'pna165_0')
    CommonVoicelines(106, 'pna165_1')
    CommonVoicelines(102, 'pna166_0')
    CommonVoicelines(103, 'pna166_1')
    CommonVoicelines(90, 'pna167_0')
    CommonVoicelines(91, 'pna167_1')
    CommonVoicelines(107, 'pna168_0')
    CommonVoicelines(108, 'pna168_1')
    CommonVoicelines(110, 'pna169_0')
    CommonVoicelines(111, 'pna169_1')
    CommonVoicelines(112, 'pna159_0')
    CommonVoicelines(113, 'pna159_1')
    CommonVoicelines(94, 'pna400_0')
    CommonVoicelines(95, 'pna400_1')
    HitSprites(0, 'na060_00')
    HitSprites(1, 'na060_01')
    HitSprites(2, 'na060_02')
    HitSprites(3, 'na060_03')
    HitSprites(4, 'na060_04')
    HitSprites(5, 'na060_05')
    HitSprites(6, 'na060_06')
    HitSprites(7, 'na041_02')
    HitSprites(8, 'na040_02')
    HitSprites(9, 'na045_02')
    HitSprites(10, 'na060_00')
    HitSprites(11, 'na060_01')
    HitSprites(12, 'na060_03')
    HitSprites(13, 'na060_05')
    HitSprites(14, 'na060_07')
    HitSprites(15, 'na125_00')
    HitSprites(16, 'na050_00')
    HitSprites(17, 'na052_00')
    HitSprites(18, 'na054_00')
    HitSprites(25, 'na063_00')
    HitSprites(26, 'na063_01')
    HitSprites(27, 'na063_02')
    HitSprites(28, 'na063_05')
    HitSprites(29, 'na060_12')
    HitSprites(24, 'na072_03')
    Unknown30036('PNA_PersonaCreate', -1, 38)
    sendToLabel(1)
    Unknown23003(0, 1, 1, 1, 300, 0, -49152, -65281)
    Unknown23008(0, 0)
    Unknown12059(0, 'CmnActInvincibleAttack')
    Unknown12059(1, 'NmlAtk4A')
    Unknown12059(2, 'SecretGunA')
    Unknown12059(3, 'SecretGunOD')
    Unknown12059(4, 'UltimateKill')
    Unknown12059(5, 'UltimateKillOD')
    Unknown12059(6, 'CmnActBDash')
    Unknown12059(7, 'NmlAtkThrow')
    Unknown12059(8, 'CmnActChangePartnerQuickOut')


@Subroutine
def MatchInit2():
    callSubroutine('CheckDeathCounterTraining')


@Subroutine
def CheckDeathCounterTraining():
    if SLOT_91:
        TrainingModeSLOT('TRI_PNADeathFlg', SLOT_67)
        if SLOT_67 == 1:
            SLOT_6 = 0
            SLOT_63 = 0
            SLOT_64 = 0
            SLOT_65 = 0
            SLOT_66 = 0
        if SLOT_67 == 2:
            SLOT_6 = 1
            SLOT_63 = 2
            SLOT_64 = 2
            SLOT_65 = 2
            SLOT_66 = 2


@Subroutine
def OnMainEnemyComboBreak():
    SLOT_4 = 0


@Subroutine
def OnSubEnemyComboBreak():
    SLOT_4 = 0


@Subroutine
def OnFrameStep():

    def upon_5():
        SLOT_4 = 0
        SLOT_5 = 0
        CopyFromRightToLeft(25, SLOT_4, 22, SLOT_95)
        SLOT_4 = SLOT_4 + 1
        if SLOT_4 == 1:
            if SLOT_63 == 1:
                SLOT_63 = 2
                if PartnerChar('pna'):

                    def RunOnObject_24():
                        SLOT_63 = 2
                SLOT_5 = 1
        if SLOT_4 == 2:
            if SLOT_64 == 1:
                SLOT_64 = 2
                if PartnerChar('pna'):

                    def RunOnObject_24():
                        SLOT_64 = 2
                SLOT_5 = 1
        if SLOT_4 == 3:
            if SLOT_65 == 1:
                SLOT_65 = 2
                if PartnerChar('pna'):

                    def RunOnObject_24():
                        SLOT_65 = 2
                SLOT_5 = 1
        if SLOT_4 == 4:
            if SLOT_66 == 1:
                SLOT_66 = 2
                if PartnerChar('pna'):

                    def RunOnObject_24():
                        SLOT_66 = 2
                SLOT_5 = 1
        if SLOT_5:
            CopyFromRightToLeft(25, SLOT_32, 22, SLOT_75)
            if SLOT_32:
                if not CheckObjectPresence(10):
                    if SLOT_95 == 0:
                        GFX_0('destinyzero_Cutin_main1_3Naoto', 1)
                        RegisterObject(9, 1)
                        if PartnerChar('pna'):

                            def RunOnObject_24():
                                RegisterObject(9, 1)
                        GFX_0('destinyzero_Cutin_main1_3dokuro', 1)
                    if SLOT_95 == 2:
                        GFX_0('destinyzero_Cutin_main1_3Naoto', 1)
                        RegisterObject(9, 1)
                        if PartnerChar('pna'):

                            def RunOnObject_24():
                                RegisterObject(9, 1)
                        GFX_0('destinyzero_Cutin_main1_3dokuro', 1)
                    if SLOT_95 == 1:
                        GFX_0('destinyzero_Cutin_main2_4Naoto', 1)
                        RegisterObject(9, 1)
                        if PartnerChar('pna'):

                            def RunOnObject_24():
                                RegisterObject(9, 1)
                        GFX_0('destinyzero_Cutin_main2_4dokuro', 1)
                    if SLOT_95 == 3:
                        GFX_0('destinyzero_Cutin_main2_4Naoto', 1)
                        RegisterObject(9, 1)
                        if PartnerChar('pna'):

                            def RunOnObject_24():
                                RegisterObject(9, 1)
                        GFX_0('destinyzero_Cutin_main2_4dokuro', 1)
                    SmartRandomVoiceline('pna306_0', 100, 'pna306_1', 100,
                        '', 0, '', 0)
            GFX_0('destinyzero_main', -1)
        SLOT_4 = 0
        SLOT_5 = 0
        CopyFromRightToLeft(25, SLOT_4, 23, SLOT_95)
        SLOT_4 = SLOT_4 + 1
        if SLOT_4 == 1:
            if SLOT_63 == 1:
                SLOT_63 = 2

                def RunOnObject_24():
                    SLOT_63 = 2
                SLOT_5 = 1
        if SLOT_4 == 2:
            if SLOT_64 == 1:
                SLOT_64 = 2

                def RunOnObject_24():
                    SLOT_64 = 2
                SLOT_5 = 1
        if SLOT_4 == 3:
            if SLOT_65 == 1:
                SLOT_65 = 2

                def RunOnObject_24():
                    SLOT_65 = 2
                SLOT_5 = 1
        if SLOT_4 == 4:
            if SLOT_66 == 1:
                SLOT_66 = 2

                def RunOnObject_24():
                    SLOT_66 = 2
                SLOT_5 = 1
        if SLOT_5:
            CopyFromRightToLeft(25, SLOT_33, 23, SLOT_75)
            if SLOT_33:
                if not CheckObjectPresence(9):
                    if SLOT_95 == 0:
                        GFX_0('destinyzero_Cutin_sub1_3Naoto', 1)
                        RegisterObject(10, 1)
                        if PartnerChar('pna'):

                            def RunOnObject_24():
                                RegisterObject(10, 1)
                        GFX_0('destinyzero_Cutin_sub1_3dokuro', 1)
                    if SLOT_95 == 2:
                        GFX_0('destinyzero_Cutin_sub1_3Naoto', 1)
                        RegisterObject(10, 1)
                        if PartnerChar('pna'):

                            def RunOnObject_24():
                                RegisterObject(10, 1)
                        GFX_0('destinyzero_Cutin_sub1_3dokuro', 1)
                    if SLOT_95 == 1:
                        GFX_0('destinyzero_Cutin_sub2_4Naoto', 1)
                        RegisterObject(10, 1)
                        if PartnerChar('pna'):

                            def RunOnObject_24():
                                RegisterObject(10, 1)
                        GFX_0('destinyzero_Cutin_sub2_4dokuro', 1)
                    if SLOT_95 == 3:
                        GFX_0('destinyzero_Cutin_sub2_4Naoto', 1)
                        RegisterObject(10, 1)
                        if PartnerChar('pna'):

                            def RunOnObject_24():
                                RegisterObject(10, 1)
                        GFX_0('destinyzero_Cutin_sub2_4dokuro', 1)
                    SmartRandomVoiceline('pna306_0', 100, 'pna306_1', 100,
                        '', 0, '', 0)
            GFX_0('destinyzero_sub', -1)
    SLOT_6 = 0
    if SLOT_158:
        CopyFromRightToLeft(25, SLOT_7, 22, SLOT_95)
        SLOT_7 = SLOT_7 + 1
        if SLOT_7 == 1:
            if SLOT_63 == 2:
                SLOT_6 = 1
        if SLOT_7 == 2:
            if SLOT_64 == 2:
                SLOT_6 = 1
        if SLOT_7 == 3:
            if SLOT_65 == 2:
                SLOT_6 = 1
        if SLOT_7 == 4:
            if SLOT_66 == 2:
                SLOT_6 = 1
    if not SLOT_81:
        if SLOT_90:
            TrainingModeSLOT('TRI_PNADeathFlg', SLOT_67)
            if SLOT_67 == 1:
                SLOT_6 = 0
                SLOT_63 = 0
                SLOT_64 = 0
                SLOT_65 = 0
                SLOT_66 = 0
            if SLOT_67 == 2:
                SLOT_6 = 1
                SLOT_63 = 2
                SLOT_64 = 2
                SLOT_65 = 2
                SLOT_66 = 2
        if SLOT_122:
            TrainingModeSLOT('TRI_PNADeathFlg', SLOT_67)
            if SLOT_67 == 1:
                SLOT_6 = 0
                SLOT_63 = 0
                SLOT_64 = 0
                SLOT_65 = 0
                SLOT_66 = 0
            if SLOT_67 == 2:
                SLOT_6 = 1
                SLOT_63 = 2
                SLOT_64 = 2
                SLOT_65 = 2
                SLOT_66 = 2
        if SLOT_123:
            TrainingModeSLOT('TRI_PNADeathFlg', SLOT_67)
            if SLOT_67 == 1:
                SLOT_6 = 0
                SLOT_63 = 0
                SLOT_64 = 0
                SLOT_65 = 0
                SLOT_66 = 0
            if SLOT_67 == 2:
                SLOT_6 = 1
                SLOT_63 = 2
                SLOT_64 = 2
                SLOT_65 = 2
                SLOT_66 = 2
    if SLOT_170:
        SLOT_6 = 0
    if SLOT_9:
        if not SLOT_30:
            EnableCollision(0)
        else:
            SLOT_9 = 0


@Subroutine
def HaikyouEx0():
    if SLOT_59:
        SLOT_59 = SLOT_59 + -1
        GFX_0('Yakkyo', 0)


@Subroutine
def ShagekiFlexChain():
    WhiffCancel('ShagekiA')
    WhiffCancel('ShagekiB')
    WhiffCancel('ShagekiC')
    WhiffCancel('KamaeCancel')
    WhiffCancel('KamaeEX')


@Subroutine
def SpecialCancelmanagement_DeriveI():
    BeginBuffer('BanditRevolverB_EX')
    BeginBuffer('WalkingShotEX_EX')
    BeginBuffer('TrapA_EX')
    BeginBuffer('TrapB_EX')
    BeginBuffer('TrapEX_EX')
    BeginBuffer('SecretGunB_EX')
    BeginBuffer('SecretGunOD_EX')
    BeginBuffer('UltimateKill_EX')
    BeginBuffer('UltimateKillOD_EX')


@Subroutine
def SpecialCancelmanagement_DeriveT():
    BufferedOrPressedGoto('BanditRevolverB_EX')
    BufferedOrPressedGoto('WalkingShotEX_EX')
    BufferedOrPressedGoto('TrapA_EX')
    BufferedOrPressedGoto('TrapB_EX')
    BufferedOrPressedGoto('TrapEX_EX')
    BufferedOrPressedGoto('SecretGunB_EX')
    BufferedOrPressedGoto('SecretGunOD_EX')
    BufferedOrPressedGoto('UltimateKill_EX')
    BufferedOrPressedGoto('UltimateKillOD_EX')


@Subroutine
def SpecialCancelmanagement_DeriveC():
    DisallowGoto('BanditRevolverB_EX')
    DisallowGoto('WalkingShotEX_EX')
    DisallowGoto('TrapA_EX')
    DisallowGoto('TrapB_EX')
    DisallowGoto('TrapEX_EX')
    DisallowGoto('SecretGunB_EX')
    DisallowGoto('SecretGunOD_EX')
    DisallowGoto('UltimateKill_EX')
    DisallowGoto('UltimateKillOD_EX')


@Subroutine
def KamaeCancelcheck():
    SLOT_47 = 1
    if Unknown23145('BanditRevolverB'):
        SLOT_47 = 0


@Subroutine
def Shot_Stack():
    ObjectUpon2(5, 3002, 0)
    if CheckObjectPresence(4):
        RegisterObject(5, 4)


@Subroutine
def Shot_Stack2():
    ObjectUpon2(8, 3003, 0)
    if CheckObjectPresence(7):
        RegisterObject(8, 7)


@State
def CmnActStand():
    label(0)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    spriteEnd()
    if random_(1, SLOT_87):
        conditionalSendToLabel(0)
    if random_(2, 90):
        conditionalSendToLabel(0)
    sprite('na001_00', 7)
    SLOT_88 = 960
    Voiceline('pna000')
    sprite('na001_01', 7)
    sprite('na001_02', 7)
    sprite('na001_03', 10)
    sprite('na001_04', 7)
    sprite('na001_05', 7)
    sprite('na001_06', 10)
    sprite('na001_01', 7)
    sprite('na001_00', 7)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActStandTurn():
    sprite('na003_00', 4)
    sprite('na003_01', 4)
    sprite('na003_02', 4)


@State
def CmnActStand2Crouch():
    sprite('na010_00', 4)
    sprite('na010_01', 4)


@State
def CmnActCrouch():
    label(0)
    sprite('na010_02', 6)
    sprite('na010_03', 6)
    sprite('na010_04', 6)
    sprite('na010_05', 6)
    sprite('na010_06', 6)
    sprite('na010_07', 6)
    sprite('na010_08', 6)
    sprite('na010_09', 6)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActCrouchTurn():
    sprite('na013_00', 4)
    sprite('na013_01', 4)
    sprite('na013_02', 4)


@State
def CmnActCrouch2Stand():
    sprite('na010_01', 4)
    sprite('na010_00', 4)


@State
def CmnActJumpPre():
    if SLOT_37:
        if SLOT_93:
            if SLOT_16:
                SetInertia(15000)
    sprite('na010_00', 4)


@State
def CmnActJumpUpper():
    label(0)
    sprite('na020_00', 4)
    sprite('na020_01', 4)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActJumpUpperEnd():
    sprite('na020_02', 3)
    sprite('na020_03', 3)
    sprite('na020_04', 3)


@State
def CmnActJumpDown():
    sprite('na020_05', 3)
    sprite('na020_06', 3)
    label(0)
    sprite('na020_07', 4)
    sprite('na020_08', 4)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActJumpLanding():
    sprite('na010_01', 3)
    sprite('na010_00', 3)


@State
def CmnActLandingStiffLoop():
    sprite('na211_00', 2)
    sprite('na211_01', 32767)
    spriteEnd()


@State
def CmnActLandingStiffEnd():
    sprite('na211_01', 3)
    sprite('na211_00', 3)


@State
def CmnActFWalk():
    sprite('na030_00', 5)
    sprite('na030_01', 5)
    label(0)
    sprite('na030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('na030_03', 5)
    sprite('na030_04', 5)
    sprite('na030_05', 5)
    sprite('na030_06', 5)
    sprite('na030_07', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('na030_08', 5)
    sprite('na030_09', 5)
    sprite('na030_10', 5)
    sprite('na030_11', 5)
    spriteEnd()
    gotoLabel(0)
    sprite('na030_00', 3)


@State
def CmnActBWalk():
    sprite('na031_00', 6)
    sprite('na031_01', 6)
    label(0)
    sprite('na031_02', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('na031_03', 6)
    sprite('na031_04', 6)
    sprite('na031_05', 6)
    sprite('na031_06', 6)
    sprite('na031_07', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('na031_08', 6)
    sprite('na031_09', 6)
    sprite('na031_10', 6)
    sprite('na031_11', 6)
    spriteEnd()
    gotoLabel(0)
    sprite('na031_00', 3)


@State
def CmnActFDash():
    sprite('na030_00', 4)
    sprite('na032_00', 2)
    label(0)
    sprite('na032_01', 4)
    sprite('na032_02', 4)
    sprite('na032_03', 4)
    Unknown8006(100, 1, 1)
    sprite('na032_04', 4)
    sprite('na032_05', 4)
    sprite('na032_06', 4)
    sprite('na032_07', 4)
    Unknown8006(100, 1, 1)
    sprite('na032_08', 4)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActFDashStop():
    sprite('na032_09', 4)
    sprite('na032_10', 4)


@State
def CmnActBDash():

    def upon_IMMEDIATE():
        SetCommonActionMark(1)
        EnterStateIfEventID(8, '_NEUTRAL')
        setInvincibleFor(7)
        EndMomentum(1)
        uponSendToLabel(upon_LANDING, 1)
        ExternalForcesRate(100, 0)
        NegativeForBackDash()
    sprite('na033_00', 2)
    sprite('na033_01', 3)
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('na033_02', 3)
    sprite('na033_01', 3)
    sprite('na033_02', 3)
    label(0)
    sprite('na033_01', 3)
    sprite('na033_02', 3)
    spriteEnd()
    gotoLabel(0)
    label(1)
    sprite('na033_03', 3)
    setInvincible(0)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    sprite('na033_04', 3)


@State
def CmnActBDashLanding():
    pass


@State
def CmnActAirTurn():
    sprite('na025_02', 1)
    Flip()
    sprite('na025_01', 2)
    sprite('na025_02', 1)
    Flip()


@State
def CmnActAirFDash():
    sprite('na035_00', 3)
    label(0)
    sprite('na035_01', 3)
    sprite('na035_02', 3)
    spriteEnd()
    gotoLabel(0)
    sprite('na035_00', 4)


@State
def CmnActAirBDash():
    sprite('na033_00', 2)
    physicsYImpulse(12000)
    sprite('na033_02', 3)
    sprite('na033_01', 3)
    sprite('na033_02', 3)
    sprite('na033_01', 3)
    sprite('na033_02', 3)
    sprite('na033_01', 3)
    sprite('na033_02', 3)
    sprite('na020_05', 3)
    sprite('na020_06', 3)
    label(0)
    sprite('na020_07', 4)
    sprite('na020_08', 4)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActHitStandLv1():
    sprite('na050_00', 1)
    sprite('na050_01', 1)
    sprite('na050_00', 2)


@State
def CmnActHitStandLv2():
    sprite('na050_01', 1)
    sprite('na050_02', 1)
    sprite('na050_01', 2)
    sprite('na050_00', 2)


@State
def CmnActHitStandLv3():
    sprite('na050_02', 1)
    sprite('na050_03', 1)
    sprite('na050_02', 2)
    sprite('na050_01', 2)
    sprite('na050_00', 2)


@State
def CmnActHitStandLv4():
    sprite('na050_03', 1)
    sprite('na050_04', 1)
    sprite('na050_03', 2)
    sprite('na050_02', 2)
    sprite('na050_01', 2)
    sprite('na050_00', 2)


@State
def CmnActHitStandLv5():
    sprite('na050_04', 1)
    sprite('na050_04', 1)
    sprite('na050_04', 2)
    sprite('na050_03', 2)
    sprite('na050_02', 2)
    sprite('na050_01', 2)
    sprite('na050_00', 2)


@State
def CmnActHitStandLowLv1():
    sprite('na052_00', 1)
    sprite('na052_01', 1)
    sprite('na052_00', 2)


@State
def CmnActHitStandLowLv2():
    sprite('na052_01', 1)
    sprite('na052_02', 1)
    sprite('na052_01', 2)
    sprite('na052_00', 2)


@State
def CmnActHitStandLowLv3():
    sprite('na052_02', 1)
    sprite('na052_03', 1)
    sprite('na052_02', 2)
    sprite('na052_01', 2)
    sprite('na052_00', 2)


@State
def CmnActHitStandLowLv4():
    sprite('na052_03', 1)
    sprite('na052_04', 1)
    sprite('na052_03', 2)
    sprite('na052_02', 2)
    sprite('na052_01', 2)
    sprite('na052_00', 2)


@State
def CmnActHitStandLowLv5():
    sprite('na052_04', 1)
    sprite('na052_04', 1)
    sprite('na052_04', 2)
    sprite('na052_03', 2)
    sprite('na052_02', 2)
    sprite('na052_01', 2)
    sprite('na052_00', 2)


@State
def CmnActHitCrouchLv1():
    sprite('na054_00', 1)
    sprite('na054_01', 1)
    sprite('na054_00', 2)


@State
def CmnActHitCrouchLv2():
    sprite('na054_01', 1)
    sprite('na054_02', 1)
    sprite('na054_01', 2)
    sprite('na054_00', 2)


@State
def CmnActHitCrouchLv3():
    sprite('na054_02', 1)
    sprite('na054_03', 1)
    sprite('na054_02', 2)
    sprite('na054_01', 2)
    sprite('na054_00', 2)


@State
def CmnActHitCrouchLv4():
    sprite('na054_03', 1)
    sprite('na054_04', 1)
    sprite('na054_03', 2)
    sprite('na054_02', 2)
    sprite('na054_01', 2)
    sprite('na054_00', 2)


@State
def CmnActHitCrouchLv5():
    sprite('na054_04', 1)
    sprite('na054_04', 1)
    sprite('na054_04', 2)
    sprite('na054_03', 2)
    sprite('na054_02', 2)
    sprite('na054_01', 2)
    sprite('na054_00', 2)


@State
def CmnActBDownUpper():
    sprite('na060_00', 4)
    label(0)
    sprite('na060_01', 4)
    sprite('na060_02', 4)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActBDownUpperEnd():
    sprite('na060_03', 4)


@State
def CmnActBDownDown():
    sprite('na060_04', 8)
    label(1)
    sprite('na060_05', 4)
    sprite('na060_06', 4)
    spriteEnd()
    gotoLabel(1)


@State
def CmnActBDownCrash():
    sprite('na063_05', 6)


@State
def CmnActBDownBound():
    sprite('na060_08', 2)
    sprite('na060_09', 2)
    sprite('na060_10', 2)
    sprite('na060_11', 2)


@State
def CmnActBDownLoop():
    sprite('na060_12', 3)


@State
def CmnActBDown2Stand():
    sprite('na064_00', 6)
    sprite('na064_01', 6)
    sprite('na064_02', 6)
    sprite('na064_03', 6)


@State
def CmnActFDownUpper():
    sprite('na063_00', 4)


@State
def CmnActFDownUpperEnd():
    sprite('na063_01', 3)


@State
def CmnActFDownDown():
    label(1)
    sprite('na063_03', 4)
    sprite('na063_04', 4)
    spriteEnd()
    gotoLabel(1)


@State
def CmnActFDownCrash():
    sprite('na063_05', 4)


@State
def CmnActFDownBound():
    sprite('na060_08', 2)
    sprite('na060_09', 2)
    sprite('na060_10', 2)
    sprite('na060_11', 2)


@State
def CmnActFDownLoop():
    sprite('na060_12', 3)


@State
def CmnActFDown2Stand():
    sprite('na064_00', 4)
    sprite('na064_01', 4)
    sprite('na064_02', 4)
    sprite('na064_03', 4)


@State
def CmnActVDownUpper():
    sprite('na060_00', 4)
    label(0)
    sprite('na060_01', 4)
    sprite('na060_02', 4)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActVDownUpperEnd():
    sprite('na060_03', 4)
    sprite('na060_04', 4)


@State
def CmnActVDownDown():
    sprite('na060_04', 8)
    label(0)
    sprite('na060_05', 4)
    sprite('na060_06', 4)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActVDownCrash():
    sprite('na060_07', 4)


@State
def CmnActBlowoff():
    sprite('na072_00', 3)
    label(0)
    sprite('na072_01', 3)
    sprite('na072_02', 3)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActKirimomiUpper():
    label(0)
    sprite('na074_00', 2)
    sprite('na074_01', 2)
    sprite('na074_02', 2)
    sprite('na074_03', 2)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActWallBound():
    sprite('na072_03', 3)


@State
def CmnActWallBoundDown():
    sprite('na063_00', 3)
    label(0)
    sprite('na063_01', 3)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActSkeleton():
    sprite('na082_00', 32767)


@State
def CmnActFreeze():
    sprite('na052_01', 1)


@State
def CmnActStaggerLoop():
    sprite('na070_00', 32767)


@State
def CmnActStaggerDown():
    sprite('na070_01', 4)
    sprite('na070_02', 4)
    sprite('na070_03', 4)
    sprite('na070_04', 4)
    sprite('na070_05', 4)
    sprite('na070_06', 4)


@State
def CmnActUkemiStagger():
    sprite('na040_03', 2)
    sprite('na040_02', 2)
    sprite('na040_01', 2)
    sprite('na040_00', 2)


@State
def CmnActUkemiAirN():
    sprite('na020_02', 3)
    sprite('na020_03', 3)
    sprite('na020_04', 32767)


@State
def CmnActUkemiAirF():
    sprite('na020_02', 3)
    sprite('na020_03', 3)
    sprite('na020_04', 32767)


@State
def CmnActUkemiAirB():
    sprite('na020_02', 3)
    sprite('na020_03', 3)
    sprite('na020_04', 32767)


@State
def CmnActUkemiLandN():
    sprite('na112_00', 3)
    sprite('na112_01', 3)
    sprite('na112_02', 3)
    sprite('na112_03', 3)
    sprite('na112_04', 3)
    sprite('na112_05', 3)
    sprite('na020_07', 4)
    sprite('na020_08', 4)
    sprite('na020_07', 4)
    sprite('na020_08', 4)


@State
def CmnActUkemiLandF():
    sprite('na112_00', 3)
    sprite('na112_01', 3)
    sprite('na112_02', 3)
    sprite('na112_03', 3)
    sprite('na112_04', 3)
    sprite('na112_05', 3)
    sprite('na020_07', 4)
    sprite('na020_08', 4)
    spriteEnd()


@State
def CmnActUkemiLandB():
    sprite('na112_00', 3)
    sprite('na112_01', 3)
    sprite('na112_02', 3)
    sprite('na112_03', 3)
    sprite('na112_04', 3)
    sprite('na112_05', 3)
    sprite('na020_07', 4)
    sprite('na020_08', 4)
    spriteEnd()


@State
def CmnActUkemiLandNLanding():
    sprite('na010_01', 3)
    sprite('na010_00', 3)


@State
def CmnActMidGuardPre():
    sprite('na040_00', 3)
    sprite('na040_01', 3)


@State
def CmnActMidGuardLoop():
    label(0)
    sprite('na040_02', 5)
    sprite('na040_03', 5)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActMidGuardEnd():
    sprite('na040_01', 3)
    sprite('na040_00', 3)


@State
def CmnActMidHeavyGuardLoop():
    sprite('na040_04', 1)
    label(0)
    sprite('na040_02', 5)
    sprite('na040_03', 5)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActMidHeavyGuardEnd():
    sprite('na040_01', 3)
    sprite('na040_00', 3)


@State
def CmnActHighGuardPre():
    sprite('na040_00', 3)
    sprite('na040_01', 3)


@State
def CmnActHighGuardLoop():
    label(0)
    sprite('na040_02', 5)
    sprite('na040_03', 5)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActHighGuardEnd():
    sprite('na040_01', 3)
    sprite('na040_00', 3)


@State
def CmnActHighHeavyGuardLoop():
    sprite('na040_04', 1)
    label(0)
    sprite('na040_02', 5)
    sprite('na040_03', 5)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActHighHeavyGuardEnd():
    sprite('na040_01', 3)
    sprite('na040_00', 3)


@State
def CmnActCrouchGuardPre():
    sprite('na043_00', 3)
    sprite('na043_01', 3)


@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('na043_02', 5)
    sprite('na043_03', 5)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActCrouchGuardEnd():
    sprite('na043_01', 3)
    sprite('na043_00', 3)


@State
def CmnActCrouchHeavyGuardLoop():
    sprite('na043_04', 1)
    label(0)
    sprite('na043_02', 5)
    sprite('na043_03', 5)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActCrouchHeavyGuardEnd():
    sprite('na043_01', 3)
    sprite('na043_00', 3)


@State
def CmnActAirGuardPre():
    sprite('na045_00', 3)
    sprite('na045_01', 3)


@State
def CmnActAirGuardLoop():
    label(0)
    sprite('na045_02', 5)
    sprite('na045_03', 5)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActAirGuardEnd():
    sprite('na045_01', 3)
    sprite('na045_00', 3)


@State
def CmnActAirHeavyGuardLoop():
    sprite('na045_04', 1)
    label(0)
    sprite('na045_02', 5)
    sprite('na045_03', 5)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActAirHeavyGuardEnd():
    sprite('na045_01', 3)
    sprite('na045_00', 3)


@State
def CmnActGuardBreakStand():
    sprite('na040_04', 2)
    sprite('na040_04', 2)
    sprite('na040_04', 1)
    SetCommonActionMark(1)
    sprite('na040_02', 4)
    sprite('na040_01', 4)
    sprite('na040_00', 4)


@State
def CmnActGuardBreakCrouch():
    pass


@State
def CmnActGuardBreakAir():
    pass


@State
def CmnActLockWait():
    sprite('na040_04', 6)


@State
def CmnActLockReject():
    sprite('na200_00', 4)
    sprite('na200_01', 5)
    sprite('na200_02', 11)
    RefreshMultihit()
    sprite('na200_03', 3)
    sprite('na200_04', 3)
    sprite('na200_05', 3)


@State
def CmnActAirLockWait():
    sprite('na045_02', 1)
    sprite('na045_01', 3)
    sprite('na045_00', 3)


@State
def CmnActAirLockReject():
    sprite('na251_00', 3)
    sprite('na251_01', 3)
    sprite('na251_03', 3)
    sprite('na251_03', 7)
    DisableAttackRestOfMove()
    sprite('na251_04', 5)
    sprite('na251_05', 4)
    EndAttack()


@State
def CmnActLandSpin():
    sprite('na071_00', 2)
    label(0)
    sprite('na071_01', 2)
    sprite('na071_02', 2)
    sprite('na071_03', 2)
    sprite('na071_04', 2)
    sprite('na071_05', 2)
    sprite('na071_06', 2)
    sprite('na071_07', 2)
    sprite('na071_08', 2)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActLandSpinDown():
    sprite('na040_02', 3)
    sprite('na040_01', 3)
    sprite('na040_00', 3)


@State
def CmnActVertSpin():
    sprite('na071_00', 2)
    label(0)
    sprite('na071_01', 2)
    sprite('na071_02', 2)
    sprite('na071_03', 2)
    sprite('na071_04', 2)
    sprite('na071_05', 2)
    sprite('na071_06', 2)
    sprite('na071_07', 2)
    sprite('na071_08', 2)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActSlideAir():
    sprite('na124_00', 2)
    label(0)
    sprite('na124_01', 2)
    sprite('na124_02', 2)
    sprite('na124_03', 2)
    sprite('na124_04', 2)
    sprite('na124_05', 2)
    sprite('na124_06', 2)
    sprite('na124_07', 2)
    sprite('na124_08', 2)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActSlideKeep():
    sprite('na077_02', 4)
    label(0)
    sprite('na077_03', 3)
    sprite('na077_04', 3)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActSlideEnd():
    sprite('na077_05', 5)
    sprite('na077_06', 4)


@State
def CmnActAomukeSlideKeep():
    pass


@State
def CmnActAomukeSlideEnd():
    pass


@State
def CmnActBurstBegin():
    pass


@State
def CmnActBurstLoop():
    pass


@State
def CmnActBurstEnd():
    pass


@State
def CmnActAirBurstBegin():
    pass


@State
def CmnActAirBurstLoop():
    pass


@State
def CmnActAirBurstEnd():
    pass


@State
def CmnActOverDriveBegin():
    label(0)
    sprite('na121_00', 3)
    sprite('na121_01', 3)
    sprite('na121_02', 3)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActOverDriveLoop():
    sprite('na121_03', 3)
    label(1)
    sprite('na121_04', 2)
    sprite('na121_05', 2)
    sprite('na121_06', 2)
    spriteEnd()
    gotoLabel(1)


@State
def CmnActOverDriveEnd():
    sprite('na121_07', 6)
    sprite('na010_00', 6)


@State
def CmnActAirOverDriveBegin():
    label(0)
    sprite('na121_00', 3)
    sprite('na121_01', 3)
    sprite('na121_02', 3)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActAirOverDriveLoop():
    sprite('na121_03', 3)
    label(1)
    sprite('na121_04', 2)
    sprite('na121_05', 2)
    sprite('na121_06', 2)
    spriteEnd()
    gotoLabel(1)


@State
def CmnActAirOverDriveEnd():
    sprite('na121_07', 3)
    sprite('na121_08', 3)
    sprite('na020_05', 3)
    sprite('na020_06', 3)
    label(0)
    sprite('na020_07', 4)
    sprite('na020_08', 4)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActCrossRushBegin():

    def upon_IMMEDIATE():
        RunLoopUpon(upon_17, 7)

        def upon_17():

            def RunOnObject_28():
                SLOT_0 = CurrentStateCheck('PNA_PersonaWait')
                CopyFromRightToLeft(3, SLOT_51, 25, SLOT_0)
            if not SLOT_51:
                ObjectUpon2(11, 3017, 0)
    label(0)
    sprite('na121_00', 3)
    sprite('na121_01', 3)
    sprite('na121_02', 3)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActCrossRushLoop():
    sprite('na121_03', 3)
    label(0)
    sprite('na121_04', 2)
    sprite('na121_05', 2)
    sprite('na121_06', 2)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActCrossRushEnd():
    sprite('na121_07', 6)
    sprite('na010_00', 6)


@State
def CmnActAirCrossRushBegin():

    def upon_IMMEDIATE():
        RunLoopUpon(upon_17, 7)

        def upon_17():

            def RunOnObject_28():
                SLOT_0 = CurrentStateCheck('PNA_PersonaWait')
                CopyFromRightToLeft(3, SLOT_51, 25, SLOT_0)
            if not SLOT_51:
                ObjectUpon2(11, 3017, 0)
    label(0)
    sprite('na121_00', 3)
    sprite('na121_01', 3)
    sprite('na121_02', 3)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActAirCrossRushLoop():
    sprite('na121_03', 3)
    label(0)
    sprite('na121_04', 2)
    sprite('na121_05', 2)
    sprite('na121_06', 2)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActAirCrossRushEnd():
    sprite('na121_07', 3)
    sprite('na121_08', 3)
    sprite('na020_05', 3)
    sprite('na020_06', 3)
    label(0)
    sprite('na020_07', 4)
    sprite('na020_08', 4)
    gotoLabel(0)


@State
def CmnActCrossChangeBegin():

    def upon_IMMEDIATE():
        RunLoopUpon(upon_17, 7)

        def upon_17():

            def RunOnObject_28():
                SLOT_0 = CurrentStateCheck('PNA_PersonaWait')
                CopyFromRightToLeft(3, SLOT_51, 25, SLOT_0)
            if not SLOT_51:
                ObjectUpon2(11, 3017, 0)
    label(0)
    sprite('na121_00', 3)
    sprite('na121_01', 3)
    sprite('na121_02', 3)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActCrossChangeLoop():
    sprite('na121_03', 3)
    label(0)
    sprite('na121_04', 2)
    sprite('na121_05', 2)
    sprite('na121_06', 2)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActCrossChangeEnd():
    sprite('na121_07', 6)
    sprite('na121_08', 6)


@State
def CmnActAirCrossChangeBegin():

    def upon_IMMEDIATE():
        RunLoopUpon(upon_17, 7)

        def upon_17():

            def RunOnObject_28():
                SLOT_0 = CurrentStateCheck('PNA_PersonaWait')
                CopyFromRightToLeft(3, SLOT_51, 25, SLOT_0)
            if not SLOT_51:
                ObjectUpon2(11, 3017, 0)
    label(0)
    sprite('na121_00', 3)
    sprite('na121_01', 3)
    sprite('na121_02', 3)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActAirCrossChangeLoop():
    sprite('na121_03', 3)
    label(0)
    sprite('na121_04', 2)
    sprite('na121_05', 2)
    sprite('na121_06', 2)
    spriteEnd()
    gotoLabel(0)


@State
def CmnActAirCrossChangeEnd():
    sprite('na121_07', 3)
    sprite('na121_08', 3)
    sprite('na020_05', 3)
    sprite('na020_06', 3)
    label(0)
    sprite('na020_07', 4)
    sprite('na020_08', 4)
    gotoLabel(0)


@State
def CmnActTagBattleWait():

    def upon_IMMEDIATE():
        setInvincible(1)
        EnableCollision(0)
        ScreenCollision(0)
        AbsoluteY(0)
    label(0)
    sprite('null', 1)
    gotoLabel(0)


@State
def CmnActChangePartnerAppeal():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()

        def upon_EVERY_FRAME():
            if Unknown30042(25):
                ScreenCollision(1)
            else:
                ScreenCollision(0)
    sprite('na000_00', 20)


@State
def CmnActChangePartnerAppealAir():

    def upon_IMMEDIATE():
        AttackDefaults_AirNoAttack()

        def upon_EVERY_FRAME():
            if Unknown30042(25):
                ScreenCollision(1)
            else:
                ScreenCollision(0)
    sprite('na000_00', 20)


@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021()

        def upon_41():
            clearUponHandler(upon_41)
            sendToLabel(100)

        def upon_LANDING():
            clearUponHandler(upon_LANDING)
            sendToLabel(9)
    sprite('null', 2)
    sprite('null', 600)
    label(100)
    sprite('null', 28)
    sprite('na407_09', 3)
    TeleportToObject(22)
    AddX(-150000)
    AbsoluteY(1200000)
    physicsYImpulse(-240000)
    setGravity(0)
    Unknown2053(1)
    EnableCollision(1)
    label(1)
    sprite('na407_09', 3)
    sprite('na407_09', 3)
    spriteEnd()
    gotoLabel(1)
    label(9)
    sprite('na407_10', 3)
    sprite('na407_11ex', 2)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('na211_00', 3)
    CrouchState(1)
    sprite('na211_01', 17)


@State
def CmnActChangePartnerQuickIn():
    sprite('na032_05', 3)
    sprite('na032_06', 5)
    sprite('na032_09', 7)
    sprite('na032_09', 7)
    sprite('na032_10', 7)


@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
    sprite('na033_01', 3)
    sprite('na033_02', 3)
    sprite('na033_01', 3)
    sprite('na033_02', 3)
    sprite('na033_01', 3)
    sprite('na033_02', 3)
    sprite('na033_01', 3)
    sprite('na033_02', 3)
    sprite('na033_01', 3)
    sprite('na033_02', 3)
    sprite('na033_01', 30)


@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
        uponSendToLabel(upon_LANDING, 1)
    sprite('na033_00', 1)
    sprite('na033_01', 4)
    sprite('na033_02', 4)
    spriteEnd()
    label(0)
    sprite('na033_02', 3)
    spriteEnd()
    gotoLabel(0)
    label(1)
    sprite('na033_03', 3)
    sprite('na033_04', 3)


@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
    sprite('na611_00', 4)
    sprite('na611_01', 4)
    sprite('na611_02', 4)
    sprite('na611_03', 4)
    sprite('na611_04', 4)
    sprite('na611_05', 11)
    sprite('na611_06', 6)
    sprite('na611_07', 7)
    sprite('na611_08', 6)
    sprite('na611_09', 6)
    sprite('na611_10', 4)
    sprite('na611_09', 4)
    sprite('na611_08', 4)
    sprite('na611_07', 4)
    sprite('na611_06', 4)


@State
def CmnActChangePartnerAssistAdmiss():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_LANDING():
            clearUponHandler(upon_LANDING)
            EndMomentum(1)
            sendToLabel(99)
    sprite('null', 2)
    label(0)
    sprite('na020_07', 4)
    XImpulseAcceleration(95)
    sprite('na020_08', 4)
    XImpulseAcceleration(95)
    spriteEnd()
    gotoLabel(0)
    label(99)
    sprite('na010_00', 2)
    LandingEffects(100, 1, 1)
    sprite('keep', 100)


@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown30039(24)
        Unknown30040(1)
        ForceFaceSprite()

        def upon_STATE_END():
            EnableCollision(1)
            ScreenCollision(1)
            Unknown2053(1)
        EndMomentum(1)
        SLOT_60 = 5
        SLOT_61 = 0
        Unknown11063(1)
        Unknown14083(0)
        Unknown30068(1)
    sprite('na401_00', 3)
    sprite('na401_01', 1)
    sprite('na401_01', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_01', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_01', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_02', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_02', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_02', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_02', 1)
    sprite('na401_03', 27)
    sprite('na401_03', 2)
    spriteEnd()
    gotoLabel(16)
    label(16)
    if SLOT_60 <= 1:
        conditionalSendToLabel(17)
    sprite('na401_52', 1)
    sprite('na404_00', 2)
    SLOT_60 = SLOT_60 + -1
    SLOT_59 = SLOT_59 + 1
    GFX_0('Dangan_PS', 1)
    ObjectUpon2(1, 3010, 0)
    PrivateSE('na001')
    sprite('na404_01', 2)
    sprite('na404_00', 1)
    sendToLabel(16)
    sprite('na404_00', 3)
    sprite('na401_03', 3)
    sprite('na401_03', 3)
    WhiffCancelEnable(0)
    sprite('na401_03', 32767)
    enterState('KamaeBase')
    spriteEnd()
    ExitState()
    label(17)
    sprite('na404_00', 1)
    sprite('na404_00', 2)
    GFX_0('DanganLastA_PS', 1)
    SmartRandomVoiceline('pna207_0', 100, 'pna207_1', 100, 'pna207_2', 100,
        '', 0)
    ScreenShake(10000, 0)
    Unknown1047(-10000)
    PrivateSE('na002')
    sprite('na404_02', 6)
    sprite('na404_03', 6)
    sprite('na404_04', 14)
    sprite('na404_05', 7)
    sprite('na404_06', 6)
    sprite('na401_03', 3)
    spriteEnd()
    sprite('na401_02', 5)
    SmartRandomVoiceline('pna211_0', 100, 'pna211_1', 100, 'pna211_2', 100,
        '', 0)
    sprite('na401_01', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_01', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_01', 1)
    sprite('na401_01', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)


@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('na410_00', 5)
    sprite('na410_01', 4)
    sprite('na410_01', 1)
    ObjectUpon2(11, 402, 0)
    GFX_1('persona_enter_ply', 0)
    TagVoiceline(1, 'pna217_0', 'pna217_1', 'pna217_2', '')
    sprite('na410_02', 4)
    sprite('na410_03', 4)
    sprite('na410_02', 4)
    sprite('na410_03', 4)
    sprite('na410_02', 4)
    sprite('na410_03', 4)
    sprite('na410_02', 4)
    Recovery()
    sprite('na410_03', 4)
    sprite('na410_02', 4)
    sprite('na410_03', 4)
    sprite('na410_02', 4)
    sprite('na410_03', 4)
    sprite('na410_02', 4)
    sprite('na410_03', 4)
    sprite('na410_02', 4)
    sprite('na410_03', 4)
    sprite('na410_02', 4)
    sprite('na410_03', 4)
    sprite('na410_04', 6)


@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        SLOT_10 = 0
        CounterHitSetting(1)

        def upon_43():
            if SLOT_48 == 3020:
                Recovery()
    sprite('na205_00', 2)
    sprite('na205_01', 2)
    sprite('na205_02', 2)
    clearUponHandler(upon_EVERY_FRAME)
    sprite('na205_02', 2)
    ObjectUpon2(11, 405, 0)
    SmartRandomVoiceline('pna120_0', 100, 'pna120_1', 100, 'pna120_2', 100,
        '', 0)
    sprite('na205_03', 3)
    GFX_1('persona_enter_ply', 0)
    sprite('na205_04', 3)
    Unknown14077(0)
    JumpCancel_(0)
    sprite('na205_05', 4)
    sprite('na205_01', 3)
    sprite('na403_00', 3)
    sprite('na403_01', 2)
    physicsXImpulse(35000)
    sprite('na403_02', 1)
    XImpulseAcceleration(160)
    sprite('na403_03', 1)
    sprite('na403_04', 2)
    sprite('na403_05', 2)
    sprite('na403_06', 1)
    sprite('na403_06', 1)
    EndMomentum(1)
    SetInertia(32000)
    sprite('na403_07', 1)
    callSubroutine('HaikyouEx0')
    sprite('na403_08', 1)
    EnableCollision(1)
    callSubroutine('HaikyouEx0')
    sprite('na403_09', 1)
    ForceFaceSprite()
    sprite('na403_09', 1)
    sprite('na403_09', 1)
    callSubroutine('HaikyouEx0')
    sprite('na403_10', 1)
    callSubroutine('HaikyouEx0')
    sprite('na403_10', 1)
    sprite('na403_11', 1)
    callSubroutine('HaikyouEx0')
    setInvincible(0)
    Unknown1051(50)
    sprite('na403_11', 1)
    callSubroutine('HaikyouEx0')
    sprite('na403_12', 1)
    sprite('na401_03', 20)
    if SLOT_10:
        SLOT_10 = 0

        def upon_EVERY_FRAME():
            if SLOT_20 < 400000:
                clearUponHandler(upon_EVERY_FRAME)
                sendToLabel(0)
    else:
        Recovery()
    spriteEnd()
    sprite('na401_02', 5)
    EndMomentum(1)
    sprite('na401_01', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_01', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_01', 1)
    sprite('na401_01', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)
    ExitState()
    label(0)
    sprite('na404_00', 1)
    SetYCollisionFromOrigin(450)
    sprite('na404_02', 6)
    GFX_0('DanganD_Ex', 1)
    SmartRandomVoiceline('pna105_0', 100, 'pna105_1', 100, 'pna105_2', 100,
        '', 0)
    ScreenShake(10000, 0)
    Unknown1047(-10000)
    PrivateSE('na002')
    sprite('na404_03', 6)
    sprite('na404_04', 14)
    Recovery()
    sprite('na404_05', 7)
    sprite('na401_00', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 3)


@State
def CmnActChangePartnerDD():

    def upon_IMMEDIATE():
        setInvincible(1)
        if SLOT_162:
            SLOT_58 = 1

        def upon_LANDING():
            clearUponHandler(upon_LANDING)
            EndMomentum(1)
            LandingEffects(100, 1, 1)
            sendToLabel(1)
    sprite('null', 1)
    DistortionSettings(103, -1, 0)
    sprite('null', 1)
    AddX(-1500000)
    AbsoluteY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    AddX(-290000)
    XImpulseAcceleration(4)
    label(0)
    sprite('na020_07', 4)
    XImpulseAcceleration(103)
    sprite('na020_08', 4)
    spriteEnd()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)
    if SLOT_58:
        enterState('UltimateWalkingShotKickOD')
    else:
        enterState('UltimateWalkingShotKick')


@State
def UltimateWalkingShotKick():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056()
        Unknown30063(1)
        AttackLevel(5)
        Damage(2000)
        AttackP1(100)
        MinimumDamage(100)
        AttackP2(100)
        Hitstop(30)
        GroundedHitstunAnimation(AIR_FACE_UP_SKIP)
        AirHitstunAnimation(AIR_FACE_UP_SKIP)
        AirUntechableTime(70)
        AirHitstunAfterWallbounce(50)
        WallbounceReboundTime(40)
        Wallbounce(3)
        NonCornerWallbounce(0)
        ResetPushbackX()
        AirPushbackX(550000)
        AirPushbackY(40000)
        Unknown11068(1)
        DamageFromStateOnly('UltimateWalkingShotKick')

        def upon_12():
            ScreenShake(50000, 0)
        EnableRapidCancel(0)
        setInvincible(1)
    sprite('na433_13', 4)
    sprite('na433_14', 4)
    sprite('na433_15', 10)
    sprite('na433_15', 10)
    ScreenShake(5000, 0)
    sprite('na433_15', 10)
    ScreenShake(7500, 0)
    sprite('na433_15', 10)
    ScreenShake(10000, 0)
    sprite('na433_15', 10)
    ScreenShake(12500, 0)
    sprite('na433_15', 14)
    sprite('na433_16', 2)
    sprite('na433_17', 2)
    GFX_0('Kick_line', 100)
    PrivateSE('slash_blade_middle')
    sprite('na433_18', 2)
    sprite('na433_20', 2)
    GFX_0('Zanzoh_kick', 100)
    Unknown23054('na433_19', 3)
    RefreshMultihit()
    TagVoiceline(0, 'pna258_0', 'pna258_1', '', '')
    sprite('na433_20', 35)
    DisableAttackRestOfMove()
    setInvincible(0)
    sprite('na433_21', 6)
    StayAfterMovement(1, 0)
    sprite('na433_22', 6)
    sprite('na433_23', 5)
    sprite('na433_24', 4)
    sprite('na433_25', 4)


@State
def UltimateWalkingShotKickOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056()
        Unknown30063(1)
        AttackLevel(5)
        Damage(2500)
        AttackP1(100)
        AttackP2(100)
        MinimumDamage(100)
        Hitstop(30)
        GroundedHitstunAnimation(AIR_FACE_UP_SKIP)
        AirHitstunAnimation(AIR_FACE_UP_SKIP)
        AirUntechableTime(70)
        AirHitstunAfterWallbounce(50)
        WallbounceReboundTime(40)
        Wallbounce(3)
        NonCornerWallbounce(0)
        ResetPushbackX()
        AirPushbackX(550000)
        AirPushbackY(40000)
        Unknown11068(1)
        DamageFromStateOnly('UltimateWalkingShotKickOD')

        def upon_12():
            ScreenShake(50000, 0)
        EnableRapidCancel(0)
        setInvincible(1)
    sprite('na433_13', 4)
    sprite('na433_14', 4)
    sprite('na433_15', 10)
    sprite('na433_15', 10)
    ScreenShake(5000, 0)
    sprite('na433_15', 10)
    ScreenShake(7500, 0)
    sprite('na433_15', 10)
    ScreenShake(10000, 0)
    sprite('na433_15', 10)
    ScreenShake(12500, 0)
    sprite('na433_15', 14)
    sprite('na433_16', 2)
    sprite('na433_17', 2)
    GFX_0('Kick_line', 100)
    PrivateSE('slash_blade_middle')
    sprite('na433_18', 2)
    sprite('na433_20', 2)
    GFX_0('Zanzoh_kick', 100)
    Unknown23054('na433_19', 3)
    RefreshMultihit()
    TagVoiceline(0, 'pna258_0', 'pna258_1', '', '')
    sprite('na433_20', 35)
    DisableAttackRestOfMove()
    setInvincible(0)
    sprite('na433_21', 6)
    StayAfterMovement(1, 0)
    sprite('na433_22', 6)
    sprite('na433_23', 5)
    sprite('na433_24', 4)
    sprite('na433_25', 4)


@State
def CmnActChangeRequest():

    def upon_IMMEDIATE():
        AttackDefaults_AirNoAttack()
    sprite('na001_00', 7)
    sprite('na001_01', 7)
    sprite('na001_02', 7)
    sprite('na001_03', 9)
    sprite('na001_04', 5)
    sprite('na001_05', 5)
    sprite('na001_06', 10)
    sprite('na001_01', 5)
    sprite('na001_00', 5)
    spriteEnd()
    label(1)
    sprite('na600_12', 1)
    if Unknown30042(24):
        conditionalSendToLabel(2)
    spriteEnd()
    gotoLabel(1)
    label(2)
    sprite('na600_13', 3)
    sprite('na600_14', 3)
    sprite('na600_15', 3)
    sprite('na600_16', 3)


@State
def CmnActChangePartnerBurst():

    def upon_IMMEDIATE():
        Unknown17021()

        def upon_41():
            clearUponHandler(upon_41)
            sendToLabel(0)

        def upon_LANDING():
            clearUponHandler(upon_LANDING)
            sendToLabel(9)
    sprite('null', 120)
    label(0)
    sprite('na407_10', 3)
    TeleportToObject(22)
    AddX(-150000)
    AddY(2400000)
    physicsYImpulse(-80000)
    setGravity(0)
    Unknown2053(1)
    PrivateSE('hit_l_slow')
    label(1)
    sprite('na407_10', 3)
    sprite('na407_10', 3)
    spriteEnd()
    gotoLabel(1)
    label(9)
    sprite('na407_11ex', 1)
    sprite('na211_00', 3)
    CrouchState(1)
    sprite('na211_01', 27)


@State
def CmnActChangeReturnAppealBurst():
    sprite('na064_01', 30)
    sprite('na064_02', 5)
    sprite('na064_03', 5)
    sprite('na010_02', 5)
    sprite('na010_01', 5)
    sprite('na010_00', 5)
    sprite('na000_00', 30)


@State
def CmnActAComboFinalBlow():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_LANDING():
            clearUponHandler(upon_LANDING)
            sendToLabel(1)
    sprite('null', 30)
    sprite('null', 1)
    AddX(-25000)
    AddY(600000)
    setGravity(0)
    physicsYImpulse(-60000)
    SLOT_12 = SLOT_19
    XImpulseAcceleration(4)
    label(0)
    sprite('na407_10', 3)
    spriteEnd()
    gotoLabel(0)
    label(1)
    sprite('na407_11ex', 1)
    if SLOT_3:
        enterState('CmnActAComboFinalBlowFinish')
    sprite('na211_00', 3)
    Unknown23022(0)
    CrouchState(1)
    sprite('na211_01', 27)


@State
def CmnActAComboFinalBlowFinish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('na407_11ex', 1)
    sprite('na211_00', 3)
    sprite('na211_01', 5)
    sprite('na010_01', 3)
    sprite('na010_00', 3)
    sprite('na433_13', 3)
    sprite('na433_14', 3)
    sprite('na433_15', 7)
    sprite('na433_16', 2)
    sprite('na433_17', 2)
    GFX_0('Kick_line', 100)
    PrivateSE('slash_blade_middle')
    sprite('na433_18', 2)
    sprite('na433_20', 2)
    GFX_0('Zanzoh_kick', 100)
    Unknown23054('na433_19', 3)
    RefreshMultihit()
    RandomCommonVoiceline(4)
    sprite('na433_20', 13)
    DisableAttackRestOfMove()
    sprite('na433_21', 6)
    StayAfterMovement(1, 0)
    sprite('na433_22', 6)
    sprite('na433_23', 5)
    sprite('na433_24', 4)
    sprite('na433_25', 4)
    spriteEnd()


@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel(3)
        HitOrBlockCancel('NmlAtk5A2nd')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        Unknown1112()
    sprite('na203_00', 4)
    sprite('na203_01', 4)
    PrivateSE('hit_l_middle')
    sprite('na203_50', 4)
    Unknown23054('na203_02', 3)
    RefreshMultihit()
    physicsXImpulse(20000)
    RandomCommonVoiceline(1)
    sprite('na203_50', 2)
    Recovery()
    Unknown2063()
    DisableAttackRestOfMove()
    XImpulseAcceleration(30)
    sprite('na203_50', 2)
    XImpulseAcceleration(80)
    sprite('na203_50', 2)
    XImpulseAcceleration(80)
    sprite('na203_03', 5)
    XImpulseAcceleration(0)
    sprite('na203_04', 5)


@State
def NmlAtk5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel(3)
        AirPushbackX(20000)
        AirPushbackY(-50000)
        PushbackX(19800)
        HardKnockdown(1)

        def upon_10():
            clearUponHandler(upon_10)
            SetActionMark(1)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')

        def upon_STATE_END():
            EndMomentum(1)
    sprite('na208_00', 2)
    EndMomentum(1)
    AddX(50000)
    sprite('na208_01', 2)
    SetInertia(24000)
    sprite('na208_02', 2)
    sprite('na208_03', 2)
    XImpulseAcceleration(0)
    Unknown1051(60)
    CommonSE('hit_m_slow')
    BeginBuffer('NmlAtk5A3rd')
    sprite('na208_04', 4)
    RefreshMultihit()
    RandomCommonVoiceline(2)
    LandingEffects(100, 1, 0)
    EndMomentum(1)
    sprite('na208_05', 3)
    Recovery()
    Unknown2063()
    sprite('na208_06', 3)
    if SLOT_2:
        BufferedOrPressedGoto('NmlAtk5A3rd')
    sprite('na208_07', 5)
    DisallowGoto('NmlAtk5A3rd')
    sprite('na208_08', 5)


@State
def NmlAtk5A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel(3)
        AttackP1(90)
        AirPushbackX(10000)
        AirPushbackY(14000)
        PushbackX(19800)
        HitLow(2)
        AttackAttributes('F')
        HitOrBlockCancel('NmlAtk5A4th')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        JumpCancel_(1)
        HitJumpCancel(1)
    sprite('na207_00', 2)
    sprite('na207_01', 4)
    PrivateSE('hit_l_middle')
    physicsXImpulse(20000)
    sprite('na207_02', 2)
    StartMultihit()
    SetInertia(20000)
    sprite('na207_03', 2)
    Unknown23054('na207_02', 2)
    RefreshMultihit()
    RandomCommonVoiceline(1)
    XImpulseAcceleration(0)
    sprite('na207_03', 2)
    Recovery()
    Unknown2063()
    Unknown1051(50)
    sprite('na207_04', 4)
    Unknown8010(100, 1, 0)
    sprite('na207_05', 5)
    sprite('na207_06', 5)


@State
def NmlAtk5A4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        JumpCancel_(0)
    sprite('na404_00', 3)
    sprite('na404_00', 3)
    sprite('na404_02', 6)
    if Unknown23145('NmlAtk5A3rd'):
        GFX_0('DanganD_CCA', 1)
    else:
        GFX_0('DanganD', 1)
    ScreenShake(10000, 0)
    Unknown1047(-10000)
    PrivateSE('na002')
    TagVoiceline(1, 'pna210_0', 'pna210_1', 'pna210_2', '')

    def upon_43():
        if SLOT_48 == 3020:
            Recovery()
            Unknown2063()
    sprite('na404_03', 6)
    sprite('na404_04', 14)
    sprite('na404_05', 7)
    sprite('na401_00', 6)


@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('NmlAtk5B2nd')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockJumpCancel(1)
        Unknown1112()
    sprite('na204_00', 3)
    sprite('na204_01', 3)
    sprite('na204_01', 2)
    ObjectUpon2(11, 102, 0)
    sprite('na204_02', 5)
    GFX_1('persona_enter_ply', 0)
    TagVoiceline(1, 'pna120_0', 'pna120_1', 'pna120_2', '')
    sprite('na204_03', 5)
    sprite('na204_04', 1)
    sprite('na204_04', 4)
    Recovery()
    Unknown2063()
    sprite('na204_03', 6)
    sprite('na204_04', 6)
    sprite('na204_03', 6)
    sprite('na204_00', 4)


@State
def NmlAtk5B2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        JumpCancel_(0)

        def upon_43():
            if SLOT_48 == 12:
                HitOrBlockCancel('NmlAtk5A')
                HitOrBlockCancel('NmlAtk2B')
                HitOrBlockCancel('NmlAtk2C')
                HitOrBlockCancel('CmnActCrushAttack')
                HitJumpCancel(1)
                HitOrBlockCancel('NmlAtk5B3rd')
                JumpCancel_(1)
            if SLOT_48 == 3020:
                Recovery()
                Unknown2063()
    sprite('na410_00', 4)
    sprite('na410_01', 4)
    ObjectUpon2(11, 103, 0)
    GFX_1('persona_enter_ply', 0)
    sprite('na410_02', 4)
    TagVoiceline(0, 'pna121_0', 'pna121_1', 'pna121_2', '')
    sprite('na410_03', 4)
    sprite('na410_02', 4)
    sprite('na410_03', 4)
    sprite('na410_02', 4)
    sprite('na410_03', 4)
    sprite('na410_02', 4)
    sprite('na410_03', 4)
    sprite('na410_04', 6)


@State
def NmlAtk5B3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('na205_00', 4)
    sprite('na205_01', 3)
    ObjectUpon2(11, 201, 0)
    sprite('na205_02', 3)
    GFX_1('persona_enter_ply', 0)
    sprite('na205_03', 3)
    sprite('na205_04', 3)
    sprite('na205_05', 3)
    sprite('na205_03', 3)
    sprite('na205_04', 3)
    Recovery()
    Unknown2063()
    sprite('na205_05', 3)
    sprite('na205_03', 4)
    sprite('na205_04', 4)
    sprite('na205_05', 4)
    sprite('na205_01', 4)
    sprite('na205_00', 4)


@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel(2)
        AirPushbackY(15000)
        HitOrBlockCancel('NmlAtk4A2nd')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('na200_00', 3)
    PrivateSE('hair')
    sprite('na200_01', 2)
    sprite('na200_50', 3)
    Unknown23054('na200_02', 2)
    RefreshMultihit()
    RandomCommonVoiceline(0)
    PrivateSE('hit_l_fast')
    sprite('na200_50', 3)
    Recovery()
    Unknown2063()
    DisableAttackRestOfMove()
    sprite('na200_03', 4)
    sprite('na200_04', 4)
    sprite('na200_05', 4)


@State
def NmlAtk4A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel(3)
        HitOrBlockCancel('NmlAtk4A3rd')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        StayAfterMovement(1, 0)
    sprite('na201_00', 3)
    sprite('na201_01', 4)
    PrivateSE('hit_l_middle')
    sprite('na201_02', 3)
    RandomCommonVoiceline(1)
    sprite('na201_03', 4)
    Recovery()
    Unknown2063()
    sprite('na201_04', 4)
    sprite('na201_05', 4)
    sprite('na201_06', 4)
    sprite('na201_07', 4)


@State
def NmlAtk4A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel(3)
        AttackP2(70)
        AirHitstunAnimation(AIR_TAILSPIN)
        GroundedHitstunAnimation(AIR_TAILSPIN)
        AirUntechableTime(30)
        AirPushbackX(12000)
        AirPushbackY(20000)

        def upon_10():
            clearUponHandler(upon_10)
            BeginBuffer('NmlAtk4A4th')
            BeginBuffer('NmlAtk5BEx')
            BeginBuffer('NmlAtk2BEx')
            BeginBuffer('NmlAtk2CEx')
            BeginBuffer('CmnActCrushAttackEx')

        def upon_LANDING():
            clearUponHandler(upon_LANDING)
            sendToLabel(1)
        HitOrBlockCancel('NmlAtk4A4th')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        JumpCancel_(0)
    sprite('na202_00', 1)
    sprite('na202_01', 4)
    physicsXImpulse(13500)
    physicsYImpulse(14000)
    setGravity(2000)
    sprite('na202_02', 8)
    PrivateSE('hit_m_slow')
    sprite('na202_03', 4)
    RefreshMultihit()
    RandomCommonVoiceline(2)
    sprite('na202_04', 32767)
    Recovery()
    label(1)
    sprite('na202_05', 3)
    BufferedOrPressedGoto('NmlAtk4A4th')
    BufferedOrPressedGoto('NmlAtk5BEx')
    BufferedOrPressedGoto('NmlAtk2BEx')
    BufferedOrPressedGoto('NmlAtk2CEx')
    BufferedOrPressedGoto('CmnActCrushAttackEx')
    JumpCancel_(1)
    EndMomentum(1)
    DisableAttackRestOfMove()
    sprite('na202_06', 5)
    Unknown2063()
    DisallowGoto('NmlAtk4A4th')
    DisallowGoto('NmlAtk5BEx')
    DisallowGoto('NmlAtk2BEx')
    DisallowGoto('NmlAtk2CEx')
    DisallowGoto('CmnActCrushAttackEx')
    sprite('na202_07', 5)
    sprite('na202_08', 3)


@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel(1)
        HitLow(2)
        AttackP1(90)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk4A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('na230_01', 3)
    sprite('na230_02', 3)
    Unknown1051(80)
    sprite('na230_04', 3)
    Unknown23054('na230_03', 3)
    PrivateSE('hit_l_fast')
    RefreshMultihit()
    RandomCommonVoiceline(0)
    sprite('na230_04', 2)
    DisableAttackRestOfMove()
    Recovery()
    Unknown2063()
    sprite('na230_02', 3)
    sprite('na230_01', 3)
    sprite('na230_00', 3)


@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockJumpCancel(1)
    sprite('na232_00', 2)
    sprite('na232_01', 2)
    sprite('na232_02', 3)
    ObjectUpon2(11, 104, 0)
    GFX_1('persona_enter_ply', 0)
    sprite('na232_03', 3)
    setInvincible(1)
    SpecificInvincibility('H')
    sprite('na232_04', 3)
    sprite('na232_05', 3)
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('na232_03', 3)
    sprite('na232_04', 3)
    sprite('na232_05', 3)
    sprite('na232_03', 3)
    sprite('na232_04', 3)
    sprite('na232_05', 3)
    sprite('na232_00', 5)


@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel(3)
        AttackP1(90)
        HitLow(2)
        AirHitstunAnimation(AIR_FACE_DOWN)
        GroundedHitstunAnimation(AIR_FACE_DOWN)
        AirPushbackX(3000)
        AirPushbackY(15000)
        AirUntechableTime(22)
    sprite('na211_00', 2)
    sprite('na211_01', 2)
    sprite('na211_02', 2)
    sprite('na211_03', 3)
    sprite('na211_04', 3)
    RefreshMultihit()
    SmartRandomVoiceline('pna107_0', 100, 'pna107_1', 100, 'pna107_2', 100,
        '', 0)
    PrivateSE('hit_l_middle')
    sprite('na211_04', 4)
    Recovery()
    Unknown2063()
    DisableAttackRestOfMove()
    sprite('na211_05', 4)
    sprite('na211_06', 4)
    EndAttack()
    sprite('na211_01', 3)
    sprite('na211_00', 3)


@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5A2nd')
        HitOrBlockCancel('NmlAtkAIR5A2ndex')
        HitOrBlockCancel('NmlAtkAIR5C')

        def upon_LANDING():
            ObjectUpon2(11, 302, 0)

        def upon_STATE_END():
            ObjectUpon2(11, 303, 0)
        Unknown4009(11)
    sprite('na254_00', 3)
    sprite('na254_01', 3)
    ObjectUpon2(11, 301, 0)
    sprite('na254_02', 6)
    GFX_1('persona_enter_ply', 0)
    SmartRandomVoiceline('pna103_0', 100, 'pna103_1', 100, 'pna103_2', 100,
        '', 0)
    sprite('na254_03', 5)
    sprite('na254_04', 5)
    Recovery()
    Unknown2063()
    sprite('na254_05', 5)
    sprite('na254_00', 4)


@State
def NmlAtkAIR5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel(3)
        AirUntechableTime(20)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('na251_00', 2)
    sprite('na251_01', 3)
    sprite('na251_03', 4)
    Unknown23054('na251_02', 3)
    RefreshMultihit()
    RandomCommonVoiceline(1)
    PrivateSE('hit_l_slow')
    sprite('na251_03', 4)
    Recovery()
    Unknown2063()
    DisableAttackRestOfMove()
    sprite('na251_04', 3)
    sprite('na251_05', 3)
    EndAttack()
    sprite('na251_00', 2)


@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5C')

        def upon_LANDING():
            ObjectUpon2(11, 302, 0)

        def upon_STATE_END():
            ObjectUpon2(11, 303, 0)
        Unknown4009(11)
    sprite('na254_00', 3)
    sprite('na254_01', 3)
    ObjectUpon2(11, 305, 0)
    sprite('na254_02', 6)
    GFX_1('persona_enter_ply', 0)
    SmartRandomVoiceline('pna103_0', 100, 'pna103_1', 100, 'pna103_2', 100,
        '', 0)
    sprite('na254_03', 5)
    sprite('na254_04', 5)
    Recovery()
    Unknown2063()
    sprite('na254_05', 5)
    sprite('na254_00', 4)
    EndAttack()


@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        HitOrBlockJumpCancel(1)
        JumpCancel_(0)

        def upon_43():
            if SLOT_48 == 12:
                JumpCancel_(1)
        ForcedLandingRecovery(9, 1)
    sprite('na255_00', 3)
    sprite('na255_01', 3)
    PushSpeedX()
    PushSpeedY()
    PushGravity()
    EndMomentum(1)
    sprite('na255_02', 12)
    ObjectUpon2(11, 304, 0)
    SmartRandomVoiceline('pna104_0', 100, 'pna104_1', 100, 'pna104_2', 100,
        '', 0)
    sprite('na255_03', 4)
    GFX_1('persona_enter_ply', 0)
    sprite('na255_04', 5)
    PopSpeedX()
    PopSpeedY()
    PopGravity()
    XImpulseAcceleration(85)
    YAccel(85)
    sprite('na255_05', 5)
    EndAttack()
    Recovery()
    Unknown2063()
    sprite('na255_01', 4)
    sprite('na255_00', 4)


@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        StayAfterMovement(1, 0)
    sprite('na210_00', 2)
    sprite('na210_01', 2)
    sprite('na210_02', 2)
    TagVoiceline(1, 'pna156_0', 'pna156_1', '', '')
    sprite('na210_03', 5)
    sprite('na210_04', 6)
    sprite('na210_05', 2)
    sprite('na210_06', 2)
    PrivateSE('hit_m_slow')
    sprite('na210_07', 3)
    RefreshMultihit()
    sprite('na210_08', 2)
    sprite('na210_09', 2)
    sprite('na210_10', 7)
    sprite('na210_11', 6)
    sprite('na210_12', 7)


@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        RunLoopUpon(upon_17, 180)

        def upon_17():
            clearUponHandler(upon_17)
            sendToLabel(11)

        def upon_LANDING():
            clearUponHandler(upon_LANDING)
            sendToLabel(10)
    sprite('na210_10', 7)
    sprite('na210_11', 7)
    sprite('na210_12', 8)
    sprite('na201_00', 3)
    sprite('na201_01', 4)
    PrivateSE('hit_l_middle')
    sprite('na201_02', 2)
    RefreshMultihit()
    TagVoiceline(1, 'pna157_0', 'pna157_1', '', '')
    sprite('na201_03', 3)
    sprite('na201_04', 3)
    sprite('na201_05', 3)
    EndAttack()
    sprite('na201_06', 3)
    sprite('na201_07', 2)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    label(10)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    spriteEnd()
    gotoLabel(10)
    label(11)
    sprite('keep', 1)


@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        DisableAttackRestOfMove()
        RunLoopUpon(upon_17, 180)

        def upon_17():
            clearUponHandler(upon_17)
            sendToLabel(1)
    sprite('na400_00', 3)
    AddX(-25000)
    RefreshMultihit()
    ObjectUpon2(11, 403, 0)
    sprite('na400_00', 4)
    sprite('na400_01', 4)
    sprite('na400_02', 3)
    sprite('na400_03', 4)
    GFX_0('ImpactReversal_CA', 1)
    Unknown4020(1)

    def RunOnObject_1():
        Unknown30048(1)
    PrivateSE('na003')
    ScreenShake(20000, 0)
    sprite('na400_05', 2)
    Unknown4020(0)
    sprite('na400_06', 2)
    sprite('na400_04', 4)
    sprite('na400_05', 4)
    sprite('na400_06', 4)
    sprite('na400_07', 3)
    sprite('na400_08', 3)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    label(10)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    spriteEnd()
    gotoLabel(10)
    label(1)
    sprite('keep', 1)


@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        UseSlashHitspark(1)
    sprite('na433_13', 3)
    sprite('na433_14', 3)
    sprite('na433_15', 7)
    sprite('na433_16', 2)
    sprite('na433_17', 2)
    GFX_0('Kick_line', 100)
    PrivateSE('slash_blade_middle')
    sprite('na433_18', 2)
    sprite('na433_20', 2)
    GFX_0('Zanzoh_kick', 100)
    Unknown23054('na433_19', 3)
    RefreshMultihit()
    TagVoiceline(1, 'pna158_0', 'pna158_1', '', '')
    sprite('na433_20', 15)
    DisableAttackRestOfMove()
    sprite('na433_21', 6)
    StayAfterMovement(1, 0)
    sprite('na433_22', 6)
    sprite('na433_23', 5)
    sprite('na433_24', 4)
    sprite('na433_25', 4)


@State
def CmnActCrushAttackExFinish():

    def upon_IMMEDIATE():
        Unknown30089(0)
        RunLoopUpon(upon_17, 60)

        def upon_17():
            clearUponHandler(upon_17)
            sendToLabel(1)
    label(0)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    spriteEnd()
    gotoLabel(0)
    label(1)
    sprite('na433_13', 3)
    sprite('na433_14', 3)
    sprite('na433_15', 7)
    sprite('na433_16', 2)
    sprite('na433_17', 2)
    GFX_0('Kick_line', 100)
    PrivateSE('slash_blade_middle')
    sprite('na433_18', 2)
    sprite('na433_20', 2)
    GFX_0('Zanzoh_kick', 100)
    Unknown23054('na433_19', 3)
    RefreshMultihit()
    TagVoiceline(1, 'pna158_0', 'pna158_1', '', '')
    sprite('na433_20', 15)
    DisableAttackRestOfMove()
    sprite('na433_21', 6)
    StayAfterMovement(1, 0)
    sprite('na433_22', 6)
    sprite('na433_23', 5)
    sprite('na433_24', 4)
    sprite('na433_25', 4)


@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
    sprite('null', 19)
    TeleportToObject(22)
    AbsoluteY(0)
    sprite('null', 1)
    Unknown30081()
    TeleportToObject(22)
    AddX(-1000000)
    physicsYImpulse(-4000)
    setGravity(0)
    SLOT_12 = SLOT_19
    XImpulseAcceleration(10)
    sprite('na407_02', 3)
    physicsXImpulse(35000)
    physicsYImpulse(23000)
    setGravity(2000)

    def upon_LANDING():
        clearUponHandler(upon_LANDING)
        sendToLabel(0)
    sprite('na407_02', 2)
    sprite('na407_02', 2)
    SetYCollisionFromOrigin(310)
    AddX(65000)
    sprite('na407_03', 2)
    StartMultihit()
    GFX_0('Tossin_atk1', 0)
    physicsXImpulse(22000)
    physicsYImpulse(17000)
    setGravity(3000)
    PrivateSE('runjump_stone_light')
    PrivateSE('hit_l_slow')
    sprite('na407_04', 2)
    GFX_0('Tossin_atk2', 100)
    callSubroutine('HaikyouEx0')
    sprite('na407_05', 2)
    callSubroutine('HaikyouEx0')
    sprite('na407_06', 2)
    callSubroutine('HaikyouEx0')
    sprite('na407_07', 2)
    callSubroutine('HaikyouEx0')
    XImpulseAcceleration(70)
    sprite('na407_08', 2)
    callSubroutine('HaikyouEx0')
    sprite('na407_09', 2)
    callSubroutine('HaikyouEx0')
    sprite('na407_10', 2)
    RefreshMultihit()
    PrivateSE('hit_l_slow')
    sprite('na407_11ex', 32767)
    label(0)
    sprite('na211_00', 3)
    EndMomentum(1)
    CrouchState(1)
    sprite('na211_01', 3)
    sprite('na010_01', 4)
    sprite('na010_00', 4)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    label(10)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    spriteEnd()
    gotoLabel(10)


@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
    sprite('na404_00', 5)
    sprite('na404_00', 6)
    sprite('na404_02', 6)
    ObjectUpon2(11, 101, 0)
    GFX_0('DanganDASS', 1)
    Unknown4020(1)
    ScreenShake(10000, 0)
    PrivateSE('na002')
    sprite('na404_03', 6)
    Unknown4020(0)
    sprite('na404_04', 6)
    sprite('na404_05', 7)
    sprite('na401_00', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 3)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    label(10)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    spriteEnd()
    gotoLabel(10)


@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('na433_13', 3)
    sprite('na433_14', 3)
    sprite('na433_15', 7)
    sprite('na433_16', 2)
    sprite('na433_17', 2)
    GFX_0('Kick_line', 100)
    PrivateSE('slash_blade_middle')
    sprite('na433_18', 2)
    sprite('na433_20', 2)
    GFX_0('Zanzoh_kick', 100)
    Unknown23054('na433_19', 3)
    RefreshMultihit()
    sprite('na433_20', 15)
    DisableAttackRestOfMove()
    sprite('na433_21', 6)
    StayAfterMovement(1, 0)
    sprite('na433_22', 6)
    sprite('na433_23', 5)
    sprite('na433_24', 4)
    sprite('na433_25', 4)


@State
def CmnActCrushAttackAssistExFinish():

    def upon_IMMEDIATE():
        Unknown30089(1)
        RunLoopUpon(upon_17, 60)

        def upon_17():
            clearUponHandler(upon_17)
            sendToLabel(1)
    label(0)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    spriteEnd()
    gotoLabel(0)
    label(1)
    sprite('na433_13', 3)
    sprite('na433_14', 3)
    sprite('na433_15', 7)
    sprite('na433_16', 2)
    sprite('na433_17', 2)
    GFX_0('Kick_line', 100)
    PrivateSE('slash_blade_middle')
    sprite('na433_18', 2)
    sprite('na433_20', 2)
    GFX_0('Zanzoh_kick', 100)
    Unknown23054('na433_19', 3)
    RefreshMultihit()
    sprite('na433_20', 15)
    DisableAttackRestOfMove()
    sprite('na433_21', 6)
    StayAfterMovement(1, 0)
    sprite('na433_22', 6)
    sprite('na433_23', 5)
    sprite('na433_24', 4)
    sprite('na433_25', 4)


@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('NmlAtkThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_EVERY_FRAME():
            if SLOT_18 == 7:
                Unknown8007(100, 1, 1)
                physicsXImpulse(18000)
            if SLOT_18 >= 7:
                XSpeed(440)
                if SLOT_12 >= 28000:
                    SLOT_12 = 28000
            if SLOT_18 >= 25:
                sendToLabel(1)
            if SLOT_18 >= 3:
                if SLOT_19 < 180000:
                    sendToLabel(1)
    sprite('na030_00', 7)
    sprite('na032_00', 2)
    label(0)
    sprite('na032_01', 4)
    physicsXImpulse(20000)
    sprite('na032_02', 4)
    XImpulseAcceleration(120)
    sprite('na032_03', 4)
    Unknown8006(100, 1, 1)
    sprite('na032_04', 4)
    XImpulseAcceleration(120)
    sprite('na032_05', 4)
    spriteEnd()
    gotoLabel(0)
    label(1)
    clearUponHandler(upon_EVERY_FRAME)
    sprite('na310_00', 1)
    EndMomentum(1)
    sprite('na310_01', 1)
    sprite('na310_01', 1)
    Unknown1051(50)
    sprite('na310_02', 3)
    RefreshMultihit()
    sprite('na310_03', 3)
    Voiceline('pna154')
    sprite('na310_04', 5)
    sprite('na310_03', 5)
    sprite('na310_01', 5)
    sprite('na310_00', 5)


@State
def NmlAtkThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel(1)
        Damage(0)
        AttackP1(100)
        AttackP2(100)
        Hitstun(70)
        AirUntechableTime(70)
        AirHitstunAnimation(STAGGER)
        GroundedHitstunAnimation(STAGGER)
        Crumple(70)
        Stagger(70)
        PushbackX(-3000)
        Hitstop(0)
        Unknown11050(5, '')
        HitAnywhere(0)
        DamageFromStateOnly('PNA_PersonaThrow')
        StayAfterMovement(1, 0)
        JumpCancel_(0)

        def upon_43():
            if SLOT_48 == 12:
                JumpCancel_(1)
    sprite('na310_02', 4)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    SetZLine(0, 80)
    sprite('na311_00', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('na311_50', 7)
    Unknown23054('na311_01', 2)
    RefreshMultihit()
    sprite('na204_02', 1)
    sprite('na204_02', 4)
    GFX_1('persona_enter_ply', 3)
    SmartRandomVoiceline('pna153', 100, '', 0, '', 0, '', 0)
    ObjectUpon2(11, 105, 0)
    sprite('na204_03', 4)
    sprite('na204_04', 4)
    sprite('na204_03', 4)
    sprite('na204_04', 4)
    sprite('na204_03', 4)
    sprite('na204_04', 4)
    sprite('na204_03', 4)
    sprite('na204_04', 4)
    sprite('na204_00', 4)


@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('NmlAtkBackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_EVERY_FRAME():
            if SLOT_18 == 7:
                Unknown8007(100, 1, 1)
                physicsXImpulse(18000)
            if SLOT_18 >= 7:
                XSpeed(440)
                if SLOT_12 >= 28000:
                    SLOT_12 = 28000
            if SLOT_18 >= 25:
                sendToLabel(1)
            if SLOT_18 >= 3:
                if SLOT_19 < 180000:
                    sendToLabel(1)
    sprite('na030_00', 7)
    sprite('na032_00', 2)
    label(0)
    sprite('na032_01', 4)
    physicsXImpulse(20000)
    sprite('na032_02', 4)
    XImpulseAcceleration(120)
    sprite('na032_03', 4)
    Unknown8006(100, 1, 1)
    sprite('na032_04', 4)
    XImpulseAcceleration(120)
    sprite('na032_05', 4)
    spriteEnd()
    gotoLabel(0)
    label(1)
    clearUponHandler(upon_EVERY_FRAME)
    sprite('na310_00', 1)
    EndMomentum(1)
    sprite('na310_01', 1)
    sprite('na310_01', 1)
    Unknown1051(50)
    sprite('na310_02', 3)
    RefreshMultihit()
    sprite('na310_03', 3)
    Voiceline('pna154')
    sprite('na310_04', 5)
    sprite('na310_03', 5)
    sprite('na310_01', 5)
    sprite('na310_00', 5)


@State
def NmlAtkBackThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel(1)
        Damage(0)
        AttackP1(100)
        AttackP2(100)
        Hitstun(70)
        AirUntechableTime(70)
        AirHitstunAnimation(STAGGER)
        GroundedHitstunAnimation(STAGGER)
        Crumple(70)
        Stagger(70)
        PushbackX(-40000)
        Hitstop(0)
        Unknown11050(5, '')
        HitAnywhere(0)
        DamageFromStateOnly('PNA_PersonaThrow')
        StayAfterMovement(1, 0)
        JumpCancel_(0)

        def upon_43():
            if SLOT_48 == 12:
                JumpCancel_(1)
    sprite('na310_02', 4)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    SetZLine(0, 80)
    sprite('na311_00', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('na311_50', 10)
    Unknown23054('na311_01', 2)
    RefreshMultihit()
    sprite('na311_50', 6)
    ForceFaceSprite()
    StartMultihit()
    sprite('na311_50', 1)
    ForceFaceSprite()
    sprite('na204_02', 1)
    sprite('na204_02', 4)
    GFX_1('persona_enter_ply', 3)
    SmartRandomVoiceline('pna153', 100, '', 0, '', 0, '', 0)
    ObjectUpon2(11, 105, 0)
    sprite('na204_03', 4)
    sprite('na204_04', 4)
    sprite('na204_03', 4)
    sprite('na204_04', 4)
    sprite('na204_03', 4)
    sprite('na204_04', 4)
    sprite('na204_03', 4)
    sprite('na204_04', 4)
    sprite('na204_00', 4)


@State
def KamaeBase():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('ShagekiFlexChain')
        PrivateSE('na000')
        Unknown11063(1)
        Unknown14083(0)
        Unknown30068(1)
        if SLOT_62:
            EnableAfterimage(1)
            Unknown3069(2)
            AfterimageColor_1(128, 0, 0, 0)
            AfterimageColor_2(0, 0, 0, 0)
            AfterimageMask_1(0, 4, 50, 160)
            AfterimageMask_2(0, 0, 0, 16)
            AfterimageSize_1(1010)
            AfterimageSize_2(900)

        def upon_EVERY_FRAME():
            if not SLOT_158:
                SLOT_52 = 1
            if not SLOT_21:
                SLOT_52 = 1
            if SLOT_52:
                if SLOT_53:
                    enterState('KamaeCancel')
    SLOT_51 = SLOT_61
    if SLOT_51 == 1:
        conditionalSendToLabel(1)
    if SLOT_51 == 2:
        conditionalSendToLabel(2)
    label(0)
    sprite('na401_52', 10)
    WhiffCancelEnable(1)
    GFX_0('GunKira', 2)
    sprite('keep', 70)
    SLOT_53 = 1
    sprite('keep', 32767)
    enterState('KamaeCancel')
    spriteEnd()
    ExitState()
    label(1)
    sprite('na401_53', 10)
    WhiffCancelEnable(1)
    GFX_0('GunKira', 2)
    sprite('keep', 70)
    SLOT_53 = 1
    sprite('keep', 32767)
    enterState('KamaeCancel')
    spriteEnd()
    ExitState()
    label(2)
    sprite('na401_54', 10)
    WhiffCancelEnable(1)
    GFX_0('GunKira', 2)
    sprite('keep', 70)
    SLOT_53 = 1
    sprite('keep', 32767)
    enterState('KamaeCancel')
    spriteEnd()
    ExitState()


@State
def KamaeA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        EndMomentum(1)
        SLOT_62 = 0
        SLOT_60 = 5
        SLOT_61 = 0
        Unknown11063(1)
    sprite('na401_00', 3)
    sprite('na401_01', 1)
    SmartRandomVoiceline('pna203_0', 100, 'pna203_1', 100, 'pna203_2', 100,
        '', 0)
    sprite('na401_01', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_01', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_01', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_02', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_02', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_02', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_02', 1)
    sprite('na401_03', 3)
    sprite('na401_03', 32767)
    enterState('KamaeBase')


@State
def ShagekiA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        NoAttackDuringAction(1)
        Unknown14083(0)
        Unknown30068(1)

        def upon_43():
            if SLOT_48 == 4001:
                Unknown14083(1)
            if SLOT_48 == 3008:
                SLOT_52 = 1
            if SLOT_48 == 3016:
                SLOT_52 = 0
        if SLOT_62:
            EnableAfterimage(1)
            Unknown3069(2)
            AfterimageColor_1(128, 0, 0, 0)
            AfterimageColor_2(0, 0, 0, 0)
            AfterimageMask_1(0, 4, 50, 160)
            AfterimageMask_2(0, 0, 0, 16)
            AfterimageSize_1(1010)
            AfterimageSize_2(900)
    SLOT_51 = SLOT_61
    SLOT_61 = 3
    if SLOT_51 == 1:
        conditionalSendToLabel(1)
    if SLOT_51 == 2:
        conditionalSendToLabel(2)
    if SLOT_51 == 3:
        conditionalSendToLabel(3)
    sprite('na401_03', 2)
    spriteEnd()
    gotoLabel(16)
    label(1)
    sprite('na401_50', 2)
    sprite('na401_03', 4)
    sprite('na401_52', 2)
    spriteEnd()
    gotoLabel(16)
    label(2)
    sprite('na401_51', 2)
    sprite('na401_03', 4)
    sprite('na401_52', 2)
    spriteEnd()
    gotoLabel(16)
    label(3)
    sprite('na401_03', 2)
    spriteEnd()
    gotoLabel(16)
    label(16)
    if SLOT_60 <= 1:
        conditionalSendToLabel(17)
    sprite('na401_52', 1)
    if SLOT_60 == 5:
        SmartRandomVoiceline('pna207_0', 100, 'pna207_1', 100, 'pna207_2', 
            100, '', 0)
    sprite('na404_00', 2)
    SLOT_60 = SLOT_60 + -1
    SLOT_59 = SLOT_59 + 1
    GFX_0('Dangan', 1)
    ObjectUpon2(1, 3010, 0)
    PrivateSE('na001')
    sprite('na404_01', 2)
    WhiffCancelEnable(1)
    WhiffCancel('ShagekiA')
    sprite('na404_00', 1)
    if not SLOT_52:
        gotoLabel(16)
    sprite('na404_00', 3)
    sprite('na401_03', 3)
    sprite('na401_03', 3)
    WhiffCancelEnable(0)
    sprite('na401_03', 32767)
    enterState('KamaeBase')
    spriteEnd()
    ExitState()
    label(17)
    WhiffCancelEnable(0)
    sprite('na404_00', 1)
    sprite('na404_00', 2)
    SLOT_60 = SLOT_60 + -1
    SLOT_59 = SLOT_59 + 1
    GFX_0('DanganLastA', 1)
    ScreenShake(10000, 0)
    Unknown1047(-10000)
    PrivateSE('na002')
    sprite('na404_02', 3)
    sprite('na404_03', 3)
    sprite('na404_04', 8)
    sprite('na404_05', 4)
    sprite('na404_06', 4)
    sprite('na401_03', 3)
    enterState('KamaeCancel')
    spriteEnd()
    ExitState()


@State
def ShagekiB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        NoAttackDuringAction(1)
        Unknown14083(0)
        Unknown30068(1)

        def upon_43():
            if SLOT_48 == 4001:
                Unknown14083(1)
            if SLOT_48 == 3008:
                SLOT_52 = 1
        if SLOT_62:
            EnableAfterimage(1)
            Unknown3069(2)
            AfterimageColor_1(128, 0, 0, 0)
            AfterimageColor_2(0, 0, 0, 0)
            AfterimageMask_1(0, 4, 50, 160)
            AfterimageMask_2(0, 0, 0, 16)
            AfterimageSize_1(1010)
            AfterimageSize_2(900)
    SLOT_51 = SLOT_61
    SLOT_61 = 1
    if SLOT_51 == 1:
        conditionalSendToLabel(1)
    if SLOT_51 == 2:
        conditionalSendToLabel(2)
    if SLOT_51 == 3:
        conditionalSendToLabel(3)
    sprite('na401_50', 2)
    spriteEnd()
    gotoLabel(16)
    label(1)
    sprite('na405_00', 2)
    spriteEnd()
    gotoLabel(16)
    label(2)
    sprite('na401_50', 2)
    sprite('na405_00', 4)
    sprite('na401_53', 2)
    spriteEnd()
    gotoLabel(16)
    label(3)
    sprite('na401_50', 2)
    sprite('na405_00', 4)
    sprite('na401_53', 2)
    spriteEnd()
    gotoLabel(16)
    label(16)
    if SLOT_60 <= 1:
        conditionalSendToLabel(17)
    sprite('na401_53', 1)
    if SLOT_60 == 5:
        SmartRandomVoiceline('pna208_0', 100, 'pna208_1', 100, 'pna208_2', 
            100, '', 0)
    sprite('na405_01', 2)
    SLOT_60 = SLOT_60 + -1
    SLOT_59 = SLOT_59 + 1
    GFX_0('Dangan', 1)
    ObjectUpon2(1, 3011, 0)
    PrivateSE('na001')
    sprite('na405_02', 2)
    WhiffCancelEnable(1)
    WhiffCancel('ShagekiB')
    sprite('na405_00', 1)
    if not SLOT_52:
        gotoLabel(16)
    sprite('na405_00', 3)
    sprite('na405_00', 3)
    sprite('na405_00', 3)
    WhiffCancelEnable(0)
    sprite('na405_00', 32767)
    enterState('KamaeBase')
    ExitState()
    label(17)
    WhiffCancelEnable(0)
    sprite('na405_01', 1)
    sprite('na405_01', 2)
    SLOT_60 = SLOT_60 + -1
    SLOT_59 = SLOT_59 + 1
    GFX_0('DanganLastB', 1)
    ScreenShake(10000, 0)
    Unknown1047(-10000)
    PrivateSE('na002')
    sprite('na404_02', 3)
    sprite('na404_03', 3)
    sprite('na404_04', 10)
    sprite('na404_05', 5)
    sprite('na404_06', 5)
    sprite('na401_03', 3)
    enterState('KamaeCancel')
    spriteEnd()
    ExitState()


@State
def ShagekiC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        NoAttackDuringAction(1)
        Unknown14083(0)
        Unknown30068(1)

        def upon_43():
            if SLOT_48 == 4001:
                Unknown14083(1)
            if SLOT_48 == 3008:
                SLOT_52 = 1
        if SLOT_62:
            EnableAfterimage(1)
            Unknown3069(2)
            AfterimageColor_1(128, 0, 0, 0)
            AfterimageColor_2(0, 0, 0, 0)
            AfterimageMask_1(0, 4, 50, 160)
            AfterimageMask_2(0, 0, 0, 16)
            AfterimageSize_1(1010)
            AfterimageSize_2(900)
    SLOT_51 = SLOT_61
    SLOT_61 = 2
    if SLOT_51 == 1:
        conditionalSendToLabel(1)
    if SLOT_51 == 2:
        conditionalSendToLabel(2)
    if SLOT_51 == 3:
        conditionalSendToLabel(3)
    sprite('na401_51', 2)
    spriteEnd()
    gotoLabel(16)
    label(1)
    sprite('na401_51', 2)
    sprite('na406_00', 4)
    sprite('na401_54', 2)
    spriteEnd()
    gotoLabel(16)
    label(2)
    sprite('na406_00', 2)
    spriteEnd()
    gotoLabel(16)
    label(3)
    sprite('na401_51', 2)
    sprite('na406_00', 4)
    sprite('na401_54', 2)
    spriteEnd()
    gotoLabel(16)
    label(16)
    if SLOT_60 <= 1:
        conditionalSendToLabel(17)
    sprite('na401_54', 1)
    if SLOT_60 == 5:
        SmartRandomVoiceline('pna208_0', 100, 'pna208_1', 100, 'pna208_2', 
            100, '', 0)
    sprite('na406_01', 2)
    SLOT_60 = SLOT_60 + -1
    SLOT_59 = SLOT_59 + 1
    GFX_0('Dangan', 1)
    ObjectUpon2(1, 3019, 0)
    PrivateSE('na001')
    sprite('na406_02', 2)
    WhiffCancelEnable(1)
    WhiffCancel('ShagekiC')
    sprite('na406_00', 1)
    if not SLOT_52:
        gotoLabel(16)
    sprite('na406_00', 3)
    sprite('na406_00', 3)
    sprite('na406_00', 3)
    WhiffCancelEnable(0)
    sprite('na406_00', 32767)
    enterState('KamaeBase')
    ExitState()
    label(17)
    WhiffCancelEnable(0)
    sprite('na406_01', 1)
    sprite('na406_01', 2)
    SLOT_60 = SLOT_60 + -1
    SLOT_59 = SLOT_59 + 1
    GFX_0('DanganLastC', 1)
    ScreenShake(10000, 0)
    Unknown1047(-10000)
    PrivateSE('na002')
    sprite('na404_02', 3)
    sprite('na404_03', 3)
    sprite('na404_04', 7)
    sprite('na404_05', 4)
    sprite('na404_06', 4)
    sprite('na401_03', 3)
    enterState('KamaeCancel')
    spriteEnd()
    ExitState()


@State
def KamaeCancel():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown14083(0)
        Unknown30068(1)
        Unknown11063(1)
        if SLOT_62:
            EnableAfterimage(1)
            Unknown3069(2)
            AfterimageColor_1(128, 0, 0, 0)
            AfterimageColor_2(0, 0, 0, 0)
            AfterimageMask_1(0, 4, 50, 160)
            AfterimageMask_2(0, 0, 0, 16)
            AfterimageSize_1(1010)
            AfterimageSize_2(900)

        def upon_STATE_END():
            SLOT_62 = 0
    sprite('na401_02', 5)
    SmartRandomVoiceline('pna211_0', 100, 'pna211_1', 100, 'pna211_2', 100,
        '', 0)
    sprite('na401_01', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_01', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_01', 1)
    sprite('na401_01', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)


@State
def KamaeEX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        SLOT_61 = 0
        Unknown14083(0)
        Unknown30068(1)
        Unknown11063(1)
        if SLOT_62:
            EnableAfterimage(1)
            Unknown3069(2)
            AfterimageColor_1(128, 0, 0, 0)
            AfterimageColor_2(0, 0, 0, 0)
            AfterimageMask_1(0, 4, 50, 160)
            AfterimageMask_2(0, 0, 0, 16)
            AfterimageSize_1(1010)
            AfterimageSize_2(900)
    sprite('na403_00', 3)
    sprite('na403_01', 2)
    SmartRandomVoiceline('pna205_0', 100, 'pna205_1', 100, 'pna205_2', 100,
        '', 0)
    physicsXImpulse(30000)
    EnableCollision(0)
    setInvincible(1)
    SpecificInvincibility('P')
    sprite('na403_02', 1)
    XImpulseAcceleration(160)
    sprite('na403_03', 1)
    sprite('na403_04', 2)
    sprite('na403_05', 2)
    sprite('na403_06', 1)
    sprite('na403_06', 1)
    EndMomentum(1)
    SetInertia(32000)
    sprite('na403_07', 2)
    callSubroutine('HaikyouEx0')
    sprite('na403_08', 2)
    EnableCollision(1)
    callSubroutine('HaikyouEx0')
    sprite('na403_09', 2)
    ForceFaceSprite()
    sprite('na403_09', 1)
    callSubroutine('HaikyouEx0')
    sprite('na403_10', 2)
    callSubroutine('HaikyouEx0')
    sprite('na403_11', 1)
    callSubroutine('HaikyouEx0')
    setInvincible(0)
    sprite('na403_11', 1)
    callSubroutine('HaikyouEx0')
    EndMomentum(1)
    sprite('na403_12', 2)
    WhiffCancelEnable(1)
    SLOT_60 = 5
    sprite('na401_03', 32767)
    enterState('KamaeBase')


@State
def BanditRevolverB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel(4)
        Damage(1000)
        AttackP1(80)
        SingleProration(1)
        GroundedHitstunAnimation(AIR_VERTICAL)
        AirHitstunAnimation(AIR_VERTICAL)
        AirPushbackX(24000)
        AirPushbackY(20000)
        AirUntechableTime(30)
        StayAfterMovement(1, 0)
        SLOT_60 = 5
        uponSendToLabel(upon_LANDING, 9)
        SLOT_62 = 0
    sprite('na407_00', 5)
    sprite('na407_01', 5)
    sprite('na407_02', 3)
    GFX_0('Jumpsmoke', 0)
    AddX(65000)
    ScreenShake(10000, 0)
    SmartRandomVoiceline('pna213_0', 100, 'pna213_1', 100, 'pna213_2', 100,
        '', 0)
    sprite('na407_03', 6)
    GFX_0('Tossin_atk1', 0)
    RefreshMultihit()
    physicsXImpulse(31000)
    physicsYImpulse(22000)
    setGravity(2000)
    PrivateSE('runjump_stone_light')
    PrivateSE('hit_l_slow')
    Unknown23087(30000)
    sprite('na407_04', 2)
    callSubroutine('HaikyouEx0')
    sprite('na407_05', 2)
    callSubroutine('HaikyouEx0')
    sprite('na407_06', 2)
    GFX_0('Tossin_atk2', 100)
    callSubroutine('HaikyouEx0')
    sprite('na407_07', 2)
    callSubroutine('HaikyouEx0')
    sprite('na407_08', 2)
    callSubroutine('HaikyouEx0')
    sprite('na407_09', 2)
    callSubroutine('HaikyouEx0')
    sprite('na407_10', 3)
    SLOT_61 = 0
    RefreshMultihit()
    AirPushbackX(19000)
    AirPushbackY(-90000)
    YImpulseBeforeWallbounce(0)
    GroundBounce(1)
    BouncePercentage(20)
    AirHitstunAfterWallbounce(60)
    EnemyHitstopAddition(0, -4, 5)
    AttackAttributes('H')
    HitOverhead(2)
    PrivateSE('hit_l_slow')
    sprite('na407_11', 3)
    Recovery()
    sprite('na402_05', 32767)
    label(9)
    sprite('na402_06', 4)
    LandingEffects(100, 1, 1)
    EndMomentum(1)
    ForceFaceSprite()
    Unknown23087(-1)
    sprite('na401_03', 32767)
    enterState('KamaeBase')


@State
def AirBanditRevolverA():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackLevel(4)
        Damage(1000)
        AttackP1(80)
        SingleProration(1)
        GroundedHitstunAnimation(AIR_VERTICAL)
        AirHitstunAnimation(AIR_VERTICAL)
        AirUntechableTime(30)
        AirPushbackX(21000)
        AirPushbackY(16000)
        clearUponHandler(upon_LANDING)
        SLOT_62 = 0
    sprite('na407_02', 4)
    sprite('na407_03', 4)
    StartMultihit()
    physicsXImpulse(22000)
    physicsYImpulse(20000)
    setGravity(2000)
    PrivateSE('runjump_stone_light')
    PrivateSE('hit_l_slow')
    SmartRandomVoiceline('pna212_0', 100, 'pna212_1', 100, 'pna212_2', 100,
        '', 0)
    uponSendToLabel(upon_LANDING, 9)
    sprite('na407_03', 3)
    GFX_0('Tossin_atk1', 0)
    RefreshMultihit()
    sprite('na407_04', 2)
    GFX_0('Tossin_atk2', 100)
    sprite('na407_05', 2)
    sprite('na407_06', 2)
    sprite('na407_07', 2)
    XImpulseAcceleration(80)
    sprite('na407_08', 2)
    sprite('na407_09', 2)
    sprite('na407_10', 6)
    RefreshMultihit()
    AirPushbackX(29000)
    AirPushbackY(-71000)
    HardKnockdown(1)
    HitOverhead(2)
    PrivateSE('hit_l_slow')
    sprite('na407_11ex', 32767)
    Recovery()
    label(9)
    sprite('na211_00', 4)
    LandingEffects(100, 1, 1)
    Recovery()
    EndMomentum(1)
    CrouchState(1)
    sprite('na211_01', 12)


@State
def AirBanditRevolverB():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackLevel(4)
        Damage(1000)
        AttackP1(80)
        SingleProration(1)
        GroundedHitstunAnimation(AIR_VERTICAL)
        AirHitstunAnimation(AIR_VERTICAL)
        AirPushbackX(24000)
        AirPushbackY(20000)
        AirUntechableTime(30)
        StayAfterMovement(1, 0)
        SLOT_60 = 5
        clearUponHandler(upon_LANDING)
        SLOT_62 = 0
    sprite('na407_02', 4)
    sprite('na407_02', 4)
    EndMomentum(1)
    sprite('na407_03', 4)
    StartMultihit()
    physicsXImpulse(22000)
    physicsYImpulse(28000)
    setGravity(2000)
    PrivateSE('runjump_stone_light')
    PrivateSE('hit_l_slow')
    SmartRandomVoiceline('pna212_0', 100, 'pna212_1', 100, 'pna212_2', 100,
        '', 0)
    uponSendToLabel(upon_LANDING, 9)
    sprite('na407_03', 6)
    GFX_0('Tossin_atk1', 0)
    RefreshMultihit()
    sprite('na407_04', 2)
    callSubroutine('HaikyouEx0')
    sprite('na407_05', 2)
    callSubroutine('HaikyouEx0')
    sprite('na407_06', 2)
    GFX_0('Tossin_atk2', 100)
    callSubroutine('HaikyouEx0')
    sprite('na407_07', 2)
    callSubroutine('HaikyouEx0')
    sprite('na407_08', 2)
    callSubroutine('HaikyouEx0')
    sprite('na407_09', 2)
    callSubroutine('HaikyouEx0')
    sprite('na407_10', 6)
    SLOT_61 = 0
    RefreshMultihit()
    AirPushbackX(29000)
    AirPushbackY(-90000)
    YImpulseBeforeWallbounce(0)
    GroundBounce(1)
    BouncePercentage(20)
    AirHitstunAfterWallbounce(60)
    EnemyHitstopAddition(0, -4, 5)
    AttackAttributes('H')
    HitOverhead(2)
    PrivateSE('hit_l_slow')
    sprite('na407_11', 3)
    Recovery()
    sprite('na402_05', 32767)
    label(9)
    sprite('na402_06', 4)
    LandingEffects(100, 1, 1)
    Recovery()
    EndMomentum(1)
    ForceFaceSprite()
    sprite('na401_03', 32767)
    enterState('KamaeBase')


@State
def AirBanditRevolverEX():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackDefaults_AirSpecial()
        AttackLevel(4)
        Damage(1300)
        AttackP1(80)
        SingleProration(1)
        GroundedHitstunAnimation(AIR_VERTICAL)
        AirHitstunAnimation(AIR_VERTICAL)
        AirPushbackX(24000)
        AirPushbackY(20000)
        AirUntechableTime(30)
        MinimumDamage(10)
        Unknown30065(0)
        StayAfterMovement(1, 0)
        SLOT_60 = 5
        clearUponHandler(upon_LANDING)
        SLOT_62 = 0
    sprite('na407_02', 4)
    sprite('na407_03', 4)
    Unknown23125()
    ConsumeSuperMeter(-5000)
    SLOT_62 = 1
    StartMultihit()
    physicsXImpulse(25000)
    physicsYImpulse(28000)
    setGravity(2000)
    PrivateSE('runjump_stone_light')
    PrivateSE('hit_l_slow')
    SmartRandomVoiceline('pna212_0', 100, 'pna212_1', 100, 'pna212_2', 100,
        '', 0)
    uponSendToLabel(upon_LANDING, 9)
    sprite('na407_03', 6)
    GFX_0('Tossin_atk1', 0)
    RefreshMultihit()
    sprite('na407_04', 2)
    callSubroutine('HaikyouEx0')
    sprite('na407_05', 2)
    callSubroutine('HaikyouEx0')
    sprite('na407_06', 2)
    GFX_0('Tossin_atk2', 100)
    callSubroutine('HaikyouEx0')
    sprite('na407_07', 2)
    callSubroutine('HaikyouEx0')
    sprite('na407_08', 2)
    callSubroutine('HaikyouEx0')
    sprite('na407_09', 2)
    callSubroutine('HaikyouEx0')
    sprite('na407_10', 6)
    SLOT_61 = 0
    RefreshMultihit()
    AirPushbackX(29000)
    AirPushbackY(-71000)
    YImpulseBeforeWallbounce(0)
    GroundBounce(1)
    BouncePercentage(50)
    AirHitstunAfterWallbounce(60)
    EnemyHitstopAddition(0, 0, 5)
    AttackAttributes('H')
    HitOverhead(2)
    PrivateSE('hit_l_slow')
    sprite('na407_11', 32767)
    Recovery()
    label(9)
    sprite('na211_00', 2)
    LandingEffects(100, 1, 1)
    Recovery()
    EndMomentum(1)
    CrouchState(1)
    sprite('na211_01', 11)


@State
def WalkingShotEX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown14083(1)
        SLOT_62 = 1
        WhiffCancel('WalkingShotKickEX')
        WhiffCancel('KamaeEX')

        def upon_EVERY_FRAME():
            if SLOT_51:
                if SLOT_52:
                    SLOT_52 = SLOT_52 + -1
                elif CheckInput(INPUT_HOLD_A):
                    if not SLOT_53 >= 5:
                        SLOT_52 = 8
                        SLOT_53 = SLOT_53 + 1
                        SLOT_59 = SLOT_59 + 1
                        GFX_0('DanganUltimate', 1)
                        ScreenShake(10000, 0)
            if CheckInput(INPUT_HOLD_B):
                if not SLOT_53 >= 5:
                    SLOT_52 = 8
                    SLOT_53 = SLOT_53 + 1
                    SLOT_59 = SLOT_59 + 1
                    GFX_0('DanganUltimate', 1)
                    ScreenShake(10000, 0)


    if SLOT_54:
        if SLOT_18 == 240:
            sendToLabel(9)
        if not SLOT_158:
            clearUponHandler(upon_EVERY_FRAME)
            sendToLabel(9)
        if not SLOT_21:
            clearUponHandler(upon_EVERY_FRAME)
            sendToLabel(9)
    endUpon()
    sprite('na433_00', 3)
    sprite('na433_01', 3)
    Unknown23125()
    ConsumeSuperMeter(-5000)
    TagVoiceline(1, 'pna219_0', 'pna219_1', '', '')
    sprite('na433_02', 3)
    WhiffCancelEnable(1)
    sprite('na433_03', 5)
    physicsXImpulse(7000)
    label(0)
    sprite('na433_04', 7)
    SLOT_51 = 1
    SLOT_54 = 1
    sprite('na433_05', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('na433_06', 7)
    sprite('na433_07', 7)
    sprite('na433_08', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('na433_09', 7)
    spriteEnd()
    gotoLabel(0)
    label(9)
    sprite('na433_10', 6)
    EndMomentum(1)
    clearUponHandler(upon_EVERY_FRAME)
    WhiffCancelEnable(0)
    SLOT_51 = 0
    SLOT_54 = 0
    sprite('na433_11', 1)
    sprite('na433_11', 1)
    callSubroutine('HaikyouEx0')
    sprite('na433_11', 1)
    callSubroutine('HaikyouEx0')
    sprite('na433_11', 1)
    callSubroutine('HaikyouEx0')
    sprite('na433_11', 1)
    callSubroutine('HaikyouEx0')
    sprite('na433_11', 1)
    callSubroutine('HaikyouEx0')
    sprite('na433_12', 6)
    endState()
    endState()


@State
def WalkingShotKickEX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel(5)
        Damage(2500)
        AttackP1(80)
        AttackP2(80)
        Hitstop(30)
        GroundedHitstunAnimation(AIR_BLOWBACK)
        AirHitstunAnimation(AIR_BLOWBACK)
        AirUntechableTime(70)
        AirPushbackX(75000)
        AirPushbackY(35000)
        WallbounceReboundTime(20)
        Wallstick(1)
        WallstickDuration(45)
        AirHitstunAfterWallbounce(70)
        MinimumDamage(10)
        Unknown30065(0)
        Unknown30068(1)
        ForceFaceSprite()
        EnableAfterimage(1)
        Unknown3069(2)
        AfterimageColor_1(128, 0, 0, 0)
        AfterimageColor_2(0, 0, 0, 0)
        AfterimageMask_1(0, 4, 50, 160)
        AfterimageMask_2(0, 0, 0, 16)
        AfterimageSize_1(1010)
        AfterimageSize_2(900)

        def upon_12():
            ScreenShake(50000, 0)
        setInvincible(1)
    sprite('na433_13', 1)
    sprite('na433_14', 2)
    TagVoiceline(0, 'pna220_0', 'pna220_1', '', '')
    sprite('na433_15', 4)
    sprite('na433_16', 1)
    sprite('na433_17', 1)
    GFX_0('Kick_line', 100)
    PrivateSE('slash_blade_middle')
    sprite('na433_18', 1)
    sprite('na433_20', 2)
    GFX_0('Zanzoh_kick', 100)
    RefreshMultihit()
    sprite('na433_20', 10)
    DisableAttackRestOfMove()
    setInvincible(0)
    sprite('na433_21', 6)
    StayAfterMovement(1, 0)
    sprite('na433_22', 6)
    sprite('na433_23', 5)
    sprite('na433_24', 1)
    sprite('na433_24', 1)
    sprite('na433_24', 1)
    sprite('na433_25', 1)
    callSubroutine('HaikyouEx0')
    sprite('na433_25', 1)
    callSubroutine('HaikyouEx0')
    sprite('na433_25', 1)
    callSubroutine('HaikyouEx0')
    sprite('na433_25', 1)
    callSubroutine('HaikyouEx0')
    sprite('na433_25', 1)
    callSubroutine('HaikyouEx0')


@State
def TrapA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11063(1)

        def upon_STATE_END():
            SLOT_8 = 0
    sprite('na408_00', 4)
    sprite('na408_01', 4)
    sprite('na408_02', 4)
    PrivateSE('na004')
    sprite('na408_03', 7)
    ObjectUpon2(11, 401, 0)
    SLOT_8 = 1
    callSubroutine('Shot_Stack')
    GFX_0('TrapMatome', 103)
    RegisterObject(4, 1)
    sprite('na408_02', 7)
    Recovery()
    sprite('na408_01', 5)
    sprite('na408_00', 5)


@State
def TrapB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11063(1)
    sprite('na408_00', 4)
    sprite('na408_01', 4)
    sprite('na408_02', 4)
    PrivateSE('na004')
    sprite('na408_03', 7)
    ObjectUpon2(11, 401, 0)
    callSubroutine('Shot_Stack2')
    GFX_0('TrapMatome', 103)
    RegisterObject(7, 1)
    sprite('na408_02', 7)
    Recovery()
    sprite('na408_01', 5)
    sprite('na408_00', 5)


@State
def TrapEX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11063(1)

        def upon_STATE_END():
            SLOT_8 = 0
    sprite('na408_00', 3)
    sprite('na408_01', 3)
    sprite('na408_02', 3)
    ObjectUpon2(11, 401, 0)
    Unknown23125()
    ConsumeSuperMeter(-5000)
    callSubroutine('Shot_Stack2')
    GFX_0('TrapMatome', 103)
    RegisterObject(7, 1)
    ObjectUpon2(7, 3004, 0)
    PrivateSE('na004')
    SLOT_8 = 1
    callSubroutine('Shot_Stack')
    GFX_0('TrapMatome', 103)
    RegisterObject(4, 1)
    ObjectUpon2(4, 3004, 0)
    sprite('na408_03', 7)
    Recovery()
    sprite('na408_02', 7)
    sprite('na408_01', 5)
    sprite('na408_00', 6)


@State
def AirTrapA():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        Unknown11063(1)

        def upon_STATE_END():
            SLOT_8 = 0
    sprite('na409_00', 3)
    sprite('na409_01', 3)
    PushSpeedX()
    PushSpeedY()
    PushGravity()
    EndMomentum(1)
    ForcedLandingRecovery(5, 1)
    sprite('na409_02', 3)
    sprite('na409_03', 7)
    ObjectUpon2(11, 401, 0)
    SLOT_8 = 1
    callSubroutine('Shot_Stack')
    GFX_0('TrapMatome', 103)
    RegisterObject(4, 1)
    sprite('na409_03', 4)
    sprite('na409_04', 4)
    Recovery()
    PopSpeedX()
    PopSpeedY()
    PopGravity()
    XImpulseAcceleration(85)
    YAccel(85)
    sprite('na409_05', 4)


@State
def AirTrapB():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        Unknown11063(1)
    sprite('na409_00', 3)
    sprite('na409_01', 3)
    PushSpeedX()
    PushSpeedY()
    PushGravity()
    EndMomentum(1)
    ForcedLandingRecovery(5, 1)
    sprite('na409_02', 3)
    sprite('na409_03', 6)
    ObjectUpon2(11, 401, 0)
    callSubroutine('Shot_Stack2')
    GFX_0('TrapMatome', 103)
    RegisterObject(7, 1)
    sprite('na409_03', 4)
    sprite('na409_04', 4)
    PopSpeedX()
    PopSpeedY()
    PopGravity()
    XImpulseAcceleration(85)
    YAccel(85)
    Recovery()
    sprite('na409_05', 5)


@State
def AirTrapEX():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        Unknown11063(1)

        def upon_STATE_END():
            SLOT_8 = 0
    sprite('na409_00', 3)
    sprite('na409_01', 3)
    PushSpeedX()
    PushSpeedY()
    PushGravity()
    EndMomentum(1)
    ForcedLandingRecovery(5, 1)
    sprite('na409_02', 5)
    ObjectUpon2(11, 401, 0)
    Unknown23125()
    ConsumeSuperMeter(-5000)
    callSubroutine('Shot_Stack2')
    GFX_0('TrapMatome', 103)
    RegisterObject(7, 1)
    ObjectUpon2(7, 3004, 0)
    SLOT_8 = 1
    callSubroutine('Shot_Stack')
    GFX_0('TrapMatome', 103)
    RegisterObject(4, 1)
    ObjectUpon2(4, 3004, 0)
    sprite('na409_03', 2)
    PopSpeedX()
    PopSpeedY()
    PopGravity()
    XImpulseAcceleration(85)
    YAccel(85)
    Recovery()
    sprite('na409_04', 2)
    sprite('na409_05', 2)


@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024()
        Unknown11063(1)
    sprite('na400_00', 2)
    GFX_0('BarrierJizoku', 0)
    GuardPoint_(1)
    Unknown22031(4, 14)
    SmartRandomVoiceline('pna200_0', 100, 'pna200_1', 100, 'pna200_2', 100,
        '', 0)
    PrivateSE('na005')

    def upon_52():
        GuardPoint_(0)
        clearUponHandler(upon_52)
        if SLOT_19 <= 350000:
            sendToLabel(1)
        else:
            sendToLabel(0)
    sprite('na400_00', 1)
    ObjectUpon2(11, 403, 0)
    sprite('na400_01', 3)
    sprite('na400_02', 3)
    sprite('na400_00', 3)
    sprite('na400_01', 3)
    sprite('na400_02', 3)
    sprite('na400_00', 3)
    sprite('na400_01', 3)
    sprite('na400_02', 1)
    sprite('na400_02', 2)
    Unknown21015('BarrierJizoku', 3012, 0)
    clearUponHandler(upon_52)
    setInvincible(0)
    sprite('na400_00', 3)
    sprite('na400_01', 3)
    sprite('na400_02', 3)
    sprite('na400_06', 3)
    sprite('na400_07', 3)
    sprite('na400_08', 3)
    ExitState()
    label(1)
    clearUponHandler(upon_52)
    sprite('na400_00', 4)
    sprite('na400_01', 3)
    sprite('na400_02', 2)
    sprite('na400_03', 4)
    GFX_0('ImpactReversal', 1)
    SLOT_51 = 0
    PrivateSE('na003')
    ScreenShake(20000, 0)
    SmartRandomVoiceline('pna201_0', 100, 'pna201_1', 100, 'pna201_2', 100,
        '', 0)
    sprite('na400_05', 2)
    setInvincible(0)
    sprite('na400_06', 2)
    sprite('na400_04', 4)
    sprite('na400_05', 4)
    sprite('na400_06', 4)
    Unknown21015('BarrierJizoku', 3012, 0)
    sprite('na400_04', 6)
    sprite('na400_05', 6)
    sprite('na400_07', 6)
    sprite('na400_08', 6)
    ExitState()
    label(0)
    clearUponHandler(upon_52)
    sprite('na400_00', 4)
    sprite('na400_01', 3)
    sprite('na400_02', 2)
    sprite('na400_03', 4)
    GFX_0('DanganReversal', 3)
    SLOT_51 = 0
    PrivateSE('na002')
    SmartRandomVoiceline('pna202_0', 100, 'pna202_1', 100, 'pna202_2', 100,
        '', 0)
    sprite('na400_04', 4)
    SpecificInvincibility('P')
    sprite('na400_05', 4)
    sprite('na400_06', 4)
    sprite('na400_04', 4)
    Unknown21015('BarrierJizoku', 3012, 0)
    sprite('na400_05', 6)
    sprite('na400_06', 6)
    sprite('na400_04', 6)
    sprite('na400_07', 6)
    sprite('na400_08', 6)
    ExitState()


@State
def SecretGunA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055()
        setInvincible(1)

        def upon_LANDING():
            sendToLabel(3)
    sprite('na430_00', 3)
    EndMomentum(1)
    sprite('na430_00', 3)
    TagVoiceline(1, 'pna252_0', 'pna252_1', '', '')
    sprite('na430_01', 4)
    physicsXImpulse(-15000)
    physicsYImpulse(30000)
    setGravity(1800)
    sprite('na430_02', 3)
    DistortionSettings(42, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080()
    sprite('na430_03', 3)
    sprite('na430_04', 3)
    sprite('na430_05', 3)
    sprite('na430_06', 2)
    sprite('na430_07', 2)
    sprite('na430_08', 2)
    sprite('na430_09', 25)
    physicsXImpulse(-500)
    physicsYImpulse(-500)
    setGravity(0)
    sprite('na430_09', 2)
    GFX_0('DanganKakushiA', 1)
    ObjectUpon(1, upon_32)
    physicsXImpulse(-300)
    physicsYImpulse(300)
    TagVoiceline(0, 'pna251_0', 'pna251_1', '', '')
    PrivateSE('na008')
    sprite('na430_09', 1)
    setInvincible(0)
    sprite('na430_10', 2)
    sprite('na430_08', 2)
    sprite('na430_09', 2)
    GFX_0('DanganKakushiA', 1)
    PrivateSE('na008')
    sprite('na430_10', 2)
    sprite('na430_08', 2)
    sprite('na430_09', 2)
    GFX_0('DanganKakushiA', 1)
    PrivateSE('na008')
    sprite('na430_10', 2)
    sprite('na430_08', 2)
    sprite('na430_09', 2)
    GFX_0('DanganKakushiA', 1)
    PrivateSE('na008')
    sprite('na430_10', 2)
    sprite('na430_08', 2)
    sprite('na430_09', 2)
    GFX_0('DanganKakushiA', 1)
    PrivateSE('na008')
    sprite('na430_10', 2)
    sprite('na430_08', 2)
    sprite('na430_09', 2)
    GFX_0('DanganKakushiA', 1)
    PrivateSE('na008')
    sprite('na430_10', 2)
    sprite('na430_08', 2)
    sprite('na430_09', 2)
    GFX_0('DanganKakushiA', 1)
    PrivateSE('na008')
    sprite('na430_10', 2)
    sprite('na430_08', 2)
    sprite('na430_09', 2)
    GFX_0('DanganKakushiA', 1)
    PrivateSE('na008')
    sprite('na430_10', 2)
    sprite('na430_08', 2)
    sprite('na430_09', 2)
    GFX_0('DanganKakushiA', 1)
    PrivateSE('na008')
    sprite('na430_10', 2)
    sprite('na430_08', 2)
    sprite('na430_09', 2)
    GFX_0('DanganKakushiA', 1)
    PrivateSE('na008')
    sprite('na430_10', 2)
    sprite('na430_08', 2)
    sprite('na430_09', 2)
    GFX_0('DanganKakushiA', 1)
    PrivateSE('na008')
    sprite('na430_10', 2)
    sprite('na430_08', 2)
    sprite('na430_09', 2)
    GFX_0('DanganKakushiA', 1)
    PrivateSE('na008')
    sprite('na430_10', 2)
    sprite('na430_11', 4)
    physicsXImpulse(-7000)
    physicsYImpulse(15000)
    setGravity(1800)
    sprite('na430_12', 5)
    sprite('na430_13', 5)
    sprite('na430_14', 5)
    sprite('na430_15', 5)
    sprite('na430_16', 5)
    label(2)
    sprite('na020_07', 4)
    sprite('na020_08', 4)
    gotoLabel(2)
    label(3)
    sprite('na010_00', 3)
    EndMomentum(1)
    sprite('na211_00', 4)
    sprite('na010_01', 4)
    sprite('na010_00', 4)


@State
def SecretGunB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055()
        setInvincible(1)

        def upon_LANDING():
            sendToLabel(3)

        def upon_43():
            if SLOT_48 == 9001:
                if not SLOT_63:
                    SLOT_63 = 1
            if SLOT_48 == 9002:
                if not SLOT_64:
                    SLOT_64 = 1
            if SLOT_48 == 9003:
                if not SLOT_65:
                    SLOT_65 = 1
            if SLOT_48 == 9004:
                if not SLOT_66:
                    SLOT_66 = 1
    label(0)
    sprite('na430_01', 3)
    EndMomentum(1)
    physicsXImpulse(-17000)
    physicsYImpulse(36000)
    setGravity(2800)
    sprite('na430_02', 1)
    TagVoiceline(1, 'pna250_0', 'pna250_1', '', '')
    sprite('na430_03', 3)
    sprite('na430_04', 3)
    sprite('na430_05', 3)
    DistortionSettings(40, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080()
    sprite('na430_30', 3)
    sprite('na430_31', 3)
    sprite('na430_32', 3)
    sprite('na430_33', 29)
    physicsXImpulse(-500)
    physicsYImpulse(-500)
    setGravity(0)
    sprite('na430_17', 4)
    GFX_0('DanganKakushiB', 0)
    physicsXImpulse(0)
    physicsYImpulse(0)
    TagVoiceline(0, 'pna253_0', 'pna253_1', '', '')
    PrivateSE('na009')
    sprite('na430_18', 4)
    physicsXImpulse(-10000)
    physicsYImpulse(18000)
    setGravity(1800)
    sprite('na430_19', 8)
    sprite('na430_20', 6)
    setInvincible(0)
    sprite('na430_14', 6)
    sprite('na430_15', 5)
    sprite('na430_16', 5)
    label(2)
    sprite('na020_07', 4)
    sprite('na020_08', 4)
    gotoLabel(2)
    label(3)
    sprite('na010_00', 3)
    EndMomentum(1)
    sprite('na211_00', 4)
    sprite('na010_01', 4)
    sprite('na010_00', 4)


@State
def SecretGunOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        setInvincible(1)
        EnableRapidCancel(0)
        Unknown23055()

        def upon_43():
            if SLOT_48 == 5001:
                EnableRapidCancel(1)
            if SLOT_48 == 9001:
                if not SLOT_63:
                    SLOT_63 = 1
            if SLOT_48 == 9002:
                if not SLOT_64:
                    SLOT_64 = 1
            if SLOT_48 == 9003:
                if not SLOT_65:
                    SLOT_65 = 1
            if SLOT_48 == 9004:
                if not SLOT_66:
                    SLOT_66 = 1

        def upon_LANDING():
            sendToLabel(3)
    if SLOT_36:
        conditionalSendToLabel(0)
    sprite('na430_00', 3)
    EndMomentum(1)
    sprite('na430_00', 3)
    TagVoiceline(1, 'pna252_0', 'pna252_1', '', '')
    sprite('na430_01', 4)
    physicsXImpulse(-15000)
    physicsYImpulse(30000)
    setGravity(1800)
    sprite('na430_02', 3)
    DistortionSettings(42, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080()
    sprite('na430_03', 3)
    sprite('na430_04', 3)
    sprite('na430_05', 3)
    sprite('na430_06', 2)
    sprite('na430_07', 2)
    sprite('na430_08', 2)
    sprite('na430_09', 25)
    physicsXImpulse(-500)
    physicsYImpulse(-500)
    setGravity(0)
    spriteEnd()
    gotoLabel(1)
    label(0)
    sprite('na430_01', 3)
    EndMomentum(1)
    physicsXImpulse(-17000)
    physicsYImpulse(36000)
    setGravity(2800)
    sprite('na430_02', 1)
    TagVoiceline(1, 'pna250_0', 'pna250_1', '', '')
    sprite('na430_03', 3)
    sprite('na430_04', 3)
    sprite('na430_05', 3)
    DistortionSettings(40, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080()
    sprite('na430_06', 3)
    sprite('na430_07', 3)
    sprite('na430_08', 3)
    physicsXImpulse(-500)
    physicsYImpulse(-500)
    setGravity(0)
    sprite('na430_09', 29)
    spriteEnd()
    gotoLabel(1)
    label(1)
    sprite('na430_09', 2)
    GFX_0('DanganKakushiA', 1)
    ObjectUpon(1, upon_32)
    physicsXImpulse(-300)
    physicsYImpulse(300)
    TagVoiceline(0, 'pna251_0', 'pna251_1', '', '')
    PrivateSE('na008')
    sprite('na430_10', 2)
    sprite('na430_08', 2)
    sprite('na430_09', 2)
    GFX_0('DanganKakushiA', 1)
    PrivateSE('na008')
    sprite('na430_10', 2)
    sprite('na430_08', 2)
    sprite('na430_09', 2)
    GFX_0('DanganKakushiA', 1)
    PrivateSE('na008')
    sprite('na430_10', 2)
    sprite('na430_08', 2)
    sprite('na430_09', 2)
    GFX_0('DanganKakushiA', 1)
    PrivateSE('na008')
    sprite('na430_10', 2)
    sprite('na430_08', 2)
    sprite('na430_09', 2)
    GFX_0('DanganKakushiA', 1)
    PrivateSE('na008')
    sprite('na430_10', 2)
    sprite('na430_08', 2)
    sprite('na430_09', 2)
    GFX_0('DanganKakushiA', 1)
    PrivateSE('na008')
    sprite('na430_10', 2)
    sprite('na430_08', 2)
    sprite('na430_09', 2)
    GFX_0('DanganKakushiA', 1)
    PrivateSE('na008')
    sprite('na430_10', 2)
    sprite('na430_08', 2)
    sprite('na430_09', 2)
    GFX_0('DanganKakushiA', 1)
    PrivateSE('na008')
    sprite('na430_10', 2)
    sprite('na430_08', 2)
    sprite('na430_09', 2)
    GFX_0('DanganKakushiA', 1)
    PrivateSE('na008')
    sprite('na430_10', 2)
    sprite('na430_08', 2)
    sprite('na430_09', 2)
    GFX_0('DanganKakushiA', 1)
    PrivateSE('na008')
    sprite('na430_10', 2)
    sprite('na430_08', 2)
    sprite('na430_09', 2)
    GFX_0('DanganKakushiA', 1)
    PrivateSE('na008')
    sprite('na430_10', 2)
    sprite('na430_08', 2)
    sprite('na430_09', 2)
    GFX_0('DanganKakushiA', 1)
    ObjectUpon2(1, 3013, 0)
    PrivateSE('na008')
    sprite('na430_10', 2)
    sprite('na430_11', 3)
    sprite('na430_12', 3)
    sprite('na430_02', 4)
    sprite('na430_03', 4)
    sprite('na430_04', 4)
    sprite('na430_05', 4)
    sprite('na430_30', 3)
    sprite('na430_31', 5)
    sprite('na430_32', 5)
    sprite('na430_33', 48)
    DistortionSettings(50, -1, 0)
    physicsXImpulse(-500)
    physicsYImpulse(-500)
    setGravity(0)
    sprite('na430_17', 4)
    GFX_0('DanganKakushiB', 0)

    def RunOnObject_1():
        MinimumDamage(15)
        AttackP1(48)
        AttackP2(100)
    physicsXImpulse(0)
    physicsYImpulse(0)
    TagVoiceline(0, 'pna253_0', 'pna253_1', '', '')
    PrivateSE('na009')
    sprite('na430_18', 4)
    physicsXImpulse(-15000)
    physicsYImpulse(18000)
    setGravity(1800)
    sprite('na430_19', 8)
    sprite('na430_20', 6)
    setInvincible(0)
    sprite('na430_14', 6)
    sprite('na430_15', 5)
    sprite('na430_16', 5)
    label(2)
    sprite('na020_07', 4)
    sprite('na020_08', 4)
    gotoLabel(2)
    label(3)
    sprite('na010_00', 3)
    EndMomentum(1)
    sprite('na211_00', 4)
    sprite('na010_01', 4)
    sprite('na010_00', 4)


@State
def UltimateKill():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        setInvincible(1)
        Unknown23055()

        def upon_12():
            if SLOT_6:
                EnableRapidCancel(0)
    sprite('na432_00', 4)
    EndMomentum(1)
    sprite('na432_01', 36)
    DistortionSettings(72, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080()
    TagVoiceline(1, 'pna254_0', 'pna254_1', '', '')
    sprite('na432_02', 3)
    sprite('na432_03', 3)
    sprite('na432_04', 3)
    sprite('na432_05', 3)
    sprite('na432_06', 3)
    sprite('na432_07', 3)
    sprite('na432_08', 4)
    ObjectUpon2(11, 502, 0)
    sprite('na432_09', 4)
    sprite('na432_10', 4)
    sprite('na432_11', 2)
    sprite('na432_11', 2)
    setInvincible(0)
    sprite('na432_09', 4)
    sprite('na432_10', 2)
    sprite('na432_10', 2)
    TagVoiceline(0, 'pna255_0', 'pna255_1', '', '')
    sprite('na432_11', 3)
    sprite('na432_12', 3)
    sprite('na432_13', 3)
    sprite('na432_14', 3)
    sprite('na432_15', 3)
    sprite('na432_16', 3)


@State
def UltimateKillOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055()
        setInvincible(1)

        def upon_12():
            if SLOT_6:
                EnableRapidCancel(0)
    sprite('na432_00', 4)
    EndMomentum(1)
    sprite('na432_01', 36)
    DistortionSettings(72, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080()
    TagVoiceline(1, 'pna254_0', 'pna254_1', '', '')
    sprite('na432_02', 3)
    sprite('na432_03', 3)
    sprite('na432_04', 3)
    sprite('na432_05', 3)
    sprite('na432_06', 3)
    sprite('na432_07', 3)
    sprite('na432_08', 4)
    ObjectUpon2(11, 503, 0)
    sprite('na432_09', 4)
    sprite('na432_10', 4)
    sprite('na432_11', 2)
    sprite('na432_11', 2)
    setInvincible(0)
    sprite('na432_09', 4)
    sprite('na432_10', 2)
    sprite('na432_10', 2)
    TagVoiceline(1, 'pna255_0', 'pna255_1', '', '')
    sprite('na432_11', 3)
    sprite('na432_12', 3)
    sprite('na432_13', 3)
    sprite('na432_14', 3)
    sprite('na432_15', 3)
    sprite('na432_16', 3)


@State
def UltimateKillAir():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        setInvincible(1)
        Unknown23055()

        def upon_43():
            if SLOT_48 == 5002:
                EnableRapidCancel(0)
        NoAttackDuringAction(1)
        SLOT_34 = 0
    sprite('na254_00', 3)
    PushSpeedX()
    PushSpeedY()
    PushGravity()
    EndMomentum(1)
    EnterStateIfEventID(2, 'CmnActJumpLanding')
    sprite('na254_01', 3)
    TagVoiceline(1, 'pna256_0', 'pna256_1', '', '')
    sprite('na254_02', 3)
    GFX_1('persona_enter_ply', 0)
    ObjectUpon2(11, 504, 0)
    clearUponHandler(upon_LANDING)
    sprite('na254_03', 5)
    DistortionSettings(30, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080()
    sprite('na254_04', 5)
    sprite('na254_05', 5)
    sprite('na254_03', 5)
    sprite('na254_04', 5)
    sprite('na254_05', 5)
    sprite('na255_00', 4)
    sprite('na255_01', 3)
    sprite('na255_02', 15)
    setInvincible(0)
    sprite('na255_03', 3)
    sprite('na255_04', 3)
    sprite('na255_05', 3)
    sprite('na255_01', 3)
    PopSpeedX()
    PopGravity()
    XImpulseAcceleration(85)
    YAccel(85)
    physicsYImpulse(8000)
    sprite('na255_00', 3)


@State
def UltimateKillAirOD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        setInvincible(1)
        Unknown23055()

        def upon_43():
            if SLOT_48 == 5002:
                EnableRapidCancel(0)
        SLOT_34 = 1
    sprite('na254_00', 3)
    PushSpeedX()
    PushSpeedY()
    PushGravity()
    EndMomentum(1)
    EnterStateIfEventID(2, 'CmnActJumpLanding')
    sprite('na254_01', 3)
    TagVoiceline(1, 'pna256_0', 'pna256_1', '', '')
    sprite('na254_02', 3)
    GFX_1('persona_enter_ply', 0)
    ObjectUpon2(11, 504, 0)
    clearUponHandler(upon_LANDING)
    sprite('na254_03', 5)
    DistortionSettings(30, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080()
    sprite('na254_04', 5)
    sprite('na254_05', 5)
    sprite('na254_03', 5)
    sprite('na254_04', 5)
    sprite('na254_05', 5)
    sprite('na255_00', 4)
    sprite('na255_01', 3)
    sprite('na255_02', 15)
    setInvincible(0)
    sprite('na255_03', 3)
    sprite('na255_04', 3)
    sprite('na255_05', 3)
    sprite('na255_01', 3)
    PopSpeedX()
    PopGravity()
    XImpulseAcceleration(85)
    YAccel(85)
    physicsYImpulse(8000)
    sprite('na255_00', 3)


@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()

        def upon_STATE_END():
            EnableCollision(1)

        def upon_43():
            if SLOT_48 == 9501:
                setInvincible(1)
                EnableCollision(0)
                Unknown23084(1)
                Unknown23088(1, 1)
                GFX_0('Ichigeki_RedRay', 100)
                Unknown23157(1)

                def RunOnObject_22():
                    DashFMaxVelocity(18000)
                    Unknown23169(0)
                    Unknown23168(1)
                    Unknown23164(0)
                    Unknown23161(0)
            if SLOT_48 == 9503:
                sendToLabel(10)
            if SLOT_48 == 9502:
                sendToLabel(0)
    sprite('na450_00', 4)
    EndMomentum(1)
    setInvincibleFor(160)
    Unknown11063(1)
    TagVoiceline(1, 'pna290_0', 'pna290_1', '', '')
    sprite('na450_01', 4)
    sprite('na450_02', 4)
    sprite('na450_03', 6)
    DistortionSettings(96, -1, 2)
    Unknown23147()
    GFX_0('RotateGun', 0)
    GFX_0('P4U_Cutin_Parent', 100)
    sprite('na450_04', 6)
    sprite('na450_05', 4)
    sprite('na450_06', 4)
    sprite('na450_07', 4)
    sprite('na450_08', 6)
    sprite('na450_09', 6)
    CommonSE('cloth_l')
    sprite('na450_10', 6)
    sprite('na450_11', 6)
    CommonSE('cloth_l')
    sprite('na450_12', 4)
    sprite('na450_13', 4)
    CommonSE('grip_fast')
    sprite('na450_14', 4)
    CommonSE('cloth_l')
    sprite('na450_15', 6)
    GFX_1('elef_cardlight_add2', 0)
    GFX_1('persona_summon', 0)
    sprite('na450_16', 6)
    CommonSE('cloth_l')
    sprite('na450_17', 6)
    clearUponHandler(upon_EVERY_FRAME)
    if SLOT_38:
        SLOT_0 = SLOT_51 * -1
    ObjectUpon2(11, 950, 0)
    sprite('na450_15', 6)
    CommonSE('cloth_l')
    sprite('na450_16', 6)
    sprite('na450_17', 6)
    CommonSE('cloth_l')
    label(1)
    sprite('na450_15', 6)
    sprite('na450_16', 6)
    sprite('na450_17', 6)
    CommonSE('cloth_l')
    spriteEnd()
    gotoLabel(1)
    label(10)
    sprite('null', 16)
    Unknown26('SCEF_Usugurai')
    Unknown26('Ichigeki_Marker')
    SystemGFX('SCEF_FadeBlack12In', 100)
    sprite('null', 60)
    Unknown23024(0)
    GFX_0('Ichigeki_Scope', 100)
    GFX_0('Ichigeki_Scope2', 100)
    GFX_0('Ichigeki_Scope3', 100)
    sprite('null', 120)

    def RunOnObject_22():
        enterState('CmnActStand')
        AbsoluteY(0)
    GFX_0('IchigekiCamera', 100)
    Unknown26('SCEF_FadeBlack12In')
    SystemGFX('SCEF_FadeBlack12Out', 100)
    SystemGFX('SCEF_Usugurai', 100)
    Unknown26('Ichigeki_Marker')
    PrivateSE('na000')
    sprite('null', 12)
    SystemGFX('SCEF_FadeBlack12In', 100)
    sprite('null', 4)
    Unknown21015('Ichigeki_Scope', 9533, 0)
    Unknown21015('Ichigeki_Scope2', 9533, 0)
    Unknown21015('Ichigeki_Scope3', 9533, 0)
    sprite('null', 40)
    Unknown26('SCEF_Usugurai')
    sprite('null', 1)
    GFX_0('IchigekiCutin', 103)
    TagVoiceline(0, 'pna291_0', 'pna291_1', '', '')
    SystemGFX('SCEF_FadeBlack12In', 100)

    def RunOnObject_22():
        enterState('CmnActStand')
        Unknown23168(0)
        Unknown23169(1)
    sprite('null', 79)

    def RunOnObject_22():
        Unknown51(1)
    sprite('null', 30)
    Unknown26('SCEF_FadeBlack12In')
    SystemGFX('SCEF_FadeBlack12Out', 100)
    SystemGFX('SCEF_Usugurai', 100)
    GFX_0('Ichigeki_Scope', 100)
    GFX_0('Ichigeki_Scope2', 100)
    GFX_0('Ichigeki_Scope3', 100)
    GFX_0('IchigekiBlack', 100)

    def RunOnObject_22():
        Unknown51(0)
    sprite('null', 10)
    GFX_0('Ichigeki_shot', 103)
    sprite('null', 15)
    GFX_0('IchigekiTame_Atk', 100)
    Unknown21015('Ichigeki_Scope', 9534, 0)
    Unknown21015('Ichigeki_Scope2', 9533, 0)
    Unknown21015('Ichigeki_Scope3', 9533, 0)
    sprite('null', 15)
    GFX_0('IchigekiExplosion', 100)
    Unknown26('SCEF_Usugurai')
    sprite('null', 30)
    GFX_0('Ichigekiwhite', 100)
    sprite('null', 30)
    GFX_0('Ichigeki_Atk', 100)
    sprite('na000_00', 30)
    Unknown21015('IchigekiCamera', 9521, 0)
    Unknown20000(1)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    TagVoiceline(1, 'pna292_0', 'pna292_1', '', '')
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    spriteEnd()
    ExitState()
    label(0)
    sprite('na450_15', 6)
    setInvincible(0)
    Unknown23084(0)
    sprite('na450_16', 6)
    sprite('na450_17', 6)
    CommonSE('cloth_l')
    sprite('na450_15', 6)
    sprite('na450_16', 6)
    sprite('na450_17', 6)
    CommonSE('cloth_l')
    sprite('na450_15', 6)
    sprite('na450_16', 6)
    sprite('na450_17', 6)
    CommonSE('cloth_l')
    setInvincible(0)
    sprite('na450_18', 6)
    sprite('na450_19', 6)
    sprite('na450_20', 6)
    sprite('keep', 1)


@Subroutine
def MouthTableInit():
    MouthToVoice('pna000', 'a7c7a7c7a7c24a7c7')
    MouthToVoice('pna500', 'c1a7c7a7c7a7c40a7c7a7c7a7c7a7c7a7c7a7c7')
    Unknown30092('pna500', '001')
    MouthToVoice('pna501', 'c1a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7')
    Unknown30092('pna501', '002')
    MouthToVoice('pna502', 'c1a7c7a7c7a7c7a7c67a7c7a7c7a7c7a7c7a7c7')
    Unknown30092('pna502', '003')
    MouthToVoice('pna503', 'c1a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7')
    Unknown30092('pna503', '004')
    MouthToVoice('pna504',
        'c1a4c4a4c9a7c7a7c67a7c7a7c47a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7')
    Unknown30092('pna504', '005')
    MouthToVoice('pna505', 'c1a7c7a7c9a7c7a7c47a7c7a7c7a7c7a7c7')
    Unknown30092('pna505', '006')
    MouthToVoice('pna506',
        'c1a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c57a7c7a7c7a7c7a7c7a7c7')
    Unknown30092('pna506', '007')
    MouthToVoice('pna507',
        'c1a7c7a7c7a7c7a7c127a7c7a7c7a7c7a7c7a7c7a7c37a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7'
        )
    Unknown30092('pna507', '008')
    MouthToVoice('pna520', 'c1a7c7a7c7a7c7a7c7a7c42a7c7a7c7a7c7a7c7')
    Unknown30092('pna520', '009')
    MouthToVoice('pna521',
        'c1a7c7a7c7a7c7a7c7a7c57a7c7a7c7a7c42a7c7a7c7a7c7a7c9a7c7a7c7')
    Unknown30092('pna521', '010')
    MouthToVoice('pna522',
        'c1a7c7a7c7a7c7a7c7a7c50a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7')
    Unknown30092('pna522', '011')
    MouthToVoice('pna523', 'c1a7c7a7c7a7c7a7c7a7c7a7c57a7c7a7c7a7c7a7c7a7c7')
    Unknown30092('pna523', '012')
    MouthToVoice('pna524',
        'c1a7c7a7c7a7c7a7c7a7c62a7c7a7c57a7c7a7c7a7c7a7c7a12c7a7c7a7c7a7c7a7c7'
        )
    Unknown30092('pna524', '013')
    MouthToVoice('pna525',
        'c1a7c7a7c7a7c107a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c47a7c7a7c7a7c7a7c7a7c7a7c7'
        )
    Unknown30092('pna525', '014')
    MouthToVoice('pna402_0', 'c1a7c7a7c7a7c9a7c7a7c7')
    MouthToVoice('pna402_1', 'c1a7c7a7c7a7c7a7c7a7c7')
    MouthToVoice('pna403_0', 'c120')
    MouthToVoice('pna403_1', 'c120')
    MouthToVoice('pna600bno',
        'c1a7c7a7c7a12c7a7c7a7c47a7c7a7c7a7c7a7c37a7c7a7c7a7c7a7c7a7c7a7c7')
    Unknown30092('pna600bno', '019')
    MouthToVoice('pna601bhz',
        'c1a7c7a7c7a7c57a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c47a7c7a7c7')
    Unknown30092('pna601bhz', '020')
    MouthToVoice('pna600biz',
        'c1a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7')
    Unknown30092('pna600biz', '021')
    MouthToVoice('pna601bes', 'c1a7c7a7c7a7c57a7c7a7c7a7c7a7c7a7c7a7c7a7c7')
    Unknown30092('pna601bes', '022')
    MouthToVoice('pna600pbc',
        'c1a5c60a7c7a7c7a7c7a7c47a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7')
    Unknown30092('pna600pbc', '023')
    MouthToVoice('pna601pka',
        'c1a4c4a4c37a7c7a7c7a7c7a7c7a7c37a7c7a7c7a7c7a7c7a7c7')
    Unknown30092('pna601pka', '024')
    MouthToVoice('pna601pmi', 'c1a7c7a7c7a7c7a7c47a7c7a7c7a7c7a7c7a7c7a7c7')
    Unknown30092('pna601pmi', '025')
    MouthToVoice('pna601uhy', 'c1a7c7a7c7a7c7a7c40a7c7a7c7a7c7a7c7a7c7a7c7')
    Unknown30092('pna601uhy', '026')
    MouthToVoice('pna601uor',
        'c1a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c33a7c7a7c7a7c7a7c7a7c7a7c7')
    Unknown30092('pna601uor', '027')
    MouthToVoice('pna601ume',
        'c1a7c7a7c7a7c55a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c50a7c7a7c7a7c7a7c7a7c7a7c7'
        )
    Unknown30092('pna601ume', '028')
    MouthToVoice('pna600rwi',
        'c1a7c7a7c7a7c87a7c7a7c7a7c7a7c7a7c7a7c7a7c7a12c7a7c7a7c7')
    Unknown30092('pna600rwi', '029')
    MouthToVoice('pna600use', 'c1a7c7a7c7a7c7a7c7a7c7a7c29a7c7a7c7a7c11')
    Unknown30092('pna600use', '030')
    MouthToVoice('pna600bnt', 'a7c7a7c7a7c7a7c7a7c32a7c7a7c7a7c11')
    Unknown30092('pna600bnt', '031')
    MouthToVoice('pna701bno',
        'c1a7c47a7c7a7c7a7c7a7c7a7c47a7c7a7c7a7c7a7c7a7c7a7c7')
    Unknown30092('pna701bno', '032')
    MouthToVoice('pna701bhz',
        'c1a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c9a7c7a7c7a7c7a7c110a7c7a7c7a7c7a7c7')
    Unknown30092('pna701bhz', '033')
    MouthToVoice('pna701bes', 'c1a7c7a7c7a7c10a5c5a5c10a7c7a7c7')
    Unknown30092('pna701bes', '034')
    MouthToVoice('pna701pbc', 'c1a7c67a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7'
        )
    Unknown30092('pna701pbc', '035')
    MouthToVoice('pna701pka', 'c1a7c7a7c7a7c7a7c7a7c37a7c7a7c7a7c7a7c7')
    Unknown30092('pna701pka', '036')
    MouthToVoice('pna700pmi', 'c1a7c7a7c7a7c7a7c90a7c7a7c7a7c7a7c7')
    Unknown30092('pna700pmi', '037')
    MouthToVoice('pna701uhy',
        'c1a7c67a7c7a7c7a7c7a7c7a7c7a7c67a7c7a7c7a7c7a7c7a7c7a7c7a7c7')
    Unknown30092('pna701uhy', '038')
    MouthToVoice('pna701uor',
        'c1a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7')
    Unknown30092('pna701uor', '039')
    MouthToVoice('pna701ume',
        'c1a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c47a7c7a7c30a7c7a7c7')
    Unknown30092('pna701ume', '040')
    MouthToVoice('pna701rwi', 'c1a12c80a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7')
    Unknown30092('pna701rwi', '041')
    MouthToVoice('pna700bhz', 'c1a7c7a7c7a7c7a7c47a7c7a7c7a7c9a7c7a7c7')
    Unknown30092('pna700bhz', '042')
    MouthToVoice('pna701use', 'c1a16c42a7c7a7c7a7c7a7c7a7c7a7c17')
    Unknown30092('pna701use', '043')
    MouthToVoice('pna701bnt', 'a18c9a7c7a7c7a7c7a16c31a7c7a7c7')
    Unknown30092('pna701bnt', '044')
    if SLOT_172:
        MouthToVoice('pna000', 'a7c7a7c7a7c24a7c7')
        MouthToVoice('pna500',
            'c1c2a7c7a7c7a7c4c17a7c7a7c7a7c7a7c7a7c7a7c4c1a7c3c6')
        MouthToVoice('pna501', 'c1c3a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c4')
        MouthToVoice('pna502', 'c1c3a7c7a7c7a7c7a7c7a7c7a7c7a4c4a7c7a3c2a5c9')
        MouthToVoice('pna503',
            'c1c3a7c7a7c7a7c7a7c7a7c7a1c4a7c7a7c7a7c6c2a7c7a7c7a7c4c8')
        MouthToVoice('pna504',
            'c1c3a7c7a3c2a7c7a7c7a1c21a7c7a7c7a7c1c1a7c7a7c7a7c7a7c7c4a7c7a7c7a4c3'
            )
        MouthToVoice('pna505', 'c1c1a7c7a7c7a7c7a7c7a7c2c1a7c7a5c14')
        MouthToVoice('pna506',
            'c1c4a7c1c1a7c7a7c7a7c7a7c7a7c7a7c1a7c7a7c7a7c2c2a7c7a7c1a6c10')
        MouthToVoice('pna507',
            'c1c2a7c7a7c7a7c2a7c7a7c3c51a7c7a7c7a7c7a7c7a7c7a7c2c1a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c6c7'
            )
        MouthToVoice('pna520',
            'c1c1a7c7a7c7a6c1a7c2c1a7c2c5a7c7c20a7c4c1a7c7a7c7a7c6c3a7c6c5')
        MouthToVoice('pna521', 'c1c1a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c3c9')
        MouthToVoice('pna522',
            'c1c1a7c5c3a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c5c8')
        MouthToVoice('pna523', 'c1c1a7c2a7c7a7c7a7c7a7c7a4c1a7c7a7c7a6c3')
        MouthToVoice('pna524',
            'c1c1a7c7a7c7a7c7a7c7a7c7a3c19a7c7a7c7a7c7a7c7a3c2a7c7a7c7a7c7a3c2a7c7a7c7c3'
            )
        MouthToVoice('pna525',
            'c1c1a7c7a7c7a4c22a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c5c21a7c7a7c7a7c7a7c7a7c7a7c7a7c1c10'
            )
        MouthToVoice('pna402_0', 'c1a7c7a7c7a7c9a7c7a7c7')
        MouthToVoice('pna402_1', 'c1a7c7a7c7a7c7a7c7a7c7')
        MouthToVoice('pna403_0', 'c120')
        MouthToVoice('pna403_1', 'c120')
        MouthToVoice('pna600bno',
            'c1c1a7c7a7c3c2a7c7a5c3a3c23a7c7a7c5c1a7c7a7c7a7c7a4c1a6c5a7c7a7c7a5c3'
            )
        MouthToVoice('pna601bhz',
            'c1c1a7c7a7c7a7c7c29a7c7a7c7a3c1a7c1c2a7c7a7c7c1a7c7a7c7a7c7a1c2a7c7a1c1a7c7a7c4a7c7c5'
            )
        MouthToVoice('pna600biz',
            'c1c1a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7a3c2a7c7a7c7a6c4')
        MouthToVoice('pna601bes',
            'c1c1a7c7a7c7a7c4c4a4c3a7c7a7c7a7c7a7c2c1a7c4c1a7c7a1c2')
        MouthToVoice('pna600pbc',
            'c1c2a7c7c10a7c7a3c3a7c7a7c7a7c1c16a7c7a7c7a7c7a7c7a7c7a7c7a7c1c1a7c7a7c7a7c7a4c3'
            )
        MouthToVoice('pna601pka',
            'c1c1a7c7a7c3a6c23a7c7a7c7a7c7a7c7a7c7a8c22a7c7a7c7a7c4c4a7c7a7c7a5c6'
            )
        MouthToVoice('pna601pmi',
            'c1c1a7c7a7c1a7c7a7c2c13a7c7a7c7a7c7a7c7a7c3c3')
        MouthToVoice('pna601uhy', 'c1c2a7c7a7c7a7c7a5c9a7c7a7c5c3a7c7a7c7c5')
        MouthToVoice('pna601uor',
            'c1c1a7c7a7c7a7c7a7c7a7c7a3c3a7c5c2a7c3c3a7c7a7c5c14a7c7a7c2c1a7c6c1a7c7a7c7a7c7a7c7a6c4'
            )
        MouthToVoice('pna601ume',
            'c1c1a7c1c3a7c7a7c7a7c7a5c29a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c4c24a7c7a7c7a7c7a7c7a7c6c4'
            )
        MouthToVoice('pna600rwi',
            'c1c3a7c7a7c7a7c6c8a7c7a7c7a7c7a7c7a7c7a2c2a7c7a7c7a1c1')
        MouthToVoice('pna600use', 'c1c1a7c5c1a7c7a7c7a7c7a7c7a7c7a7c7a7c4c3')
        MouthToVoice('pna600bnt', 'c1c1a7c7a7c7c1a7c7a7c7a7c4c2a7c7a7c7a5c4')
        MouthToVoice('pna701bno',
            'c1c2a7c7a5c6a7c7a7c1c3a7c7a7c7a7c5c17a7c7a7c7a7c7a7c7a2c1a7c7a7c5c2a4c4'
            )
        MouthToVoice('pna701bhz',
            'c1c1a7c7a7c7a7c7a7c7a4c1a7c7a7c7a7c7a7c7a7c6c31a7c7a7c7a7c7a7c7a7c7a7c7a1c5'
            )
        MouthToVoice('pna701bes', 'c1c1a7c7a7c7a7c7a7c7a7c7a7c7a7c7a7c3c3')
        MouthToVoice('pna701pbc',
            'c1c2a7c7a2c4a7c7a2c1a7c7a7c7a7c7a7c7a7c7a7c7a7c14')
        MouthToVoice('pna701pka',
            'c1a7c7a7c7a7c15a7c7a7c7a7c7a7c1c1a7c7a7c7c15')
        MouthToVoice('pna700pmi',
            'c1c1a7c7a7c7a7c3c19a7c7a7c7a7c7a3c1a7c7a7c7a7c7a6c4')
        MouthToVoice('pna701uhy',
            'c1c1a7c7a1c24a7c7a7c7c2a7c7a7c2c18a7c7a7c3c2a7c4c1a1c2a7c7a1c5')
        MouthToVoice('pna701uor',
            'c1c1a7c7a7c7a7c7a7c7a2c3a7c7a5c2a7c7a7c1c3a7c7a7c6c5')
        MouthToVoice('pna701ume',
            'c1c1a7c7a7c7a7c7a7c7a7c7a7c7a7c7a1c44a7c7a7c7a7c7a7c7a5c2a7c7c3')
        MouthToVoice('pna701rwi', 'c1c8a7c7a7c7a7c7a7c7c2a7c7a7c7a7c7a7c5c4')
        MouthToVoice('pna701use',
            'c1c1a7c7a2c2a7c7a1c2a6c1a7c7a7c1a7c4c1a7c7a7c2c4')
        MouthToVoice('pna701bnt',
            'c1c1a7c7a7c7a7c7a7c7a7c5c2a7c7a7c7a7c7a2c2a7c7a7c2c4')
        MouthToVoice('pna700bhz', 'c1a7c7a7c7a7c7a7c47a7c7a7c7a7c9a7c7a7c7')


@State
def CmnActEntry():
    label(0)
    sprite('null', 1)
    spriteEnd()
    if SLOT_17:
        conditionalSendToLabel(0)
    if SLOT_169:
        conditionalSendToLabel(482)
    if SLOT_122:
        conditionalSendToLabel(482)
    if SLOT_123:
        conditionalSendToLabel(482)
    if PartnerChar('bno'):
        conditionalSendToLabel(100)
    if PartnerChar('bes'):
        conditionalSendToLabel(110)
    if PartnerChar('pbc'):
        conditionalSendToLabel(120)
    if PartnerChar('bhz'):
        conditionalSendToLabel(130)
    if PartnerChar('uhy'):
        conditionalSendToLabel(140)
    if PartnerChar('rwi'):
        conditionalSendToLabel(150)
    if PartnerChar('pka'):
        conditionalSendToLabel(160)
    if PartnerChar('uor'):
        conditionalSendToLabel(170)
    if PartnerChar('pmi'):
        conditionalSendToLabel(180)
    if PartnerChar('biz'):
        conditionalSendToLabel(190)
    if PartnerChar('ume'):
        conditionalSendToLabel(200)
    if PartnerChar('bnt'):
        conditionalSendToLabel(210)
    if PartnerChar('use'):
        conditionalSendToLabel(220)
    label(482)
    if not SLOT_158:
        conditionalSendToLabel(991)
    if random_(2, 50):
        conditionalSendToLabel(10)
    sprite('na600_00', 6)
    sprite('na600_01', 6)
    sprite('na600_02', 6)
    sprite('na600_03', 5)
    sprite('na600_04', 12)
    PrivateSE('cloth_l')
    sprite('na600_05', 8)
    sprite('na600_06', 20)
    RandomVoiceline('pna500', 100, 'pna501', 100, 'pna502', 100, 'pna506', 100)
    sprite('na600_07', 30)
    sprite('na600_08', 6)
    PrivateSE('slash_rapier_fast')
    sprite('na600_09', 4)
    PrivateSE('slash_rapier_fast')
    sprite('na600_10', 4)
    PrivateSE('grip_fast')
    label(1)
    sprite('na600_11', 1)
    if SLOT_97:
        conditionalSendToLabel(1)
    sprite('na600_11', 30)
    sprite('na600_12', 6)
    Unknown23018(1)
    label(2)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(2)
    ExitState()
    label(10)
    sprite('na601_00', 6)
    sprite('na601_50', 3)
    sprite('na601_51', 3)
    sprite('na601_52', 3)
    sprite('na601_53', 75)
    RandomVoiceline('pna503', 100, 'pna504', 100, 'pna505', 100, 'pna507', 100)
    sprite('na601_01', 6)
    sprite('na601_02', 3)
    sprite('na601_54', 14)
    PrivateSE('walk_marble_heavy')
    sprite('na601_03', 6)
    sprite('na601_04', 6)
    sprite('na601_05', 6)
    sprite('na601_06', 4)
    sprite('na601_07', 4)
    sprite('na601_08', 6)
    sprite('na601_09', 6)
    sprite('na601_10', 6)
    sprite('na601_11', 6)
    PrivateSE('hair')
    sprite('na601_12', 6)
    sprite('na601_13', 8)
    sprite('na601_14', 7)
    Unknown23018(1)
    label(11)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(11)
    ExitState()
    label(20)
    sprite('na000_00', 1)
    Voiceline('pna701ume')
    label(21)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(21)
    label(100)
    sprite('na600_00', 6)
    if SLOT_158:
        XPositionRelativeFacing(-1230000)
    else:
        XPositionRelativeFacing(-1465000)
    sprite('na600_01', 6)
    sprite('na600_02', 6)
    sprite('na600_03', 5)
    sprite('na600_04', 12)
    PrivateSE('cloth_l')
    sprite('na600_05', 8)
    sprite('na600_06', 20)
    Voiceline('pna600bno')
    sprite('na600_07', 30)
    sprite('na600_08', 6)
    PrivateSE('slash_rapier_fast')
    sprite('na600_09', 4)
    PrivateSE('slash_rapier_fast')
    sprite('na600_10', 4)
    PrivateSE('grip_fast')
    label(101)
    sprite('na600_11', 1)
    if SLOT_97:
        conditionalSendToLabel(101)
    sprite('na600_11', 30)
    sprite('na600_12', 6)
    DemoTimer(240)
    ObjectUpon(24, upon_40)
    label(102)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(102)
    ExitState()
    label(110)
    sprite('na000_00', 1)
    if SLOT_158:
        XPositionRelativeFacing(-1230000)
    else:
        XPositionRelativeFacing(-1515000)

    def upon_40():
        clearUponHandler(upon_40)
        sendToLabel(112)
    label(111)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(111)
    label(112)
    sprite('na001_00', 7)
    Voiceline('pna601bes')
    sprite('na001_01', 7)
    sprite('na001_02', 7)
    sprite('na001_03', 10)
    sprite('na001_04', 7)
    sprite('na001_05', 7)
    sprite('na001_06', 10)
    sprite('na001_01', 7)
    sprite('na001_00', 7)
    Unknown23018(1)
    label(113)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(113)
    ExitState()
    label(120)
    sprite('na601_00', 6)
    if SLOT_158:
        XPositionRelativeFacing(-1230000)
    else:
        XPositionRelativeFacing(-1465000)
    sprite('na601_50', 3)
    sprite('na601_51', 3)
    sprite('na601_52', 3)
    sprite('na601_53', 75)
    Voiceline('pna600pbc')
    sprite('na601_01', 6)
    sprite('na601_02', 3)
    sprite('na601_54', 14)
    PrivateSE('walk_marble_heavy')
    sprite('na601_03', 6)
    sprite('na601_04', 6)
    sprite('na601_05', 6)
    sprite('na601_06', 4)
    sprite('na601_07', 4)
    sprite('na601_08', 6)
    sprite('na601_09', 6)
    sprite('na601_10', 6)
    sprite('na601_11', 6)
    PrivateSE('hair')
    sprite('na601_12', 6)
    sprite('na601_13', 8)
    sprite('na601_14', 7)
    label(121)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    if SLOT_97:
        conditionalSendToLabel(121)
    sprite('na000_00', 1)
    ObjectUpon(24, upon_40)
    DemoTimer(300)
    label(122)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(122)
    ExitState()
    label(130)
    sprite('na000_00', 1)
    if SLOT_158:
        XPositionRelativeFacing(-1230000)
    else:
        XPositionRelativeFacing(-1465000)

    def upon_40():
        clearUponHandler(upon_40)
        sendToLabel(132)
    label(131)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(131)
    label(132)
    sprite('na001_00', 7)
    Voiceline('pna601bhz')
    sprite('na001_01', 7)
    sprite('na001_02', 7)
    sprite('na001_03', 10)
    sprite('na001_04', 7)
    sprite('na001_05', 7)
    sprite('na001_06', 10)
    sprite('na001_01', 7)
    sprite('na001_00', 7)
    Unknown23018(1)
    label(133)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(133)
    ExitState()
    label(140)
    sprite('na601_00', 32767)
    if SLOT_158:
        XPositionRelativeFacing(-1230000)
    else:
        XPositionRelativeFacing(-1465000)

    def upon_40():
        clearUponHandler(upon_40)
        sendToLabel(141)
    label(141)
    sprite('na601_50', 3)
    sprite('na601_51', 3)
    sprite('na601_52', 3)
    sprite('na601_53', 75)
    Voiceline('pna601uhy')
    sprite('na601_01', 6)
    sprite('na601_02', 3)
    sprite('na601_54', 14)
    PrivateSE('walk_marble_heavy')
    sprite('na601_03', 6)
    sprite('na601_04', 6)
    sprite('na601_05', 6)
    sprite('na601_06', 4)
    sprite('na601_07', 4)
    sprite('na601_08', 6)
    sprite('na601_09', 6)
    sprite('na601_10', 6)
    sprite('na601_11', 6)
    PrivateSE('hair')
    sprite('na601_12', 6)
    sprite('na601_13', 8)
    sprite('na601_14', 7)
    Unknown23018(1)
    label(142)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(142)
    ExitState()
    label(150)
    sprite('na601_00', 6)
    if SLOT_158:
        XPositionRelativeFacing(-1465000)
    else:
        XPositionRelativeFacing(-1465000)
    sprite('na601_50', 3)
    sprite('na601_51', 3)
    sprite('na601_52', 3)
    sprite('na601_53', 75)
    Voiceline('pna600rwi')
    sprite('na601_01', 6)
    sprite('na601_02', 3)
    sprite('na601_54', 14)
    PrivateSE('walk_marble_heavy')
    sprite('na601_03', 6)
    sprite('na601_04', 6)
    sprite('na601_05', 6)
    sprite('na601_06', 4)
    sprite('na601_07', 4)
    sprite('na601_08', 6)
    sprite('na601_09', 6)
    sprite('na601_10', 6)
    sprite('na601_11', 6)
    PrivateSE('hair')
    sprite('na601_12', 6)
    sprite('na601_13', 8)
    sprite('na601_14', 7)
    label(151)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    if SLOT_97:
        conditionalSendToLabel(151)
    sprite('na000_00', 1)
    ObjectUpon(24, upon_40)
    DemoTimer(240)
    label(152)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(152)
    ExitState()
    label(160)
    sprite('na600_00', 1)
    if SLOT_158:
        XPositionRelativeFacing(-1230000)
    else:
        XPositionRelativeFacing(-1505000)

    def upon_40():
        clearUponHandler(upon_40)
        sendToLabel(162)
    label(161)
    sprite('na600_00', 6)
    sprite('na600_01', 6)
    sprite('na600_02', 6)
    gotoLabel(161)
    label(162)
    sprite('na600_03', 5)
    Voiceline('pna601pka')
    sprite('na600_04', 12)
    PrivateSE('cloth_l')
    sprite('na600_05', 8)
    sprite('na600_06', 20)
    sprite('na600_07', 30)
    sprite('na600_08', 6)
    PrivateSE('slash_rapier_fast')
    sprite('na600_09', 4)
    PrivateSE('slash_rapier_fast')
    sprite('na600_10', 4)
    PrivateSE('grip_fast')
    label(163)
    sprite('na600_11', 1)
    if SLOT_97:
        conditionalSendToLabel(163)
    sprite('na600_11', 30)
    sprite('na600_12', 6)
    Unknown23018(1)
    label(164)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(164)
    ExitState()
    label(170)
    sprite('na601_00', 32767)
    if SLOT_158:
        XPositionRelativeFacing(-1230000)
    else:
        XPositionRelativeFacing(-1465000)

    def upon_40():
        clearUponHandler(upon_40)
        sendToLabel(171)
    label(171)
    sprite('na601_50', 3)
    sprite('na601_51', 3)
    sprite('na601_52', 3)
    sprite('na601_53', 75)
    Voiceline('pna601uor')
    sprite('na601_01', 6)
    sprite('na601_02', 3)
    sprite('na601_54', 14)
    PrivateSE('walk_marble_heavy')
    sprite('na601_03', 6)
    sprite('na601_04', 6)
    sprite('na601_05', 6)
    sprite('na601_06', 4)
    sprite('na601_07', 4)
    sprite('na601_08', 6)
    sprite('na601_09', 6)
    sprite('na601_10', 6)
    sprite('na601_11', 6)
    PrivateSE('hair')
    sprite('na601_12', 6)
    sprite('na601_13', 8)
    sprite('na601_14', 7)
    Unknown23018(1)
    label(172)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(172)
    ExitState()
    label(180)
    sprite('na000_00', 1)
    if SLOT_158:
        XPositionRelativeFacing(-1230000)
    else:
        XPositionRelativeFacing(-1465000)

    def upon_40():
        clearUponHandler(upon_40)
        sendToLabel(182)
    label(181)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(181)
    label(182)
    sprite('na001_00', 7)
    Voiceline('pna601pmi')
    sprite('na001_01', 7)
    sprite('na001_02', 7)
    sprite('na001_03', 10)
    sprite('na001_04', 7)
    sprite('na001_05', 7)
    sprite('na001_06', 10)
    sprite('na001_01', 7)
    sprite('na001_00', 7)
    Unknown23018(1)
    label(183)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(183)
    ExitState()
    label(190)
    sprite('na600_00', 6)
    if SLOT_158:
        XPositionRelativeFacing(-1230000)
    else:
        XPositionRelativeFacing(-1465000)
    sprite('na600_01', 6)
    Voiceline('pna600biz')
    sprite('na600_02', 6)
    sprite('na600_03', 5)
    sprite('na600_04', 12)
    PrivateSE('cloth_l')
    sprite('na600_05', 8)
    sprite('na600_06', 20)
    sprite('na600_07', 30)
    sprite('na600_08', 6)
    PrivateSE('slash_rapier_fast')
    sprite('na600_09', 4)
    PrivateSE('slash_rapier_fast')
    sprite('na600_10', 4)
    PrivateSE('grip_fast')
    label(191)
    sprite('na600_11', 1)
    if SLOT_97:
        conditionalSendToLabel(191)
    sprite('na600_12', 6)
    DemoTimer(240)
    ObjectUpon(24, upon_40)
    label(192)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(192)
    ExitState()
    label(200)
    sprite('na600_00', 1)
    if SLOT_158:
        XPositionRelativeFacing(-1230000)
    else:
        XPositionRelativeFacing(-1465000)

    def upon_40():
        clearUponHandler(upon_40)
        sendToLabel(202)
    label(201)
    sprite('na600_00', 6)
    sprite('na600_01', 6)
    sprite('na600_02', 6)
    gotoLabel(201)
    label(202)
    sprite('na600_03', 5)
    Voiceline('pna601ume')
    sprite('na600_04', 12)
    PrivateSE('cloth_l')
    sprite('na600_05', 8)
    sprite('na600_06', 20)
    sprite('na600_07', 30)
    sprite('na600_08', 6)
    PrivateSE('slash_rapier_fast')
    sprite('na600_09', 4)
    PrivateSE('slash_rapier_fast')
    sprite('na600_10', 4)
    PrivateSE('grip_fast')
    label(203)
    sprite('na600_11', 1)
    if SLOT_97:
        conditionalSendToLabel(203)
    sprite('na600_11', 30)
    sprite('na600_12', 6)
    Unknown23018(1)
    label(204)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(204)
    ExitState()
    label(210)
    sprite('na600_00', 6)
    sprite('na600_01', 6)
    sprite('na600_02', 6)
    sprite('na600_03', 5)
    sprite('na600_04', 12)
    PrivateSE('cloth_l')
    sprite('na600_05', 8)
    sprite('na600_06', 1)
    Voiceline('pna600bnt')
    label(211)
    sprite('na600_06', 1)
    if SLOT_97:
        conditionalSendToLabel(211)
    sprite('na600_06', 30)
    sprite('na600_07', 6)
    sprite('na600_08', 6)
    PrivateSE('slash_rapier_fast')
    sprite('na600_09', 4)
    PrivateSE('slash_rapier_fast')
    sprite('na600_10', 4)
    PrivateSE('grip_fast')
    sprite('na600_11', 4)
    sprite('na600_12', 4)
    ObjectUpon(24, upon_40)
    DemoTimer(120)
    label(212)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(212)
    label(220)
    sprite('na601_00', 6)
    XPositionRelativeFacing(-1465000)
    sprite('na601_50', 3)
    sprite('na601_51', 3)
    sprite('na601_52', 3)
    sprite('na601_53', 75)
    Voiceline('pna600use')
    sprite('na601_01', 6)
    sprite('na601_02', 3)
    sprite('na601_54', 14)
    PrivateSE('walk_marble_heavy')
    sprite('na601_03', 6)
    sprite('na601_04', 6)
    sprite('na601_05', 6)
    sprite('na601_06', 4)
    sprite('na601_07', 4)
    sprite('na601_08', 6)
    sprite('na601_09', 6)
    sprite('na601_10', 6)
    sprite('na601_11', 6)
    PrivateSE('hair')
    sprite('na601_12', 6)
    sprite('na601_13', 8)
    sprite('na601_14', 7)
    label(221)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    if SLOT_97:
        conditionalSendToLabel(221)
    sprite('na000_00', 1)
    ObjectUpon(24, upon_40)
    DemoTimer(120)
    label(222)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(222)
    label(991)
    sprite('na000_00', 1)
    SetZVal(1000)
    DemoTimer(120)
    label(992)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(992)
    label(993)
    sprite('na033_00', 2)

    def upon_LANDING():
        clearUponHandler(upon_LANDING)
        sendToLabel(995)

    def upon_STATE_END():
        SetZVal(0)
        Visibility(1)
        Unknown3001(255)
    ScreenCollision(0)
    EnableCollision(0)
    Unknown2053(0)
    Unknown3001(255)
    ConstantAlphaModifier(-20)
    physicsXImpulse(-51000)
    physicsYImpulse(18800)
    setGravity(1500)
    Unknown8002()
    sprite('na033_01', 3)
    label(994)
    sprite('na033_01', 3)
    sprite('na033_02', 3)
    spriteEnd()
    gotoLabel(994)
    label(995)
    sprite('null', 3)
    ExitState()


@State
def CmnActRoundWin():
    sprite('keep', 32767)


@State
def CmnActMatchWin():
    if SLOT_169:
        conditionalSendToLabel(482)
    if SLOT_122:
        conditionalSendToLabel(482)
    if SLOT_123:
        conditionalSendToLabel(482)
    sprite('keep', 2)

    def upon_EVERY_FRAME():
        SLOT_58 = 1
        CopyFromRightToLeft(25, SLOT_52, 24, SLOT_58)
        if SLOT_52:
            if PartnerChar('bno'):
                if SLOT_145 <= 500000:
                    sendToLabel(100)
                    clearUponHandler(upon_EVERY_FRAME)
            if PartnerChar('bhz'):
                if SLOT_145 <= 500000:
                    sendToLabel(110)
                    clearUponHandler(upon_EVERY_FRAME)
            if PartnerChar('bes'):
                if SLOT_145 <= 500000:
                    sendToLabel(120)
                    clearUponHandler(upon_EVERY_FRAME)
            if PartnerChar('pbc'):
                if SLOT_145 <= 500000:
                    sendToLabel(130)
                    clearUponHandler(upon_EVERY_FRAME)
            if PartnerChar('pka'):
                if SLOT_145 <= 500000:
                    sendToLabel(140)
                    clearUponHandler(upon_EVERY_FRAME)
            if PartnerChar('uhy'):
                if SLOT_145 <= 500000:
                    sendToLabel(150)
                    clearUponHandler(upon_EVERY_FRAME)
            if PartnerChar('rwi'):
                if SLOT_145 <= 500000:
                    sendToLabel(160)
                    clearUponHandler(upon_EVERY_FRAME)
            if PartnerChar('uor'):
                if SLOT_145 <= 500000:
                    sendToLabel(170)
                    clearUponHandler(upon_EVERY_FRAME)
            if PartnerChar('pmi'):
                if SLOT_145 <= 500000:
                    sendToLabel(180)
                    clearUponHandler(upon_EVERY_FRAME)
            if PartnerChar('ume'):
                if SLOT_145 <= 500000:
                    sendToLabel(190)
                    clearUponHandler(upon_EVERY_FRAME)
            if PartnerChar('bnt'):
                if SLOT_145 <= 500000:
                    sendToLabel(200)
                    clearUponHandler(upon_EVERY_FRAME)
            if PartnerChar('use'):
                if SLOT_145 <= 500000:
                    sendToLabel(210)
                    clearUponHandler(upon_EVERY_FRAME)
    label(482)
    sprite('keep', 1)
    clearUponHandler(upon_EVERY_FRAME)
    SLOT_58 = 0
    if random_(2, 50):
        conditionalSendToLabel(10)
    sprite('na610_00', 3)
    sprite('na610_01', 3)
    sprite('na610_02', 5)
    sprite('na610_03', 3)
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 3)
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 4)
    GFX_0('WinYakkyo', 0)
    sprite('na610_04', 7)
    sprite('na610_05', 7)
    sprite('na610_06', 7)
    if SLOT_158:
        if SLOT_52:
            RandomVoiceline('pna524', 100, '', 0, '', 0, '', 0)
        elif SLOT_108:
            RandomVoiceline('pna402_0', 100, 'pna402_1', 100, '', 0, '', 0)
        else:
            RandomVoiceline('pna520', 100, 'pna521', 100, '', 0, '', 0)
    sprite('na610_07', 6)
    sprite('na610_08', 6)
    sprite('na610_07', 6)
    sprite('na610_08', 10)
    sprite('na610_09', 5)
    sprite('na610_10', 3)
    sprite('na610_11', 4)
    sprite('na610_12', 10)
    sprite('na610_13', 4)
    sprite('na610_14', 7)
    sprite('na610_15', 8)
    sprite('na610_16', 6)
    sprite('na610_17', 6)
    sprite('na610_18', 6)
    Unknown23018(1)
    label(1)
    sprite('na610_16', 6)
    sprite('na610_17', 6)
    sprite('na610_18', 6)
    spriteEnd()
    gotoLabel(1)
    label(10)
    sprite('na611_00', 6)

    def RunOnObject_24():
        ScreenCollision(0)
        Unknown2053(0)
    StayAfterMovement(1, 0)
    ObjectUpon2(11, 6001, 0)
    sprite('na611_01', 6)
    sprite('na611_02', 6)
    sprite('na611_03', 6)
    sprite('na611_04', 6)
    sprite('na611_05', 6)
    sprite('na611_06', 6)
    sprite('na611_07', 6)
    if SLOT_158:
        if SLOT_52:
            RandomVoiceline('pna525', 100, '', 0, '', 0, '', 0)
        elif SLOT_108:
            RandomVoiceline('pna402_0', 100, '', 0, '', 0, '', 0)
        else:
            RandomVoiceline('pna522', 100, 'pna523', 100, '', 0, '', 0)
    sprite('na611_08', 3)
    sprite('na611_09', 6)
    sprite('na611_10', 6)
    sprite('na611_08', 3)
    sprite('na611_09', 6)
    sprite('na611_10', 6)
    sprite('na611_08', 3)
    sprite('na611_09', 6)
    sprite('na611_10', 6)
    sprite('na611_08', 3)
    sprite('na611_09', 6)
    sprite('na611_10', 6)
    sprite('na611_08', 6)
    sprite('na611_09', 6)
    Unknown23018(1)
    label(11)
    sprite('na611_50', 3)
    sprite('na611_51', 6)
    sprite('na611_52', 6)
    spriteEnd()
    gotoLabel(11)
    label(100)
    sprite('na000_00', 1)

    def upon_40():
        clearUponHandler(upon_40)
        sendToLabel(102)
    label(101)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(101)
    label(102)
    sprite('na611_00', 6)
    StayAfterMovement(1, 0)
    ObjectUpon2(11, 6001, 0)
    sprite('na611_01', 6)
    sprite('na611_02', 6)
    sprite('na611_03', 6)
    sprite('na611_04', 6)
    sprite('na611_05', 6)
    sprite('na611_06', 6)
    sprite('na611_07', 6)
    Voiceline('pna701bno')
    sprite('na611_08', 3)
    sprite('na611_09', 6)
    sprite('na611_10', 6)
    sprite('na611_08', 3)
    sprite('na611_09', 6)
    sprite('na611_10', 6)
    sprite('na611_08', 3)
    sprite('na611_09', 6)
    sprite('na611_10', 6)
    sprite('na611_08', 3)
    sprite('na611_09', 6)
    sprite('na611_10', 6)
    sprite('na611_08', 6)
    sprite('na611_09', 6)
    Unknown23018(1)
    label(103)
    sprite('na611_50', 3)
    sprite('na611_51', 6)
    sprite('na611_52', 6)
    spriteEnd()
    gotoLabel(103)
    label(110)
    sprite('na000_00', 1)

    def upon_40():
        clearUponHandler(upon_40)
        sendToLabel(112)
    label(111)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(111)
    label(112)
    sprite('na610_00', 3)
    sprite('na610_01', 3)
    sprite('na610_02', 5)
    sprite('na610_03', 3)
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 3)
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 4)
    GFX_0('WinYakkyo', 0)
    sprite('na610_04', 7)
    sprite('na610_05', 7)
    sprite('na610_06', 7)
    sprite('na610_07', 6)
    Voiceline('pna701bhz')
    sprite('na610_08', 6)
    sprite('na610_07', 6)
    sprite('na610_08', 10)
    sprite('na610_09', 5)
    sprite('na610_10', 3)
    sprite('na610_11', 4)
    sprite('na610_12', 10)
    sprite('na610_13', 4)
    sprite('na610_14', 7)
    sprite('na610_15', 8)
    sprite('na610_16', 6)
    sprite('na610_17', 6)
    sprite('na610_18', 6)
    Unknown23018(1)
    label(113)
    sprite('na610_16', 6)
    sprite('na610_17', 6)
    sprite('na610_18', 6)
    spriteEnd()
    gotoLabel(113)
    label(120)
    sprite('na000_00', 1)

    def upon_40():
        clearUponHandler(upon_40)
        sendToLabel(122)
    label(121)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(121)
    label(122)
    sprite('na610_00', 3)
    sprite('na610_01', 3)
    sprite('na610_02', 5)
    sprite('na610_03', 3)
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 3)
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 4)
    GFX_0('WinYakkyo', 0)
    sprite('na610_04', 7)
    sprite('na610_05', 7)
    sprite('na610_06', 7)
    sprite('na610_07', 6)
    Voiceline('pna701bes')
    sprite('na610_08', 6)
    sprite('na610_07', 6)
    sprite('na610_08', 10)
    sprite('na610_09', 5)
    sprite('na610_10', 3)
    sprite('na610_11', 4)
    sprite('na610_12', 10)
    sprite('na610_13', 4)
    sprite('na610_14', 7)
    sprite('na610_15', 8)
    sprite('na610_16', 6)
    sprite('na610_17', 6)
    sprite('na610_18', 6)
    Unknown23018(1)
    label(123)
    sprite('na610_16', 6)
    sprite('na610_17', 6)
    sprite('na610_18', 6)
    spriteEnd()
    gotoLabel(123)
    label(130)
    sprite('na000_00', 1)

    def upon_40():
        clearUponHandler(upon_40)
        sendToLabel(132)
    label(131)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(131)
    label(132)
    sprite('na611_00', 6)
    StayAfterMovement(1, 0)
    ObjectUpon2(11, 6001, 0)
    sprite('na611_01', 6)
    sprite('na611_02', 6)
    sprite('na611_03', 6)
    sprite('na611_04', 6)
    sprite('na611_05', 6)
    sprite('na611_06', 6)
    sprite('na611_07', 6)
    Voiceline('pna701pbc')
    sprite('na611_08', 3)
    sprite('na611_09', 6)
    sprite('na611_10', 6)
    sprite('na611_08', 3)
    sprite('na611_09', 6)
    sprite('na611_10', 6)
    sprite('na611_08', 3)
    sprite('na611_09', 6)
    sprite('na611_10', 6)
    sprite('na611_08', 3)
    sprite('na611_09', 6)
    sprite('na611_10', 6)
    sprite('na611_08', 6)
    sprite('na611_09', 6)
    Unknown23018(1)
    label(133)
    sprite('na611_50', 3)
    sprite('na611_51', 6)
    sprite('na611_52', 6)
    spriteEnd()
    gotoLabel(133)
    label(140)
    sprite('na000_00', 1)

    def upon_40():
        clearUponHandler(upon_40)
        sendToLabel(142)
    label(141)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(141)
    label(142)
    sprite('na610_00', 3)
    sprite('na610_01', 3)
    sprite('na610_02', 5)
    sprite('na610_03', 3)
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 3)
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 4)
    GFX_0('WinYakkyo', 0)
    sprite('na610_04', 7)
    sprite('na610_05', 7)
    sprite('na610_06', 7)
    Voiceline('pna701pka')
    sprite('na610_07', 6)
    sprite('na610_08', 6)
    sprite('na610_07', 6)
    sprite('na610_08', 10)
    sprite('na610_09', 5)
    sprite('na610_10', 3)
    sprite('na610_11', 4)
    sprite('na610_12', 10)
    sprite('na610_13', 4)
    sprite('na610_14', 7)
    sprite('na610_15', 8)
    sprite('na610_16', 6)
    sprite('na610_17', 6)
    sprite('na610_18', 6)
    Unknown23018(1)
    label(143)
    sprite('na610_16', 6)
    sprite('na610_17', 6)
    sprite('na610_18', 6)
    spriteEnd()
    gotoLabel(143)
    label(150)
    sprite('na000_00', 1)

    def upon_40():
        clearUponHandler(upon_40)
        sendToLabel(152)
    label(151)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(151)
    label(152)
    sprite('na610_00', 3)
    sprite('na610_01', 3)
    sprite('na610_02', 5)
    sprite('na610_03', 3)
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 3)
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 4)
    GFX_0('WinYakkyo', 0)
    sprite('na610_04', 7)
    sprite('na610_05', 7)
    sprite('na610_06', 7)
    Voiceline('pna701uhy')
    sprite('na610_07', 6)
    sprite('na610_08', 6)
    sprite('na610_07', 6)
    sprite('na610_08', 10)
    sprite('na610_09', 5)
    sprite('na610_10', 3)
    sprite('na610_11', 4)
    sprite('na610_12', 10)
    sprite('na610_13', 4)
    sprite('na610_14', 7)
    sprite('na610_15', 8)
    sprite('na610_16', 6)
    sprite('na610_17', 6)
    sprite('na610_18', 6)
    Unknown23018(1)
    label(153)
    sprite('na610_16', 6)
    sprite('na610_17', 6)
    sprite('na610_18', 6)
    spriteEnd()
    gotoLabel(153)
    label(160)
    sprite('na000_00', 1)

    def upon_40():
        clearUponHandler(upon_40)
        sendToLabel(162)
    label(161)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(161)
    label(162)
    sprite('na610_00', 3)
    sprite('na610_01', 3)
    sprite('na610_02', 5)
    sprite('na610_03', 3)
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 3)
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 4)
    GFX_0('WinYakkyo', 0)
    sprite('na610_04', 7)
    sprite('na610_05', 7)
    sprite('na610_06', 7)
    Voiceline('pna701rwi')
    sprite('na610_07', 6)
    sprite('na610_08', 6)
    sprite('na610_07', 6)
    sprite('na610_08', 10)
    sprite('na610_09', 5)
    sprite('na610_10', 3)
    sprite('na610_11', 4)
    sprite('na610_12', 10)
    sprite('na610_13', 4)
    sprite('na610_14', 7)
    sprite('na610_15', 8)
    sprite('na610_16', 6)
    sprite('na610_17', 6)
    sprite('na610_18', 6)
    Unknown23018(1)
    label(163)
    sprite('na610_16', 6)
    sprite('na610_17', 6)
    sprite('na610_18', 6)
    spriteEnd()
    gotoLabel(163)
    label(170)
    sprite('na000_00', 1)

    def upon_40():
        clearUponHandler(upon_40)
        sendToLabel(172)
    label(171)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(171)
    label(172)
    sprite('na610_00', 3)
    sprite('na610_01', 3)
    sprite('na610_02', 5)
    sprite('na610_03', 3)
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 3)
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 4)
    GFX_0('WinYakkyo', 0)
    sprite('na610_04', 7)
    sprite('na610_05', 7)
    sprite('na610_06', 7)
    Voiceline('pna701uor')
    sprite('na610_07', 6)
    sprite('na610_08', 6)
    sprite('na610_07', 6)
    sprite('na610_08', 10)
    sprite('na610_09', 5)
    sprite('na610_10', 3)
    sprite('na610_11', 4)
    sprite('na610_12', 10)
    sprite('na610_13', 4)
    sprite('na610_14', 7)
    sprite('na610_15', 8)
    sprite('na610_16', 6)
    sprite('na610_17', 6)
    sprite('na610_18', 6)
    Unknown23018(1)
    label(173)
    sprite('na610_16', 6)
    sprite('na610_17', 6)
    sprite('na610_18', 6)
    spriteEnd()
    gotoLabel(173)
    label(180)
    sprite('na610_00', 3)
    sprite('na610_01', 3)
    sprite('na610_02', 5)
    sprite('na610_03', 3)
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 3)
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 4)
    GFX_0('WinYakkyo', 0)
    sprite('na610_04', 7)
    sprite('na610_05', 7)
    sprite('na610_06', 7)
    sprite('na610_07', 6)
    Voiceline('pna700pmi')
    sprite('na610_08', 6)
    sprite('na610_07', 6)
    sprite('na610_08', 10)
    sprite('na610_09', 5)
    sprite('na610_10', 3)
    sprite('na610_11', 4)
    sprite('na610_12', 10)
    sprite('na610_13', 4)
    sprite('na610_14', 7)
    sprite('na610_15', 8)
    sprite('na610_16', 6)
    sprite('na610_17', 6)
    sprite('na610_18', 6)
    label(181)
    sprite('na610_16', 6)
    sprite('na610_17', 6)
    sprite('na610_18', 6)
    spriteEnd()
    if SLOT_97:
        conditionalSendToLabel(181)
    sprite('na610_16', 1)
    ObjectUpon(24, upon_40)
    DemoTimer(320)
    label(182)
    sprite('na610_16', 6)
    sprite('na610_17', 6)
    sprite('na610_18', 6)
    spriteEnd()
    gotoLabel(182)
    label(190)
    sprite('na000_00', 1)

    def upon_40():
        clearUponHandler(upon_40)
        sendToLabel(192)
    label(191)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(191)
    label(192)
    sprite('na610_00', 3)
    sprite('na610_01', 3)
    sprite('na610_02', 5)
    sprite('na610_03', 3)
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 3)
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 4)
    GFX_0('WinYakkyo', 0)
    sprite('na610_04', 7)
    sprite('na610_05', 7)
    sprite('na610_06', 7)
    Voiceline('pna701ume')
    sprite('na610_07', 6)
    sprite('na610_08', 6)
    sprite('na610_07', 6)
    sprite('na610_08', 10)
    sprite('na610_09', 5)
    sprite('na610_10', 3)
    sprite('na610_11', 4)
    sprite('na610_12', 10)
    sprite('na610_13', 4)
    sprite('na610_14', 7)
    sprite('na610_15', 8)
    sprite('na610_16', 6)
    sprite('na610_17', 6)
    sprite('na610_18', 6)
    Unknown23018(1)
    label(193)
    sprite('na610_16', 6)
    sprite('na610_17', 6)
    sprite('na610_18', 6)
    spriteEnd()
    gotoLabel(193)
    label(200)
    sprite('na000_00', 1)

    def upon_40():
        clearUponHandler(upon_40)
        sendToLabel(202)
    label(201)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(201)
    label(202)
    sprite('na611_00', 6)
    StayAfterMovement(1, 0)
    ObjectUpon2(11, 6001, 0)
    sprite('na611_01', 6)
    sprite('na611_02', 6)
    sprite('na611_03', 6)
    sprite('na611_04', 6)
    sprite('na611_05', 6)
    sprite('na611_06', 6)
    sprite('na611_07', 6)
    Voiceline('pna701bnt')
    label(203)
    sprite('na611_08', 3)
    sprite('na611_09', 6)
    sprite('na611_10', 6)
    if SLOT_97:
        conditionalSendToLabel(203)
    sprite('na611_08', 3)
    sprite('na611_09', 6)
    sprite('na611_10', 6)
    Unknown23018(1)
    label(204)
    sprite('na611_50', 3)
    sprite('na611_51', 6)
    sprite('na611_52', 6)
    spriteEnd()
    gotoLabel(204)
    label(210)
    sprite('na000_00', 1)

    def upon_40():
        clearUponHandler(upon_40)
        sendToLabel(212)
    label(211)
    sprite('na000_00', 6)
    sprite('na000_01', 6)
    sprite('na000_02', 6)
    sprite('na000_03', 6)
    sprite('na000_04', 6)
    sprite('na000_05', 6)
    sprite('na000_06', 6)
    sprite('na000_07', 6)
    gotoLabel(211)
    label(212)
    sprite('na610_00', 3)
    sprite('na610_01', 3)
    sprite('na610_02', 5)
    sprite('na610_03', 3)
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 3)
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 4)
    GFX_0('WinYakkyo', 0)
    sprite('na610_04', 7)
    sprite('na610_05', 7)
    sprite('na610_06', 7)
    Voiceline('pna701use')
    sprite('na610_07', 6)
    sprite('na610_08', 6)
    sprite('na610_07', 6)
    sprite('na610_08', 10)
    sprite('na610_09', 5)
    sprite('na610_10', 3)
    sprite('na610_11', 4)
    sprite('na610_12', 10)
    sprite('na610_13', 4)
    sprite('na610_14', 7)
    sprite('na610_15', 8)
    sprite('na610_16', 6)
    sprite('na610_17', 6)
    sprite('na610_18', 6)
    Unknown23018(1)
    label(213)
    sprite('na610_16', 6)
    sprite('na610_17', 6)
    sprite('na610_18', 6)
    spriteEnd()
    gotoLabel(213)


@State
def CmnActLose():
    sprite('na070_00', 15)
    if SLOT_158:
        RandomVoiceline('pna403_0', 100, 'pna403_1', 100, '', 0, '', 0)
    sprite('na070_01', 6)
    sprite('na070_02', 2)
    Unknown23018(1)
    sprite('na070_03', 32767)
