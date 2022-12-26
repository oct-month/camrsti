<template>
  <div id="ExperimentView">
    <h4 align="left">矿物含量信息</h4>
    <el-table
      :data="mineContentInfos"
      :span-method="mineContentSpan"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="id" label="样品号"></el-table-column>
      <el-table-column prop="clay" label="黏土">
        <template slot-scope="scope">
          <el-input v-if="editContentModel[scope.row.id]" v-model="nowEditContent.clay"></el-input>
          <span v-else>
            {{ scope.row.clay }}
          </span>
        </template>
      </el-table-column>
      <el-table-column prop="quartz" label="粉砂">
        <template slot-scope="scope">
          <el-input v-if="editContentModel[scope.row.id]" v-model="nowEditContent.quartz"></el-input>
          <span v-else>
            {{ scope.row.quartz }}
          </span>
        </template>
      </el-table-column>
      <el-table-column label="砂">
        <el-table-column prop="sand_quartz" label="石英">
          <template slot-scope="scope">
            <el-input v-if="editContentModel[scope.row.id]" v-model="nowEditContent.sand_quartz"></el-input>
            <span v-else>
              {{ scope.row.sand_quartz }}
            </span>
          </template>
        </el-table-column>
        <el-table-column prop="sand_feldspar" label="长石">
          <template slot-scope="scope">
            <el-input v-if="editContentModel[scope.row.id]" v-model="nowEditContent.sand_feldspar"></el-input>
            <span v-else>
              {{ scope.row.sand_feldspar }}
            </span>
          </template>
        </el-table-column>
        <el-table-column prop="sand_other" label="其他矿物">
          <template slot-scope="scope">
            <el-input v-if="editContentModel[scope.row.id]" v-model="nowEditContent.sand_other"></el-input>
            <span v-else>
              {{ scope.row.sand_other }}
            </span>
          </template>
        </el-table-column>
        <el-table-column label="小计">
          <template slot-scope="scope">
            <span v-if="!editContentModel[scope.row.id]">{{ sum([scope.row.sand_quartz, scope.row.sand_feldspar, scope.row.sand_other]) }}</span>
          </template>
        </el-table-column>
      </el-table-column>
      <el-table-column prop="debris" label="岩屑">
        <template slot-scope="scope">
          <el-input v-if="editContentModel[scope.row.id]" v-model="nowEditContent.debris"></el-input>
          <span v-else>
            {{ scope.row.debris }}
          </span>
        </template>
      </el-table-column>
      <el-table-column label="空洞">
        <el-table-column prop="hollow_close" label="闭气孔">
          <template slot-scope="scope">
            <el-input v-if="editContentModel[scope.row.id]" v-model="nowEditContent.hollow_close"></el-input>
            <span v-else>
              {{ scope.row.hollow_close }}
            </span>
          </template>
        </el-table-column>
        <el-table-column prop="hollow_open" label="开气孔">
          <template slot-scope="scope">
            <el-input v-if="editContentModel[scope.row.id]" v-model="nowEditContent.hollow_open"></el-input>
            <span v-else>
              {{ scope.row.hollow_open }}
            </span>
          </template>
        </el-table-column>
        <el-table-column prop="hollow_through" label="贯通气孔">
          <template slot-scope="scope">
            <el-input v-if="editContentModel[scope.row.id]" v-model="nowEditContent.hollow_through"></el-input>
            <span v-else>
              {{ scope.row.hollow_through }}
            </span>
          </template>
        </el-table-column>
      </el-table-column>
      <el-table-column label="操作" width="119">
        <template slot-scope="scope">
          <div v-if="!scope.row.temp">
            <div v-if="editContentModel[scope.row.id]" style="text-align:center;">
              <el-button size="small" type="success" icon="el-icon-check" circle @click="submitContentEdit(scope.row.id)"></el-button>
              <el-button size="mini" type="danger" icon="el-icon-close" circle @click="cancelContentEdit(scope.row.id)"></el-button>
            </div>
            <div v-else style="text-align:center;">
              <el-button size="mini" round plain type="warning" icon="el-icon-edit" @click="editContent(scope.row.id)"></el-button>
              <el-button size="mini" round plain type="danger" icon="el-icon-delete" @click="deleteContentDialogVisible[scope.row.id]=true"></el-button>
              <el-dialog title="确认" :visible.sync="deleteContentDialogVisible[scope.row.id]" width="30%">
                <span>删除{{ scope.row.id }}?</span>
                <span slot="footer" class="dialog-footer">
                  <el-button @click="deleteContentDialogVisible[scope.row.id]=false">取 消</el-button>
                  <el-button type="primary" @click="deleteContent(scope.row.id)">确 定</el-button>
                </span>
              </el-dialog>
            </div>
          </div>
        </template>
      </el-table-column>
    </el-table>

    <hr>

    <h4 align="left">矿物测量数据</h4>

    <el-table
      :data="mineSurveyInfos"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="id" label="样品号"></el-table-column>
      <el-table-column label="岩屑直径分布">
        <el-table-column prop="debris_0um" label="≤67μm">
          <template slot-scope="scope">
            <el-input v-if="editSurveyModel[scope.row.id]" v-model="nowEditSurvey.debris_0um"></el-input>
            <span v-else>
              {{ scope.row.debris_0um }}
            </span>
          </template>
        </el-table-column>
        <el-table-column prop="debris_67um" label="67-167μm">
          <template slot-scope="scope">
            <el-input v-if="editSurveyModel[scope.row.id]" v-model="nowEditSurvey.debris_67um"></el-input>
            <span v-else>
              {{ scope.row.debris_67um }}
            </span>
          </template>
        </el-table-column>
        <el-table-column prop="debris_167um" label="167-501μm">
          <template slot-scope="scope">
            <el-input v-if="editSurveyModel[scope.row.id]" v-model="nowEditSurvey.debris_167um"></el-input>
            <span v-else>
              {{ scope.row.debris_167um }}
            </span>
          </template>
        </el-table-column>
        <el-table-column prop="debris_501um" label="501-1002μm">
          <template slot-scope="scope">
            <el-input v-if="editSurveyModel[scope.row.id]" v-model="nowEditSurvey.debris_501um"></el-input>
            <span v-else>
              {{ scope.row.debris_501um }}
            </span>
          </template>
        </el-table-column>
        <el-table-column prop="debris_1002um" label="≥1002μm">
          <template slot-scope="scope">
            <el-input v-if="editSurveyModel[scope.row.id]" v-model="nowEditSurvey.debris_1002um"></el-input>
            <span v-else>
              {{ scope.row.debris_1002um }}
            </span>
          </template>
        </el-table-column>
      </el-table-column>
      <el-table-column label="空洞长度分布">
        <el-table-column prop="hollow_0um" label="≤67μm">
          <template slot-scope="scope">
            <el-input v-if="editSurveyModel[scope.row.id]" v-model="nowEditSurvey.hollow_0um"></el-input>
            <span v-else>
              {{ scope.row.hollow_0um }}
            </span>
          </template>
        </el-table-column>
        <el-table-column prop="hollow_67um" label="67-501μm">
          <template slot-scope="scope">
            <el-input v-if="editSurveyModel[scope.row.id]" v-model="nowEditSurvey.hollow_67um"></el-input>
            <span v-else>
              {{ scope.row.hollow_67um }}
            </span>
          </template>
        </el-table-column>
        <el-table-column prop="hollow_501um" label="501-1002μm">
          <template slot-scope="scope">
            <el-input v-if="editSurveyModel[scope.row.id]" v-model="nowEditSurvey.hollow_501um"></el-input>
            <span v-else>
              {{ scope.row.hollow_501um }}
            </span>
          </template>
        </el-table-column>
        <el-table-column prop="hollow_1002um" label="1002-2004μm">
          <template slot-scope="scope">
            <el-input v-if="editSurveyModel[scope.row.id]" v-model="nowEditSurvey.hollow_1002um"></el-input>
            <span v-else>
              {{ scope.row.hollow_1002um }}
            </span>
          </template>
        </el-table-column>
        <el-table-column prop="hollow_2004um" label="≥2004μm">
          <template slot-scope="scope">
            <el-input v-if="editSurveyModel[scope.row.id]" v-model="nowEditSurvey.hollow_2004um"></el-input>
            <span v-else>
              {{ scope.row.hollow_2004um }}
            </span>
          </template>
        </el-table-column>
      </el-table-column>
      <el-table-column label="操作" width="119">
        <template slot-scope="scope">
          <div v-if="!scope.row.temp">
            <div v-if="editSurveyModel[scope.row.id]" style="text-align:center;">
              <el-button size="small" type="success" icon="el-icon-check" circle @click="submitSurveyEdit(scope.row.id)"></el-button>
              <el-button size="mini" type="danger" icon="el-icon-close" circle @click="cancelSurveyEdit(scope.row.id)"></el-button>
            </div>
            <div v-else style="text-align:center;">
              <el-button size="mini" round plain type="warning" icon="el-icon-edit" @click="editSurvey(scope.row.id)"></el-button>
              <el-button size="mini" round plain type="danger" icon="el-icon-delete" @click="deleteSurveyDialogVisible[scope.row.id]=true"></el-button>
              <el-dialog title="确认" :visible.sync="deleteSurveyDialogVisible[scope.row.id]" width="30%">
                <span>删除{{ scope.row.id }}?</span>
                <span slot="footer" class="dialog-footer">
                  <el-button @click="deleteSurveyDialogVisible[scope.row.id]=false">取 消</el-button>
                  <el-button type="primary" @click="deleteSurvey(scope.row.id)">确 定</el-button>
                </span>
              </el-dialog>
            </div>
          </div>
        </template>
      </el-table-column>
    </el-table>

    <hr>

    <h4 align="left">XRD分析数据</h4>

    <el-table
      :data="mineXRDInfos"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="id" label="样品编号"></el-table-column>
      <el-table-column prop="type" label="类型">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.type"></el-input>
          <span v-else>{{ scope.row.type }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="quartz" label="石英">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.quartz"></el-input>
          <span v-else>{{ scope.row.quartz }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="albite" label="钠长石">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.albite"></el-input>
          <span v-else>{{ scope.row.albite }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="potashFeldspar" label="钾长石">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.potashFeldspar"></el-input>
          <span v-else>{{ scope.row.potashFeldspar }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="mica" label="云母">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.mica"></el-input>
          <span v-else>{{ scope.row.mica }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="amphibole" label="闪石">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.amphibole"></el-input>
          <span v-else>{{ scope.row.amphibole }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="hematite" label="赤铁矿">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.hematite"></el-input>
          <span v-else>{{ scope.row.hematite }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="magnetite" label="磁铁矿">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.magnetite"></el-input>
          <span v-else>{{ scope.row.magnetite }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="dolomite" label="白云石">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.dolomite"></el-input>
          <span v-else>{{ scope.row.dolomite }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="analcite" label="方沸石">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.analcite"></el-input>
          <span v-else>{{ scope.row.analcite }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="tridymite" label="磷石英">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.tridymite"></el-input>
          <span v-else>{{ scope.row.tridymite }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="cristobalite" label="方石英">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.cristobalite"></el-input>
          <span v-else>{{ scope.row.cristobalite }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="mullite" label="莫来石">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.mullite"></el-input>
          <span v-else>{{ scope.row.mullite }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="other" label="其他">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.other"></el-input>
          <span v-else>{{ scope.row.other }}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="119">
        <template slot-scope="scope">
          <div v-if="editXRDModel[scope.row.id]" style="text-align:center;">
            <el-button size="small" type="success" icon="el-icon-check" circle @click="submitXRDEdit(scope.row.id)"></el-button>
            <el-button size="mini" type="danger" icon="el-icon-close" circle @click="cancelXRDEdit(scope.row.id)"></el-button>
          </div>
          <div v-else style="text-align:center;">
            <el-button size="mini" round plain type="warning" icon="el-icon-edit" @click="editXRD(scope.row.id)"></el-button>
            <el-button size="mini" round plain type="danger" icon="el-icon-delete" @click="deleteXRDDialogVisible[scope.row.id]=true"></el-button>
            <el-dialog title="确认" :visible.sync="deleteXRDDialogVisible[scope.row.id]" width="30%">
              <span>删除{{ scope.row.id }}?</span>
              <span slot="footer" class="dialog-footer">
                <el-button @click="deleteXRDDialogVisible[scope.row.id]=false">取 消</el-button>
                <el-button type="primary" @click="deleteXRD(scope.row.id)">确 定</el-button>
              </span>
            </el-dialog>
          </div>
        </template>
      </el-table-column>
    </el-table>

    <hr>

    <!-- <h4 align="left">化学成分数据</h4> -->
    <h4 align="left" v-show="(mineChemistryInfos.length > 0) || (mineChemistryInfos.length + mineChemistryInfoSingle.length <= 0)">化学成分数据（氧化物）</h4>

    <el-table
      v-show="(mineChemistryInfos.length > 0) || (mineChemistryInfos.length + mineChemistryInfoSingle.length <= 0)"
      :data="mineChemistryInfos"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="id" label="样品号"></el-table-column>
      <el-table-column prop="Na2O" label="Na₂O">
        <template slot-scope="scope">
          <el-input v-if="editChemistryModel[scope.row.id]" v-model="nowEditChemistry.Na2O"></el-input>
          <span v-else>{{ scope.row.Na2O }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="MgO" label="MgO">
        <template slot-scope="scope">
          <el-input v-if="editChemistryModel[scope.row.id]" v-model="nowEditChemistry.MgO"></el-input>
          <span v-else>{{ scope.row.MgO }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="Al2O3" label="Al₂O₃">
        <template slot-scope="scope">
          <el-input v-if="editChemistryModel[scope.row.id]" v-model="nowEditChemistry.Al2O3"></el-input>
          <span v-else>{{ scope.row.Al2O3 }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="SiO2" label="SiO₂">
        <template slot-scope="scope">
          <el-input v-if="editChemistryModel[scope.row.id]" v-model="nowEditChemistry.SiO2"></el-input>
          <span v-else>{{ scope.row.SiO2 }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="K2O" label="K₂O">
        <template slot-scope="scope">
          <el-input v-if="editChemistryModel[scope.row.id]" v-model="nowEditChemistry.K2O"></el-input>
          <span v-else>{{ scope.row.K2O }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="CaO" label="CaO">
        <template slot-scope="scope">
          <el-input v-if="editChemistryModel[scope.row.id]" v-model="nowEditChemistry.CaO"></el-input>
          <span v-else>{{ scope.row.CaO }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="Fe2O3" label="Fe₂O₃">
        <template slot-scope="scope">
          <el-input v-if="editChemistryModel[scope.row.id]" v-model="nowEditChemistry.Fe2O3"></el-input>
          <span v-else>{{ scope.row.Fe2O3 }}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="119">
        <template slot-scope="scope">
          <div v-if="editChemistryModel[scope.row.id]" style="text-align:center;">
            <el-button size="small" type="success" icon="el-icon-check" circle @click="submitChemistryEdit(scope.row.id)"></el-button>
            <el-button size="mini" type="danger" icon="el-icon-close" circle @click="cancelChemistryEdit(scope.row.id)"></el-button>
          </div>
          <div v-else style="text-align:center;">
            <el-button size="mini" round plain type="warning" icon="el-icon-edit" @click="editChemistry(scope.row.id)"></el-button>
            <el-button size="mini" round plain type="danger" icon="el-icon-delete" @click="deleteChemistryDialogVisible[scope.row.id]=true"></el-button>
            <el-dialog title="确认" :visible.sync="deleteChemistryDialogVisible[scope.row.id]" width="30%">
              <span>删除{{ scope.row.id }}?</span>
              <span slot="footer" class="dialog-footer">
                <el-button @click="deleteChemistryDialogVisible[scope.row.id]=false">取 消</el-button>
                <el-button type="primary" @click="deleteChemistry(scope.row.id)">确 定</el-button>
              </span>
            </el-dialog>
          </div>
        </template>
      </el-table-column>
    </el-table>

    <h4 align="left" v-show="(mineChemistryInfoSingle.length > 0)">化学成分数据（单质）</h4>

    <el-table
      v-show="(mineChemistryInfoSingle.length > 0)"
      :data="mineChemistryInfoSingle"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="id" label="样品号"></el-table-column>
      <el-table-column prop="C" label="C">
        <template slot-scope="scope">
          <el-input v-if="editChemistrySingleModel[scope.row.id]" v-model="nowEditChemistrySingle.C"></el-input>
          <span v-else>{{ scope.row.C }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="Na" label="Na">
        <template slot-scope="scope">
          <el-input v-if="editChemistrySingleModel[scope.row.id]" v-model="nowEditChemistrySingle.Na"></el-input>
          <span v-else>{{ scope.row.Na }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="Mg" label="Mg">
        <template slot-scope="scope">
          <el-input v-if="editChemistrySingleModel[scope.row.id]" v-model="nowEditChemistrySingle.Mg"></el-input>
          <span v-else>{{ scope.row.Mg }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="Al" label="Al">
        <template slot-scope="scope">
          <el-input v-if="editChemistrySingleModel[scope.row.id]" v-model="nowEditChemistrySingle.Al"></el-input>
          <span v-else>{{ scope.row.Al }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="Si" label="Si">
        <template slot-scope="scope">
          <el-input v-if="editChemistrySingleModel[scope.row.id]" v-model="nowEditChemistrySingle.Si"></el-input>
          <span v-else>{{ scope.row.Si }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="P" label="P">
        <template slot-scope="scope">
          <el-input v-if="editChemistrySingleModel[scope.row.id]" v-model="nowEditChemistrySingle.P"></el-input>
          <span v-else>{{ scope.row.P }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="S" label="S">
        <template slot-scope="scope">
          <el-input v-if="editChemistrySingleModel[scope.row.id]" v-model="nowEditChemistrySingle.S"></el-input>
          <span v-else>{{ scope.row.S }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="Cl" label="Cl">
        <template slot-scope="scope">
          <el-input v-if="editChemistrySingleModel[scope.row.id]" v-model="nowEditChemistrySingle.Cl"></el-input>
          <span v-else>{{ scope.row.Cl }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="K" label="K">
        <template slot-scope="scope">
          <el-input v-if="editChemistrySingleModel[scope.row.id]" v-model="nowEditChemistrySingle.K"></el-input>
          <span v-else>{{ scope.row.K }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="Ca" label="Ca">
        <template slot-scope="scope">
          <el-input v-if="editChemistrySingleModel[scope.row.id]" v-model="nowEditChemistrySingle.Ca"></el-input>
          <span v-else>{{ scope.row.Ca }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="Ti" label="Ti">
        <template slot-scope="scope">
          <el-input v-if="editChemistrySingleModel[scope.row.id]" v-model="nowEditChemistrySingle.Ti"></el-input>
          <span v-else>{{ scope.row.Ti }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="V" label="V">
        <template slot-scope="scope">
          <el-input v-if="editChemistrySingleModel[scope.row.id]" v-model="nowEditChemistrySingle.V"></el-input>
          <span v-else>{{ scope.row.V }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="Mn" label="Mn">
        <template slot-scope="scope">
          <el-input v-if="editChemistrySingleModel[scope.row.id]" v-model="nowEditChemistrySingle.Mn"></el-input>
          <span v-else>{{ scope.row.Mn }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="Fe" label="Fe">
        <template slot-scope="scope">
          <el-input v-if="editChemistrySingleModel[scope.row.id]" v-model="nowEditChemistrySingle.Fe"></el-input>
          <span v-else>{{ scope.row.Fe }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="Co" label="Co">
        <template slot-scope="scope">
          <el-input v-if="editChemistrySingleModel[scope.row.id]" v-model="nowEditChemistrySingle.Co"></el-input>
          <span v-else>{{ scope.row.Co }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="Ni" label="Ni">
        <template slot-scope="scope">
          <el-input v-if="editChemistrySingleModel[scope.row.id]" v-model="nowEditChemistrySingle.Ni"></el-input>
          <span v-else>{{ scope.row.Ni }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="Cu" label="Cu">
        <template slot-scope="scope">
          <el-input v-if="editChemistrySingleModel[scope.row.id]" v-model="nowEditChemistrySingle.Cu"></el-input>
          <span v-else>{{ scope.row.Cu }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="Zn" label="Zn">
        <template slot-scope="scope">
          <el-input v-if="editChemistrySingleModel[scope.row.id]" v-model="nowEditChemistrySingle.Zn"></el-input>
          <span v-else>{{ scope.row.Zn }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="As" label="As">
        <template slot-scope="scope">
          <el-input v-if="editChemistrySingleModel[scope.row.id]" v-model="nowEditChemistrySingle.As"></el-input>
          <span v-else>{{ scope.row.As }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="Ag" label="Ag">
        <template slot-scope="scope">
          <el-input v-if="editChemistrySingleModel[scope.row.id]" v-model="nowEditChemistrySingle.Ag"></el-input>
          <span v-else>{{ scope.row.Ag }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="Sn" label="Sn">
        <template slot-scope="scope">
          <el-input v-if="editChemistrySingleModel[scope.row.id]" v-model="nowEditChemistrySingle.Sn"></el-input>
          <span v-else>{{ scope.row.Sn }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="Sb" label="Sb">
        <template slot-scope="scope">
          <el-input v-if="editChemistrySingleModel[scope.row.id]" v-model="nowEditChemistrySingle.Sb"></el-input>
          <span v-else>{{ scope.row.Sb }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="Au" label="Au">
        <template slot-scope="scope">
          <el-input v-if="editChemistrySingleModel[scope.row.id]" v-model="nowEditChemistrySingle.Au"></el-input>
          <span v-else>{{ scope.row.Au }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="Hg" label="Hg">
        <template slot-scope="scope">
          <el-input v-if="editChemistrySingleModel[scope.row.id]" v-model="nowEditChemistrySingle.Hg"></el-input>
          <span v-else>{{ scope.row.Hg }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="Pb" label="Pb">
        <template slot-scope="scope">
          <el-input v-if="editChemistrySingleModel[scope.row.id]" v-model="nowEditChemistrySingle.Pb"></el-input>
          <span v-else>{{ scope.row.Pb }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="other" label="其他">
        <template slot-scope="scope">
          <el-input v-if="editChemistrySingleModel[scope.row.id]" v-model="nowEditChemistrySingle.other"></el-input>
          <span v-else>{{ scope.row.other }}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="119">
        <template slot-scope="scope">
          <div v-if="editChemistrySingleModel[scope.row.id]" style="text-align:center;">
            <el-button size="small" type="success" icon="el-icon-check" circle @click="submitChemistrySingleEdit(scope.row.id)"></el-button>
            <el-button size="mini" type="danger" icon="el-icon-close" circle @click="cancelChemistrySingleEdit(scope.row.id)"></el-button>
          </div>
          <div v-else style="text-align:center;">
            <el-button size="mini" round plain type="warning" icon="el-icon-edit" @click="editChemistrySingle(scope.row.id)"></el-button>
            <el-button size="mini" round plain type="danger" icon="el-icon-delete" @click="deleteChemistrySingleDialogVisible[scope.row.id]=true"></el-button>
            <el-dialog title="确认" :visible.sync="deleteChemistrySingleDialogVisible[scope.row.id]" width="30%">
              <span>删除{{ scope.row.id }}?</span>
              <span slot="footer" class="dialog-footer">
                <el-button @click="deleteChemistrySingleDialogVisible[scope.row.id]=false">取 消</el-button>
                <el-button type="primary" @click="deleteChemistrySingle(scope.row.id)">确 定</el-button>
              </span>
            </el-dialog>
          </div>
        </template>
      </el-table-column>
    </el-table>

    <hr>

    <h4 align="left">热分析</h4>

    <el-table
      :data="mineThermalInfos"
      :span-method="mineThermalSpan"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="id" label="样品号"></el-table-column>
      <el-table-column prop="melting" label="熔点">
        <template slot-scope="scope">
          <el-input v-if="editThermalModel[scope.row.id]" v-model="nowEditThermal.melting"></el-input>
          <span v-else>{{ scope.row.melting }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="fireResis" label="耐火度">
        <template slot-scope="scope">
          <el-input v-if="editThermalModel[scope.row.id]" v-model="nowEditThermal.fireResis"></el-input>
          <span v-else>{{ scope.row.fireResis }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="termTemper" label="烧成温度">
        <template slot-scope="scope">
          <el-input v-if="editThermalModel[scope.row.id]" v-model="nowEditThermal.termTemper"></el-input>
          <span v-else>{{ scope.row.termTemper }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="data" label="原始数据">
        <template slot-scope="scope">
          <el-upload
            v-if="editThermalModel[scope.row.id]"
            action="/api/excel"
            accept=".xlsx, .xls"
            ref="upload"
            name="upload"
            :on-success="handleExcelUploadSuccess"
            :on-error="handleExcelUploadError"
            :auto-upload="true">
            <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
            <div slot="tip" class="el-upload__tip">只能上传xlsx/xls文件，且不超过8MB</div>
          </el-upload>
          <el-link v-else type="primary" target="_blank" :href="'/api/excel/'+scope.row.data" :download="scope.row.data">
            {{ scope.row.data }}
          </el-link>
        </template>
      </el-table-column>
      <el-table-column prop="surveImage" label="曲线图">
        <template slot-scope="scope">
          <el-upload
            v-if="editThermalModel[scope.row.id]"
            action="/api/image"
            accept="image/png, image/jpeg"
            ref="upload"
            name="upload"
            :on-success="handleImgUploadSuccess"
            :on-error="handleImgUploadError"
            :auto-upload="true">
            <el-button slot="trigger" size="small" type="primary">选取图片</el-button>
            <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过4MB</div>
          </el-upload>
          <el-image
            v-else-if="scope.row.surveImage"
            style="height: 200px"
            :src="'/api/image/' + scope.row.surveImage"
            fit="contain">
            <div slot="error" class="image-slot">
              <i class="el-icon-picture-outline"></i>
            </div>
          </el-image>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="119">
        <template slot-scope="scope">
          <div v-if="editThermalModel[scope.row.id]" style="text-align:center;">
            <el-button size="small" type="success" icon="el-icon-check" circle @click="submitThermalEdit(scope.row.id)"></el-button>
            <el-button size="mini" type="danger" icon="el-icon-close" circle @click="cancelThermalEdit(scope.row.id)"></el-button>
          </div>
          <div v-else style="text-align:center;">
            <el-button size="mini" round plain type="warning" icon="el-icon-edit" @click="editThermal(scope.row.id)"></el-button>
            <el-button size="mini" round plain type="danger" icon="el-icon-delete" @click="deleteThermalDialogVisible[scope.row.id]=true"></el-button>
            <el-dialog title="确认" :visible.sync="deleteThermalDialogVisible[scope.row.id]" width="30%">
              <span>删除{{ scope.row.id }}?</span>
              <span slot="footer" class="dialog-footer">
                <el-button @click="deleteThermalDialogVisible[scope.row.id]=false">取 消</el-button>
                <el-button type="primary" @click="deleteThermal(scope.row.id)">确 定</el-button>
              </span>
            </el-dialog>
          </div>
        </template>
      </el-table-column>
      <!-- <el-table-column prop="surveImage" label="热分析曲线" miniwidth="400">
        <template slot-scope="scope">
          <el-image
            style="height: 200px"
            :src="'/api/image/' + scope.row.surveImage"
            fit="contain">
            <div slot="error" class="image-slot">
              <i class="el-icon-picture-outline"></i>
            </div>
          </el-image>
        </template>
      </el-table-column> -->
    </el-table>
    <!-- <div style="float:right;">
      导出：
      <el-button size="small" type="success" icon="el-icon-download" @click="exportTableData"></el-button>
    </div> -->
  </div>
</template>

<style scoped>
#ExperimentView {
  padding: 15px;
}

.table-expand {
  font-size: 0;
}

.table-expand label {
  width: 90px;
  color: #99a9bf;
}

.table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 50%;
}
</style>

<script>
import xlsx from 'xlsx'

import { deepObjCopy } from '@/utils'

export default {
  name: "ExperimentPage",
  props: {
    sampleId: String
  },
  data() {
    return {
      token: '',
      mineContentInfos: [],
      editContentModel: {},
      deleteContentDialogVisible: {},
      nowEditContent: null,
      mineSurveyInfos: [],
      editSurveyModel: {},
      deleteSurveyDialogVisible: {},
      nowEditSurvey: null,
      mineXRDInfos: [],
      editXRDModel: {},
      deleteXRDDialogVisible: {},
      nowEditXRD: null,
      mineChemistryInfos: [],
      editChemistryModel: {},
      deleteChemistryDialogVisible: {},
      nowEditChemistry: null,
      mineChemistryInfoSingle: [],
      editChemistrySingleModel: {},
      deleteChemistrySingleDialogVisible: {},
      nowEditChemistrySingle: null,
      mineThermalInfos: [],
      editThermalModel: {},
      deleteThermalDialogVisible: {},
      nowEditThermal: null,
    }
  },
  mounted() {
    if (this.$route.query.token) {
      this.token = this.$route.query.token
    }
    else if (this.$cookies.isKey('token')) {
      this.token = this.$cookies.get('token')
    }
    else {
      this.$router.replace({
        name: 'SignView'
      })
    }

    if (!this.sampleId) {
      this.$message.error('出错啦！')
      return
    }
    this.axios.get('/api/minecontentinfo/' + this.sampleId, {
      params: {
        token: this.token
      }
    })
      .then((res) => {
        if (res.status == 200) {
          var v = res.data.data
          this.$set(this.editContentModel, v.id, false)
          this.$set(this.deleteContentDialogVisible, v.id, false)
          this.mineContentInfos = [v]
          this.mineContentCompute()
        }
        else {
          this.$message.error('出错啦！')
        }
      })
    this.axios.get('/api/minesurveyinfo/' + this.sampleId, {
      params: {
        token: this.token
      }
    })
      .then((res) => {
        if (res.status == 200) {
          var v = res.data.data
          this.$set(this.editSurveyModel, v.id, false)
          this.$set(this.deleteSurveyDialogVisible, v.id, false)
          this.mineSurveyInfos = [v]
        }
        else {
          this.$message.error('出错啦！')
        }
      })
    this.axios.get('/api/minexrdinfo/' + this.sampleId, {
      params: {
        token: this.token
      }
    })
      .then(res => {
        if (res.status == 200) {
          var v = res.data.data
          this.$set(this.editXRDModel, v.id, false)
          this.$set(this.deleteXRDDialogVisible, v.id, false)
          this.mineXRDInfos = [v]
        }
        else {
          this.$message.error('出错啦！')
        }
      })
    this.axios.get('/api/minechemistryinfo/' + this.sampleId, {
      params: {
        token: this.token
      }
    })
      .then(res => {
        if (res.status == 200) {
          var v = res.data.data
          this.$set(this.editChemistryModel, v.id, false)
          this.$set(this.deleteChemistryDialogVisible, v.id, false)
          this.mineChemistryInfos = [v]
        }
        else {
          this.$message.error('出错啦！')
        }
      })
    this.axios.get('/api/minethermalinfo/' + this.sampleId, {
      params: {
        token: this.token
      }
    })
      .then(res => {
        if (res.status == 200) {
          var v = res.data.data
          this.$set(this.editThermalModel, v.id, false)
          this.$set(this.deleteThermalDialogVisible, v.id, false)
          this.mineThermalInfos = [v]
        }
        else {
          this.$message.error('出错啦！')
        }
      })
  },
  methods: {
    sum(array) {
      var res = 0
      array.forEach(v => {
        res += Number(v)
      })
      return res
    },
    mineContentCompute() {
      if (this.mineContentInfos && this.mineContentInfos.length > 0) {
        this.mineContentInfos = this.mineContentInfos.filter(v => !v.temp)
        var temp = this.mineContentInfos
        var obj = {
            id: '平均值',
            clay: 0,
            quartz: 0,
            sand_quartz: 0,
            sand_feldspar: 0,
            sand_other: 0,
            debris: 0,
            hollow_close: 0,
            hollow_open: 0,
            hollow_through: 0,
            temp: true
          }
          temp.forEach(v => {
            obj.clay += v.clay
            obj.quartz += v.quartz
            obj.sand_quartz += v.sand_quartz
            obj.sand_feldspar += v.sand_feldspar
            obj.sand_other += v.sand_other
            obj.debris += v.debris
            obj.hollow_close += v.hollow_close
            obj.hollow_open += v.hollow_open
            obj.hollow_through += v.hollow_through
          })
          obj.clay /= temp.length
          obj.quartz /= temp.length
          obj.sand_quartz /= temp.length
          obj.sand_feldspar /= temp.length
          obj.sand_other /= temp.length
          obj.debris /= temp.length
          obj.hollow_close /= temp.length
          obj.hollow_open /= temp.length
          obj.hollow_through /= temp.length
          var obj2 = {
            id: '变异系数',
            clay: 0,
            quartz: 0,
            sand_quartz: 0,
            sand_feldspar: 0,
            sand_other: 0,
            debris: 0,
            hollow_close: 0,
            hollow_open: 0,
            hollow_through: 0,
            temp: true
          }
          temp.forEach(v => {
            obj2.clay += Math.pow(v.clay - obj.clay, 2)
            obj2.quartz += Math.pow(v.quartz - obj.quartz, 2)
            obj2.sand_quartz += Math.pow(v.sand_quartz - obj.sand_quartz, 2)
            obj2.sand_feldspar += Math.pow(v.sand_feldspar - obj.sand_feldspar, 2)
            obj2.sand_other += Math.pow(v.sand_other - obj.sand_other, 2)
            obj2.debris += Math.pow(v.debris - obj.debris, 2)
            obj2.hollow_close += Math.pow(v.hollow_close - obj.hollow_close, 2)
            obj2.hollow_open += Math.pow(v.hollow_open - obj.hollow_open, 2)
            obj2.hollow_through += Math.pow(v.hollow_through - obj.hollow_through, 2)
          })
          obj2.clay = obj.clay ? Math.pow(obj2.clay / temp.length, 0.5) / obj.clay : null
          obj2.quartz = obj.quartz ? Math.pow(obj2.quartz / temp.length, 0.5) / obj.quartz : null
          obj2.sand_quartz = obj.sand_quartz ? Math.pow(obj2.sand_quartz / temp.length, 0.5) / obj.sand_quartz : null
          obj2.sand_feldspar = obj.sand_feldspar ? Math.pow(obj2.sand_feldspar / temp.length, 0.5) / obj.sand_feldspar : null
          obj2.sand_other = obj.sand_other ? Math.pow(obj2.sand_other / temp.length, 0.5) / obj.sand_other : null
          obj2.debris = obj.debris ? Math.pow(obj2.debris / temp.length, 0.5) / obj.debris : null
          obj2.hollow_close = obj.hollow_close ? Math.pow(obj2.hollow_close / temp.length, 0.5) / obj.hollow_close : null
          obj2.hollow_open = obj.hollow_open ? Math.pow(obj2.hollow_open / temp.length, 0.5) / obj.hollow_open : null
          obj2.hollow_through = obj.hollow_through ? Math.pow(obj2.hollow_through / temp.length, 0.5) / obj.hollow_through : null
          this.mineContentInfos.push(obj)
          this.mineContentInfos.push(obj2)
      }
    },
    mineContentSpan({ rowIndex, columnIndex }) {
      var length = this.mineContentInfos.length
      if (rowIndex >= length - 2 && columnIndex <= 0) {
        return {
          rowspan: 1,
          colspan: 2
        }
      }
      else if (rowIndex >= length - 2 && columnIndex == 1) {
        return {
          rowspan: 0,
          colspan: 0
        }
      }
      else {
        return {
          rowspan: 1,
          colspan: 1
        }
      }
    },
    mineThermalSpan({ rowIndex, columnIndex }) {
      if (rowIndex == 0 && columnIndex >= 5) {
        // console.log(this.mineThermalInfos.length);
        return {
          rowspan: this.mineThermalInfos.length,
          colspan: 1
        }
      }
      else if (rowIndex > 0 && columnIndex >= 5) {
        return {
          rowspan: 0,
          colspan: 0
        }
      }
      else {
        return {
          rowspan: 1,
          colspan: 1
        }
      }
    },
    editContent(id) {
      if (this.nowEditContent) {
        this.$message.warning('您正在编辑' + this.nowEditContent.id + '，请优先完成')
        return
      }
      let mi = this.mineContentInfos.filter(v => v.id == id && !v.temp)[0]
      this.nowEditContent = deepObjCopy(mi)
      this.editContentModel[id] = true
    },
    submitContentEdit(id) {
      let t = this.nowEditContent
      t.clay = t.clay ? Number(t.clay) : null
      t.quartz = t.quartz ? Number(t.quartz) : null
      t.sand_quartz = t.sand_quartz ? Number(t.sand_quartz) : null
      t.sand_feldspar = t.sand_feldspar ? Number(t.sand_feldspar) : null
      t.sand_other = t.sand_other ? Number(t.sand_other) : null
      t.debris = t.debris ? Number(t.debris) : null
      t.hollow_close = t.hollow_close ? Number(t.hollow_close) : null
      t.hollow_open = t.hollow_open ? Number(t.hollow_open) : null
      t.hollow_through = t.hollow_through ? Number(t.hollow_through) : null
      this.axios.put('/api/minecontentinfo/' + id, t, {
        params: {
          token: this.token
        }
      })
        .then(res => {
          if (res.status == 200) {
            for (let i = 0; i < this.mineContentInfos.length; ++ i) {
              if (this.mineContentInfos[i].id == id && !this.mineContentInfos[i].temp) {
                this.$set(this.mineContentInfos, i, t)
                this.mineContentCompute()
                break
              }
            }
            this.$message.success('修改' + id + '成功！')
          }
          else {
            this.$message.error('出错啦！')
          }
        })
      this.editContentModel[id] = false
      this.nowEditContent = null
    },
    cancelContentEdit(id) {
      this.editContentModel[id] = false
      this.nowEditContent= null
    },
    deleteContent(id) {
      this.axios.delete('/api/minecontentinfo/' + id, {
        params: {
          token: this.token
        }
      })
        .then(res => {
          if (res.status == 200) {
            this.mineContentInfos = this.mineContentInfos.filter(v => v.id != id || v.temp)
            this.mineContentCompute()
            this.$message.success('删除' + id + '成功！')
          }
          else {
            this.$message.error('出错啦！')
          }
        })
    },
    editXRD(id) {
      if (this.nowEditXRD) {
        this.$message.warning('您正在编辑' + this.nowEditXRD.id + '，请优先完成')
        return
      }
      let mi = this.mineXRDInfos.filter(v => v.id == id)[0]
      this.nowEditXRD = deepObjCopy(mi)
      this.editXRDModel[id] = true
    },
    submitXRDEdit(id) {
      let t = this.nowEditXRD
      t.type = t.type.trim()
      t.quartz = t.quartz ? Number(t.quartz) : null
      t.albite = t.albite ? Number(t.albite) : null
      t.potashFeldspar = t.potashFeldspar ? Number(t.potashFeldspar) : null
      t.mica = t.mica ? Number(t.mica) : null
      t.amphibole = t.amphibole ? Number(t.amphibole) : null
      t.hematite = t.hematite ? Number(t.hematite) : null
      t.magnetite = t.magnetite ? Number(t.magnetite) : null
      t.dolomite = t.dolomite ? Number(t.dolomite) : null
      t.analcite = t.analcite ? Number(t.analcite) : null
      t.tridymite = t.tridymite ? Number(t.tridymite) : null
      t.cristobalite = t.cristobalite ? Number(t.cristobalite) : null
      t.mullite = t.mullite ? Number(t.mullite) : null
      t.other = t.other ? Number(t.other) : null
      this.axios.put('/api/minexrdinfo/' + id, t, {
        params: {
          token: this.token
        }
      })
        .then(res => {
          if (res.status == 200) {
            for (let i = 0; i < this.mineXRDInfos.length; ++ i) {
              if (this.mineXRDInfos[i].id == id) {
                this.$set(this.mineXRDInfos, i, t)
                break
              }
            }
            this.$message.success('修改' + id + '成功！')
          }
          else {
            this.$message.error('出错啦！')
          }
        })
      this.editXRDModel[id] = false
      this.nowEditXRD = null
    },
    cancelXRDEdit(id) {
      this.editXRDModel[id] = false
      this.nowEditXRD= null
    },
    deleteXRD(id) {
      this.axios.delete('/api/minexrdinfo/' + id, {
        params: {
          token: this.token
        }
      })
        .then(res => {
          if (res.status == 200) {
            this.mineXRDInfos = this.mineXRDInfos.filter(v => v.id != id || v.temp)
            this.$message.success('删除' + id + '成功！')
          }
          else {
            this.$message.error('出错啦！')
          }
        })
    },
    editChemistry(id) {
      if (this.nowEditChemistry) {
        this.$message.warning('您正在编辑' + this.nowEditChemistry.id + '，请优先完成')
        return
      }
      let mi = this.mineChemistryInfos.filter(v => v.id == id)[0]
      this.nowEditChemistry = deepObjCopy(mi)
      this.editChemistryModel[id] = true
    },
    submitChemistryEdit(id) {
      let t = this.nowEditChemistry
      t.Na2O = Number(t.Na2O)
      t.MgO = Number(t.MgO)
      t.Al2O3 = Number(t.Al2O3)
      t.SiO2 = Number(t.SiO2)
      t.P2O5 = Number(t.P2O5)
      t.SO2 = Number(t.SO2)
      t.K2O = Number(t.K2O)
      t.CaO = Number(t.CaO)
      t.TiO2 = Number(t.TiO2)
      t.MnO = Number(t.MnO)
      t.FeO = Number(t.FeO)
      t.CuO = Number(t.CuO)
      t.ZnO = Number(t.ZnO)
      t.As2O3 = Number(t.As2O3)
      t.SnO2 = Number(t.SnO2)
      t.PbO = Number(t.PbO)
      t.other = Number(t.other)
      this.axios.put('/api/minechemistryinfo/' + id, t, {
        params: {
          token: this.token
        }
      })
        .then(res => {
          if (res.status == 200) {
            for (let i = 0; i < this.mineChemistryInfos.length; ++ i) {
              if (this.mineChemistryInfos[i].id == id) {
                this.$set(this.mineChemistryInfos, i, t)
                break
              }
            }
            this.$message.success('修改' + id + '成功！')
          }
          else {
            this.$message.error('出错啦！')
          }
        })
      this.editChemistryModel[id] = false
      this.nowEditChemistry = null
    },
    cancelChemistryEdit(id) {
      this.editChemistryModel[id] = false
      this.nowEditChemistry= null
    },
    deleteChemistry(id) {
      this.axios.delete('/api/minechemistryinfo/' + id, {
        params: {
          token: this.token
        }
      })
        .then(res => {
          if (res.status == 200) {
            this.mineChemistryInfos = this.mineChemistryInfos.filter(v => v.id != id || v.temp)
            this.$message.success('删除' + id + '成功！')
          }
          else {
            this.$message.error('出错啦！')
          }
        })
    },
    editChemistrySingle(id) {
      if (this.nowEditChemistrySingle) {
        this.$message.warning('您正在编辑' + this.nowEditChemistrySingle.id + '，请优先完成')
        return
      }
      let mi = this.mineChemistrySingleInfos.filter(v => v.id == id)[0]
      this.nowEditChemistrySingle = deepObjCopy(mi)
      this.editChemistrySingleModel[id] = true
    },
    submitChemistrySingleEdit(id) {
      let t = this.nowEditChemistrySingle
      t.C = Number(t.C)
      t.Na = Number(t.Na)
      t.Mg = Number(t.Mg)
      t.Al = Number(t.Al)
      t.Si = Number(t.Si)
      t.P = Number(t.P)
      t.S = Number(t.S)
      t.Cl = Number(t.Cl)
      t.K = Number(t.K)
      t.Ca = Number(t.Ca)
      t.Ti = Number(t.Ti)
      t.V = Number(t.V)
      t.Mn = Number(t.Mn)
      t.Fe = Number(t.Fe)
      t.Co = Number(t.Co)
      t.Ni = Number(t.Ni)
      t.Cu = Number(t.Cu)
      t.Zn = Number(t.Zn)
      t.As = Number(t.As)
      t.Ag = Number(t.Ag)
      t.Sn = Number(t.Sn)
      t.Sb = Number(t.Sb)
      t.Au = Number(t.Au)
      t.Hg = Number(t.Hg)
      t.Pb = Number(t.Pb)
      t.other = Number(t.other)
      this.axios.put('/api/minechemistryinfosingle/' + id, t, {
        params: {
          token: this.token
        }
      })
        .then(res => {
          if (res.status == 200) {
            for (let i = 0; i < this.mineChemistrySingleInfos.length; ++ i) {
              if (this.mineChemistrySingleInfos[i].id == id) {
                this.$set(this.mineChemistrySingleInfos, i, t)
                break
              }
            }
            this.$message.success('修改' + id + '成功！')
          }
          else {
            this.$message.error('出错啦！')
          }
        })
      this.editChemistrySingleModel[id] = false
      this.nowEditChemistrySingle = null
    },
    cancelChemistrySingleEdit(id) {
      this.editChemistrySingleModel[id] = false
      this.nowEditChemistrySingle= null
    },
    deleteChemistrySingle(id) {
      this.axios.delete('/api/minechemistryinfosingle/' + id, {
        params: {
          token: this.token
        }
      })
        .then(res => {
          if (res.status == 200) {
            this.mineChemistrySingleInfos = this.mineChemistrySingleInfos.filter(v => v.id != id || v.temp)
            this.$message.success('删除' + id + '成功！')
          }
          else {
            this.$message.error('出错啦！')
          }
        })
    },
    editThermal(id) {
      if (this.nowEditThermal) {
        this.$message.warning('您正在编辑' + this.nowEditThermal.id + '，请优先完成')
        return
      }
      let mi = this.mineThermalInfos.filter(v => v.id == id)[0]
      this.nowEditThermal = deepObjCopy(mi)
      this.editThermalModel[id] = true
    },
    submitThermalEdit(id) {
      let t = this.nowEditThermal
      t.melting = t.melting ? Number(t.melting) : null
      t.fireResis = t.fireResis ? Number(t.fireResis) : null
      t.termTemper = t.termTemper ? Number(t.termTemper) : null
      t.data = t.data ? t.data : null
      t.surveImage = t.surveImage ? t.surveImage : null
      this.axios.put('/api/minethermalinfo/' + id, t, {
        params: {
          token: this.token
        }
      })
        .then(res => {
          if (res.status == 200) {
            for (let i = 0; i < this.mineThermalInfos.length; ++ i) {
              if (this.mineThermalInfos[i].id == id) {
                this.$set(this.mineThermalInfos, i, t)
                break
              }
            }
            this.$message.success('修改' + id + '成功！')
          }
          else {
            this.$message.error('出错啦！')
          }
        })
      this.editThermalModel[id] = false
      this.nowEditThermal = null
    },
    cancelThermalEdit(id) {
      this.editThermalModel[id] = false
      this.nowEditThermal= null
    },
    deleteThermal(id) {
      this.axios.delete('/api/minethermalinfo/' + id, {
        params: {
          token: this.token
        }
      })
        .then(res => {
          if (res.status == 200) {
            this.mineThermalInfos = this.mineThermalInfos.filter(v => v.id != id || v.temp)
            this.$message.success('删除' + id + '成功！')
          }
          else {
            this.$message.error('出错啦！')
          }
        })
    },
    handleExcelUploadSuccess(res) {
      this.nowEditThermal.data = res.data
    },
    handleExcelUploadError(err, file) {
      this.$message.error(file.name + '没有上传成功：' + JSON.parse(err.message).msg)
    },
    handleImgUploadSuccess(res) {
      this.nowEditThermal.surveImage = res.data[0]
    },
    handleImgUploadError(err, file) {
      this.$message.error(file.name + '没有上传成功：' + JSON.parse(err.message).msg)
    },
    editSurvey(id) {
      if (this.nowEditSurvey) {
        this.$message.warning('您正在编辑' + this.nowEditSurvey.id + '，请优先完成')
        return
      }
      let mi = this.mineSurveyInfos.filter(v => v.id == id)[0]
      this.nowEditSurvey = deepObjCopy(mi)
      this.editSurveyModel[id] = true
    },
    submitSurveyEdit(id) {
      let t = this.nowEditSurvey
      t.debris_0um = t.debris_0um ? Number(t.debris_0um) : null
      t.debris_67um = t.debris_67um ? Number(t.debris_67um) : null
      t.debris_167um = t.debris_167um ? Number(t.debris_167um) : null
      t.debris_501um = t.debris_501um ? Number(t.debris_501um) : null
      t.debris_1002um = t.debris_1002um ? Number(t.debris_1002um) : null
      t.hollow_0um = t.hollow_0um ? Number(t.hollow_0um) : null
      t.hollow_67um = t.hollow_67um ? Number(t.hollow_67um) : null
      t.hollow_501um = t.hollow_501um ? Number(t.hollow_501um) : null
      t.hollow_1002um = t.hollow_1002um ? Number(t.hollow_1002um) : null
      t.hollow_2004um = t.hollow_2004um ? Number(t.hollow_2004um) : null
      this.axios.put('/api/minesurveyinfo/' + id, t, {
        params: {
          token: this.token
        }
      })
        .then(res => {
          if (res.status == 200) {
            for (let i = 0; i < this.mineSurveyInfos.length; ++ i) {
              if (this.mineSurveyInfos[i].id == id) {
                this.$set(this.mineSurveyInfos, i, t)
                break
              }
            }
            this.$message.success('修改' + id + '成功！')
          }
          else {
            this.$message.error('出错啦！')
          }
        })
      this.editSurveyModel[id] = false
      this.nowEditSurvey = null
    },
    cancelSurveyEdit(id) {
      this.editSurveyModel[id] = false
      this.nowEditSurvey= null
    },
    deleteSurvey(id) {
      this.axios.delete('/api/minesurveyinfo/' + id, {
        params: {
          token: this.token
        }
      })
        .then(res => {
          if (res.status == 200) {
            this.mineSurveyInfos = this.mineSurveyInfos.filter(v => v.id != id || v.temp)
            this.$message.success('删除' + id + '成功！')
          }
          else {
            this.$message.error('出错啦！')
          }
        })
    },
    exportTableData() {
      // TODO 导出方法修改
      var wb = xlsx.utils.book_new()
      var temp = []
      this.mineContentInfos.forEach(v => {
        temp.push({
          '样品号': v.id,
          '黏土': v.clay,
          '粉砂': v.quartz,
          '石英': v.sand_quartz,
          '长石': v.sand_feldspar,
          '其他矿物': v.sand_other,
          '小计': this.sum([v.sand_quartz, v.sand_feldspar, v.sand_other]),
          '岩屑': v.debris,
          '闭气孔': v.hollow_close,
          '开气孔': v.hollow_open,
          '贯通气孔': v.hollow_through
        })
      })
      var ws = xlsx.utils.json_to_sheet(temp)
      xlsx.utils.book_append_sheet(wb, ws, '3.矿物含量信息')
      temp = []
      var temp2 = []
      this.mineSurveyInfos.forEach(v => {
        temp.push({
          '样品号': v.id,
          '≤67μm': v.debrisData['≤67μm'],
          '67-167μm': v.debrisData['67-167μm'],
          '167-501': v.debrisData['167-501'],
          '501-1002': v.debrisData['501-1002'],
          '≥1002': v.debrisData['≥1002']
        })
        temp2.push({
          '样品号': v.id,
          '≤167': v.hollowData['≤167'],
          '167-501': v.hollowData['167-501'],
          '501-1002': v.hollowData['501-1002'],
          '1002-2004': v.hollowData['1002-2004'],
          '＞2004': v.hollowData['＞2004']
        })
      })
      ws = xlsx.utils.json_to_sheet(temp)
      xlsx.utils.book_append_sheet(wb, ws, '4.矿物测量数据-岩屑直径分布')
      ws = xlsx.utils.json_to_sheet(temp2)
      xlsx.utils.book_append_sheet(wb, ws, '4.矿物测量数据-空洞长度分布')
      temp = []
      this.mineXRDInfos.forEach(v => {
        temp.push({
          '样品编号': v.id,
          '类型': v.type,
          '石英': v.quartz,
          '钠长石': v.albite,
          '钾长石': v.potashFeldspar,
          '云母': v.mica,
          '闪石': v.amphibole,
          '赤铁矿': v.hematite,
          '磁铁矿': v.magnetite,
          '白云石': v.dolomite,
          '方沸石': v.analcite,
          '磷石英': v.tridymite,
          '方石英': v.cristobalite,
          '莫来石': v.mullite
        })
      })
      ws = xlsx.utils.json_to_sheet(temp)
      xlsx.utils.book_append_sheet(wb, ws, '5.XRD分析数据')
      temp = []
      this.mineChemistryInfos.forEach(v => {
        temp.push({
          '样品号': v.id,
          '类型': v.type,
          'Na₂O': v.Na2O,
          'MgO': v.MgO,
          'Al₂O₃': v.Al2O3,
          'SiO₂': v.SiO2,
          'K₂O': v.K2O,
          'CaO': v.CaO,
          'Fe₂O₃': v.Fe2O3
        })
      })
      ws = xlsx.utils.json_to_sheet(temp)
      xlsx.utils.book_append_sheet(wb, ws, '6.化学成分数据')
      temp = []
      this.mineThermalInfos.forEach(v => {
        temp.push({
          '样品号': v.id,
          '终止温度': v.termTemper,
          '耐火度': v.fireResis,
          '热分析数据': v.data
          // '热分析曲线': '' //v.surveImage
        })
      })
      ws = xlsx.utils.json_to_sheet(temp)
      xlsx.utils.book_append_sheet(wb, ws, '8.热分析')
      xlsx.writeFileXLSX(wb, `Export-EXP-${new Date().toISOString().split('T')[0]}.xlsx`)
    }
  }
}
</script>
