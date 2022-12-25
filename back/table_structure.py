from factory import get_app

__all__ = [
    'User',
    'MicroViewData',
    'SampleInfo',
    'MicroView',
    'MineContentInfo',
    'MineSurveyInfo',
    'MineXRDInfo',
    'MineChemistryInfo',
    'MineChemistryInfoSingle',
    'MinePhysicsInfo',
    'MineThermalInfo'
]

_, db = get_app(__name__)

# 管理员
class User(db.Model):
    __tablename__ = 'User'

    username = db.Column('username', db.Unicode(40), primary_key=True)  # 用户名
    passwd = db.Column('passwd', db.Unicode(65))                        # 密码

    def __init__(self, username, passwd) -> None:
        self.username = username
        self.passwd = passwd
    
    def to_json(self):
        return {
            'username': self.username,
            'passwd': self.passwd
        }

# 样品基本信息
class SampleInfo(db.Model):
    __tablename__ = 'SampleInfo'

    id = db.Column('id', db.Unicode(30), primary_key=True)      # 样品号
    type = db.Column('type', db.Unicode(30))                    # 样品类型
    source = db.Column('source', db.Unicode(30))                # 样品来源
    year = db.Column('year', db.DATE)                           # 取样年份
    people = db.Column('people', db.Unicode(30))                # 取样人
    imageId = db.Column('imageId', db.JSON)                     # 照片号（多个）
    describe = db.Column('describe', db.UnicodeText)            # 描述
    explain = db.Column('explain', db.UnicodeText)              # 样品制备说明

    def __init__(self, id, type=None, source=None, year=None, people=None, imageId=None, describe=None, explain=None):
        self.id = id
        self.type = type
        self.source = source
        self.year = year
        self.people = people
        self.imageId = imageId
        self.describe = describe
        self.explain = explain

    def to_json(self):
        return {
            'id': self.id,
            'type': self.type,
            'source': self.source,
            'year': self.year,
            'people': self.people,
            'imageId': self.imageId,
            'describe': self.describe,
            'explain': self.explain
        }

# 显微组织观察
class MicroView(db.Model):
    __tablename__ = 'MicroView'

    id = db.Column('id', db.Integer, primary_key=True)              # id
    type = db.Column('type', db.Unicode(30), nullable=False)        # 金相、矿相、电子显微照片
    sampleImage = db.Column('sampleImage', db.JSON)                 # 样品全图
    sampleDescribe = db.Column('sampleDescribe', db.UnicodeText)    # 描述
    device = db.Column('device', db.Unicode(100))                   # 设备

    sampleId = db.Column('sampleId', db.Unicode(30), db.ForeignKey('SampleInfo.id'))    # 样品id（外键）
    sampleInfo = db.relationship('SampleInfo', backref=db.backref('microViews'))

    def __init__(self, id=None, type=None, sampleImage=None, sampleDescribe=None, device=None, sampleId=None):
        self.id = id
        self.type = type
        self.sampleImage = sampleImage
        self.sampleDescribe = sampleDescribe
        self.device = device
        self.sampleId = sampleId

    def to_json(self):
        return {
            'id': self.id,
            'type': self.type,
            'sampleImage': self.sampleImage,
            'sampleDescribe': self.sampleDescribe,
            'device': self.device,
            'sampleId': self.sampleId,
            'imageData': [v.to_json() for v in self.imageData] if hasattr(self, 'imageData') else []
        }
    
# 显微 照片数据
class MicroViewData(db.Model):
    __tablename__ = 'MicroViewData'

    id = db.Column('id', db.Integer, primary_key=True)
    zoom = db.Column('zoom', db.Float)                  # 放大倍数
    image = db.Column('image', db.Unicode(50))          # 图片
    photoMode = db.Column('photoMode', db.Unicode(30))  # 拍摄模式
    describe = db.Column('describe', db.UnicodeText)    # 描述

    microId = db.Column('microId', db.Integer, db.ForeignKey('MicroView.id'))   # micro id 外键
    microView = db.relationship('MicroView', backref=db.backref('imageData'))

    def __init__(self, id=None, zoom=None, image=None, photoMode=None, describe=None, microId=None):
        self.id = id
        self.zoom = zoom
        self.image = image
        self.photoMode = photoMode
        self.describe = describe
        self.microId = microId
    
    def to_json(self):
        return {
            'id': self.id,
            'zoom': self.zoom,
            'image': self.image,
            'photoMode': self.photoMode,
            'describe': self.describe,
            'microId': self.microId
        }

# 矿物含量信息
class MineContentInfo(db.Model):
    __tablename__ = 'MineContentInfo'

    id = db.Column('id', db.Unicode(30), primary_key=True)  # 样品号
    clay = db.Column('clay', db.Float)                      # 粘土
    quartz = db.Column('quartz', db.Float)                  # 粉砂
    sand_quartz = db.Column('sand_quartz', db.Float)        # 砂-石英
    sand_feldspar = db.Column('sand_feldspar', db.Float)    # 砂-长石
    sand_other = db.Column('sand_other', db.Float)          # 砂-其他矿物
    debris = db.Column('debris', db.Float)                  # 岩屑
    hollow_close = db.Column('hollow_close', db.Float)      # 空洞-闭气孔
    hollow_open = db.Column('hollow_open', db.Float)        # 空洞-开气孔
    hollow_through = db.Column('hollow_through', db.Float)  # 空洞-贯通气孔

    def __init__(self, id=None, clay=None, quartz=None, sand_quartz=None, sand_feldspar=None, sand_other=None, debris=None, hollow_close=None, hollow_open=None, hollow_through=None):
        self.id = id
        self.clay = clay
        self.quartz = quartz
        self.sand_quartz = sand_quartz
        self.sand_feldspar = sand_feldspar
        self.sand_other = sand_other
        self.debris = debris
        self.hollow_close = hollow_close
        self.hollow_open = hollow_open
        self.hollow_through = hollow_through

    def to_json(self):
        return {
            'id': self.id,
            'clay': self.clay,
            'quartz': self.quartz,
            'sand_quartz': self.sand_quartz,
            'sand_feldspar': self.sand_feldspar,
            'sand_other': self.sand_other,
            'debris': self.debris,
            'hollow_close': self.hollow_close,
            'hollow_open': self.hollow_open,
            'hollow_through': self.hollow_through
        }

# 矿物测量数据
class MineSurveyInfo(db.Model):
    __tablename__ = 'MineSurveyInfo'

    id = db.Column('id', db.Unicode(30), primary_key=True)  # 样品号
    debris_0um = db.Column('debris_0um', db.Float)          # 岩屑直径≤67μm
    debris_67um = db.Column('debris_67um', db.Float)        # 岩屑直径67-167μm
    debris_167um = db.Column('debris_167um', db.Float)      # 岩屑直径167-501μm
    debris_501um = db.Column('debris_501um', db.Float)      # 岩屑直径501-1002μm
    debris_1002um = db.Column('debris_1002um', db.Float)    # 岩屑直径≥1002μm
    hollow_0um = db.Column('hollow_0um', db.Float)          # 空洞长度≤67μm
    hollow_67um = db.Column('hollow_67um', db.Float)        # 空洞长度67-501μm
    hollow_501um = db.Column('hollow_501um', db.Float)      # 空洞长度501-1002μm
    hollow_1002um = db.Column('hollow_1002um', db.Float)    # 空洞长度1002-2004μm
    hollow_2004um = db.Column('hollow_2004um', db.Float)    # 空洞长度≥2004μm

    def __init__(self, id=None, debris_0um=None, debris_67um=None, debris_167um=None, debris_501um=None, debris_1002um=None, hollow_0um=None, hollow_67um=None, hollow_501um=None, hollow_1002um=None, hollow_2004um=None):
        self.id = id
        self.debris_0um = debris_0um
        self.debris_67um = debris_67um
        self.debris_167um = debris_167um
        self.debris_501um = debris_501um
        self.debris_1002um = debris_1002um
        self.hollow_0um = hollow_0um
        self.hollow_67um = hollow_67um
        self.hollow_501um = hollow_501um
        self.hollow_1002um = hollow_1002um
        self.hollow_2004um = hollow_2004um

    def to_json(self):
        return {
            'id': self.id,
            'debris_0um': self.debris_0um,
            'debris_67um': self.debris_67um,
            'debris_167um': self.debris_167um,
            'debris_501um': self.debris_501um,
            'debris_1002um': self.debris_1002um,
            'hollow_0um': self.hollow_0um,
            'hollow_67um': self.hollow_67um,
            'hollow_501um': self.hollow_501um,
            'hollow_1002um': self.hollow_1002um,
            'hollow_2004um': self.hollow_2004um
        }

# XRD分析数据
class MineXRDInfo(db.Model):
    __tablename__ = 'MineXRDInfo'

    id = db.Column('id', db.Unicode(30), primary_key=True)  # 样品编号
    type = db.Column('type', db.Unicode(40))                # 类型
    quartz = db.Column('quartz', db.Float)                  # 石英
    albite = db.Column('albite', db.Float)                  # 钠长石
    potashFeldspar = db.Column('potashFeldspar', db.Float)  # 钾长石
    mica = db.Column('mica', db.Float)                      # 云母
    amphibole = db.Column('amphibole', db.Float)            # 闪石
    hematite = db.Column('hematite', db.Float)              # 赤铁矿
    magnetite = db.Column('magnetite', db.Float)            # 磁铁矿
    dolomite = db.Column('dolomite', db.Float)              # 白云石
    analcite = db.Column('analcite', db.Float)              # 方沸石
    tridymite = db.Column('tridymite', db.Float)            # 磷石英
    cristobalite = db.Column('cristobalite', db.Float)      # 方石英
    mullite = db.Column('mullite', db.Float)                # 莫来石
    other = db.Column('other', db.Float)                    # 其他

    def __init__(self, id=None, type=None, quartz=None, albite=None, potashFeldspar=None, mica=None, amphibole=None, hematite=None, magnetite=None, dolomite=None, analcite=None, tridymite=None, cristobalite=None, mullite=None, other=None):
        self.id = id
        self.type = type
        self.quartz = quartz
        self.albite = albite
        self.potashFeldspar = potashFeldspar
        self.mica = mica
        self.amphibole = amphibole
        self.hematite = hematite
        self.magnetite = magnetite
        self.dolomite = dolomite
        self.analcite = analcite
        self.tridymite = tridymite
        self.cristobalite = cristobalite
        self.mullite = mullite
        self.other = other

    def to_json(self):
        return {
            'id': self.id,
            'type': self.type,
            'quartz': self.quartz,
            'albite': self.albite,
            'potashFeldspar': self.potashFeldspar,
            'mica': self.mica,
            'amphibole': self.amphibole,
            'hematite': self.hematite,
            'magnetite': self.magnetite,
            'dolomite': self.dolomite,
            'analcite': self.analcite,
            'tridymite': self.tridymite,
            'cristobalite': self.cristobalite,
            'mullite': self.mullite,
            'other': self.other
        }

# 化学成分数据（氧化物）
class MineChemistryInfo(db.Model):
    __tablename__ = 'MineChemistryInfo'

    id = db.Column('id', db.Unicode(30), primary_key=True)  # 样品号
    Na2O = db.Column('Na2O', db.Float)                      # Na₂O
    MgO = db.Column('MgO', db.Float)                        # MgO
    Al2O3 = db.Column('Al2O3', db.Float)                    # Al₂O₃
    SiO2 = db.Column('SiO2', db.Float)                      # SiO₂
    P2O5 = db.Column('P2O5', db.Float)                      # P₂O₅
    SO2 = db.Column('SO2', db.Float)                        # SO₂
    K2O = db.Column('K2O', db.Float)                        # K₂O
    CaO = db.Column('CaO', db.Float)                        # CaO
    TiO2 = db.Column('TiO2', db.Float)                      # TiO₂
    MnO = db.Column('MnO', db.Float)                        # MnO
    FeO = db.Column('FeO', db.Float)                        # FeO
    CuO = db.Column('CuO', db.Float)                        # CuO
    ZnO = db.Column('ZnO', db.Float)                        # ZnO
    As2O3 = db.Column('As2O3', db.Float)                    # As₂O₃
    SnO2 = db.Column('SnO2', db.Float)                      # SnO₂
    PbO = db.Column('PbO', db.Float)                        # PbO
    other = db.Column('other', db.Float)                    # 其他

    def __init__(self, id=None, Na2O=None, MgO=None, Al2O3=None, SiO2=None, P2O5=None, SO2=None, K2O=None, CaO=None, TiO2=None, MnO=None, FeO=None, CuO=None, ZnO=None, As2O3=None, SnO2=None, PbO=None, other=None):
        self.id = id
        self.Na2O = Na2O
        self.MgO = MgO
        self.Al2O3 = Al2O3
        self.SiO2 = SiO2
        self.P2O5 = P2O5
        self.SO2 = SO2
        self.K2O = K2O
        self.CaO = CaO
        self.TiO2 = TiO2
        self.MnO = MnO
        self.FeO = FeO
        self.CuO = CuO
        self.ZnO = ZnO
        self.As2O3 = As2O3
        self.SnO2 = SnO2
        self.PbO = PbO
        self.other = other
    
    def to_json(self):
        return {
            'id': self.id,
            'Na2O': self.Na2O,
            'MgO': self.MgO,
            'Al2O3': self.Al2O3,
            'SiO2': self.SiO2,
            'P2O5': self.P2O5,
            'SO2': self.SO2,
            'K2O': self.K2O,
            'CaO': self.CaO,
            'TiO2': self.TiO2,
            'MnO': self.MnO,
            'FeO': self.FeO,
            'CuO': self.CuO,
            'ZnO': self.ZnO,
            'As2O3': self.As2O3,
            'SnO2': self.SnO2,
            'PbO': self.PbO,
            'other': self.other
        }

# 化学成分数据（单质）
class MineChemistryInfoSingle(db.Model):
    __tablename__ = 'MineChemistryInfoSingle'

    id = db.Column('id', db.Unicode(30), primary_key=True)  # 样品号
    C = db.Column('C', db.Float)
    Na = db.Column('Na', db.Float)
    Mg = db.Column('Mg', db.Float)
    Al = db.Column('Al', db.Float)
    Si = db.Column('Si', db.Float)
    P = db.Column('P', db.Float)
    S = db.Column('S', db.Float)
    Cl = db.Column('Cl', db.Float)
    K = db.Column('K', db.Float)
    Ca = db.Column('Ca', db.Float)
    Ti = db.Column('Ti', db.Float)
    V = db.Column('V', db.Float)
    Mn = db.Column('Mn', db.Float)
    Fe = db.Column('Fe', db.Float)
    Co = db.Column('Co', db.Float)
    Ni = db.Column('Ni', db.Float)
    Cu = db.Column('Cu', db.Float)
    Zn = db.Column('Zn', db.Float)
    As = db.Column('As', db.Float)
    Ag = db.Column('Ag', db.Float)
    Sn = db.Column('Sn', db.Float)
    Sb = db.Column('Sb', db.Float)
    Au = db.Column('Au', db.Float)
    Hg = db.Column('Hg', db.Float)
    Pb = db.Column('Pb', db.Float)
    other = db.Column('other', db.Float)                    # 其他

    def __init__(self, id=None, C=None, Na=None, Mg=None, Al=None, Si=None, P=None, S=None, Cl=None, K=None, Ca=None, Ti=None, V=None, Mn=None, Fe=None, Co=None, Ni=None, Cu=None, Zn=None, As=None, Ag=None, Sn=None, Sb=None, Au=None, Hg=None, Pb=None, other=None):
        self.id = id
        self.C = C
        self.Na = Na
        self.Mg = Mg
        self.Al = Al
        self.Si = Si
        self.P = P
        self.S = S
        self.Cl = Cl
        self.K = K
        self.Ca = Ca
        self.Ti = Ti
        self.V = V
        self.Mn = Mn
        self.Fe = Fe
        self.Co = Co
        self.Ni = Ni
        self.Cu = Cu
        self.Zn = Zn
        self.As = As
        self.Ag = Ag
        self.Sn = Sn
        self.Sb = Sb
        self.Au = Au
        self.Hg = Hg
        self.Pb = Pb
        self.other = other
    
    def to_json(self):
        return {
            'id': self.id,
            'C': self.C,
            'Na': self.Na,
            'Mg': self.Mg,
            'Al': self.Al,
            'Si': self.Si,
            'P': self.P,
            'S': self.S,
            'Cl': self.Cl,
            'K': self.K,
            'Ca': self.Ca,
            'Ti': self.Ti,
            'V': self.V,
            'Mn': self.Mn,
            'Fe': self.Fe,
            'Co': self.Co,
            'Ni': self.Ni,
            'Cu': self.Cu,
            'Zn': self.Zn,
            'As': self.As,
            'Ag': self.Ag,
            'Sn': self.Sn,
            'Sb': self.Sb,
            'Au': self.Au,
            'Hg': self.Hg,
            'Pb': self.Pb,
            'other': self.other
        }

# 物理性能数据
class MinePhysicsInfo(db.Model):
    __tablename__ = 'MinePhysicsInfo'

    id = db.Column('id', db.Unicode(30), primary_key=True)      # 样品号
    type = db.Column('type', db.Unicode(40))                    # 类型
    trueDensity = db.Column('trueDensity', db.Float)            # 密度
    apparentPorosity = db.Column('apparentPorosity', db.Float)  # 气孔率
    waterAbsorption = db.Column('waterAbsorption', db.Float)    # 吸水率
    bending = db.Column('bending', db.Float)                    # 高温抗折强度
    resistance = db.Column('resistance', db.Float)              # 热震稳定性系数
    slag = db.Column('slag', db.Float)                          # 抗渣性系数
    alkali = db.Column('alkali', db.Float)                      # 耐碱性系数
    refractoriness = db.Column('refractoriness', db.Float)      # 荷重软化温度
    heat = db.Column('heat', db.Float)                          # 导热系数

    def __init__(self, id=None, type=None, trueDensity=None, apparentPorosity=None, waterAbsorption=None, bending=None, resistance=None, slag=None, alkali=None, refractoriness=None, heat=None):
        self.id = id
        self.type = type
        self.trueDensity = trueDensity
        self.apparentPorosity = apparentPorosity
        self.waterAbsorption = waterAbsorption
        self.bending = bending
        self.resistance = resistance
        self.slag = slag
        self.alkali = alkali
        self.refractoriness = refractoriness
        self.heat = heat
    
    def to_json(self):
        return {
            'id': self.id,
            'type': self.type,
            'trueDensity': self.trueDensity,
            'apparentPorosity': self.apparentPorosity,
            'waterAbsorption': self.waterAbsorption,
            'bending': self.bending,
            'resistance': self.resistance,
            'slag': self.slag,
            'alkali': self.alkali,
            'refractoriness': self.refractoriness,
            'heat': self.heat
        }

# 热分析
class MineThermalInfo(db.Model):
    __tablename__ = 'MineThermalInfo'

    id = db.Column('id', db.Unicode(30), primary_key=True)  # 样品号
    melting = db.Column('melting', db.Float)                # 熔点
    fireResis = db.Column('fireResis', db.Float)            # 耐火度
    termTemper = db.Column('termTemper', db.Float)          # 烧成温度
    data = db.Column('data', db.Unicode(100))               # 原始数据
    surveImage = db.Column('surveImage', db.Unicode(100))   # 曲线图

    def __init__(self, id=None, melting=None, fireResis=None, termTemper=None, data=None, surveImage=None):
        self.id = id
        self.melting = melting
        self.fireResis = fireResis
        self.termTemper = termTemper
        self.data = data
        self.surveImage = surveImage
    
    def to_json(self):
        return {
            'id': self.id,
            'melting': self.melting,
            'fireResis': self.fireResis,
            'termTemper': self.termTemper,
            'data': self.data,
            'surveImage': self.surveImage
        }
