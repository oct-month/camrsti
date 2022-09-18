from factory import get_app


_, db = get_app(__name__)

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
    experimentId = db.Column('experimentId', db.JSON)           # 实验编号（多个）

    def __init__(self, id, type=None, source=None, year=None, people=None, imageId=None, describe=None, explain=None, experimentId=None):
        self.id = id
        self.type = type
        self.source = source
        self.year = year
        self.people = people
        self.imageId = imageId
        self.describe = describe
        self.explain = explain
        self.experimentId = experimentId

    def to_json(self):
        return {
            'id': self.id,
            'type': self.type,
            'source': self.source,
            'year': self.year,
            'people': self.people,
            'imageId': self.imageId,
            'describe': self.describe,
            'explain': self.explain,
            'experimentId': self.experimentId
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
    sampleName = db.Column('sampleName', db.Unicode(50))    # 样品名称
    clay = db.Column('clay', db.Float)                      # 粘土基质
    quartz = db.Column('quartz', db.Float)                  # 石英粉砂
    sand = db.Column('sand', db.JSON)                       # 砂
    debris = db.Column('debris', db.Float)                  # 岩屑
    hollow = db.Column('hollow', db.Float)                  # 空洞
    other = db.Column('other', db.Float)                    # 其他

    def __init__(self, id, sampleName=None, clay=None, quartz=None, sand=None, debris=None, hollow=None, other=None):
        self.id = id
        self.sampleName = sampleName
        self.clay = clay
        self.quartz = quartz
        self.sand = sand
        self.debris = debris
        self.hollow = hollow
        self.other = other

    def to_json(self):
        return {
            'id': self.id,
            'sampleName': self.sampleName,
            'clay': self.clay,
            'quartz': self.quartz,
            'sand': self.sand,
            'debris': self.debris,
            'hollow': self.hollow,
            'other': self.other
        }

# 矿物测量数据
class MineSurveyInfo(db.Model):
    __tablename__ = 'MineSurveyInfo'

    id = db.Column('id', db.Unicode(30), primary_key=True)  # 样品号
    debrisData = db.Column('debrisData', db.JSON)           # 岩屑直径分布
    hollowData = db.Column('hollowData', db.JSON)           # 空洞长度分布

    def __init__(self, id, debrisData=None, hollowData=None):
        self.id = id
        self.debrisData = debrisData
        self.hollowData = hollowData

    def to_json(self):
        return {
            'id': self.id,
            'debrisData': self.debrisData,
            'hollowData': self.hollowData
        }

# XRD分析数据
class MineXRDInfo(db.Model):
    __tablename__ = 'MineXRDInfo'

    id = db.Column('id', db.Unicode(30), primary_key=True)  # 样品号
    type = db.Column('type', db.Unicode(40))                # 类型
    quartz = db.Column('quartz', db.Float)                # 石英
    albite = db.Column('albite', db.Float)                # 钠长石
    potashFeldspar = db.Column('potashFeldspar', db.Float)    # 钾长石
    mica = db.Column('mica', db.Float)                    # 云母
    amphibole = db.Column('amphibole', db.Float)          # 闪石
    hematite = db.Column('hematite', db.Float)            # 赤铁矿
    magnetite = db.Column('magnetite', db.Float)          # 磁铁矿
    dolomite = db.Column('dolomite', db.Float)            # 白云石
    analcite = db.Column('analcite', db.Float)            # 方沸石
    tridymite = db.Column('tridymite', db.Float)          # 磷石英
    cristobalite = db.Column('cristobalite', db.Float)    # 方石英
    mullite = db.Column('mullite', db.Float)              # 莫来石

    def __init__(self, id, type=None, quartz=None, albite=None, potashFeldspar=None, mica=None, amphibole=None, hematite=None, magnetite=None, dolomite=None, analcite=None, tridymite=None, cristobalite=None, mullite=None):
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
            'mullite': self.mullite
        }

# 化学成分数据
class MineChemistryInfo(db.Model):
    __tablename__ = 'MineChemistryInfo'

    id = db.Column('id', db.Unicode(30), primary_key=True)  # 样品号
    type = db.Column('type', db.Unicode(40))                # 类型
    Na2O = db.Column('Na2O', db.Float)
    MgO = db.Column('MgO', db.Float)
    Al2O3 = db.Column('Al2O3', db.Float)
    SiO2 = db.Column('SiO2', db.Float)
    K2O = db.Column('K2O', db.Float)
    CaO = db.Column('CaO', db.Float)
    Fe2O3 = db.Column('Fe2O3', db.Float)

    def __init__(self, id, type=None, Na2O=None, MgO=None, Al2O3=None, SiO2=None, K2O=None, CaO=None, Fe2O3=None):
        self.id = id
        self.type = type
        self.Na2O = Na2O
        self.MgO = MgO
        self.Al2O3 = Al2O3
        self.SiO2 = SiO2
        self.K2O = K2O
        self.CaO = CaO
        self.Fe2O3 = Fe2O3
    
    def to_json(self):
        return {
            'id': self.id,
            'type': self.type,
            'Na2O': self.Na2O,
            'MgO': self.MgO,
            'Al2O3': self.Al2O3,
            'SiO2': self.SiO2,
            'K2O': self.K2O,
            'CaO': self.CaO,
            'Fe2O3': self.Fe2O3
        }

# 物理结构数据
class MinePhysicsInfo(db.Model):
    __tablename__ = 'MinePhysicsInfo'

    id = db.Column('id', db.Unicode(30), primary_key=True)      # 样品号
    type = db.Column('type', db.Unicode(40))                    # 类型
    apparentPorosity = db.Column('apparentPorosity', db.Float) # 显气孔率
    trueDensity = db.Column('trueDensity', db.Float)           # 真密度
    waterAbsorption = db.Column('waterAbsorption', db.Float)   # 吸水率

    def __init__(self, id, type=None, apparentPorosity=None, trueDensity=None, waterAbsorption=None):
        self.id = id
        self.type = type
        self.apparentPorosity = apparentPorosity
        self.trueDensity = trueDensity
        self.waterAbsorption = waterAbsorption
    
    def to_json(self):
        return {
            'id': self.id,
            'type': self.type,
            'apparentPorosity': self.apparentPorosity,
            'trueDensity': self.trueDensity,
            'waterAbsorption': self.waterAbsorption
        }

# 热分析
class MineThermalInfo(db.Model):
    __tablename__ = 'MineThermalInfo'

    id = db.Column('id', db.Unicode(30), primary_key=True)   # 样品号
    termTemper = db.Column('termTemper', db.Float)         # 终止温度
    fireResis = db.Column('fireResis', db.Float)           # 耐火度
    data = db.Column('data', db.JSON)                       # 热分析数据
    surveImage = db.Column('surveImage', db.Unicode(100))   # 热分析曲线

    def __init__(self, id, termTemper=None, fireResis=None, data=None, surveImage=None):
        self.id = id
        self.termTemper = termTemper
        self.fireResis = fireResis
        self.data = data
        self.surveImage = surveImage
    
    def to_json(self):
        return {
            'id': self.id,
            'termTemper': self.termTemper,
            'fireResis': self.fireResis,
            'data': self.data,
            'surveImage': self.surveImage
        }
