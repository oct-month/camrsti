import json
from typing import List, Optional
from flask import request

from utils import get_app
from table_structure import MicroViewData, SampleInfo, MicroView, MineContentInfo, MineSurveyInfo, MineXRDInfo, MineChemistryInfo, MinePhysicsInfo, MineThermalInfo


app, db = get_app(__name__)


# 系统异常
@app.errorhandler(Exception)
def all_exception_handler(e):
    return {
        'status': 500,
        'msg': str(e)
    }

# 404错误
@app.errorhandler(404)
def error_404(e):
    print(e)
    return {
        'status': 404,
        'msg': 'Not Found'
    }

# 获取样本信息
@app.route('/api/sampleinfo', methods=['GET'])
def get_sampleinfos():
    sample_infos = SampleInfo.query.all()
    return {
        'status': 200,
        'data': [s.to_json() for s in sample_infos]
    }

def get_sampleinfo_dao(sampleId) -> SampleInfo:
    return SampleInfo.query.filter_by(id=sampleId).first()

# 获取特定样本信息
@app.route('/api/sampleinfo/<sampleId>', methods=['GET'])
def get_sampleinfo(sampleId):
    sample_info = get_sampleinfo_dao(sampleId)
    return {
        'status': 200,
        'data': sample_info.to_json() if sample_info is not None else None
    }

# 删除特定样本信息
@app.route('/api/sampleinfo/<sampleId>', methods=['DELETE'])
def delete_sampleinfo(sampleId):
    db.session.delete(get_sampleinfo_dao(sampleId))
    db.session.commit()
    return {
        'status': 200
    }

# 更改特定样本信息
@app.route('/api/sampleinfo', methods=['PUT'])
def modify_sampleinfo():
    sampleInfo_json = json.loads(request.data)
    sampleId = sampleInfo_json.get('id')
    sampleInfo = get_sampleinfo_dao(sampleId)
    sampleInfo.type = sampleInfo_json.get('type', sampleInfo.type)
    sampleInfo.source = sampleInfo_json.get('source', sampleInfo.source)
    sampleInfo.year = sampleInfo_json.get('year', sampleInfo.year)
    sampleInfo.people = sampleInfo_json.get('people', sampleInfo.people)
    sampleInfo.imageId = sampleInfo_json.get('imageId', sampleInfo.imageId)
    sampleInfo.describe = sampleInfo_json.get('describe', sampleInfo.describe)
    sampleInfo.explain = sampleInfo_json.get('explain', sampleInfo.explain)
    db.session.commit()
    return {
        'status': 200
    }

# 增加样本信息
@app.route('/api/sampleinfo', methods=['POST'])
def add_sampleinfo():
    sampleInfo_json = json.loads(request.data)
    sampleId = sampleInfo_json.get('id')
    sampleInfo = get_sampleinfo_dao(sampleId)
    if (sampleInfo):
        return {
            'status': 400,
            'msg': '样本已存在'
        }
    else:
        instance = SampleInfo(
            id=sampleInfo_json.get('id'),
            type=sampleInfo_json.get('type'),
            source=sampleInfo_json.get('source'),
            year=sampleInfo_json.get('year'),
            people=sampleInfo_json.get('people'),
            imageId=sampleInfo_json.get('imageId'),
            describe=sampleInfo_json.get('describe'),
            explain=sampleInfo_json.get('explain'),
            experimentId=sampleInfo_json.get('experimentId')
        )
        db.session.add(instance)
        db.session.commit()
        return {
            'status': 200
        }

def get_microviews_dao(sampleId) -> List[MicroView]:
    sampleInfo = get_sampleinfo_dao(sampleId)
    if sampleInfo:
        micro_views = sampleInfo.microViews
    else:
        micro_views = []
    return micro_views

def get_microview_dao(sampleId, type_) -> Optional[MicroView]:
    micro_view = MicroView.query.filter_by(sampleId=sampleId, type=type_).first()
    return micro_view

# 获取特定样本的显微观察信息
@app.route('/api/microview/<sampleId>', methods=['GET'])
def get_microviews(sampleId):
    micro_views = get_microviews_dao(sampleId)
    return {
        'status': 200,
        'data': [s.to_json() for s in micro_views]
    }

# 设置特定样本的显微数据
@app.route('/api/microview', methods=['PUT'])
def set_microview():
    micro_json = json.loads(request.data)
    sampleId = micro_json.get('sampleId')
    type_ = micro_json.get('type')
    micro_view = get_microview_dao(sampleId, type_)
    id_opt = None
    if micro_view:
        micro_view.sampleImage = micro_json.get('sampleImage', micro_view.sampleImage)
        micro_view.sampleDescribe = micro_json.get('sampleDescribe', micro_view.sampleDescribe)
        micro_view.device = micro_json.get('device', micro_view.device)
        db.session.commit()
    else:
        instance = MicroView(
            type=micro_json.get('type'),
            sampleImage=micro_json.get('sampleImage'),
            sampleDescribe=micro_json.get('sampleDescribe'),
            device=micro_json.get('device'),
            sampleId=micro_json.get('sampleId')
        )
        db.session.add(instance)
        db.session.flush()
        id_opt = instance.id
        db.session.commit()
    return {
        'status': 200,
        'id': id_opt
    }

# 增加特定显微数据的条目
@app.route('/api/microview/<microId>', methods=['POST'])
def add_microview_item(microId):
    image_data_json = json.loads(request.data)
    instance = MicroViewData(
        zoom=image_data_json.get('zoom'),
        image=image_data_json.get('image'),
        photoMode=image_data_json.get('photoMode'),
        describe=image_data_json.get('describe'),
        microId=microId
    )
    db.session.add(instance)
    db.session.flush()
    db.session.commit()
    return {
        'status': 200,
        'id': instance.id
    }

# 修改特定显微数据的条目
@app.route('/api/microview/<id>', methods=['PUT'])
def set_microview_item(id):
    imD_json = json.loads(request.data)
    imD = MicroViewData.query.filter_by(id=id).first()
    imD.zoom = imD_json.get('zoom', imD.zoom)
    imD.image = imD_json.get('image', imD.image)
    imD.photoMode = imD_json.get('photoMode', imD.photoMode)
    imD.describe = imD_json.get('describe', imD.describe)
    db.session.commit()
    return {
        'status': 200
    }

# 删除特定显微数据的条目
@app.route('/api/microview/<id>', methods=['DELETE'])
def delete_microview_item(id):
    imD = MicroViewData.query.filter_by(id=id).first()
    db.session.delete(imD)
    db.session.commit()
    return {
        'status': 200
    }

# 获取特定样本的矿物含量信息
@app.route('/api/minecontentinfo/<sampleId>', methods=['GET'])
def get_mine_content_infos(sampleId):
    experimentIds = get_sampleinfo_dao(sampleId).experimentId
    content_infos = MineContentInfo.query.filter(MineContentInfo.id.in_(experimentIds)).all()
    return {
        'status': 200,
        'data': [s.to_json() for s in content_infos]
    }

# 获取特定样本的矿物测量数据
@app.route('/api/minesurveyinfo/<sampleId>', methods=['GET'])
def get_mine_survey_infos(sampleId):
    experimentIds = get_sampleinfo_dao(sampleId).experimentId
    survey_infos = MineSurveyInfo.query.filter(MineSurveyInfo.id.in_(experimentIds)).all()
    return {
        'status': 200,
        'data': [s.to_json() for s in survey_infos]
    }

# 获取特定样本的XRD分析数据
@app.route('/api/minexrdinfo/<sampleId>', methods=['GET'])
def get_mine_xrd_infos(sampleId):
    experimentIds = get_sampleinfo_dao(sampleId).experimentId
    xrd_infos = MineXRDInfo.query.filter(MineXRDInfo.id.in_(experimentIds)).all()
    return {
        'status': 200,
        'data': [s.to_json() for s in xrd_infos]
    }

# 获取特定样本的化学成分数据
@app.route('/api/minechemistryinfo/<sampleId>', methods=['GET'])
def get_mine_chemistry_infos(sampleId):
    experimentIds = get_sampleinfo_dao(sampleId).experimentId
    chem_infos = MineChemistryInfo.query.filter(MineChemistryInfo.id.in_(experimentIds)).all()
    return {
        'status': 200,
        'data': [s.to_json() for s in chem_infos]
    }

# 获取特定样本的物理结构数据
@app.route('/api/minephysicsinfo/<sampleId>', methods=['GET'])
def get_mine_physics_info(sampleId):
    physics_info = MinePhysicsInfo.query.filter_by(id=sampleId).first()
    return {
        'status': 200,
        'data': physics_info.to_json() if physics_info is not None else None
    }

# 修改特定样本的物理结构数据
@app.route('/api/minephysicsinfo', methods=['PUT'])
def set_mine_physics_info():
    phy_info_json = json.loads(request.data)
    physics_info = MinePhysicsInfo.query.filter_by(id=phy_info_json.get('id')).first()
    if physics_info:
        physics_info.type = phy_info_json.get('type', physics_info.type)
        physics_info.apparentPorosity = phy_info_json.get('apparentPorosity', physics_info.apparentPorosity)
        physics_info.trueDensity = phy_info_json.get('trueDensity', physics_info.trueDensity)
        physics_info.waterAbsorption = phy_info_json.get('waterAbsorption', physics_info.waterAbsorption)
        db.session.commit()
    else:
        instance = MinePhysicsInfo(
            id=phy_info_json.get('id'), 
            type=phy_info_json.get('type'),
            apparentPorosity=phy_info_json.get('apparentPorosity'),
            trueDensity=phy_info_json.get('trueDensity'),
            waterAbsorption=phy_info_json.get('waterAbsorption'),
        )
        db.session.add(instance)
        db.session.commit()
    return {
        'status': 200
    }

# 获取特定样本的热分析
@app.route('/api/minethermalinfo/<sampleId>', methods=['GET'])
def get_mine_thermal_infos(sampleId):
    experimentIds = get_sampleinfo_dao(sampleId).experimentId
    thermal_infos = MineThermalInfo.query.filter(MineThermalInfo.id.in_(experimentIds)).all()
    return {
        'status': 200,
        'data': [s.to_json() for s in thermal_infos]
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
