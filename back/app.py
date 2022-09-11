import json
from flask import request

from utils import get_app
from table_structure import SampleInfo, MicroView, MineContentInfo, MineSurveyInfo, MineXRDInfo, MineChemistryInfo, MinePhysicsInfo, MineThermalInfo


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
    sampleId = sampleInfo_json['id']
    sampleInfo = get_sampleinfo_dao(sampleId)
    sampleInfo.type = sampleInfo_json['type']
    sampleInfo.source = sampleInfo_json['source']
    sampleInfo.year = sampleInfo_json['year']
    sampleInfo.people = sampleInfo_json['people']
    sampleInfo.imageId = sampleInfo_json['imageId']
    sampleInfo.describe = sampleInfo_json['describe']
    sampleInfo.explain = sampleInfo_json['explain']
    db.session.commit()
    return {
        'status': 200
    }

# 获取特定样本的显微观察信息
@app.route('/api/microview/<sampleId>', methods=['GET'])
def get_microviews(sampleId):
    micro_views = MicroView.query.filter_by(sampleId=sampleId).all()
    return {
        'status': 200,
        'data': [s.to_json() for s in micro_views]
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

# 获取特定样本的热分析
@app.route('/api/minethermalinfo/<sampleId>', methods=['GET'])
def get_mine_thermal_infos(sampleId):
    experimentIds = get_sampleinfo_dao(sampleId).experimentId
    thermal_infos = MineThermalInfo.query.filter(MineThermalInfo.id.in_(experimentIds)).all()
    return {
        'status': 200,
        'data': [s.to_json() for s in thermal_infos]
    }

# @app.route('/api/request/base', methods=['GET'])
# def get_base():  # put application's code here
#     examples = Example.query.all()
#     t = {str(i): examples[i].to_json() for i in range(len(examples))}
#     t["length"] = str(len(examples))
#     return t


# @app.route('/api/request/phase/<sampleId>', methods=['GET'])
# def get_oom(sampleId):
#     base_data = Example.query.filter_by(sampleId=sampleId).first()
#     metal_phase = MetalPhase.query.filter_by(sampleId=sampleId).first()
#     mine_phase = MinePhase.query.filter_by(sampleId=sampleId).first()
#     em_phase = ElectronMicroPhase.query.filter_by(sampleId=sampleId).first()
#     physical_porosity = PhysicalPorosity.query.filter_by(sampleId=sampleId).first()
#     t = {'metalPhaseData': metal_phase.to_json(),
#          'minePhaseData': mine_phase.to_json(),
#          'emPhaseData': em_phase.to_json(),
#          'physicalPorosity': physical_porosity.to_json(),
#          'baseData': base_data.to_json()
#          }
#     return t


# @app.route('/api/request/experiment/<sampleId>', methods=['GET'])
# def get_experiment(sampleId):
#     t = {}
#     experiment_data_all = ExperimentData.query.filter_by(sampleId=sampleId).all()
#     for experiment_data in experiment_data_all:
#         data = experiment_data.to_json()
#         data['mineralContent'][u'实验编号'] = experiment_data.experimentId
#         data['XRDContent'][u'实验编号'] = experiment_data.experimentId
#         data['chemicalContent'][u'实验编号'] = experiment_data.experimentId
#         data['thermalPerform'][u'实验编号'] = experiment_data.experimentId
#         data['diameterDisplay'][u'实验编号'] = experiment_data.experimentId
#         data['cavityDisplay'][u'实验编号'] = experiment_data.experimentId
#         t[experiment_data.experimentId] = data
#     return t


# @app.route('/api/request/graphic/<imageIndex>', methods=['GET'])
# def get_graphic(imageIndex):
#     graphic_data = PhaseGraphic.query.filter_by(imageIndex=imageIndex).first()
#     t = {
#         'imageIndex': graphic_data.imageIndex,
#         'omDescription': graphic_data.omDescription,
#         'omEquipment': graphic_data.omEquipment,
#         'omZoom': graphic_data.omZoom,
#         'omPhotoMod': graphic_data.omPhotoMod
#     }
#     return t


# @app.route('/api/request/img/<imgid>', methods=['GET'])
# def get_img(imgid):
#     return send_file('./static/img/{}'.format(imgid), mimetype='image/jpeg')


# @app.route('/api/request/delete', methods=['POST'])
# def delete_data():
#     sample_id = (request.get_json())['sampleId']
#     on_delete_data = Example.query.filter_by(sampleId=sample_id).first()
#     img_list = on_delete_data.imageId
#     if img_list is not None and img_list:
#         for img in img_list:
#             if exists('./static/img/{}'.format(img)):
#                 remove('./static/img/{}'.format(img))
#     db.session.delete(on_delete_data)
#     db.session.commit()
#     return {'delete_status': 'success'}


# @app.route('/api/upload/base', methods=['POST'])
# def upload_base():
#     form = request.get_json()
#     new_record = Example(form['sampleId'], form['sampleType'], form['sampleSource'], form['samplingYear'],
#                          form['samplingPeople'], form['imageId'], form['sampleDescribe'],
#                          form['sampleExplain'], form['experimentId'])
#     db.session.add(new_record)

#     for experiment in form['experimentId']:
#         new_record = ExperimentData(experiment, form['sampleId'])
#         db.session.add(new_record)

#     db.session.commit()

#     return {'upload_base_status': 'success'}


# @app.route('/api/upload/phase/metal', methods=['POST'])
# def upload_phase_metal():
#     metal_phase_data = request.get_json()
#     db.session.query(MetalPhase).filter(MetalPhase.sampleId == metal_phase_data['sampleId']).update({
#         'metalPhase': metal_phase_data['metalPhase'],
#         'sfFullImg': metal_phase_data['sfFullImg'],
#         'sfDescription': metal_phase_data['sfDescription'],
#         'sfEquipment': metal_phase_data['sfEquipment'],
#         'sfZoom': metal_phase_data['sfZoom'],
#         'sfPhotoMod': metal_phase_data['sfPhotoMod'],
#         'sfImgList': metal_phase_data['sfImgList']
#     })

#     for img in metal_phase_data['sfImgList']:
#         new = PhaseGraphic(img)
#         db.session.add(new)

#     db.session.commit()

#     return {'status_code': 200}


# @app.route('/api/upload/phase/mine', methods=['POST'])
# def upload_phase_mine():
#     mine_phase_data = request.get_json()
#     db.session.query(MinePhase).filter(MinePhase.sampleId == mine_phase_data['sampleId']).update({
#         'minePhase': mine_phase_data['minePhase'],
#         'mpFullImg': mine_phase_data['mpFullImg'],
#         'mpDescription': mine_phase_data['mpDescription'],
#         'mpEquipment': mine_phase_data['mpEquipment'],
#         'mpZoom': mine_phase_data['mpZoom'],
#         'mpPhotoMod': mine_phase_data['mpPhotoMod'],
#         'mpImgList': mine_phase_data['mpImgList']
#     })

#     for img in mine_phase_data['mpImgList']:
#         new = PhaseGraphic(img)
#         db.session.add(new)

#     db.session.commit()

#     return {'status_code': 200}


# @app.route('/api/upload/phase/em', methods=['POST'])
# def upload_phase_em():
#     em_phase_data = request.get_json()
#     db.session.query(ElectronMicroPhase).filter(ElectronMicroPhase.sampleId == em_phase_data['sampleId']).update({
#         'emPhase': em_phase_data['emPhase'],
#         'emFullImg': em_phase_data['emFullImg'],
#         'emDescription': em_phase_data['emDescription'],
#         'emEquipment': em_phase_data['emEquipment'],
#         'emZoom': em_phase_data['emZoom'],
#         'emPhotoMod': em_phase_data['emPhotoMod'],
#         'emImgList': em_phase_data['emImgList']
#     })

#     for img in em_phase_data['emImgList']:
#         new = PhaseGraphic(img)
#         db.session.add(new)

#     db.session.commit()

#     return {'status_code': 200}


# @app.route('/api/upload/physical_porosity', methods=['POST'])
# def upload_physical_porosity():
#     physical_porosity = request.get_json()
#     db.session.query(PhysicalPorosity).filter(PhysicalPorosity.sampleId == physical_porosity['sampleId']).update({
#         'apparentPorosity': physical_porosity['apparentPorosity'],
#         'trueDensity': physical_porosity['trueDensity'],
#         'waterAbsorption': physical_porosity['waterAbsorption']
#     })
#     db.session.commit()

#     return {'status_code': 200}


# @app.route('/api/upload/experiment', methods=['POST'])
# def upload_experiment():
#     experiment_datas = request.get_json()
#     for i in range(len(experiment_datas['mineralContent'])):
#         mineralContent = experiment_datas['mineralContent'][i]
#         experiment_id = mineralContent.pop(u'实验编号')
#         XRDContent = experiment_datas['XRDContent'][i]
#         XRDContent.pop(u'实验编号')
#         chemicalContent = experiment_datas['chemicalContent'][i]
#         chemicalContent.pop(u'实验编号')
#         thermalPerform = experiment_datas['thermalPerform'][i]
#         thermalPerform.pop(u'实验编号')
#         diameterDisplay = experiment_datas['diameterDisplay'][i]
#         diameterDisplay.pop(u'实验编号')
#         cavityDisplay = experiment_datas['cavityDisplay'][i]
#         cavityDisplay.pop(u'实验编号')

#         db.session.query(ExperimentData).filter(ExperimentData.experimentId == experiment_id).update({
#             'mineralContent': mineralContent,
#             'XRDContent': XRDContent,
#             'chemicalContent': chemicalContent,
#             'thermalPerform': thermalPerform,
#             'diameterDisplay': diameterDisplay,
#             'cavityDisplay': cavityDisplay
#         })
#     db.session.commit()

#     return {'status_code': 200}


# @app.route('/api/upload/graphic', methods=['POST'])
# def upload_graphic():
#     phase_graphic = request.get_json()
#     db.session.query(PhaseGraphic).filter(PhaseGraphic.imageIndex == phase_graphic['imageIndex']).update({
#         'omDescription': phase_graphic['omDescription'],
#         'omEquipment': phase_graphic['omEquipment'],
#         'omZoom': phase_graphic['omZoom'],
#         'omPhotoMod': phase_graphic['omPhotoMod']
#     })
#     db.session.commit()

#     return {'status_code': 200}


# @app.route('/api/upload/img', methods=['POST'])
# def upload_img():
#     file = request.files.get('fileToUpload')
#     file.save('./static/img/' + file.filename)
#     return {'upload_img_status': 'success'}


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081, debug=True)
