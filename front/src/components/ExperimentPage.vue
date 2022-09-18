<template>
  <div id="ExperimentView">
    <h3>矿物含量信息</h3>
    <el-table
      :data="mineContentInfos"
      :span-method="mineContentSpan"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="id" label="样品号" width="80"></el-table-column>
      <el-table-column prop="sampleName" label="样品名称" width="90">
        <template slot-scope="scope">
          <el-input v-if="editContentModel[scope.row.id]" v-model="nowEditContent.sampleName"></el-input>
          <span v-else>
            {{ scope.row.sampleName }}
          </span>
        </template>
      </el-table-column>
      <el-table-column prop="clay" label="黏土基质" miniwidth="100">
        <template slot-scope="scope">
          <el-input v-if="editContentModel[scope.row.id]" v-model="nowEditContent.clay"></el-input>
          <span v-else>
            {{ scope.row.clay }}
          </span>
        </template>
      </el-table-column>
      <el-table-column prop="quartz" label="石英粉砂" miniwidth="100">
        <template slot-scope="scope">
          <el-input v-if="editContentModel[scope.row.id]" v-model="nowEditContent.quartz"></el-input>
          <span v-else>
            {{ scope.row.quartz }}
          </span>
        </template>
      </el-table-column>
      <el-table-column label="砂">
        <el-table-column prop="sand.quartz" label="石英" miniwidth="100">
          <template slot-scope="scope">
            <el-input v-if="editContentModel[scope.row.id]" v-model="nowEditContent.sand.quartz"></el-input>
            <span v-else>
              {{ scope.row.sand.quartz }}
            </span>
          </template>
        </el-table-column>
        <el-table-column prop="sand.feldspar" label="长石" miniwidth="100">
          <template slot-scope="scope">
            <el-input v-if="editContentModel[scope.row.id]" v-model="nowEditContent.sand.feldspar"></el-input>
            <span v-else>
              {{ scope.row.sand.feldspar }}
            </span>
          </template>
        </el-table-column>
        <el-table-column prop="sand.Ominerals" label="其他矿物" miniwidth="100">
          <template slot-scope="scope">
            <el-input v-if="editContentModel[scope.row.id]" v-model="nowEditContent.sand.Ominerals"></el-input>
            <span v-else>
              {{ scope.row.sand.Ominerals }}
            </span>
          </template>
        </el-table-column>
        <el-table-column label="小计" miniwidth="100">
          <template slot-scope="scope">
            <span v-if="!editContentModel[scope.row.id]">{{ sum(Object.values(scope.row.sand)) }}</span>
          </template>
        </el-table-column>
      </el-table-column>
      <el-table-column prop="debris" label="岩屑" miniwidth="100">
        <template slot-scope="scope">
          <el-input v-if="editContentModel[scope.row.id]" v-model="nowEditContent.debris"></el-input>
          <span v-else>
            {{ scope.row.debris }}
          </span>
        </template>
      </el-table-column>
      <el-table-column prop="hollow" label="空洞" miniwidth="100">
        <template slot-scope="scope">
          <el-input v-if="editContentModel[scope.row.id]" v-model="nowEditContent.hollow"></el-input>
          <span v-else>
            {{ scope.row.hollow }}
          </span>
        </template>
      </el-table-column>
      <el-table-column prop="other" label="其他" miniwidth="100">
        <template slot-scope="scope">
          <el-input v-if="editContentModel[scope.row.id]" v-model="nowEditContent.other"></el-input>
          <span v-else>
            {{ scope.row.other }}
          </span>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="118">
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

    <h3>矿物测量数据</h3>

    岩屑直径分布
    <el-table
      :data="mineSurveyInfos.debrisData"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="id" label="样品号" width="80"></el-table-column>
      <!-- <el-table-column v-for="key in Object.keys(mineSurveyInfos.debrisData[0]).filter(x => x != 'id')" :key="key" :prop="key" :label="key" miniwidth="100"></el-table-column> -->
      <el-table-column prop="≤67μm" label="≤67μm" miniwidth="100"></el-table-column>
      <el-table-column prop="67-167μm" label="67-167μm" miniwidth="100"></el-table-column>
      <el-table-column prop="167-501" label="167-501" miniwidth="100"></el-table-column>
      <el-table-column prop="501-1002" label="501-1002" miniwidth="100"></el-table-column>
      <el-table-column prop="≥1002" label="≥1002" miniwidth="100"></el-table-column>
    </el-table>
    空洞长度分布
    <el-table
      :data="mineSurveyInfos.hollowData"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="id" label="样品号" width="80"></el-table-column>
      <!-- <el-table-column v-for="key in Object.keys(mineSurveyInfos.hollowData[0]).filter(x => x != 'id')" :key="key" :prop="key" :label="key" miniwidth="100"></el-table-column> -->
      <el-table-column prop="≤167" label="≤167" miniwidth="100"></el-table-column>
      <el-table-column prop="167-501" label="167-501" miniwidth="100"></el-table-column>
      <el-table-column prop="501-1002" label="501-1002" miniwidth="100"></el-table-column>
      <el-table-column prop="1002-2004" label="1002-2004" miniwidth="100"></el-table-column>
      <el-table-column prop="＞2004" label="＞2004" miniwidth="100"></el-table-column>
    </el-table>

    <hr>

    <h3>XRD分析数据</h3>

    <el-table
      :data="mineXRDInfos"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="id" label="样品编号" width="80"></el-table-column>
      <el-table-column prop="type" label="类型" width="90">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.type"></el-input>
          <span v-else>{{ scope.row.type }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="quartz" label="石英" miniwidth="100">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.quartz"></el-input>
          <span v-else>{{ scope.row.quartz ? scope.row.quartz + '%' : '' }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="albite" label="钠长石" miniwidth="100">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.albite"></el-input>
          <span v-else>{{ scope.row.albite ? scope.row.albite + '%' : '' }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="potashFeldspar" label="钾长石" miniwidth="100">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.potashFeldspar"></el-input>
          <span v-else>{{ scope.row.potashFeldspar ? scope.row.potashFeldspar + '%' : '' }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="mica" label="云母" miniwidth="100">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.mica"></el-input>
          <span v-else>{{ scope.row.mica ? scope.row.mica + '%' : '' }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="amphibole" label="闪石" miniwidth="100">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.amphibole"></el-input>
          <span v-else>{{ scope.row.amphibole ? scope.row.amphibole + '%' : '' }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="hematite" label="赤铁矿" miniwidth="100">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.hematite"></el-input>
          <span v-else>{{ scope.row.hematite ? scope.row.hematite + '%' : '' }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="magnetite" label="磁铁矿" miniwidth="100">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.magnetite"></el-input>
          <span v-else>{{ scope.row.magnetite ? scope.row.magnetite + '%' : '' }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="dolomite" label="白云石" miniwidth="100">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.dolomite"></el-input>
          <span v-else>{{ scope.row.dolomite ? scope.row.dolomite + '%' : '' }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="analcite" label="方沸石" miniwidth="100">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.analcite"></el-input>
          <span v-else>{{ scope.row.analcite ? scope.row.analcite + '%' : '' }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="tridymite" label="磷石英" miniwidth="100">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.tridymite"></el-input>
          <span v-else>{{ scope.row.tridymite ? scope.row.tridymite + '%' : '' }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="cristobalite" label="方石英" miniwidth="100">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.cristobalite"></el-input>
          <span v-else>{{ scope.row.cristobalite ? scope.row.cristobalite + '%' : '' }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="mullite" label="莫来石" miniwidth="100">
        <template slot-scope="scope">
          <el-input v-if="editXRDModel[scope.row.id]" v-model="nowEditXRD.mullite"></el-input>
          <span v-else>{{ scope.row.mullite ? scope.row.mullite + '%' : '' }}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="118">
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

    <h3>化学成分数据</h3>

    <el-table
      :data="mineChemistryInfos"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="id" label="样品号" width="80"></el-table-column>
      <el-table-column prop="type" label="类型" width="90">
        <template slot-scope="scope">
          <el-input v-if="editChemistryModel[scope.row.id]" v-model="nowEditChemistry.type"></el-input>
          <span v-else>{{ scope.row.type }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="Na2O" label="Na₂O" miniwidth="100">
        <template slot-scope="scope">
          <el-input v-if="editChemistryModel[scope.row.id]" v-model="nowEditChemistry.Na2O"></el-input>
          <span v-else>{{ scope.row.Na2O }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="MgO" label="MgO" miniwidth="100">
        <template slot-scope="scope">
          <el-input v-if="editChemistryModel[scope.row.id]" v-model="nowEditChemistry.MgO"></el-input>
          <span v-else>{{ scope.row.MgO }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="Al2O3" label="Al₂O₃" miniwidth="100">
        <template slot-scope="scope">
          <el-input v-if="editChemistryModel[scope.row.id]" v-model="nowEditChemistry.Al2O3"></el-input>
          <span v-else>{{ scope.row.Al2O3 }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="SiO2" label="SiO₂" miniwidth="100">
        <template slot-scope="scope">
          <el-input v-if="editChemistryModel[scope.row.id]" v-model="nowEditChemistry.SiO2"></el-input>
          <span v-else>{{ scope.row.SiO2 }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="K2O" label="K₂O" miniwidth="100">
        <template slot-scope="scope">
          <el-input v-if="editChemistryModel[scope.row.id]" v-model="nowEditChemistry.K2O"></el-input>
          <span v-else>{{ scope.row.K2O }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="CaO" label="CaO" miniwidth="100">
        <template slot-scope="scope">
          <el-input v-if="editChemistryModel[scope.row.id]" v-model="nowEditChemistry.CaO"></el-input>
          <span v-else>{{ scope.row.CaO }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="Fe2O3" label="Fe₂O₃" miniwidth="100">
        <template slot-scope="scope">
          <el-input v-if="editChemistryModel[scope.row.id]" v-model="nowEditChemistry.Fe2O3"></el-input>
          <span v-else>{{ scope.row.Fe2O3 }}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="118">
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

    <h3>热分析</h3>

    <el-table
      :data="mineThermalInfos"
      :span-method="mineThermalSpan"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="id" label="样品号" width="80"></el-table-column>
      <el-table-column prop="termTemper" label="终止温度" miniwidth="100">
        <template slot-scope="scope">
          <el-input v-if="editThermalModel[scope.row.id]" v-model="nowEditThermal.termTemper"></el-input>
          <span v-else>{{ scope.row.termTemper }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="fireResis" label="耐火度" miniwidth="100">
        <template slot-scope="scope">
          <el-input v-if="editThermalModel[scope.row.id]" v-model="nowEditThermal.fireResis"></el-input>
          <span v-else>{{ scope.row.fireResis }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="data" label="热分析数据" miniwidth="100"></el-table-column>
      <el-table-column label="操作" width="118">
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
      <el-table-column prop="surveImage" label="热分析曲线" miniwidth="400">
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
      </el-table-column>
    </el-table>
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
import { deepObjCopy } from '@/utils'
export default {
  name: "ExperimentPage",
  props: {
    sampleId: String
  },
  data() {
    return {
      mineContentInfos: [],
      editContentModel: {},
      deleteContentDialogVisible: {},
      nowEditContent: null,
      mineSurveyInfos: {
        debrisData: [],
        hollowData: []
      },
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
      mineThermalInfos: [],
      editThermalModel: {},
      deleteThermalDialogVisible: {},
      nowEditThermal: null,
    }
  },
  mounted() {
    if (!this.sampleId) {
      this.$message.error('出错啦！')
      return
    }
    this.axios.get('/api/minecontentinfo/' + this.sampleId)
      .then((res) => {
        if (res.status == 200 && res.data.status == 200) {
          if (res.data.data.length <= 0) {
            return
          }
          var temp = res.data.data
          temp.forEach(v => {
            this.$set(this.editContentModel, v.id, false)
            this.$set(this.deleteContentDialogVisible, v.id, false)
          })
          this.mineContentInfos = temp
          this.mineContentCompute()
        }
        else {
          this.$message.error('出错啦！')
        }
      })
    this.axios.get('/api/minesurveyinfo/' + this.sampleId)
      .then((res) => {
        if (res.status == 200 && res.data.status == 200) {
          var temp = res.data.data
          temp.forEach(v => {
            v.debrisData.id = v.id
            this.mineSurveyInfos.debrisData.push(v.debrisData)
            v.hollowData.id = v.id
            this.mineSurveyInfos.hollowData.push(v.hollowData)
            // TODO
            // this.$set(this.editSurveyModel, v.id, false)
            // this.$set(this.deleteSurveyDialogVisible, v.id, false)
          })
        }
        else {
          this.$message.error('出错啦！')
        }
      })
    this.axios.get('/api/minexrdinfo/' + this.sampleId)
      .then(res => {
        if (res.status == 200 && res.data.status == 200) {
          this.mineXRDInfos = res.data.data
          this.mineXRDInfos.forEach(v => {
            this.$set(this.editXRDModel, v.id, false)
            this.$set(this.deleteXRDDialogVisible, v.id, false)
          })
        }
        else {
          this.$message.error('出错啦！')
        }
      })
    this.axios.get('/api/minechemistryinfo/' + this.sampleId)
      .then(res => {
        if (res.status == 200 && res.data.status == 200) {
          this.mineChemistryInfos = res.data.data
          this.mineChemistryInfos.forEach(v => {
            this.$set(this.editChemistryModel, v.id, false)
            this.$set(this.deleteChemistryDialogVisible, v.id, false)
          })
        }
        else {
          this.$message.error('出错啦！')
        }
      })
    this.axios.get('/api/minethermalinfo/' + this.sampleId)
      .then(res => {
        if (res.status == 200 && res.data.status == 200) {
          this.mineThermalInfos = res.data.data
          this.mineThermalInfos.forEach(v => {
            this.$set(this.editThermalModel, v.id, false)
            this.$set(this.deleteThermalDialogVisible, v.id, false)
          })
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
            sampleName: null,
            clay: 0,
            debris: 0,
            hollow: 0,
            quartz: 0,
            sand: {
              Ominerals: 0,
              feldspar: 0,
              quartz: 0
            },
            other: 0,
            temp: true
          }
          temp.forEach(v => {
            obj.clay += v.clay
            obj.debris += v.debris            
            obj.hollow += v.hollow
            obj.quartz += v.quartz 
            obj.sand.Ominerals += v.sand.Ominerals
            obj.sand.feldspar += v.sand.feldspar
            obj.sand.quartz += v.sand.quartz
            obj.other += v.other
          })
          obj.clay /= temp.length
          obj.debris /= temp.length
          obj.hollow /= temp.length
          obj.quartz /= temp.length
          obj.sand.Ominerals /= temp.length
          obj.sand.feldspar /= temp.length
          obj.sand.quartz /= temp.length
          obj.other /= temp.length
          var obj2 = {
            id: '变异系数',
            clay: 0,
            debris: 0,
            hollow: 0,
            quartz: 0,
            sampleName: null,
            sand: {
              Ominerals: 0,
              feldspar: 0,
              quartz: 0
            },
            other: 0,
            temp: true
          }
          temp.forEach(v => {
            obj2.clay += Math.pow(v.clay - obj.clay, 2)
            obj2.debris += Math.pow(v.debris - obj.debris, 2)
            obj2.hollow += Math.pow(v.hollow - obj.hollow, 2)
            obj2.quartz  += Math.pow(v.quartz  - obj.quartz, 2)
            obj2.sand.Ominerals += Math.pow(v.sand.Ominerals - obj.sand.Ominerals, 2)
            obj2.sand.feldspar += Math.pow(v.sand.feldspar - obj.sand.feldspar, 2)
            obj2.sand.quartz += Math.pow(v.sand.quartz - obj.sand.quartz, 2)
            obj2.other += Math.pow(v.other - obj.other, 2)
          })
          obj2.clay = obj.clay ? Math.pow(obj2.clay / temp.length, 0.5) / obj.clay : null
          obj2.debris = obj.debris ? Math.pow(obj2.debris / temp.length, 0.5) / obj.debris : null
          obj2.hollow = obj.hollow ? Math.pow(obj2.hollow / temp.length, 0.5) / obj.hollow : null
          obj2.quartz  = obj.quartz  ? Math.pow(obj2.quartz  / temp.length, 0.5) / obj.quartz  : null
          obj2.sand.Ominerals = obj.sand.Ominerals ? Math.pow(obj2.sand.Ominerals / temp.length, 0.5) / obj.sand.Ominerals : null
          obj2.sand.feldspar = obj.sand.feldspar ? Math.pow(obj2.sand.feldspar / temp.length, 0.5) / obj.sand.feldspar : null
          obj2.sand.quartz = obj.sand.quartz ? Math.pow(obj2.sand.quartz / temp.length, 0.5) / obj.sand.quartz : null
          obj2.other = obj.other ? Math.pow(obj2.other / temp.length, 0.5) / obj.other : null
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
      t.clay = Number(t.clay)
      t.debris = Number(t.debris)
      t.hollow = Number(t.hollow)
      t.quartz = Number(t.quartz)
      t.sand.Ominerals = Number(t.sand.Ominerals)
      t.sand.feldspar = Number(t.sand.feldspar)
      t.sand.quartz = Number(t.sand.quartz)
      t.other = Number(t.other)
      this.axios.put('/api/minecontentinfo/' + id, t)
        .then(res => {
          if (res.status == 200 && res.data.status == 200) {
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
      this.axios.delete('/api/minecontentinfo/' + id)
        .then(res => {
          if (res.status == 200 && res.data.status == 200) {
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
      t.quartz = Number(t.quartz)  
      t.albite = Number(t.albite)  
      t.potashFeldspar = Number(t.potashFeldspar)  
      t.mica = Number(t.mica)  
      t.amphibole = Number(t.amphibole)  
      t.hematite = Number(t.hematite)  
      t.magnetite = Number(t.magnetite)  
      t.dolomite = Number(t.dolomite)  
      t.analcite = Number(t.analcite)  
      t.tridymite = Number(t.tridymite)  
      t.cristobalite = Number(t.cristobalite)
      t.mullite = Number(t.mullite)
      this.axios.put('/api/minexrdinfo/' + id, t)
        .then(res => {
          if (res.status == 200 && res.data.status == 200) {
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
      this.axios.delete('/api/minexrdinfo/' + id)
        .then(res => {
          if (res.status == 200 && res.data.status == 200) {
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
      t.K2O = Number(t.K2O)
      t.CaO = Number(t.CaO)
      t.Fe2O3 = Number(t.Fe2O3)
      this.axios.put('/api/minechemistryinfo/' + id, t)
        .then(res => {
          if (res.status == 200 && res.data.status == 200) {
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
      this.axios.delete('/api/minechemistryinfo/' + id)
        .then(res => {
          if (res.status == 200 && res.data.status == 200) {
            this.mineChemistryInfos = this.mineChemistryInfos.filter(v => v.id != id || v.temp)
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
      t.termTemper = Number(t.termTemper)
      t.fireResis = Number(t.fireResis)
      this.axios.put('/api/minethermalinfo/' + id, t)
        .then(res => {
          if (res.status == 200 && res.data.status == 200) {
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
      this.axios.delete('/api/minethermalinfo/' + id)
        .then(res => {
          if (res.status == 200 && res.data.status == 200) {
            this.mineThermalInfos = this.mineThermalInfos.filter(v => v.id != id || v.temp)
            this.$message.success('删除' + id + '成功！')
          }
          else {
            this.$message.error('出错啦！')
          }
        })
    }
  }
}
</script>
