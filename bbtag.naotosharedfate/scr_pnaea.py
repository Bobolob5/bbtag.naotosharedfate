@State
def PNA_PersonaCreate():

    def upon_IMMEDIATE():
        Unknown23022(1)
        ShadowOffsetY(-75000)
        AbsoluteY(0)
        Unknown23013(1)
    sprite('null', 32767)
    Visibility(1)
    Unknown24('PNA_PersonaWait', 100)


@State
def PNA_PersonaWait():

    def upon_IMMEDIATE():
        SLOT_11 = 0
        SLOT_59 = -1
        callSubroutine('PNA_ReceptionSignal')
    sprite('null', 32767)
    Visibility(1)
    Unknown3001(0)
    ConstantAlphaModifier(0)
    spriteEnd()


@Subroutine
def PNA_ReceptionSignal():

    def upon_43():
        if SLOT_48 == 101:
            Unknown23185('PNA_Persona5A4th', 50)
        if SLOT_48 == 102:
            Unknown23185('PNA_Persona5B', 50)
        if SLOT_48 == 103:
            Unknown23185('PNA_Persona5B2nd', 50)
        if SLOT_48 == 104:
            Unknown23185('PNA_Persona5B3rd', 50)
        if SLOT_48 == 105:
            Unknown23185('PNA_PersonaThrow', 50)
        if SLOT_48 == 201:
            Unknown23185('PNA_Persona2B', 50)
        if SLOT_48 == 203:
            Unknown23185('PNA_Persona2BHold', 50)
        if SLOT_48 == 204:
            Unknown23185('PNA_Persona2B_2', 50)
        if SLOT_48 == 301:
            Unknown23185('PNA_PersonaJB', 50)
        if SLOT_48 == 304:
            Unknown23185('PNA_PersonaJC', 50)
        if SLOT_48 == 305:
            Unknown23185('PNA_PersonaJ_Test', 50)
        if SLOT_48 == 401:
            Unknown23185('Trap', 100)
        if SLOT_48 == 402:
            Unknown23185('PartnerAssistAtk_B', 100)
        if SLOT_48 == 403:
            Unknown23185('PAssault2_RA', 100)
        if SLOT_48 == 405:
            Unknown23185('PartnerAssistAtk_D', 100)
        if SLOT_48 == 502:
            Unknown23185('PBC_PersonaUltimateHAMAON', 200)
        if SLOT_48 == 503:
            Unknown23185('PBC_PersonaUltimateODHAMAON', 200)
        if SLOT_48 == 504:
            Unknown23185('PBC_PersonaUltimateMUDOON', 200)
        if SLOT_48 == 950:
            Unknown23185('PNA_PersonaIchigeki', 200)
        if SLOT_48 == 6001:
            Unknown23185('PersonaMatchWin2', 300)
        if SLOT_48 == 3017:
            Unknown23185('PersonaDeleteAndIdling', 300)


@Subroutine
def PersonaReset():
    PaletteIndex(1)
    Unknown23022(0)
    Unknown2053(0)
    Unknown23015(11)
    SetZVal(-1)
    EndMomentum(1)
    Unknown4009(0)
    Unknown4008(0)
    Unknown4007(0)
    EnableCollision(0)
    Unknown30041('')


@Subroutine
def PNA_EffectInit():
    SetZVal(5)
    Unknown23015(11)


@Subroutine
def PNA_AttackInit():
    Unknown23028(1, 1)
    Unknown30037('')
    Unknown30035(1)
    callSubroutine('PersonaReset')
    Unknown23015(11)
    SetZVal(10)
    if SLOT_11 == 0:
        SLOT_58 = 1
    if SLOT_11 == 10:
        SLOT_58 = 1
    SLOT_11 = 100
    callSubroutine('PNA_ReceptionSignal')
    StrikeProjectileLevel(1)
    ProjectileLevel(0)
    Unknown23023()
    EnableCollision(1)
    Unknown30040(1)
    Unknown30040(2)


@Subroutine
def PNA_SPAttackInit():
    Unknown23028(2, 1)
    Unknown30037('')
    Unknown30035(1)
    callSubroutine('PersonaReset')
    Unknown23015(11)
    SetZVal(10)
    if SLOT_11 == 0:
        SLOT_58 = 1
    if SLOT_11 == 10:
        SLOT_58 = 1
    SLOT_11 = 110
    callSubroutine('PNA_ReceptionSignal')
    StrikeProjectileLevel(1)
    ProjectileLevel(0)
    Unknown23023()
    EnableCollision(1)
    Unknown30040(1)
    Unknown30040(2)


@Subroutine
def PNA_DDAttackInit():
    Unknown23028(3, 1)
    Unknown30037('')
    callSubroutine('PersonaReset')
    Unknown23015(11)
    SetZVal(10)
    if SLOT_11 == 0:
        SLOT_58 = 1
    if SLOT_11 == 10:
        SLOT_58 = 1
    StrikeProjectileLevel(1)
    ProjectileLevel(0)
    SLOT_11 = 120
    callSubroutine('PNA_ReceptionSignal')
    Unknown23023()


@Subroutine
def PNA_CheckWarp():
    if SLOT_58:
        Unknown3001(0)
        ConstantAlphaModifier(85)
        RunLoopUpon(upon_17, 4)

        def upon_17():
            Unknown3001(255)
            ConstantAlphaModifier(0)


@Subroutine
def PNA_ForceWarp():
    SLOT_58 = 1
    Unknown3001(0)
    ConstantAlphaModifier(85)
    RunLoopUpon(upon_17, 4)

    def upon_17():
        Unknown3001(255)
        ConstantAlphaModifier(0)


@State
def PersonaDeleteAndIdling():

    def upon_IMMEDIATE():
        callSubroutine('PersonaReset')
    sprite('keep', 32767)
    if SLOT_143:
        GFX_0('PersonaDeleteEffect', 100)
        PrivateSE('persona_disappear')
    SLOT_11 = 10
    SLOT_59 = -1
    enterState('PNA_PersonaWait')


@State
def PersonaSummonEffect():
    sprite('null', 30)
    Unknown23015(13)
    ParticleLayer(11)
    Unknown4045('persona_summon', 100)


@State
def PersonaSummonEffect_PLAYER():
    sprite('null', 30)
    AddY(288000)
    AddX(112000)
    GFX_1('persona_summon_ply', 100)


@State
def PersonaDeleteEffect():

    def upon_IMMEDIATE():
        callSubroutine('PersonaReset')
        callSubroutine('PNA_ReceptionSignal')
    sprite('null', 30)
    SetZVal(1)
    Unknown23053(25, 11)
    PaletteIndex(1)
    BlendMode_Normal()
    Unknown1059(-100)
    Unknown1067(150)
    ConstantAlphaModifier(-20)
    Unknown23022(1)
    ParticleLayer(11)
    Unknown4045('persona_delete', 100)
    Unknown2054(1)
    EnableCollision(0)
    EndMomentum(1)


@State
def PNA_Persona5A4th():

    def upon_IMMEDIATE():
        callSubroutine('PersonaReset')
        Unknown23184(3, 100, -150000, 200000, 0, 0, 0, 0)
        Unknown23023()
        callSubroutine('PNA_CheckWarp')
        Unknown4007(3)
        Unknown23022(1)
        StrikeProjectileLevel(1)
    sprite('su400_00', 3)
    sprite('su400_01', 3)
    sprite('su400_02', 3)
    sprite('su400_00', 3)
    sprite('su400_01', 3)
    sprite('su400_02', 3)
    sprite('su400_00', 3)
    sprite('su400_01', 3)
    sprite('su400_02', 3)
    sprite('su400_00', 3)
    sprite('su400_01', 3)
    sprite('su400_02', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')


@State
def PNA_Persona5B():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, -100000, 100000, -100000, 500000, 100000, 100000)
        callSubroutine('PNA_AttackInit')
        AttackLevel(3)
        AttackP1(90)
        UseSlashHitspark(1)
        PushbackX(23000)
        AirPushbackY(20000)
        AttackAttributes('B')
        callSubroutine('PNA_CheckWarp')
        Unknown2053(1)
        Unknown4007(3)
        Unknown23078(1)
        Unknown23059(1)
    sprite('su204_00', 3)
    sprite('su204_01', 3)
    PrivateSE('cloth_l')
    sprite('su204_03', 3)
    ObjectUpon2(3, 12, 0)
    RefreshMultihit()
    GFX_0('suef_5C', 100)
    PrivateSE('slash_beam_fast')
    Unknown4007(0)
    sprite('su204_04', 4)
    sprite('su204_05', 15)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')


@State
def PNA_Persona5B2nd():

    def upon_IMMEDIATE():
        Unknown23023()
        callSubroutine('PNA_AttackInit')
        AttackLevel(3)
        Damage(1000)
        AttackP1(90)
        AttackP2(80)
        SingleProration(1)
        AirPushbackX(5000)
        AirPushbackY(10000)
        Hitstun(20)
        AirUntechableTime(20)
        Hitstop(9)
        PushbackX(12000)
        UseSlashHitspark(1)
        AttackAttributes('B')
        physicsXImpulse(40000)
        callSubroutine('PNA_CheckWarp')
        Unknown2053(1)
        Unknown23078(1)
        Unknown23059(1)
    sprite('su205_00', 1)
    sprite('su205_01', 1)
    sprite('su205_02', 1)
    sprite('su206_01', 1)
    sprite('su206_02', 2)
    sprite('su206_03', 2)
    GFX_0('suef_5DD', 100)
    sprite('su206_04', 2)
    EndMomentum(1)
    RefreshMultihit()
    PrivateSE('slash_beam_middle')
    sprite('su206_06', 2)
    physicsXImpulse(20000)
    XImpulseAcceleration(120)
    GFX_0('suef_5DDD', 100)
    sprite('su206_07', 6)
    ObjectUpon2(2, 12, 0)
    RefreshMultihit()
    PrivateSE('slash_beam_middle')
    sprite('su206_07', 7)
    ObjectUpon2(2, 3020, 0)
    StartMultihit()
    XImpulseAcceleration(25)
    sprite('su206_08', 6)
    XImpulseAcceleration(25)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')


@State
def PNA_Persona5B3rd():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, 0, 50000, 0, 5000000, 100000, 100000)
        callSubroutine('PNA_AttackInit')
        AttackLevel(3)
        AttackP1(90)
        AttackP2(80)
        AirHitstunAnimation(AIR_VERTICAL)
        AirUntechableTime(24)
        UseSlashHitspark(1)
        AttackAttributes('B')
        callSubroutine('PNA_CheckWarp')
        Unknown2053(1)
        Unknown4007(3)
        Unknown23078(1)
        Unknown23059(1)
    sprite('su206_09', 3)
    setInvincible(1)
    SpecificInvincibility('H')
    sprite('su206_10', 3)
    physicsXImpulse(20000)
    SetAcceleration(-500)
    physicsYImpulse(20000)
    GFX_0('suef_5DDDD', 100)
    sprite('su206_11', 3)
    PrivateSE('slash_beam_middle')
    Unknown4007(0)
    sprite('su206_12', 3)
    setInvincible(0)
    sprite('su206_13', 3)
    EndMomentum(1)
    sprite('su206_14', 3)
    sprite('su206_12', 3)
    sprite('su206_13', 3)
    sprite('su206_14', 3)
    sprite('su206_12', 3)
    PrivateSE('cloth_l')
    sprite('su206_13', 3)
    sprite('su206_14', 3)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')


@State
def PNA_PersonaThrow():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, -100000, 100000, 0, 0, 0, 0)
        callSubroutine('PNA_AttackInit')
        AttackLevel(4)
        Damage(2000)
        MinimumDamage(100)
        AttackP1(100)
        AttackP2(50)
        GroundedHitstunAnimation(AIR_BLOWBACK)
        AirHitstunAnimation(AIR_BLOWBACK)
        AirPushbackX(80000)
        AirPushbackY(30000)
        AirUntechableTime(120)
        AirHitstunAfterWallbounce(60)
        Floorslide(20)
        Wallstick(1)
        WallstickDuration(30)
        AttackAttributes('B')
        UseSlashHitspark(1)
        IgnoreBurst(1)
        setInvincible(1)
        Unknown30048(1)
        callSubroutine('PNA_CheckWarp')
        Unknown2053(1)
        Unknown23078(1)
    sprite('su232_00', 4)
    sprite('su232_01', 4)
    sprite('su232_04', 4)
    physicsXImpulse(15000)
    PrivateSE('slash_beam_slow')
    sprite('su232_05', 4)
    GFX_0('suef_2C', 0)
    ObjectUpon2(2, 12, 0)
    RefreshMultihit()
    XImpulseAcceleration(70)
    sprite('su232_06', 4)
    XImpulseAcceleration(60)
    sprite('su232_07', 4)
    XImpulseAcceleration(60)
    sprite('su232_08', 4)
    XImpulseAcceleration(60)
    sprite('su232_06', 4)
    XImpulseAcceleration(60)
    sprite('su232_07', 4)
    XImpulseAcceleration(0)
    sprite('su232_08', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')


@State
def PNA_Persona2B():

    def upon_IMMEDIATE():
        Unknown23023()
        callSubroutine('PNA_AttackInit')
        AttackLevel(3)
        AttackP1(90)
        AttackP2(80)
        GroundedHitstunAnimation(AIR_TAILSPIN)
        AirHitstunAnimation(AIR_TAILSPIN)
        UseSlashHitspark(1)
        AirUntechableTime(40)
        AirPushbackX(25000)
        AttackAttributes('B')
        callSubroutine('PNA_CheckWarp')
        Unknown2053(1)
        Unknown23078(1)

        def upon_11():
            XImpulseAcceleration(40)
        Unknown23059(1)
    sprite('su232_00', 4)
    ForceFaceSprite()
    sprite('su232_01', 4)
    sprite('su232_04', 2)
    physicsXImpulse(50000)
    PrivateSE('slash_beam_slow')
    sprite('su232_05', 4)
    GFX_0('suef_2C', 0)
    ObjectUpon2(2, 12, 0)
    RefreshMultihit()
    XImpulseAcceleration(70)
    sprite('su232_06', 4)
    XImpulseAcceleration(60)
    sprite('su232_07', 4)
    StartMultihit()
    XImpulseAcceleration(60)
    sprite('su232_08', 4)
    XImpulseAcceleration(60)
    StartMultihit()
    sprite('su232_06', 4)
    XImpulseAcceleration(60)
    StartMultihit()
    sprite('su232_07', 4)
    XImpulseAcceleration(0)
    StartMultihit()
    sprite('su232_08', 4)
    StartMultihit()
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')


@State
def PNA_Persona2BHold():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, 0, 50000, -10000000, 10000000, -10000000, 10000000
            )
        callSubroutine('PNA_AttackInit')
        AttackLevel(4)
        Damage(1700)
        AttackP1(90)
        AttackP2(70)
        GroundedHitstunAnimation(AIR_TAILSPIN)
        AirHitstunAnimation(AIR_TAILSPIN)
        AirUntechableTime(40)
        UseSlashHitspark(1)
        AirPushbackX(80000)
        AirPushbackY(30000)
        StrikeProjectileLevel(1)
        ProjectileLevel(0)
        callSubroutine('PNA_CheckWarp')
        Unknown2053(1)
        Unknown23078(1)

        def upon_11():
            XImpulseAcceleration(40)
        ObjectUpon2(3, 3018, 0)
    sprite('su232_01', 5)
    ScreenShake(5000, 0)
    sprite('su232_01', 5)
    ScreenShake(5000, 0)
    sprite('su232_01', 5)
    ScreenShake(5000, 0)
    sprite('su232_01', 5)
    ScreenShake(5000, 0)
    label(0)
    sprite('su232_04', 4)
    physicsXImpulse(50000)
    PrivateSE('slash_beam_slow')
    sprite('su232_05', 4)
    GFX_0('suef_2C', 0)
    ObjectUpon2(2, 12, 0)
    RefreshMultihit()
    XImpulseAcceleration(70)
    sprite('su232_06', 4)
    XImpulseAcceleration(60)
    sprite('su232_07', 4)
    XImpulseAcceleration(60)
    sprite('su232_08', 4)
    XImpulseAcceleration(60)
    sprite('su232_06', 4)
    XImpulseAcceleration(60)
    StartMultihit()
    sprite('su232_07', 4)
    XImpulseAcceleration(0)
    StartMultihit()
    sprite('su232_08', 4)
    StartMultihit()
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')


@State
def PNA_PersonaJB():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, -50000, 180000, 0, 0, 0, 0)
        callSubroutine('PNA_AttackInit')
        EnableCollision(0)
        AttackLevel(3)
        HitOverhead(2)
        UseSlashHitspark(1)
        AttackAttributes('H')
        StrikeProjectileLevel(1)
        ProjectileLevel(0)
        Unknown4007(3)
        Unknown2053(1)
        Unknown23078(1)
        callSubroutine('PNA_CheckWarp')

        def upon_43():
            if SLOT_48 == 302:
                sendToLabel(580)
            if SLOT_48 == 303:
                sendToLabel(580)
    sprite('su254_00', 3)
    sprite('su254_01', 3)
    PrivateSE('slash_beam_fast')
    sprite('su254_03', 7)
    RefreshMultihit()
    GFX_0('suef_Air5C', 0)
    sprite('su254_04', 3)
    sprite('su254_05', 3)
    sprite('su254_06', 3)
    sprite('su254_07', 3)
    label(580)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')


@State
def PNA_PersonaJC():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, 100000, 0, 0, 2000000, -300000, 500000)
        callSubroutine('PNA_AttackInit')
        AttackLevel(4)
        AttackP2(75)
        AirPushbackX(23000)
        AirPushbackY(15000)
        AirUntechableTime(30)
        AirHitstunAnimation(AIR_FACE_UP_SKIP)
        GroundedHitstunAnimation(AIR_FACE_UP_SKIP)
        Hitstop(6)
        PushbackX(29000)
        AttackAttributes('H')
        Unknown2053(1)
        EnableCollision(0)
        Unknown23078(1)
        callSubroutine('PNA_CheckWarp')
        Unknown23059(1)
    sprite('su255_00', 8)
    GFX_0('Air5DTossinAura', 0)
    physicsXImpulse(3000)
    StartMultihit()
    sprite('su255_01', 2)
    ObjectUpon2(2, 12, 0)
    RefreshMultihit()
    ProjectileLevel(1)
    StrikeProjectileLevel(0)
    Unknown4007(0)
    physicsXImpulse(49700)
    PrivateSE('slash_pole_slow')
    sprite('su255_02', 2)
    XImpulseAcceleration(80)
    sprite('su255_03', 2)
    XImpulseAcceleration(80)
    sprite('su255_04', 2)
    XImpulseAcceleration(80)
    sprite('su255_05', 2)
    XImpulseAcceleration(80)
    sprite('su255_00', 2)
    XImpulseAcceleration(30)
    sprite('su255_01', 2)
    DisableAttackRestOfMove()
    sprite('su255_02', 2)
    sprite('su255_03', 2)
    sprite('su255_06', 4)
    XImpulseAcceleration(50)
    sprite('su255_07', 4)
    sprite('su255_08', 4)
    XImpulseAcceleration(50)
    sprite('su255_09', 4)
    PrivateSE('cloth_l')
    sprite('su255_07', 4)
    XImpulseAcceleration(0)
    sprite('su255_08', 4)
    sprite('su255_09', 4)
    PrivateSE('cloth_l')
    sprite('su255_07', 4)
    sprite('su255_08', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')


@State
def PNA_PersonaJ_Test():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, 0, 100000, 0, 0, 100000, 100000)
        callSubroutine('PNA_AttackInit')
        EnableCollision(0)
        AttackLevel(3)
        AirPushbackY(20000)
        HitOverhead(2)
        UseSlashHitspark(1)
        AttackAttributes('H')
        Hitstop(9)
        StrikeProjectileLevel(1)
        ProjectileLevel(0)
        Unknown4007(3)
        Unknown2053(1)
        Unknown23078(1)
        callSubroutine('PNA_CheckWarp')

        def upon_43():
            if SLOT_48 == 302:
                sendToLabel(580)
            if SLOT_48 == 303:
                sendToLabel(580)
    sprite('su205_00', 2)
    physicsXImpulse(5000)
    sprite('su205_01', 1)
    sprite('su205_02', 1)
    sprite('su206_01', 1)
    sprite('su206_02', 2)
    sprite('su206_03', 2)
    GFX_0('suef_5DD', 100)
    physicsXImpulse(0)
    sprite('su206_04', 3)
    RefreshMultihit()
    PrivateSE('slash_beam_middle')
    sprite('su206_06', 4)
    GFX_0('suef_5DDD', 100)
    sprite('su206_07', 3)
    ObjectUpon2(2, 12, 0)
    RefreshMultihit()
    PrivateSE('slash_beam_middle')
    sprite('su206_07', 10)
    StartMultihit()
    XImpulseAcceleration(25)
    sprite('su206_08', 6)
    XImpulseAcceleration(25)
    label(580)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')


@State
def Trap():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, -90000, 70000, 0, 0, 0, 0)
        callSubroutine('PNA_AttackInit')
        BlendMode_Normal()
        Unknown3001(50)
        ConstantAlphaModifier(20)
        Unknown23022(1)
        callSubroutine('PNA_CheckWarp')
    sprite('su400_00', 3)
    sprite('su400_01', 3)
    sprite('su400_02', 3)
    sprite('su400_00', 3)
    sprite('su400_01', 3)
    sprite('su400_02', 3)
    sprite('su400_00', 4)
    sprite('su400_01', 4)
    sprite('su400_02', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')


@State
def PartnerAssistAtk_B():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, 220000, 20000, 0, 0, 0, 0)
        callSubroutine('PNA_SPAttackInit')
        AttackLevel(4)
        Damage(600)
        AttackP1(70)
        SingleProration(1)
        Hitstop(1)
        PushbackX(12000)
        AirUntechableTime(60)
        AirPushbackX(5000)
        AirPushbackY(40000)
        GroundedHitstunAnimation(AIR_FACE_UP)
        AirHitstunAnimation(AIR_FACE_UP)
        UseSlashHitspark(1)
        CounterHitSetting(1)
        ChipPercentage(5)
        BlendMode_Normal()
        Unknown3001(50)
        ConstantAlphaModifier(20)
        Unknown11057(500)
        Unknown2053(1)
        EnableCollision(1)
        SetXCollisionFromOrigin(50)
        callSubroutine('PNA_CheckWarp')
        AttackAttributes('B')
        Unknown23059(1)
    sprite('su410_03', 1)
    StartMultihit()
    physicsXImpulse(0)
    GFX_0('suef_410', 103)
    GFX_0('suef_410_add', 103)
    GFX_0('suef_410_zapper', 103)
    sprite('su410_03', 3)
    RefreshMultihit()
    physicsYImpulse(3000)
    physicsXImpulse(2000)
    sprite('su410_04', 3)
    YAccel(200)
    XImpulseAcceleration(200)
    RefreshMultihit()
    sprite('su410_05', 3)
    YAccel(200)
    XImpulseAcceleration(200)
    RefreshMultihit()
    sprite('su410_04', 3)
    YAccel(200)
    XImpulseAcceleration(200)
    RefreshMultihit()
    sprite('su410_05', 3)
    YAccel(200)
    XImpulseAcceleration(200)
    RefreshMultihit()
    sprite('su410_04', 2)
    YAccel(80)
    XImpulseAcceleration(50)
    RefreshMultihit()
    sprite('su410_06', 2)
    EnableCollision(0)
    YAccel(0)
    XImpulseAcceleration(0)
    setInvincible(0)
    sprite('su410_07', 3)
    Unknown26('suef_410_zapper')
    sprite('su410_08', 5)
    sprite('su410_07', 5)
    sprite('su410_08', 5)
    sprite('su410_07', 5)
    sprite('su410_08', 5)
    sprite('su410_07', 5)
    sprite('su410_08', 5)
    sprite('su410_07', 5)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')
    Unknown26('suef_410')
    Unknown26('suef_410_add')


@State
def PAssault2_RA():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, -100000, 150000, 0, 0, 0, 0)
        callSubroutine('PNA_AttackInit')
        Unknown23022(1)
        EnableCollision(0)
        Unknown4007(3)
        callSubroutine('PNA_CheckWarp')
    sprite('su400_00', 3)
    sprite('su400_01', 3)
    sprite('su400_02', 3)
    sprite('su400_00', 3)
    sprite('su400_01', 3)
    sprite('su400_02', 3)
    sprite('su400_00', 4)
    sprite('su400_01', 4)
    sprite('su400_02', 4)
    sprite('su400_00', 5)
    sprite('su400_01', 5)
    sprite('su400_02', 5)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')


@State
def PBC_PersonaUltimateHAMAON():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23023()
        Unknown23184(3, 100, -50000, 100000, 0, 0, 0, 0)
        callSubroutine('PNA_AttackInit')
        Hitstop(0)
        Unknown2053(1)
        Unknown23022(1)
        callSubroutine('PNA_CheckWarp')
    sprite('su432_00', 4)
    ForceFaceSprite()
    sprite('su432_01', 10)
    sprite('su432_02', 4)
    sprite('su432_03', 4)
    GFX_0('Hamaon_search', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AbsoluteY(0)
        AddX(100000)
    Unknown2054(0)
    sprite('su432_04', 4)
    sprite('su432_05', 4)
    PrivateSE('cloth_l')
    sprite('su432_03', 4)
    sprite('su432_04', 4)
    sprite('su432_05', 4)
    PrivateSE('cloth_l')
    sprite('su432_03', 4)
    sprite('su432_04', 4)
    sprite('su432_05', 4)
    PrivateSE('cloth_l')
    sprite('su432_03', 4)
    sprite('su432_04', 4)
    sprite('su432_05', 4)
    PrivateSE('cloth_l')
    sprite('su432_03', 4)
    sprite('su432_04', 4)
    sprite('su432_05', 4)
    PrivateSE('cloth_l')
    sprite('su432_03', 4)
    sprite('su432_04', 4)
    sprite('su432_05', 4)
    PrivateSE('cloth_l')
    sprite('su432_03', 4)
    sprite('su432_04', 4)
    sprite('su432_05', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')


@State
def PBC_PersonaUltimateODHAMAON():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23023()
        Unknown23184(3, 100, -50000, 100000, 0, 0, 0, 0)
        callSubroutine('PNA_AttackInit')
        Unknown23056()
        Hitstop(0)
        Unknown2053(1)
        Unknown23022(1)
        callSubroutine('PNA_CheckWarp')
    sprite('su432_00', 4)
    ForceFaceSprite()
    sprite('su432_01', 10)
    sprite('su432_02', 4)
    sprite('su432_03', 4)
    GFX_0('Hamaon_search', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AbsoluteY(0)
        AddX(100000)
    Unknown2054(0)
    sprite('su432_04', 4)
    sprite('su432_05', 4)
    PrivateSE('cloth_l')
    sprite('su432_03', 4)
    sprite('su432_04', 4)
    sprite('su432_05', 4)
    PrivateSE('cloth_l')
    sprite('su432_03', 4)
    sprite('su432_04', 4)
    sprite('su432_05', 4)
    PrivateSE('cloth_l')
    sprite('su432_03', 4)
    sprite('su432_04', 4)
    sprite('su432_05', 4)
    PrivateSE('cloth_l')
    sprite('su432_03', 4)
    sprite('su432_04', 4)
    sprite('su432_05', 4)
    PrivateSE('cloth_l')
    sprite('su432_03', 4)
    sprite('su432_04', 4)
    sprite('su432_05', 4)
    PrivateSE('cloth_l')
    sprite('su432_03', 4)
    sprite('su432_04', 4)
    sprite('su432_05', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')


@State
def PartnerAssistAtk_D():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, 0, 100000, -10000000, 10000000, -10000000, 
            10000000)
        callSubroutine('PNA_SPAttackInit')
        AttackLevel(4)
        Damage(1200)
        AttackP1(70)
        SingleProration(1)
        AirUntechableTime(40)
        AirPushbackX(15000)
        AirPushbackY(3000)
        UseSlashHitspark(1)
        Hitstop(7)
        CounterHitSetting(1)
        ChipPercentage(5)
        physicsXImpulse(30000)
        callSubroutine('PNA_CheckWarp')
        Unknown2053(1)
        AttackAttributes('B')
        Unknown23059(1)
    sprite('su205_00', 2)
    SetInertia(40000)
    sprite('su205_01', 1)
    sprite('su205_02', 1)
    sprite('su206_01', 1)
    sprite('su206_02', 2)
    sprite('su206_03', 2)
    GFX_0('suef_5DD', 100)
    sprite('su206_04', 2)
    EndMomentum(1)
    RefreshMultihit()
    PrivateSE('slash_beam_middle')
    sprite('su206_06', 2)
    physicsXImpulse(20000)
    XImpulseAcceleration(140)
    GFX_0('suef_5DDD', 100)
    sprite('su206_07', 6)

    def upon_78():
        clearUponHandler(upon_78)
        SLOT_10 = 1
    RefreshMultihit()
    AirHitstunAnimation(AIR_FACE_UP_SKIP)
    GroundedHitstunAnimation(AIR_FACE_UP_SKIP)
    AirPushbackY(20000)
    PrivateSE('slash_beam_middle')
    sprite('su206_07', 10)
    StartMultihit()
    XImpulseAcceleration(25)
    sprite('su206_08', 20)
    XImpulseAcceleration(25)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')


@State
def PBC_PersonaUltimateMUDOON():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, -100000, 105000, 0, 2000000, -1000000, 1000000)
        callSubroutine('PNA_AttackInit')
        Unknown23056()
        EnableCollision(0)
        Unknown2053(1)
        Unknown23022(1)
        callSubroutine('PNA_CheckWarp')
    sprite('su432_00', 3)
    sprite('su432_01', 3)
    sprite('su432_06', 4)
    GFX_0('Mudoon_search', 100)
    sprite('su432_07', 4)
    GFX_0('Mudoon', 100)
    sprite('su432_08', 4)
    sprite('su432_09', 4)
    PrivateSE('cloth_l')
    sprite('su432_07', 4)
    sprite('su432_08', 4)
    sprite('su432_09', 4)
    PrivateSE('cloth_l')
    sprite('su432_07', 4)
    sprite('su432_08', 4)
    sprite('su432_09', 4)
    PrivateSE('cloth_l')
    sprite('su432_07', 4)
    sprite('su432_08', 4)
    sprite('su432_09', 4)
    PrivateSE('cloth_l')
    sprite('su432_07', 4)
    sprite('su432_08', 4)
    sprite('su432_09', 4)
    PrivateSE('cloth_l')
    sprite('su432_07', 4)
    sprite('su432_08', 4)
    sprite('su432_09', 4)
    PrivateSE('cloth_l')
    sprite('su432_07', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')


@State
def PNA_PersonaIchigeki():

    def upon_IMMEDIATE():
        Unknown23023()
        callSubroutine('PersonaReset')
        BlendMode_Normal()
        AttackDefaults_AstralHeatProjectile()
        Unknown23022(1)
        Unknown23184(3, 100, -150000, 200000, 0, 0, 0, 0)
        callSubroutine('PNA_CheckWarp')
        TeleportToObject(22)
        AbsoluteY(120000)
        Unknown4009(3)
        Unknown23066(1)
        Unknown2053(0)
        SLOT_53 = 0

        def upon_43():
            if SLOT_48 == 9512:
                SLOT_53 = SLOT_53 + 1
                if SLOT_53 == 3:
                    clearUponHandler(upon_43)
                    sendToLabel(10)
            if SLOT_48 == 9511:
                sendToLabel(0)

        def upon_44():
            sendToLabel(0)
    sprite('su450_00', 8)
    sprite('su450_01', 4)
    GFX_0('ZanzohCircle', 100)
    CommonSE('magiccircle_b')
    sprite('su450_02', 4)
    sprite('su450_03', 4)
    sprite('su450_04', 4)
    sprite('su450_05', 4)
    sprite('su450_06', 4)
    GFX_0('Ichigeki_Marker', 0)
    CommonSE('magiccircle_b')
    sprite('su450_07', 4)
    sprite('su450_08', 4)
    sprite('su450_06', 4)
    sprite('su450_07', 4)
    sprite('su450_08', 4)
    sprite('su450_06', 4)
    sprite('su450_07', 4)
    sprite('su450_08', 4)
    sprite('su450_06', 4)
    ConstantAlphaModifier(-16)
    sprite('su450_07', 4)
    sprite('su450_08', 4)
    sprite('su450_06', 4)
    spriteEnd()
    sprite('null', 16)
    GFX_0('Ichigeki_Marker', 103)
    SLOT_0 = 3
    CopyFromRightToLeft(1, SLOT_51, 25, SLOT_0)

    def RunOnObject_1():
        SetPosXByScreenPer(90)
        AbsoluteY(550000)
    CommonSE('magiccircle_b')
    sprite('null', 1)
    GFX_0('Ichigeki_Marker', 103)
    SLOT_0 = 2
    CopyFromRightToLeft(1, SLOT_51, 25, SLOT_0)

    def RunOnObject_1():
        SetPosXByScreenPer(10)
        AbsoluteY(250000)
    CommonSE('magiccircle_b')
    sprite('null', 32767)
    label(10)
    sprite('null', 1)
    Unknown21015('AstralHeat', 9502, 0)
    Unknown21015('Ichigeki_Marker', 9532, 0)
    label(0)
    sprite('keep', 32767)
    enterState('PNA_PersonaWait')


@State
def destinyzero_damy():

    def upon_IMMEDIATE():
        Unknown23067('suef_destinyzero_09')
        TeleportToObject(22)
        AddY(230000)
        FaceLeft()
    sprite('null', 60)


@State
def destinyzero_main():

    def upon_IMMEDIATE():
        Unknown23067('suef_destinyzero_09')
        TeleportToObject(22)
        AddY(230000)
        FaceLeft()
    sprite('null', 60)


@State
def destinyzero_sub():

    def upon_IMMEDIATE():
        Unknown23067('suef_destinyzero_09')
        TeleportToObject(23)
        AddY(230000)
        FaceLeft()
    sprite('null', 60)


@State
def destinyzero_Cutin_main1_3Naoto():

    def upon_IMMEDIATE():
        FaceLeft()
        ScreenPosition(1)
        SetZVal(500)
        XPositionRelativeFacing(-640000)
        AbsoluteY(-640000)
        AddX(676500)
        AddY(353000)
        Size(720)
        Unknown3001(125)
    sprite('vr_pna_cutin', 3)
    ConstantAlphaModifier(43)
    physicsXImpulse(-40000)
    SetAcceleration(3000)
    sprite('vr_pna_cutin', 5)
    sprite('vr_pna_cutin', 25)
    physicsXImpulse(-1000)
    SetAcceleration(0)
    sprite('vr_pna_cutin', 4)
    ConstantAlphaModifier(-25)
    physicsXImpulse(-20000)
    sprite('vr_pna_cutin', 22)
    ConstantAlphaModifier(-255)


@State
def destinyzero_Cutin_main1_3dokuro():

    def upon_IMMEDIATE():
        FaceLeft()
        ScreenPosition(1)
        SetZVal(1000)
        XPositionRelativeFacing(-640000)
        AbsoluteY(-640000)
        AddX(676500)
        AddY(370000)
        Size(720)
        Unknown3001(0)
    sprite('vr_pna_cutin_skull', 8)
    ConstantAlphaModifier(31)
    physicsXImpulse(-40000)
    SetAcceleration(3000)
    sprite('vr_pna_cutin_skull', 25)
    physicsXImpulse(-1000)
    SetAcceleration(0)
    sprite('vr_pna_cutin_skull', 27)
    ConstantAlphaModifier(-51)
    physicsXImpulse(-20000)


@State
def destinyzero_Cutin_sub1_3Naoto():

    def upon_IMMEDIATE():
        FaceLeft()
        ScreenPosition(1)
        SetZVal(500)
        XPositionRelativeFacing(-640000)
        AbsoluteY(-640000)
        AddX(676500)
        AddY(353000)
        Size(720)
        Unknown3001(125)
    sprite('vr_pna_cutin', 3)
    ConstantAlphaModifier(43)
    physicsXImpulse(-40000)
    SetAcceleration(3000)
    sprite('vr_pna_cutin', 5)
    sprite('vr_pna_cutin', 25)
    physicsXImpulse(-1000)
    SetAcceleration(0)
    sprite('vr_pna_cutin', 4)
    ConstantAlphaModifier(-25)
    physicsXImpulse(-20000)
    sprite('vr_pna_cutin', 22)
    ConstantAlphaModifier(-255)


@State
def destinyzero_Cutin_sub1_3dokuro():

    def upon_IMMEDIATE():
        FaceLeft()
        ScreenPosition(1)
        SetZVal(1000)
        XPositionRelativeFacing(-640000)
        AbsoluteY(-640000)
        AddX(676500)
        AddY(370000)
        Size(720)
        Unknown3001(0)
    sprite('vr_pna_cutin_skull', 8)
    ConstantAlphaModifier(31)
    physicsXImpulse(-40000)
    SetAcceleration(3000)
    sprite('vr_pna_cutin_skull', 25)
    physicsXImpulse(-1000)
    SetAcceleration(0)
    sprite('vr_pna_cutin_skull', 27)
    ConstantAlphaModifier(-51)
    physicsXImpulse(-20000)


@State
def destinyzero_Cutin_main2_4Naoto():

    def upon_IMMEDIATE():
        FaceRight()
        ScreenPosition(1)
        SetZVal(500)
        XPositionRelativeFacing(640000)
        AbsoluteY(-640000)
        AddX(676500)
        AddY(353000)
        Size(720)
        Unknown3001(125)
    sprite('vr_pna_cutin', 3)
    ConstantAlphaModifier(43)
    physicsXImpulse(-40000)
    SetAcceleration(3000)
    sprite('vr_pna_cutin', 5)
    sprite('vr_pna_cutin', 25)
    physicsXImpulse(-1000)
    SetAcceleration(0)
    sprite('vr_pna_cutin', 4)
    ConstantAlphaModifier(-25)
    physicsXImpulse(-20000)
    sprite('vr_pna_cutin', 22)
    ConstantAlphaModifier(-255)


@State
def destinyzero_Cutin_main2_4dokuro():

    def upon_IMMEDIATE():
        FaceLeft()
        ScreenPosition(1)
        SetZVal(1000)
        XPositionRelativeFacing(-640000)
        AbsoluteY(-640000)
        AddX(-676500)
        AddY(370000)
        Size(720)
        Unknown3001(0)
    sprite('vr_pna_cutin_skull', 8)
    ConstantAlphaModifier(31)
    physicsXImpulse(40000)
    SetAcceleration(-3000)
    sprite('vr_pna_cutin_skull', 25)
    physicsXImpulse(1000)
    SetAcceleration(0)
    sprite('vr_pna_cutin_skull', 27)
    ConstantAlphaModifier(-51)
    physicsXImpulse(20000)


@State
def destinyzero_Cutin_sub2_4Naoto():

    def upon_IMMEDIATE():
        FaceRight()
        ScreenPosition(1)
        SetZVal(500)
        XPositionRelativeFacing(640000)
        AbsoluteY(-640000)
        AddX(676500)
        AddY(353000)
        Size(720)
        Unknown3001(125)
    sprite('vr_pna_cutin', 3)
    ConstantAlphaModifier(43)
    physicsXImpulse(-40000)
    SetAcceleration(3000)
    sprite('vr_pna_cutin', 5)
    sprite('vr_pna_cutin', 25)
    physicsXImpulse(-1000)
    SetAcceleration(0)
    sprite('vr_pna_cutin', 4)
    ConstantAlphaModifier(-25)
    physicsXImpulse(-20000)
    sprite('vr_pna_cutin', 22)
    ConstantAlphaModifier(-255)


@State
def destinyzero_Cutin_sub2_4dokuro():

    def upon_IMMEDIATE():
        FaceLeft()
        ScreenPosition(1)
        SetZVal(1000)
        XPositionRelativeFacing(-640000)
        AbsoluteY(-640000)
        AddX(-676500)
        AddY(370000)
        Size(720)
        Unknown3001(0)
    sprite('vr_pna_cutin_skull', 8)
    ConstantAlphaModifier(31)
    physicsXImpulse(40000)
    SetAcceleration(-3000)
    sprite('vr_pna_cutin_skull', 25)
    physicsXImpulse(1000)
    SetAcceleration(0)
    sprite('vr_pna_cutin_skull', 27)
    ConstantAlphaModifier(-51)
    physicsXImpulse(20000)


@State
def DanganD_CCA():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel(3)
        Damage(1800)
        GroundedHitstunAnimation(AIR_FACE_UP)
        AirPushbackX(30000)
        AirPushbackY(35000)
        YImpulseBeforeWallbounce(3000)
        AirUntechableTime(40)
        StrikeProjectileLevel(1)
        ProjectileLevel(1)
        MinimumDamage(0)
        BlendMode_Add()
        Unknown2054(1)
        IgnoreBurst(1)
        Unknown30088(1)
    sprite('vr_impact2_Ex', 2)
    GFX_0('BarrierBrake', 100)
    RefreshMultihit()
    PrivateSE('ice_break_fast')
    sprite('vr_impact2_Ex', 20)
    ObjectUpon2(3, 3020, 0)
    EndAttack()


@State
def DanganD():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel(3)
        Damage(1800)
        GroundedHitstunAnimation(AIR_FACE_UP)
        AirPushbackX(30000)
        AirPushbackY(35000)
        YImpulseBeforeWallbounce(3000)
        AirUntechableTime(40)
        StrikeProjectileLevel(1)
        ProjectileLevel(1)
        MinimumDamage(0)
        BlendMode_Add()
        Unknown2054(1)
    sprite('vr_impact2_Ex', 2)
    GFX_0('BarrierBrake', 100)
    RefreshMultihit()
    PrivateSE('ice_break_fast')
    sprite('vr_impact2_Ex', 20)
    ObjectUpon2(3, 3020, 0)
    EndAttack()


@State
def DanganD_Ex():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel(3)
        Damage(1500)
        AttackP1(70)
        GroundedHitstunAnimation(AIR_BLOWBACK)
        AirHitstunAnimation(AIR_BLOWBACK)
        Wallbounce(1)
        WallbounceReboundTime(0)
        AirHitstunAfterWallbounce(40)
        AirPushbackX(60000)
        AirPushbackY(25000)
        AirUntechableTime(50)
        CounterHitSetting(1)
        BlendMode_Add()
        Unknown2054(1)
        StrikeProjectileLevel(1)
        ProjectileLevel(1)
    sprite('vr_impact2_Ex', 2)
    GFX_0('BarrierBrake', 100)
    RefreshMultihit()
    PrivateSE('ice_break_fast')
    sprite('vr_impact2_Ex', 20)
    ObjectUpon2(3, 3020, 0)
    EndAttack()


@State
def DanganDASS():

    def upon_IMMEDIATE():
        BlendMode_Add()
        Unknown2054(1)
    sprite('vr_impact2', 2)
    GFX_0('BarrierBrake', 100)
    RefreshMultihit()
    PrivateSE('ice_break_fast')
    sprite('vr_impact2', 20)
    EndAttack()


@State
def BarrierBrake():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Unknown4015()
        Unknown3001(150)
    sprite('null', 10)
    GFX_1('suef_sheldbrakeb_08', 100)
    Unknown1099(50)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def suef_5C():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        BlendMode_Add()
        PaletteIndex(1)
        Unknown3001(255)
        ConstantAlphaModifier(-25)
    sprite('vr_su204_00', 3)
    sprite('vr_su204_01', 16)


@State
def suef_5DD():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        BlendMode_Add()
        PaletteIndex(1)
        Unknown3001(255)
        ConstantAlphaModifier(-25)
    sprite('vr_su206_00', 2)
    sprite('vr_su206_01', 2)


@State
def suef_5DDD():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        BlendMode_Add()
        PaletteIndex(1)
        Unknown3001(255)
        ConstantAlphaModifier(-25)
    sprite('vr_su206_10', 2)
    sprite('vr_su206_11', 3)


@State
def suef_5DDDD():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        BlendMode_Add()
        PaletteIndex(1)
        Unknown3001(255)
        ConstantAlphaModifier(-25)
    sprite('vr_su206_20', 3)
    sprite('vr_su206_21', 3)
    sprite('vr_su206_22', 16)


@State
def suef_2C():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Unknown4003('suef_232tukisub.DIG', '')
        Unknown4015()
        Unknown4009(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
    sprite('null', 20)
    Unknown23067('suef_bannotuki_07')
    sprite('null', 15)
    ConstantAlphaModifier(-17)


@State
def suef_Air5C():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown2054(1)
    sprite('null', 60)
    PaletteIndex(1)
    Unknown4047(55, 55, 55)
    Unknown23067('suef_air5c')


@State
def Air5DTossinAura():

    def upon_IMMEDIATE():
        Unknown23015(2)
        BlendMode_Normal()
        Unknown23067('suef_tossin_04')
        Unknown4003('suef_121tossinsub.DIG', '')
        Unknown4015()
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 30)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def GunKira():

    def upon_IMMEDIATE():
        GFX_2('naef_gunkira')
        Unknown4010(2)
        Unknown4007(2)
    sprite('null', 6)
    sprite('null', 60)
    EndMomentum(1)


@State
def Yakkyo():

    def upon_IMMEDIATE():

        def upon_5():
            YAccel(-60)
            XImpulseAcceleration(60)

        def upon_LANDING():
            PrivateSE('na006')
        PaletteIndex(2)
    sprite('vr_trap_yakkyo', 50)
    RandSpeedX(-7500, -12500)
    RandSpeedY(2500, 3250)
    Unknown1078(-80000, -100000)
    setGravity(2000)
    sprite('vr_trap_yakkyo', 20)
    BlendMode_Normal()
    ConstantAlphaModifier(-20)


@State
def Jumpsmoke():

    def upon_IMMEDIATE():
        Unknown23067('naef_kicksmoke_04')
    sprite('null', 30)


@State
def Tossin_atk1():

    def upon_IMMEDIATE():
        Unknown23067('naef_407circleA')
        Unknown4007(2)
        Unknown23015(1)
        Unknown4010(2)
    sprite('null', 3)
    Unknown1099(40)
    sprite('null', 7)
    ConstantAlphaModifier(-40)


@State
def Tossin_atk2():

    def upon_IMMEDIATE():
        Unknown4003('naef_402tossin_01.DIG', '')
        Unknown4015()
        Unknown4007(2)
        Unknown4009(2)
        BlendMode_Normal()
        Unknown3001(180)
        Unknown4010(2)
    sprite('null', 14)


@State
def Dangan():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel(3)
        AttackP1(80)
        AttackP2(90)
        Hitstop(5)
        PushbackX(15000)
        Unknown14083(0)
        Unknown23026(80000)
        EnableAfterimage(1)
        physicsXImpulse(120000)
        PaletteIndex(2)
        SLOT_51 = 12

        def upon_EVERY_FRAME():
            SLOT_51 = SLOT_51 + -1

            def upon_10():
                clearUponHandler(upon_10)
                clearUponHandler(upon_EVERY_FRAME)
                DeleteObject(25)
                Unknown21015('ShagekiA', 3016, 0)
                Unknown21015('ShagekiB', 3016, 0)
                Unknown21015('ShagekiC', 3016, 0)

        def upon_43():
            if SLOT_48 == 3010:
                Unknown1072(0)
                Unknown4055(0)
                Unknown4045('naef_401gunfire', 0)
                Unknown1110(120000, 0)
                Damage(600)
                CopyFromRightToLeft(25, SLOT_0, 3, SLOT_62)
                if SLOT_0:
                    MinimumDamage(10)
                    Unknown30065(0)
            if SLOT_48 == 3011:
                Unknown1072(-20000)
                Unknown4055(0)
                Unknown4045('naef_401gunfire', 0)
                Unknown1110(120000, 0)
                AirHitstunAnimation(AIR_VERTICAL)
                GroundedHitstunAnimation(AIR_VERTICAL)
                Damage(700)
                CopyFromRightToLeft(25, SLOT_0, 3, SLOT_62)
                if SLOT_0:
                    MinimumDamage(10)
                    Unknown30065(0)
                sendToLabel(1)
            if SLOT_48 == 3019:
                Unknown1072(60000)
                Unknown4055(0)
                Unknown4045('naef_401gunfire', 0)
                Unknown1110(120000, 0)
                AirHitstunAnimation(AIR_FACE_DOWN)
                GroundedHitstunAnimation(AIR_FACE_DOWN)
                Damage(500)
                CopyFromRightToLeft(25, SLOT_0, 3, SLOT_62)
                if SLOT_0:
                    MinimumDamage(10)
                    Unknown30065(0)
                sendToLabel(2)

                def upon_5():
                    YAccel(-100)
                    Unknown1108(0)
                    GFX_1('naef_tyakudan', 100)
        Unknown23067('naef_401dando')
    label(0)
    sprite('vr_dangan_a_front', 2)
    sprite('vr_dangan_a_front', 298)
    spriteEnd()
    ExitState()
    label(1)
    sprite('vr_dangan_a_front', 1)
    spriteEnd()
    gotoLabel(9)
    label(2)
    sprite('vr_dangan_a_front', 1)
    label(9)
    sprite('vr_dangan_a', 298)


@State
def Dangan_PS():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel(3)
        AttackP1(70)
        AttackP2(90)
        Hitstop(5)
        PushbackX(15000)
        Unknown14083(0)
        Unknown23026(80000)
        CounterHitSetting(1)
        EnableAfterimage(1)
        physicsXImpulse(120000)
        PaletteIndex(2)

        def upon_EVERY_FRAME():

            def upon_10():
                clearUponHandler(upon_10)
                clearUponHandler(upon_EVERY_FRAME)
                DeleteObject(25)

        def upon_43():
            if SLOT_48 == 3010:
                Unknown1072(0)
                Unknown4055(0)
                Unknown4045('naef_401gunfire', 0)
                Unknown1110(120000, 0)
                Damage(600)
                CopyFromRightToLeft(25, SLOT_0, 3, SLOT_62)
                if SLOT_0:
                    MinimumDamage(10)
                    Unknown30065(0)
            if SLOT_48 == 3011:
                Unknown1072(-20000)
                Unknown4055(0)
                Unknown4045('naef_401gunfire', 0)
                Unknown1110(120000, 0)
                AirHitstunAnimation(AIR_VERTICAL)
                GroundedHitstunAnimation(AIR_VERTICAL)
                Damage(700)
                CopyFromRightToLeft(25, SLOT_0, 3, SLOT_62)
                if SLOT_0:
                    MinimumDamage(10)
                    Unknown30065(0)
                sendToLabel(1)
            if SLOT_48 == 3019:
                Unknown1072(60000)
                Unknown4055(0)
                Unknown4045('naef_401gunfire', 0)
                Unknown1110(120000, 0)
                AirHitstunAnimation(AIR_FACE_DOWN)
                GroundedHitstunAnimation(AIR_FACE_DOWN)
                Damage(500)
                CopyFromRightToLeft(25, SLOT_0, 3, SLOT_62)
                if SLOT_0:
                    MinimumDamage(10)
                    Unknown30065(0)
                sendToLabel(2)

                def upon_5():
                    YAccel(-100)
                    Unknown1108(0)
                    GFX_1('naef_tyakudan', 100)
        Unknown23067('naef_401dando')
    label(0)
    sprite('vr_dangan_a_front', 2)
    sprite('vr_dangan_a_front', 298)
    spriteEnd()
    ExitState()
    label(1)
    sprite('vr_dangan_a_front', 1)
    spriteEnd()
    gotoLabel(9)
    label(2)
    sprite('vr_dangan_a_front', 1)
    label(9)
    sprite('vr_dangan_a', 298)


@State
def DanganLastA_PS():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel(5)
        Damage(1800)
        AttackP1(70)
        ChipPercentage(20)
        CounterHitSetting(1)
        AirUntechableTime(50)
        Hitstop(0)
        AirPushbackX(60000)
        AirPushbackY(10000)
        YImpulseBeforeWallbounce(1000)
        AirHitstunAnimation(AIR_BLOWBACK)
        GroundedHitstunAnimation(AIR_BLOWBACK)
        WallbounceReboundTime(0)

        def upon_10():
            DeleteObject(25)
        PushbackX(30000)
        EnemyHitstopAddition(8, 0, 0)
        EnableAfterimage(1)
        physicsXImpulse(120000)
        PaletteIndex(2)
        Unknown1072(0)
        Unknown4055(0)
        Unknown4045('naef_401gunfirelast', 0)
        Unknown1110(120000, 0)
        Unknown23067('naef_401dando')
    sprite('vr_dangan_a_front', 2)
    RefreshMultihit()
    sprite('vr_dangan_a_front', 300)
    PushbackX(12000)
    EnemyHitstopAddition(0, 0, 0)


@State
def DanganLastA():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel(5)
        Damage(1800)
        AttackP1(80)
        AirUntechableTime(50)
        Hitstop(0)
        AirPushbackX(60000)
        AirPushbackY(10000)
        YImpulseBeforeWallbounce(1000)
        AirHitstunAnimation(AIR_BLOWBACK)
        GroundedHitstunAnimation(AIR_BLOWBACK)
        WallbounceReboundTime(0)
        CopyFromRightToLeft(25, SLOT_0, 3, SLOT_62)
        if SLOT_0:
            MinimumDamage(10)
            Unknown30065(0)
        PushbackX(30000)
        EnemyHitstopAddition(8, 0, 0)
        EnableAfterimage(1)
        physicsXImpulse(120000)
        PaletteIndex(2)
        Unknown1072(0)
        Unknown4055(0)
        Unknown4045('naef_401gunfirelast', 0)
        Unknown1110(120000, 0)

        def upon_10():
            Unknown21015('ShagekiA', 4001, 0)
            DeleteObject(25)
        Unknown23067('naef_401dando')
    sprite('vr_dangan_a_front', 2)
    RefreshMultihit()
    sprite('vr_dangan_a_front', 300)
    PushbackX(12000)
    EnemyHitstopAddition(0, 0, 0)


@State
def DanganLastB():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel(5)
        Damage(2100)
        AttackP1(80)
        AirUntechableTime(50)
        Hitstop(0)
        AirPushbackY(40000)
        AirPushbackX(24000)
        AirHitstunAnimation(AIR_TAILSPIN)
        GroundedHitstunAnimation(AIR_TAILSPIN)
        CopyFromRightToLeft(25, SLOT_0, 3, SLOT_62)
        if SLOT_0:
            MinimumDamage(10)
            Unknown30065(0)
        PushbackX(30000)
        EnemyHitstopAddition(8, 0, 0)
        EnableAfterimage(1)
        physicsXImpulse(120000)
        PaletteIndex(2)
        Unknown1072(-20000)
        Unknown4055(0)
        Unknown4045('naef_401gunfirelast', 0)
        Unknown1110(120000, 0)

        def upon_10():
            DeleteObject(25)
            Unknown21015('ShagekiB', 4001, 0)
        Unknown23067('naef_401dando')
    sprite('vr_dangan_a_front', 2)
    RefreshMultihit()
    sprite('vr_dangan_a', 298)
    PushbackX(12000)
    EnemyHitstopAddition(0, 0, 0)


@State
def DanganLastC():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel(5)
        Damage(1500)
        AttackP1(80)
        AirUntechableTime(50)
        Hitstop(0)
        AirPushbackX(1000)
        AirPushbackY(34000)
        AirHitstunAnimation(AIR_VERTICAL)
        GroundedHitstunAnimation(AIR_VERTICAL)
        Unknown23026(80000)
        CopyFromRightToLeft(25, SLOT_0, 3, SLOT_62)
        if SLOT_0:
            MinimumDamage(10)
            Unknown30065(0)
        PushbackX(30000)
        EnemyHitstopAddition(8, 0, 0)
        EnableAfterimage(1)
        physicsXImpulse(120000)
        PaletteIndex(2)
        Unknown1072(60000)
        Unknown4055(0)
        Unknown4045('naef_401gunfirelast', 0)
        Unknown1110(120000, 0)

        def upon_5():
            YAccel(-100)
            Unknown1108(0)

        def upon_10():
            DeleteObject(25)
            Unknown21015('ShagekiC', 4001, 0)
        Unknown23067('naef_401dando')
    sprite('vr_dangan_a_front', 2)
    RefreshMultihit()
    sprite('vr_dangan_a', 298)
    PushbackX(12000)
    EnemyHitstopAddition(0, 0, 0)


@State
def Tossin_atk2AB():

    def upon_IMMEDIATE():
        Unknown4003('naef_402tossin_01.DIG', '')
        Unknown4015()
        Unknown4007(2)
        Unknown4009(2)
        BlendMode_Normal()
        Unknown3001(180)
        Unknown4010(2)
    sprite('null', 14)


@Subroutine
def ShotDelete_dmy():
    Unknown4011(2)
    Unknown4010(2)
    Unknown4007(2)
    Unknown4009(2)
    GuardPoint_(1)
    setInvincible(1)
    SpecificInvincibility('P')
    Unknown22031(0, 0)
    Unknown22032(1)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if not SLOT_30:

            def upon_42():
                if SLOT_2:
                    ObjectUpon2(2, 3021, 0)
                    AddActionMark(-1)


@State
def vr_trap_aircore_damy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('vr_trap_aircore_damy', 32767)


@State
def vr_trap_landcore_damy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('vr_trap_landcore_damy', 32767)


@State
def TrapMatome():

    def upon_IMMEDIATE():
        Visibility(1)
        Unknown23089(1, 0, 0, 0, 0, 0, 1, 0)
        Unknown23091(1)
        AddX(40000)
        if SLOT_8:
            Unknown23022(1)

            def upon_43():
                if SLOT_48 == 3002:
                    Unknown23090(25)
                if SLOT_48 == 3004:
                    SLOT_55 = 1
                if SLOT_48 == 3021:
                    Unknown23090(25)

            def upon_EVERY_FRAME():
                if SLOT_29 < 400000:
                    Unknown3001(255)
                    if not SLOT_2:
                        SetActionMark(1)
                        GFX_1('naef_trapdetection_a', 103)
                    Unknown23022(0)
                if SLOT_29 < 210000:
                    sendToLabel(14)
                    clearUponHandler(upon_EVERY_FRAME)
                if SLOT_165 < 210000:
                    sendToLabel(14)
                    clearUponHandler(upon_EVERY_FRAME)
                CopyFromRightToLeft(25, SLOT_0, 2, SLOT_158)
                if not SLOT_0:
                    Unknown26('TrapMatome')
                    Unknown26('vr_trap_aircore_damy')
                    Unknown26('vr_trap_landcore_damy')
            uponSendToLabel(upon_54, 580)
        else:

            def upon_LANDING():
                sendToLabel(3)

            def upon_43():
                if SLOT_48 == 3003:
                    Unknown23090(25)
                if SLOT_48 == 3004:
                    SLOT_56 = 1
                if SLOT_48 == 3021:
                    Unknown23090(25)

            def upon_EVERY_FRAME():
                if SLOT_54:
                    CopyFromRightToLeft(25, SLOT_0, 22, SLOT_37)
                    if SLOT_0:
                        if SLOT_29 < 400000:
                            Unknown23022(0)
                            Unknown3001(255)
                            if not SLOT_2:
                                SetActionMark(1)
                                GFX_1('naef_trapdetection_a', 103)
                        if SLOT_19 < 210000:
                            sendToLabel(141)
                            clearUponHandler(upon_EVERY_FRAME)
                        if SLOT_166 < 210000:
                            sendToLabel(141)
                            clearUponHandler(upon_EVERY_FRAME)
                CopyFromRightToLeft(25, SLOT_0, 2, SLOT_158)
                if not SLOT_0:
                    Unknown26('TrapMatome')

            def upon_54():
                sendToLabel(581)
                clearUponHandler(upon_LANDING)
    if not SLOT_8:
        gotoLabel(100)
    sprite('vr_trap_aircore', 2)
    GFX_1('naef_atrapstart_03', 103)
    GFX_1('naef_trapdetection_a', 103)
    if SLOT_95 == 0:
        GFX_2('naef_airtrapjizoku2p_00')
    elif SLOT_95 == 2:
        GFX_2('naef_airtrapjizoku2p_00')
    else:
        GFX_2('naef_airtrapjizoku_05')
    EndMomentum(1)
    GFX_0('vr_trap_aircore_damy', -1)
    sprite('vr_trap_aircore', 10)
    ConstantAlphaModifier(-5)
    label(4)
    sprite('vr_trap_aircore', 10)
    sprite('vr_trap_aircore', 10)
    sprite('vr_trap_aircore', 10)
    sprite('vr_trap_aircore', 10)
    if not SLOT_2:
        Unknown3006(-100)
    else:
        Unknown3001(255)
        ConstantAlphaModifier(0)
    SLOT_57 = SLOT_57 + 1
    if SLOT_57 >= 12:
        sendToLabel(5)
    spriteEnd()
    gotoLabel(4)
    label(5)
    Unknown3001(0)
    ConstantAlphaModifier(-5)
    sprite('vr_trap_aircore', 10)
    Unknown3006(-300)
    SLOT_57 = SLOT_57 + 1
    if SLOT_57 >= 17:
        sendToLabel(580)
    spriteEnd()
    gotoLabel(5)
    label(580)
    sprite('null', 1)
    SLOT_51 = 0
    GFX_1('naef_atrapend_04', 103)
    GFX_0('TrapAntiAirKowareEff', 103)
    spriteEnd()
    ExitState()
    label(14)
    sprite('null', 1)
    GFX_0('TrapAntiAir', 103)
    if SLOT_55:

        def RunOnObject_1():
            MinimumDamage(10)
            Unknown30065(0)
    Unknown23090(25)
    ExitState()
    label(100)
    sprite('vr_trap_seed', 12)
    physicsYImpulse(-4000)
    physicsXImpulse(571)
    Unknown23022(1)
    GFX_2('naef_trap_seed')
    Unknown3001(200)
    ConstantAlphaModifier(-5)
    spriteEnd()
    XImpulseAcceleration(2200)
    YAccel(2200)
    ConstantAlphaModifier(-20)
    label(0)
    sprite('vr_trap_seed', 1)
    spriteEnd()
    gotoLabel(0)
    label(3)
    sprite('vr_trap_landcore', 2)
    SLOT_54 = 1
    BlendMode_Normal()
    GFX_1('naef_trapstart_03', 103)
    GFX_1('naef_trapdetection_b', 103)
    if SLOT_95 == 0:
        Unknown4003('naef_trapicon2p_ground.DIG', '')
        Unknown4015()
    elif SLOT_95 == 2:
        Unknown4003('naef_trapicon2p_ground.DIG', '')
        Unknown4015()
    else:
        Unknown4003('naef_trapicon_ground.DIG',
            'naef_trapicon_ground_0000.mmot')
        Unknown4015()
    GFX_2('naef_trapjizoku_07')
    AbsoluteY(0)
    EndMomentum(1)
    GFX_0('vr_trap_landcore_damy', -1)
    sprite('vr_trap_landcore', 10)
    ConstantAlphaModifier(-5)
    label(8)
    sprite('vr_trap_landcore', 10)
    sprite('vr_trap_landcore', 10)
    sprite('vr_trap_landcore', 10)
    sprite('vr_trap_landcore', 10)
    if not SLOT_2:
        Unknown3006(-100)
    else:
        Unknown3001(255)
        ConstantAlphaModifier(0)
    SLOT_58 = SLOT_58 + 1
    if SLOT_58 >= 12:
        sendToLabel(9)
    spriteEnd()
    gotoLabel(8)
    label(9)
    Unknown3001(0)
    ConstantAlphaModifier(-5)
    sprite('vr_trap_aircore', 10)
    Unknown3006(-300)
    SLOT_58 = SLOT_58 + 1
    if SLOT_58 >= 17:
        sendToLabel(581)
    spriteEnd()
    gotoLabel(9)
    label(581)
    sprite('null', 1)
    SLOT_51 = 0
    GFX_1('naef_trapend_05', 103)
    GFX_0('TrapAntiLandKowareEff', 103)
    spriteEnd()
    ExitState()
    label(141)
    sprite('null', 1)
    GFX_0('TrapAntiLand', 103)
    if SLOT_56:

        def RunOnObject_1():
            MinimumDamage(10)
            Unknown30065(0)
    Unknown23090(25)


@State
def TrapAntiLand():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel(5)
        AttackP1(80)
        AttackP2(85)
        Hitstop(4)
        Blockstun(11)
        AirPushbackY(22000)
        AirHitstunAnimation(AIR_VERTICAL)
        GroundedHitstunAnimation(AIR_VERTICAL)
        EnemyHitstopAddition(0, 8, 8)
        ChipPercentage(20)
        Visibility(1)
    sprite('vr_trap_landexp', 2)
    StartMultihit()
    GFX_2('naef_traphitg_sub')
    Unknown3001(255)
    Unknown23022(1)
    sprite('vr_trap_landexp', 3)
    RefreshMultihit()
    PrivateSE('bomb_m')
    sprite('vr_trap_landexp', 3)
    DisableAttackRestOfMove()
    sprite('vr_trap_landexp', 30)
    EndAttack()


@State
def TrapAntiLandKowareEff():
    sprite('vr_trap_landexp', 30)
    GFX_2('naef_trap_core')
    Visibility(1)
    Unknown3001(255)
    ConstantAlphaModifier(-20)
    Unknown1059(100)


@State
def TrapAntiAir():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel(5)
        AttackP1(80)
        AttackP2(85)
        Hitstop(1)
        Blockstun(11)
        AirPushbackY(22000)
        AirHitstunAnimation(AIR_VERTICAL)
        GroundedHitstunAnimation(AIR_VERTICAL)
        EnemyHitstopAddition(0, 8, 8)
        ChipPercentage(20)
        Visibility(1)
    sprite('vr_trap_airexp', 5)
    GFX_2('naef_trapexplosion_05')
    Unknown3001(255)
    DisableAttackRestOfMove()
    Unknown23022(1)
    sprite('vr_trap_airexp', 3)
    RefreshMultihit()
    PrivateSE('bomb_m')
    sprite('vr_trap_airexp', 3)
    DisableAttackRestOfMove()
    sprite('vr_trap_airexp', 30)
    EndAttack()


@State
def TrapAntiAirKowareEff():
    sprite('vr_trap_airexp', 30)
    GFX_2('naef_trap_core_aa')
    Visibility(1)
    Unknown3001(255)
    ConstantAlphaModifier(-20)
    Unknown1059(100)


@State
def suef_410():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(2)
        Unknown2054(1)
        Unknown4007(2)
        AddY(145000)
        AddX(-10000)

        def upon_30():
            Unknown4007(0)
    label(0)
    sprite('null', 3)
    GFX_0('suef_410_body', 100)
    gotoLabel(0)


@State
def suef_410_body():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(2)
        Unknown2054(1)
        Unknown4007(2)
        GFX_2('suef_410')
    sprite('null', 30)


@State
def suef_410_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown2054(1)
    label(0)
    sprite('null', 6)
    GFX_1('suef_410_add', 100)
    gotoLabel(0)


@State
def suef_410_zapper():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(2)
        Unknown2054(1)
        Unknown4007(2)
    label(0)
    sprite('null', 6)
    GFX_0('suef_410_slash', 100)
    gotoLabel(0)


@State
def suef_410_slash():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown2054(1)
        Unknown4003('suef_410.DIG', '')
        Unknown4015()
        BlendMode_Add()
        Size(1800)
        Unknown3001(255)
        ConstantAlphaModifier(-8)
        Unknown1077(0, 360000)
        AddY(40000)
        AddX(30000)
    sprite('null', 15)


@State
def ImpactReversal():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel(3)
        Damage(2500)
        AttackP1(80)
        AttackP2(60)
        AirUntechableTime(60)
        Hitstop(0)
        AirHitstunAnimation(AIR_VERTICAL)
        GroundedHitstunAnimation(AIR_VERTICAL)
        AirPushbackY(40000)
        BlendMode_Add()
        Unknown2054(1)
        Unknown30065(100)
        Unknown4007(3)
        HitAirUnblockable(4)
        IgnoreBurst(1)
        ProjectileLevel(1)
        AttackAttributes('B')
    sprite('vr_impact', 4)
    GFX_0('BarrierBrake', 100)
    RefreshMultihit()
    PrivateSE('ice_break_fast')
    sprite('vr_impact', 20)
    EndAttack()


@State
def ImpactReversal_CA():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel(3)
        Damage(2500)
        AttackP1(80)
        AttackP2(60)
        AirUntechableTime(60)
        Hitstop(0)
        AirHitstunAnimation(AIR_VERTICAL)
        GroundedHitstunAnimation(AIR_VERTICAL)
        AirPushbackY(40000)
        BlendMode_Add()
        Unknown2054(1)
        Unknown30065(100)
        Unknown4007(3)
        HitAirUnblockable(4)
        IgnoreBurst(1)
        ProjectileLevel(1)
        AttackAttributes('B')
        Unknown23022(1)
    sprite('vr_impact', 4)
    GFX_0('BarrierBrake', 100)
    PrivateSE('ice_break_fast')
    sprite('vr_impact', 20)
    EndAttack()


@State
def DanganReversal():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel(2)
        Damage(2500)
        AttackP1(80)
        AttackP2(60)
        Hitstop(0)
        ProjectileLevel(3)
        PushbackX(40000)
        AirUntechableTime(32)
        AirPushbackY(20000)
        AirPushbackX(30000)
        YImpulseBeforeWallbounce(2000)
        AirHitstunAnimation(AIR_TAILSPIN)
        GroundedHitstunAnimation(AIR_TAILSPIN)
        Wallbounce(1)
        AirHitstunAfterWallbounce(60)
        Unknown30065(100)
        IgnoreBurst(1)
        BlendMode_Normal()
        Unknown4003('naef_400_flysheld01.DIG', 'naef_400_flysheld01_0000.mmot')
        Unknown4015()
        Unknown4007(2)
        physicsXImpulse(70000)
        HitAirUnblockable(4)
    sprite('vr_dangan_a', 300)
    PaletteIndex(1)
    Unknown23067('suef_danganaura_00')
    GFX_1('naef_401gunfire', 0)
    GFX_0('FlyBarrierDandou', 1)
    GFX_0('FlyBarrierBrake', 100)
    RefreshMultihit()
    PrivateSE('ice_break_fast')


@State
def BarrierJizoku():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Unknown4003('naef_400_sheld00.DIG', '')
        Unknown4015()
        Unknown4007(2)
        Unknown4011(2)
        Unknown3001(0)

        def upon_43():
            if SLOT_48 == 3012:
                sendToLabel(1)
    sprite('null', 20)
    ConstantAlphaModifier(26)
    GFX_0('BarrierYugamiLoop', 100)
    sprite('null', 32767)
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def BarrierYugamiLoop():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Unknown4015()
        Unknown4007(2)
        Unknown4010(2)
        Unknown3001(0)
    label(1)
    sprite('null', 15)
    GFX_0('BarrierYugami', 100)
    sprite('null', 15)
    GFX_0('BarrierYugami', 100)
    gotoLabel(1)


@State
def BarrierYugami():
    sprite('vr_na400_yugami', 1)
    Unknown4007(2)
    Unknown4010(2)
    BlendMode_Normal()
    Unknown3057(1)
    Unknown3058(14000)
    sprite('keep', 20)
    Unknown1059(100)
    Unknown1067(200)
    ConstantAlphaModifier(-13)
    spriteEnd()


@State
def FlyBarrierBrake():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Unknown4015()
    sprite('null', 5)
    sprite('null', 5)
    GFX_1('suef_sheldbrake_05', 100)
    Unknown1099(50)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def FlyBarrierDandou():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    label(1)
    sprite('null', 3)
    GFX_1('suef_sheldatk_03', 100)
    gotoLabel(1)


@State
def DanganUltimate():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel(3)
        ProjectileLevel(1)
        Damage(800)
        AttackP1(80)
        AttackP2(90)
        AirUntechableTime(80)
        Hitstop(0)
        AirHitstunAnimation(AIR_VERTICAL)
        GroundedHitstunAnimation(AIR_VERTICAL)
        AirPushbackY(18000)
        AirPushbackX(1000)
        YImpulseBeforeWallbounce(1000)
        EnemyHitstopAddition(11, 11, 11)
        physicsXImpulse(130000)
        PaletteIndex(2)

        def upon_11():
            DeleteObject(25)
        Unknown23067('naef_433dandoA')
        MinimumDamage(10)
        Unknown30065(0)
    sprite('vr_dangan_d_big', 1)
    GFX_1('naef_401gunfireEX', 0)
    RefreshMultihit()
    PrivateSE('na003')
    sprite('vr_dangan_d', 300)


@State
def Zanzoh_kick():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(2)
        Unknown2054(1)
        BlendMode_Add()
        PaletteIndex(2)
        Size(1100)
        Unknown3001(255)
        ConstantAlphaModifier(-25)
    sprite('vr_na433_00', 30)
    GFX_1('naef_407smoke', 100)


@State
def Kick_line():

    def upon_IMMEDIATE():
        Unknown4003('naef_433kick.DIG', '')
        Unknown23067('naef_433kicksub')
        Unknown4009(2)
        Unknown2054(1)
        Unknown4015()
        Size(1100)
        Unknown3001(0)
    sprite('null', 10)
    ConstantAlphaModifier(50)
    sprite('null', 7)
    ConstantAlphaModifier(-40)


@State
def DanganKakushiA():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel(4)
        Damage(700)
        MinimumDamage(17)
        AttackP2(96)
        Unknown23182(2)
        Hitstop(0)
        PushbackX(1000)
        AirUntechableTime(70)
        Hitstop(1)
        Unknown9021(1)
        AirPushbackX(20000)
        AirPushbackY(10000)
        YImpulseBeforeWallbounce(2000)
        Unknown11068(1)
        EnemyHitstopAddition(0, 11, 11)
        GroundedHitstunAnimation(AIR_FACE_UP_SKIP)
        AirHitstunAnimation(AIR_FACE_UP_SKIP)
        Unknown30056(-200000, 100, 0)
        HardKnockdown(1)
        Unknown2054(1)
        PaletteIndex(2)
        Unknown1072(20000)
        Unknown4055(0)
        Unknown4045('naef_401gunfireB', 0)
        Unknown1110(100000, 0)

        def upon_43():
            if SLOT_48 == 3013:
                Unknown1072(20000)
                Unknown4055(0)
                Unknown4045('naef_401gunfireB', 0)
                Unknown1110(100000, 0)
                AirUntechableTime(150)
                YImpulseBeforeWallbounce(1100)
                AirPushbackY(8000)
                HardKnockdown(60)

        def upon_LANDING():
            DeleteObject(25)
        Unknown23067('naef_401dandoB')
    sprite('vr_dangan_b', 300)
    GFX_1('naef_401gunfireB', 0)
    RefreshMultihit()


@State
def DanganKakushiB():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel(5) # was 4
        Damage(4000)
        MinimumDamage(25)
        AttackP2(60)
        Hitstop(12) #WAS12
        PushbackX(1000)
        AirUntechableTime(30) #was 30
        AirPushbackY(-100000)
        AirPushbackX(100000)
        GroundedHitstunAnimation(AIR_TAILSPIN)
        AirHitstunAnimation(AIR_TAILSPIN)
        Floorslide(10)
        HardKnockdown(10)
        Unknown11110(97)
        Unknown23078(1)
        PaletteIndex(2)
        Unknown1072(20000)
        Unknown4055(0)
        Unknown4045('naef_401gunfireC', 0)
        Unknown1110(130000, 0)

        def upon_LANDING():
            DeleteObject(25)

        def upon_12():
            ScreenShake(80000, 0)
            CopyFromRightToLeft(25, SLOT_51, 27, SLOT_95)
            SLOT_51 = SLOT_51 + 1
            if SLOT_51 == 1:
                ObjectUpon2(3, 9001, 0)
            if SLOT_51 == 2:
                ObjectUpon2(3, 9002, 0)
            if SLOT_51 == 3:
                ObjectUpon2(3, 9003, 0)
            if SLOT_51 == 4:
                ObjectUpon2(3, 9004, 0)

        def upon_10():
            clearUponHandler(upon_10)
            Unknown21015('SecretGunOD', 5001, 0)
        Unknown23067('naef_401dandoC')
    sprite('vr_dangan_c', 300)
    RefreshMultihit()


@State
def Hamaon_search():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        Unknown23056()
        BlendMode_Normal()
        Unknown4003('naef_432hama_search.DIG', '')
        Unknown23067('suef_431hama_search')
        Unknown4015()
        AbsoluteY(0)
        AddX(150000)
        Unknown3001(0)
        Unknown4011(3)

        def upon_43():
            if SLOT_48 == 3014:
                Unknown4011(0)
    sprite('null', 12)
    ConstantAlphaModifier(25)
    PrivateSE('magiccircle_a')
    sprite('null', 18)
    GFX_0('Hamaon', 100)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def Hamaon():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        Unknown23056()
        AttackLevel(3)
        Damage(0)
        AttackP2(100)
        Hitstop(0)
        Unknown9021(1)
        AirPushbackX(0)
        AirPushbackY(4000)
        YImpulseBeforeWallbounce(200)
        PushbackX(0)
        Unknown11064(1)
        Unknown30055(0, 50, 20)
        Unknown30056(120000, 50, 0)
        Unknown11070(1)
        AbsoluteY(0)
        Unknown1064(1500)
        Unknown4051(0)
        Unknown4011(3)
        BlendMode_Normal()
        Unknown4003('naef_432hama.DIG', '')
        GFX_2('suef_431hama')
        Unknown23015(2)
        Unknown4015()

        def upon_78():
            SLOT_55 = 1
            CopyFromRightToLeft(25, SLOT_51, 22, SLOT_95)
            if SLOT_51 == 0:
                CopyFromRightToLeft(25, SLOT_52, 3, SLOT_63)
                if SLOT_52 == 2:
                    SLOT_53 = 1
                if PartnerChar('pna'):
                    CopyFromRightToLeft(25, SLOT_52, 24, SLOT_63)
                    if SLOT_52 == 2:
                        SLOT_53 = 1
            elif SLOT_51 == 1:
                CopyFromRightToLeft(25, SLOT_52, 3, SLOT_64)
                if SLOT_52 == 2:
                    SLOT_53 = 1
                if PartnerChar('pna'):
                    CopyFromRightToLeft(25, SLOT_52, 24, SLOT_64)
                    if SLOT_52 == 2:
                        SLOT_53 = 1
            elif SLOT_51 == 2:
                CopyFromRightToLeft(25, SLOT_52, 3, SLOT_65)
                if SLOT_52 == 2:
                    SLOT_53 = 1
                if PartnerChar('pna'):
                    CopyFromRightToLeft(25, SLOT_52, 24, SLOT_65)
                    if SLOT_52 == 2:
                        SLOT_53 = 1
            elif SLOT_51 == 3:
                CopyFromRightToLeft(25, SLOT_52, 3, SLOT_66)
                if SLOT_52 == 2:
                    SLOT_53 = 1
                if PartnerChar('pna'):
                    CopyFromRightToLeft(25, SLOT_52, 24, SLOT_66)
                    if SLOT_52 == 2:
                        SLOT_53 = 1
            if SLOT_53:
                Unknown23083(1)
                DamageFromStateOnly('Hamaon')
                SLOT_9 = 1

        def upon_82():
            SLOT_56 = 1
    sprite('vr_dmy_hamaon', 5)
    RefreshMultihit()
    PrivateSE('na010')
    sprite('vr_dmy_hamaon', 5)
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 5)
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 5)
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 5)
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 5)
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 5)
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 5)
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 5)
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 5)
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 5)
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 5)
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 5)
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 5)
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 4)
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 1)
    if SLOT_56:
        GFX_0('MissMarkHsub', 100)
    spriteEnd()
    clearUponHandler(upon_78)
    if SLOT_55:
        conditionalSendToLabel(1)
    sprite('vr_dmy_hamaon', 24)
    ConstantAlphaModifier(-10)
    EndAttack()
    spriteEnd()
    ExitState()
    label(1)
    sprite('vr_dmy_hamaon_big', 5)
    RefreshMultihit()

    def upon_78():
        Unknown21015('Hamaon_search', 3014, 0)
        Unknown4011(0)
        SLOT_53 = 0
        CopyFromRightToLeft(25, SLOT_51, 22, SLOT_95)
        if SLOT_51 == 0:
            CopyFromRightToLeft(25, SLOT_52, 3, SLOT_63)
            if SLOT_52 == 2:
                DamageFromStateOnly('HamaonKill1P')
                GFX_0('HamaonKill', 103)
                ObjectUpon2(1, 9011, 0)
                SLOT_53 = 1
            if PartnerChar('pna'):
                CopyFromRightToLeft(25, SLOT_52, 24, SLOT_63)
                if SLOT_52 == 2:
                    DamageFromStateOnly('HamaonKill1P')
                    GFX_0('HamaonKill', 103)
                    ObjectUpon2(1, 9011, 0)
                    SLOT_53 = 1
        elif SLOT_51 == 1:
            CopyFromRightToLeft(25, SLOT_52, 3, SLOT_64)
            if SLOT_52 == 2:
                DamageFromStateOnly('HamaonKill2P')
                GFX_0('HamaonKill', 103)
                ObjectUpon2(1, 9012, 0)
                SLOT_53 = 1
            if PartnerChar('pna'):
                CopyFromRightToLeft(25, SLOT_52, 24, SLOT_64)
                if SLOT_52 == 2:
                    DamageFromStateOnly('HamaonKill2P')
                    GFX_0('HamaonKill', 103)
                    ObjectUpon2(1, 9012, 0)
                    SLOT_53 = 1
        elif SLOT_51 == 2:
            CopyFromRightToLeft(25, SLOT_52, 3, SLOT_65)
            if SLOT_52 == 2:
                DamageFromStateOnly('HamaonKill3P')
                GFX_0('HamaonKill', 103)
                ObjectUpon2(1, 9013, 0)
                SLOT_53 = 1
            if PartnerChar('pna'):
                CopyFromRightToLeft(25, SLOT_52, 24, SLOT_65)
                if SLOT_52 == 2:
                    DamageFromStateOnly('HamaonKill3P')
                    GFX_0('HamaonKill', 103)
                    ObjectUpon2(1, 9013, 0)
                    SLOT_53 = 1
        elif SLOT_51 == 3:
            CopyFromRightToLeft(25, SLOT_52, 3, SLOT_66)
            if SLOT_52 == 2:
                DamageFromStateOnly('HamaonKill4P')
                GFX_0('HamaonKill', 103)
                ObjectUpon2(1, 9014, 0)
                SLOT_53 = 1
            if PartnerChar('pna'):
                CopyFromRightToLeft(25, SLOT_52, 24, SLOT_66)
                if SLOT_52 == 2:
                    DamageFromStateOnly('HamaonKill4P')
                    GFX_0('HamaonKill', 103)
                    ObjectUpon2(1, 9014, 0)
                    SLOT_53 = 1
        if SLOT_53:
            AirPushbackX(0)
            AirPushbackY(1)
            YImpulseBeforeWallbounce(0)
            Hitstun(350)
            AirUntechableTime(350)
            Unknown30048(1)
            Unknown11062(1)
        else:
            AirPushbackX(0)
            AirPushbackY(30000)
            YImpulseBeforeWallbounce(2000)
            AirHitstunAnimation(AIR_FACE_UP_SKIP)
            GroundedHitstunAnimation(AIR_FACE_UP_SKIP)
            GFX_0('MissMarkH', 100)
            EnemyHitstopAddition(0, 19, 19)
    sprite('vr_dmy_hamaon', 10)
    EndAttack()


@State
def HamaonKill():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel(5)
        Unknown11057(1500)
        UseSlashHitspark(1)
        Damage(99999)
        MinimumDamage(100)
        Unknown11106(0)
        AirPushbackX(0)
        AirPushbackY(40000)
        YImpulseBeforeWallbounce(2000)
        AirHitstunAnimation(AIR_VERTICAL)
        GroundedHitstunAnimation(AIR_VERTICAL)
        Visibility(1)
        Unknown23151(22, 103)
        Unknown4007(22)
        Unknown20000(1)
        Unknown30048(1)
        DamageFromStateOnly('HamaonKill')
        CounterHitSetting(1)

        def upon_12():
            SLOT_9 = 0

            def RunOnObject_22():
                ConstantAlphaModifier(0)
                Unknown3001(255)
        Unknown23083(1)
        SLOT_6 = 0

        def upon_43():
            if SLOT_48 == 9011:
                Unknown30070('HamaonKill1P')
            if SLOT_48 == 9012:
                Unknown30070('HamaonKill2P')
            if SLOT_48 == 9013:
                Unknown30070('HamaonKill3P')
            if SLOT_48 == 9014:
                Unknown30070('HamaonKill4P')
    sprite('vr_dmy_hamaon', 1)
    StartMultihit()
    sprite('vr_dmy_hamaon', 3)
    StartMultihit()

    def RunOnObject_22():
        BlendMode_Normal()
        ConstantAlphaModifier(-4)
    sprite('vr_dmy_hamaon', 10)
    StartMultihit()
    sprite('vr_dmy_hamaon', 10)
    StartMultihit()
    PrivateSE('cut_l')
    sprite('vr_dmy_hamaon', 10)
    StartMultihit()
    GFX_0('HamaonKillIcon', 100)
    sprite('vr_dmy_hamaon', 10)
    StartMultihit()
    sprite('vr_dmy_hamaon', 10)
    StartMultihit()
    sprite('vr_dmy_hamaon', 10)
    StartMultihit()
    sprite('vr_dmy_hamaon', 10)
    StartMultihit()
    sprite('vr_dmy_hamaon', 1)
    ScreenShake(300000, 100000)
    RefreshMultihit()
    HitAnywhere(1)
    Unknown23008(0, 0)


@State
def HamaonKillIcon():

    def upon_IMMEDIATE():
        GFX_2('suef_hamadeath_05')
        Unknown4007(2)
        FaceLeft()
    sprite('null', 60)


@State
def MissMarkH():

    def upon_IMMEDIATE():
        FaceLeft()

        def upon_EVERY_FRAME():
            Unknown23151(22, 103)
            AddY(90000)
    sprite('null', 20)
    GFX_2('naef_miss')


@State
def MissMarkHsub():

    def upon_IMMEDIATE():
        FaceLeft()

        def upon_EVERY_FRAME():
            Unknown23151(23, 103)
            AddY(90000)
    sprite('null', 20)
    GFX_2('naef_miss')


@State
def MissMarkM():

    def upon_IMMEDIATE():
        FaceLeft()

        def upon_EVERY_FRAME():
            Unknown23151(22, 103)
            AddY(60000)
    sprite('null', 20)
    sprite('null', 40)
    GFX_2('naef_miss')


@State
def MissMarkMprt():

    def upon_IMMEDIATE():
        FaceLeft()

        def upon_EVERY_FRAME():
            Unknown23151(23, 103)
            AddY(60000)
    sprite('null', 20)
    sprite('null', 40)
    GFX_2('naef_miss')


@State
def Mudoon_search():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4003('naef_432mudo_search.DIG', '')
        Unknown23067('suef_431mudo_search')
        Unknown4015()
        BlendMode_Normal()
        Unknown3001(0)
        AddX(130000)
        AddY(160000)

        def upon_43():
            if SLOT_48 == 3015:
                Unknown4011(0)
    sprite('null', 30)
    ConstantAlphaModifier(25)
    PrivateSE('magiccircle_b')
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def Mudoon():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel(5)
        Damage(0)
        AttackP2(100)
        AirPushbackX(0)
        AirPushbackY(0)
        YImpulseBeforeWallbounce(100)
        AirHitstunAnimation(AIR_FACE_UP_SKIP)
        GroundedHitstunAnimation(AIR_FACE_UP_SKIP)
        Unknown11064(1)
        Unknown4011(3)
        Unknown4051(0)

        def upon_EVERY_FRAME():
            SLOT_51 = SLOT_51 + 1
            if SLOT_51 >= 100:
                clearUponHandler(upon_EVERY_FRAME)
                SLOT_34 = 0
        SetActionMark(0)

        def upon_78():
            CopyFromRightToLeft(25, SLOT_51, 3, SLOT_6)
            if SLOT_51:
                SetActionMark(1)
            if PartnerChar('pna'):
                CopyFromRightToLeft(25, SLOT_51, 24, SLOT_6)
                if SLOT_51:
                    SetActionMark(1)
            CopyFromRightToLeft(25, SLOT_52, 22, SLOT_170)
            if SLOT_52:
                SetActionMark(0)
            if SLOT_2:
                Unknown21015('UltimateKillAir', 5002, 0)
                Unknown21015('UltimateKillAirOD', 5002, 0)
                AirPushbackX(0)
                AirPushbackY(1)
                YImpulseBeforeWallbounce(0)
                Unknown30056(-190000, 100, 0)
                AirUntechableTime(320)
                DamageFromStateOnly('MudoonKill')
                Unknown30048(1)
                Unknown23083(1)
                SLOT_9 = 1
                AirHitstunAnimation(AIR_FACE_UP_SKIP)
                GroundedHitstunAnimation(AIR_FACE_UP_SKIP)
                Wallstick(0)
                Unknown11062(1)
            else:
                Unknown30056(-190000, 50, 0)
                AirPushbackX(150000)
                AirPushbackY(10000)
                YImpulseBeforeWallbounce(0)
                EnemyHitstopAddition(0, 29, 29)
                Wallstick(1)
                WallstickDuration(66)
                AirHitstunAfterWallbounce(100)
                WallbounceReboundTime(10)
                AirHitstunAnimation(AIR_BLOWBACK)
                GroundedHitstunAnimation(AIR_BLOWBACK)
                GFX_0('MissMarkM', 100)
                SLOT_34 = 0
            SLOT_56 = 1
            Unknown21015('Mudoon_search', 3015, 0)
            Unknown4011(0)
            SLOT_57 = SLOT_2

        def upon_82():
            Unknown30056(-190000, 50, 0)
            AirPushbackX(150000)
            AirPushbackY(10000)
            YImpulseBeforeWallbounce(0)
            EnemyHitstopAddition(0, 29, 29)
            Wallstick(1)
            WallstickDuration(66)
            AirHitstunAfterWallbounce(100)
            WallbounceReboundTime(10)
            AirHitstunAnimation(AIR_BLOWBACK)
            GroundedHitstunAnimation(AIR_BLOWBACK)
            GFX_0('MissMarkMprt', 100)
            SLOT_34 = 0
        Unknown4003('naef_432mudo.DIG', '')
        Unknown4015()
        Unknown23015(2)
        BlendMode_Normal()
        AddX(110000)
        AddY(160000)

        def upon_16():
            GFX_0('MudoBall', 100)
    sprite('vr_dmy_mudoon', 4)
    PrivateSE('na011')
    sprite('vr_dmy_mudoon', 11)
    sprite('vr_dmy_mudoon2', 40)
    sprite('vr_dmy_mudoon2', 1)
    ConstantAlphaModifier(-26)
    DisableAttackRestOfMove()
    clearUponHandler(upon_16)
    sprite('vr_dmy_mudoon2', 10)
    if SLOT_56:
        if SLOT_57:
            GFX_0('MudoonKill', 100)
    spriteEnd()
    ExitState()


@State
def MudoBall():

    def upon_IMMEDIATE():
        Unknown2054(1)
        GFX_2('suef_432mudoball')
        physicsXImpulse(90000)
        RandSpeedX(10000, -10000)
        RandSpeedY(10000, -10000)
        Unknown1099(20)
        DeviationY(50000, -50000)
        DeviationX(25000, -25000)
    sprite('null', 6)
    XImpulseAcceleration(6)
    YAccel(6)
    Size(50)
    Unknown3001(50)
    ConstantAlphaModifier(20)
    Unknown1099(150)
    sprite('null', 4)
    GFX_1('suef_432mudoball_sub', 100)
    XImpulseAcceleration(1000)
    YAccel(1000)
    Unknown1099(30)
    sprite('null', 4)
    GFX_1('suef_432mudoball_sub', 100)
    sprite('null', 4)
    GFX_1('suef_432mudoball_sub', 100)
    sprite('null', 4)
    GFX_1('suef_432mudoball_sub', 100)
    Unknown3001(180)
    ConstantAlphaModifier(-20)
    XImpulseAcceleration(15)
    YAccel(15)
    sprite('null', 22)
    GFX_1('suef_432mudoball_sub', 100)


@State
def MudoonKillIcon():

    def upon_IMMEDIATE():
        GFX_2('suef_mudodeath_05')
        Unknown4007(2)
        FaceLeft()
    sprite('null', 60)


@State
def MudoonKill():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel(5)
        Unknown11057(1500)
        UseSlashHitspark(1)
        Damage(99999)
        MinimumDamage(100)
        Unknown11106(0)
        AirPushbackX(70000)
        AirPushbackY(30000)
        YImpulseBeforeWallbounce(2000)
        AirHitstunAnimation(AIR_FACE_UP_SKIP)
        GroundedHitstunAnimation(AIR_FACE_UP_SKIP)
        Visibility(1)
        Unknown23151(22, 103)
        Unknown4007(22)
        Unknown20000(1)
        Unknown30048(1)
        DamageFromStateOnly('MudoonKill')
        CounterHitSetting(1)

        def upon_12():
            SLOT_9 = 0

            def RunOnObject_22():
                ConstantAlphaModifier(0)
                Unknown3001(255)
        Unknown23083(1)
        SLOT_5 = 0
    sprite('vr_dmy_hamaon', 4)
    StartMultihit()

    def RunOnObject_22():
        BlendMode_Normal()
        ConstantAlphaModifier(-4)
    sprite('vr_dmy_hamaon', 10)
    StartMultihit()
    sprite('vr_dmy_hamaon', 10)
    StartMultihit()
    PrivateSE('cut_l')
    sprite('vr_dmy_hamaon', 10)
    StartMultihit()
    GFX_0('MudoonKillIcon', 100)
    sprite('vr_dmy_hamaon', 10)
    StartMultihit()
    sprite('vr_dmy_hamaon', 10)
    StartMultihit()
    sprite('vr_dmy_hamaon', 10)
    StartMultihit()
    sprite('vr_dmy_hamaon', 10)
    StartMultihit()
    sprite('vr_dmy_hamaon', 10)
    ScreenShake(300000, 100000)
    RefreshMultihit()
    HitAnywhere(1)
    Unknown23008(0, 0)


@State
def Ichigeki_RedRay():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown23151(22, 103)
    sprite('null', 20)
    GFX_2('naef_ichigekikakutei_05')
    sprite('null', 1)
    Unknown21015('AstralHeat', 9503, 0)


@State
def RotateGun():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(2)
        BlendMode_Normal()
        PaletteIndex(0)
        EnableAfterimage(1)
    sprite('vr_na450_rotategun_00', 2)
    physicsXImpulse(3000)
    physicsYImpulse(45000)
    sprite('vr_na450_rotategun_01', 2)
    PrivateSE('slash_rapier_fast')
    sprite('vr_na450_rotategun_02', 2)
    physicsXImpulse(1000)
    physicsYImpulse(7000)
    PrivateSE('slash_rapier_fast')
    sprite('vr_na450_rotategun_01', 2)
    sprite('vr_na450_rotategun_02', 2)
    physicsYImpulse(6000)
    PrivateSE('slash_rapier_fast')
    sprite('vr_na450_rotategun_01', 2)
    sprite('vr_na450_rotategun_02', 2)
    PrivateSE('slash_rapier_fast')
    sprite('vr_na450_rotategun_00', 2)
    sprite('vr_na450_rotategun_01', 2)
    PrivateSE('slash_rapier_fast')
    sprite('vr_na450_rotategun_02', 2)
    sprite('vr_na450_rotategun_00', 2)
    PrivateSE('slash_rapier_fast')
    sprite('vr_na450_rotategun_01', 2)
    sprite('vr_na450_rotategun_02', 2)
    PrivateSE('slash_rapier_fast')
    PrivateSE('slash_rapier_fast')
    sprite('vr_na450_rotategun_02', 2)
    physicsYImpulse(-27000)
    physicsXImpulse(2250)
    sprite('vr_na450_rotategun_00', 2)
    PrivateSE('slash_rapier_fast')
    sprite('vr_na450_rotategun_01', 2)
    sprite('vr_na450_rotategun_02', 2)
    PrivateSE('slash_rapier_fast')
    sprite('vr_na450_rotategun_00', 2)
    sprite('vr_na450_rotategun_01', 2)
    PrivateSE('slash_rapier_fast')
    sprite('vr_na450_rotategun_02', 2)
    sprite('vr_na450_rotategun_00', 2)
    sprite('vr_na450_rotategun_02', 2)
    GFX_1('naef_guncatchi_03', 0)


@State
def ZanzohCircle():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(2)
        BlendMode_Add()
        PaletteIndex(3)
    sprite('vr_su450_00', 2)
    GFX_1('suef_circlekidou_01', 0)
    sprite('vr_su450_00', 2)
    GFX_1('suef_circlekidou_01', 1)
    sprite('vr_su450_01', 4)
    GFX_1('suef_circlekidou_01', 0)
    sprite('vr_su450_02', 4)
    GFX_1('suef_circlekidou_01', 0)
    sprite('vr_su450_03', 10)
    GFX_1('suef_circlekidou_01', 0)
    sprite('vr_su450_03', 10)
    ConstantAlphaModifier(-26)


@Subroutine
def Ichigeki_MarkerSetting():
    GFX_0('Ichigeki_Marker', 103)
    SLOT_0 = 6
    CopyFromRightToLeft(1, SLOT_51, 25, SLOT_0)

    def RunOnObject_1():
        SetPosXByScreenPer(-15)
        SetPosYByScreenPer(70)
    GFX_0('Ichigeki_Marker', 103)
    SLOT_0 = 4
    CopyFromRightToLeft(1, SLOT_51, 25, SLOT_0)

    def RunOnObject_1():
        SetPosXByScreenPer(115)
        SetPosYByScreenPer(40)
    GFX_0('Ichigeki_Marker', 103)
    SLOT_0 = 3
    CopyFromRightToLeft(1, SLOT_51, 25, SLOT_0)

    def RunOnObject_1():
        SetPosXByScreenPer(40)
        SetPosYByScreenPer(-5)


@State
def Ichigeki_Marker():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        Unknown4010(3)
        Unknown2054(1)
        AttackLevel(0)
        Damage(0)
        Hitstop(0)
        PushbackX(0)
        AirPushbackX(0)
        AirPushbackY(500)
        YImpulseBeforeWallbounce(20)
        AirUntechableTime(120)
        EnemyHitstopAddition(20, 20, 20)
        Unknown11064(1)
        DistanceCheck(140000, -140000, -1, -1)
        Unknown11050(5, '')

        def upon_5():
            SLOT_13 = SLOT_13 * -1

        def upon_78():
            clearUponHandler(upon_43)
            sendToLabel(1)
            Unknown23144(22, 0, 103, 0, 0, 0, 0, 0, -15, 0, 15)

        def upon_61():
            clearUponHandler(upon_43)
            sendToLabel(0)

        def upon_44():
            clearUponHandler(upon_43)
            sendToLabel(0)

        def upon_43():
            if SLOT_48 == 9532:
                sendToLabel(0)
            if SLOT_48 == 9531:
                sendToLabel(1)
        Unknown23026(100000)
        Unknown23067('suef_jizokutarget_02')
        DisableAttackRestOfMove()
    sprite('vr_su450_dmy', 1)
    Size(800)
    sprite('vr_su450_dmy', 5)
    ConstantAlphaModifier(32)
    if SLOT_23 < 110000:
        AbsoluteY(110000)
    sprite('vr_su450_dmy', 5)
    ConstantAlphaModifier(-12)
    sprite('vr_su450_dmy', 2)
    Unknown3001(255)
    ConstantAlphaModifier(0)
    Unknown1099(160)
    sprite('vr_su450_dmy', 2)
    Unknown1099(-20)
    sprite('vr_su450_dmy', 2)
    Unknown1099(0)
    sprite('vr_su450_dmy', 10)
    RefreshMultihit()
    sprite('vr_su450_dmy', 1)
    sprite('vr_su450_dmy', 130)
    if SLOT_51 == 1:
        physicsXImpulse(-525)
        physicsYImpulse(-525)
    if SLOT_51 == 2:
        physicsXImpulse(0)
        physicsYImpulse(-700)
    if SLOT_51 == 3:
        physicsXImpulse(525)
        physicsYImpulse(-525)
    if SLOT_51 == 4:
        physicsXImpulse(-700)
        physicsYImpulse(0)
    if SLOT_51 == 6:
        physicsXImpulse(700)
        physicsYImpulse(0)
    if SLOT_51 == 7:
        physicsXImpulse(-525)
        physicsYImpulse(525)
    if SLOT_51 == 8:
        physicsXImpulse(0)
        physicsYImpulse(700)
    if SLOT_51 == 9:
        physicsXImpulse(525)
        physicsYImpulse(525)
    sprite('vr_su450_dmy', 50)
    EndAttack()
    sprite('vr_su450_dmy', 16)
    Unknown21015('PNA_PersonaIchigeki', 9512, 0)
    ConstantAlphaModifier(-16)
    Unknown1099(20)
    EndMomentum(1)
    EndAttack()
    sprite('null', 32767)
    spriteEnd()
    label(1)
    sprite('null', 32767)
    clearUponHandler(upon_43)
    Unknown21015('PNA_PersonaIchigeki', 9511, 0)
    Unknown21015('AstralHeat', 9501, 0)
    Unknown21015('Ichigeki_Marker', 9531, 0)

    def upon_EVERY_FRAME():
        Unknown21015('Ichigeki_Marker', 9531, 0)
    label(0)
    sprite('null', 16)
    Unknown21015('PNA_PersonaIchigeki', 9512, 0)
    ConstantAlphaModifier(-16)
    Unknown1099(20)
    EndMomentum(1)
    EndAttack()


@State
def Ichigeki_Scope():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        FaceLeft()
        Unknown23015(1)
        SetZVal(100)
        Unknown23180(1)
        ScreenPosition(1)
        Size(1800)
        XPositionRelativeFacing(-640000)
        AbsoluteY(-380000)
        Unknown3001(255)
        Unknown23013(0)
        Unknown2053(0)
        ScreenCollision(0)

        def upon_43():
            if SLOT_48 == 9533:
                sendToLabel(0)
            if SLOT_48 == 9534:
                sendToLabel(1)
    sprite('vr_scope', 32767)
    label(0)
    sprite('vr_scope', 10)
    ConstantAlphaModifier(-26)
    label(1)
    sprite('vr_scope', 5)
    ConstantAlphaModifier(-51)
    Unknown1099(800)


@State
def Ichigeki_Scope2():

    def upon_IMMEDIATE():
        BlendMode_Add()
        FaceLeft()
        Unknown23015(3)
        Unknown23180(1)
        ScreenPosition(1)
        Size(1800)
        XPositionRelativeFacing(-640000)
        AbsoluteY(-380000)
        Unknown1074(4000)
        Unknown23013(0)
        Unknown2053(0)
        ScreenCollision(0)

        def upon_43():
            if SLOT_48 == 9533:
                sendToLabel(0)
    sprite('vr_scope2', 32767)
    label(0)
    sprite('vr_scope2', 10)
    ConstantAlphaModifier(-26)


@State
def Ichigeki_Scope3():

    def upon_IMMEDIATE():
        BlendMode_Add()
        FaceLeft()
        Unknown23015(3)
        Unknown23180(1)
        ScreenPosition(1)
        Size(1800)
        XPositionRelativeFacing(-640000)
        AbsoluteY(-380000)
        Unknown23013(0)
        Unknown2053(0)
        ScreenCollision(0)

        def upon_43():
            if SLOT_48 == 9533:
                sendToLabel(0)
    label(1)
    sprite('null', 20)
    GFX_0('Ichigeki_Scope4', 100)
    gotoLabel(1)
    label(0)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def Ichigeki_Scope4():

    def upon_IMMEDIATE():
        BlendMode_Add()
        FaceLeft()
        Unknown23015(3)
        Unknown23180(1)
        ScreenPosition(1)
        Size(1800)
        XPositionRelativeFacing(-640000)
        AbsoluteY(-380000)
        Unknown23013(0)
        Unknown2053(0)
        ScreenCollision(0)
    sprite('vr_scope3', 10)
    Unknown1099(-50)
    ConstantAlphaModifier(-9)
    sprite('vr_scope3', 20)


@State
def IchigekiCamera():

    def upon_IMMEDIATE():
        EnableAfterimage(1)
        BlendMode_Normal()
        Unknown3001(80)
        Unknown23013(0)
        Unknown2053(0)
        ScreenCollision(0)
        Unknown20003(1)
        Visibility(1)

        def upon_43():
            if SLOT_48 == 9521:
                sendToLabel(0)

        def upon_STATE_END():
            Unknown20000(0)
            Unknown20002(0)
            Unknown20003(0)
    label(1)
    sprite('dmy_camera', 32767)
    Unknown20003(1)
    Unknown23151(22, 103)
    Unknown20001(1)
    Unknown20000(1)
    Unknown20009(900)

    def upon_EVERY_FRAME():
        Unknown23151(22, 103)
        AddY(-20000)
    label(0)
    sprite('keep', 1)
    spriteEnd()


@State
def IchigekiCutin():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23015(4)
        ScreenPosition(1)
        BlendMode_Normal()
        ScreenPosition(1)
        XPositionRelativeFacingAbsolute(640000)
        AddX(250000)
        AbsoluteY(-384000)
        AddY(500000)
        Unknown3001(0)
        Size(3000)
    sprite('ichigeki0', 10)
    ConstantAlphaModifier(8)
    physicsXImpulse(40000)
    Unknown1099(-100)
    sprite('ichigeki0', 10)
    physicsXImpulse(200)
    sprite('ichigeki0', 40)
    Unknown1099(0)
    Size(900)
    sprite('ichigeki0', 1)
    PrivateSE('na000')
    sprite('ichigeki0', 1)
    PrivateSE('na000')
    sprite('ichigeki0', 1)
    PrivateSE('na000')
    sprite('ichigeki0', 2)
    PrivateSE('na000')
    sprite('ichigeki0', 6)
    sprite('ichigeki0', 5)
    Unknown1099(300)
    physicsXImpulse(250000)
    physicsYImpulse(130000)
    ConstantAlphaModifier(-52)


@State
def IchigekiTame_Atk():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        AttackLevel(5)
        Hitstop(120)
        Damage(1)
        AirHitstunAnimation(AIR_FACE_UP_SKIP)
        GroundedHitstunAnimation(AIR_FACE_UP_SKIP)
        Unknown11050(1, '')
        HitAnywhere(1)
        HitLow(99)
        HitOverhead(99)
        HitAirUnblockable(99)
        Unknown23015(4)
    sprite('dmy_atk00', 4)
    RefreshMultihit()
    GFX_0('naef_ichigehit_obj', 100)
    sprite('dmy_atk00', 120)


@State
def naef_ichigehit_obj():

    def upon_IMMEDIATE():
        GFX_2('naef_ichigehit_la')
        Unknown23151(22, 103)
    sprite('null', 124)


@State
def Ichigeki_shot():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown2054(1)
        ParticleLayer(4)
        AbsoluteY(260000)
        XPositionRelativeFacing(-400000)
        Unknown4003('suef_450_shot00.DIG', '')
        Unknown4015()
        Unknown23015(4)
        Unknown23151(22, 103)
    sprite('vr_su450_dandou', 10)
    physicsXImpulse(200000)
    Unknown23067('naef_ichigtekishot_07')
    PrivateSE('na003')
    sprite('vr_su450_dandou', 20)
    physicsXImpulse(50000)
    sprite('vr_su450_dandou', 10)
    ConstantAlphaModifier(-26)


@State
def IchigekiExplosion():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        ParticleLayer(1)
        Unknown4003('suef_450_bom00.DIG', '')
        Unknown4015()
        Size(300)
        Unknown3001(0)
        BlendMode_Normal()
        GFX_2('naef_ichigekihit_09')
        Unknown23151(22, 103)
    sprite('null', 5)
    ConstantAlphaModifier(51)
    Unknown1099(30)
    sprite('null', 2)
    Size(600)
    Unknown1099(0)
    sprite('null', 2)
    Size(1200)
    sprite('null', 4)
    Size(2400)
    sprite('null', 4)
    Size(2600)
    sprite('null', 4)
    Size(2800)
    sprite('null', 30)
    Size(3000)


@State
def IchigekiBlack():

    def upon_IMMEDIATE():
        Unknown2054(1)
        PaletteIndex(2)
        SetZVal(500)
        ScreenPosition(1)
        FaceLeft()
        XPositionRelativeFacing(-500000)
        AbsoluteY(-384000)
        ColorForTransition(0xff000000)
        BlendMode_Normal()
        Unknown23013(0)
    sprite('vr_na450_white', 120)


@State
def Ichigekiwhite():

    def upon_IMMEDIATE():
        Unknown2054(1)
        PaletteIndex(2)
        Unknown23015(1)
        ScreenPosition(1)
        FaceLeft()
        XPositionRelativeFacing(-500000)
        AbsoluteY(-384000)
        BlendMode_Normal()
        Unknown3001(0)
        Unknown23013(0)
    sprite('vr_na450_white', 20)
    ConstantAlphaModifier(26)
    sprite('vr_na450_white', 140)
    sprite('vr_na450_white', 20)
    ConstantAlphaModifier(-17)


@State
def Ichigeki_Atk():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        AttackLevel(5)
        Hitstop(60)
        Damage(100000)
        AirHitstunAnimation(AIR_FACE_UP_SKIP)
        GroundedHitstunAnimation(AIR_FACE_UP_SKIP)
        Unknown11064(3)
        Unknown11050(5, '')
        HitAnywhere(1)
        HitLow(99)
        HitOverhead(99)
        HitAirUnblockable(99)
        TeleportToObject(22)
        AddY(55000)
    sprite('dmy_atk00', 4)
    RefreshMultihit()
    sprite('null', 1)


@State
def WinYakkyo():

    def upon_IMMEDIATE():

        def upon_5():
            YAccel(-45)
            XImpulseAcceleration(45)

        def upon_LANDING():
            PrivateSE('na006')
        PaletteIndex(2)
    sprite('vr_trap_yakkyo', 50)
    RandSpeedX(-1750, -3000)
    RandSpeedY(1125, 1625)
    Unknown1078(-5000, -8000)
    setGravity(900)
    sprite('vr_trap_yakkyo', 20)
    BlendMode_Normal()
    ConstantAlphaModifier(-20)


@State
def PersonaMatchWin2():

    def upon_IMMEDIATE():
        callSubroutine('PersonaReset')
        Unknown23022(1)
        Unknown23023()
        Unknown23184(3, 100, -200000, 60000, 0, 0, 0, 0)
        callSubroutine('PNA_CheckWarp')
    sprite('su611_00', 4)
    SetZVal(-500)
    sprite('su611_01', 4)
    sprite('su611_02', 4)
    sprite('su611_03', 4)
    sprite('su611_04', 4)
    SetZVal(500)
    sprite('su611_05', 4)
    sprite('su611_06', 4)
    sprite('su611_07', 4)
    sprite('su611_08', 4)
    SetZVal(-500)
    sprite('su611_09', 4)
    sprite('su611_10', 60)
    physicsXImpulse(40000)
    physicsYImpulse(40000)
    sprite('su611_11', 5)
    SLOT_52 = SLOT_23
    TeleportToObject(3)
    SLOT_23 = SLOT_52
    AddX(-120000)
    AbsoluteY(500000)
    physicsXImpulse(0)
    physicsYImpulse(-20000)
    sprite('su611_12', 5)
    sprite('su611_11', 5)
    sprite('su611_13', 3)
    YAccel(50)
    sprite('su611_14', 3)
    YAccel(50)
    sprite('su611_15', 5)
    YAccel(0)
    sprite('su611_16', 5)
    sprite('su611_17', 5)
    label(0)
    sprite('su611_15', 5)
    sprite('su611_16', 5)
    sprite('su611_17', 5)
    spriteEnd()
    gotoLabel(0)
    enterState('PersonaDeleteAndIdling')


@State
def P4U_Cutin_Parent():

    def upon_IMMEDIATE():
        Unknown2054(1)
    sprite('null', 1)
    GFX_0('P4U_Cutin_Face', 100)


@State
def P4U_Cutin_Face():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Unknown23015(5)
        FaceLeft()
        Unknown4009(2)
        Unknown2054(1)
        ForceBloomMaskOn(0)
        ScreenPosition(1)
        XPositionRelativeFacing(-650000)
        AbsoluteY(-292000)
        Size(1350)
        SetActionMark(0)
        Unknown3001(0)

        def upon_EVERY_FRAME():
            if SLOT_2 == 2:
                AddY(15000)
                Unknown3001(150)
            if SLOT_2 == 3:
                AddY(-30000)
                Unknown3001(180)
            if SLOT_2 == 4:
                AddY(25000)
                Unknown3001(210)
            if SLOT_2 == 5:
                AddY(-20000)
                Unknown3001(255)
            if SLOT_2 == 6:
                AddY(10000)
            AddActionMark(1)
    sprite('vr_99p4u_face00', 45)
    CommonSE('spsys_over_power')
    CommonSE('spsys_over_power')
    if SLOT_168:
        GFX_0('P4U_ka_NotJPN', 100)
    else:
        GFX_0('P4U_ka_JPN', 100)
    sprite('vr_99p4u_face00', 1)
    Unknown3001(180)
    sprite('vr_99p4u_face00', 1)
    Unknown3001(120)
    sprite('vr_99p4u_face00', 1)
    Unknown3001(60)


@State
def P4U_ka_JPN():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Unknown23015(5)
        FaceLeft()
        Unknown4009(2)
        ScreenPosition(1)
        XPositionRelativeFacing(-950000)
        AbsoluteY(-232000)
        Size(1350)
    sprite('vr_p4_ka_mozi', 1)
    Size(100)
    Unknown3001(40)
    sprite('vr_p4_ka_mozi', 1)
    AddX(-2000)
    AddY(500)
    Size(300)
    Unknown3001(70)
    sprite('vr_p4_ka_mozi', 1)
    AddX(-2000)
    AddY(550)
    Size(700)
    Unknown3001(100)
    sprite('vr_p4_ka_mozi', 1)
    AddX(-2000)
    AddY(600)
    Size(900)
    Unknown3001(130)
    sprite('vr_p4_ka_mozi', 1)
    AddX(-2000)
    AddY(6500)
    Size(800)
    Unknown3001(160)
    sprite('vr_p4_ka_mozi', 1)
    AddX(-2000)
    AddY(700)
    Size(900)
    Unknown3001(190)
    sprite('vr_p4_ka_mozi', 1)
    AddX(-2000)
    AddY(800)
    Size(1150)
    Unknown3001(220)
    sprite('vr_p4_ka_mozi', 38)
    AddX(-2000)
    AddY(800)
    Size(1100)
    Unknown3001(255)
    physicsXImpulse(-50)
    physicsYImpulse(50)
    sprite('vr_p4_ka_mozi', 1)
    Unknown3001(180)
    Size(700)
    sprite('vr_p4_ka_mozi', 1)
    Unknown3001(120)
    Size(300)
    sprite('vr_p4_ka_mozi', 1)
    Unknown3001(60)
    Size(100)


@State
def P4U_ka_NotJPN():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Unknown23015(5)
        FaceLeft()
        Unknown4009(2)
        ScreenPosition(1)
        XPositionRelativeFacing(-950000)
        AbsoluteY(-232000)
        Size(1350)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    Size(100)
    Unknown3001(40)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    AddX(-2000)
    AddY(500)
    Size(300)
    Unknown3001(70)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    AddX(-2000)
    AddY(550)
    Size(700)
    Unknown3001(100)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    AddX(-2000)
    AddY(600)
    Size(900)
    Unknown3001(130)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    AddX(-2000)
    AddY(6500)
    Size(800)
    Unknown3001(160)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    AddX(-2000)
    AddY(700)
    Size(900)
    Unknown3001(190)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    AddX(-2000)
    AddY(800)
    Size(1150)
    Unknown3001(220)
    sprite('vr_p4_ka_mozi_notjpn', 38)
    AddX(-2000)
    AddY(800)
    Size(1100)
    Unknown3001(255)
    physicsXImpulse(-50)
    physicsYImpulse(50)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    Unknown3001(180)
    Size(700)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    Unknown3001(120)
    Size(300)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    Unknown3001(60)
    Size(100)
