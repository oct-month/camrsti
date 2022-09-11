<template>
  <div id="ExperimentView">
    <h3>矿物含量信息</h3>
    <el-table
      :data="mineContentInfos"
      :span-method="mineContentSpan"
      stripe
      border
      style="width: 100%">
      <template v-if="mineContentInfos.length">
        <el-table-column prop="id" label="样品号" width="80"></el-table-column>
        <el-table-column prop="sampleName" label="样品名称" width="90"></el-table-column>
        <el-table-column prop="clay" label="黏土基质" miniwidth="100"></el-table-column>
        <el-table-column prop="quartz" label="石英粉砂" miniwidth="100"></el-table-column>
        <el-table-column label="砂">
          <el-table-column prop="sand.quartz" label="石英" miniwidth="100"></el-table-column>
          <el-table-column prop="sand.feldspar" label="长石" miniwidth="100"></el-table-column>
          <el-table-column prop="sand.Ominerals" label="其他矿物" miniwidth="100"></el-table-column>
          <el-table-column label="小计" miniwidth="100">
            <template slot-scope="scope">
              {{ sum(Object.values(scope.row.sand)) }}
            </template>
          </el-table-column>
        </el-table-column>
        <el-table-column prop="debris" label="岩屑" miniwidth="100"></el-table-column>
        <el-table-column prop="hollow" label="空洞" miniwidth="100"></el-table-column>
      </template>
      <template v-else>
        <el-table-column label="样品号" width="80"></el-table-column>
        <el-table-column label="样品名称" width="90"></el-table-column>
        <el-table-column label="黏土基质" miniwidth="100"></el-table-column>
        <el-table-column label="石英粉砂" miniwidth="100"></el-table-column>
        <el-table-column label="砂">
          <el-table-column label="石英" miniwidth="100"></el-table-column>
          <el-table-column label="长石" miniwidth="100"></el-table-column>
          <el-table-column label="其他矿物" miniwidth="100"></el-table-column>
          <el-table-column label="小计" miniwidth="100"></el-table-column>
        </el-table-column>
        <el-table-column label="岩屑" miniwidth="100"></el-table-column>
        <el-table-column label="空洞" miniwidth="100"></el-table-column>
      </template>
    </el-table>

    <hr>

    <h3>矿物测量数据</h3>

    岩屑直径分布
    <el-table
      :data="mineSurveyInfos.debrisData"
      stripe
      border
      style="width: 100%">
      <template v-if="mineSurveyInfos.debrisData.length">
        <el-table-column prop="id" label="样品号" width="80"></el-table-column>
        <el-table-column v-for="key in Object.keys(mineSurveyInfos.debrisData[0]).filter(x => x != 'id')" :key="key" :prop="key" :label="key" miniwidth="100"></el-table-column>
      </template>
    </el-table>
    空洞长度分布
    <el-table
      :data="mineSurveyInfos.hollowData"
      stripe
      border
      style="width: 100%">
      <template v-if="mineSurveyInfos.hollowData.length">
        <el-table-column prop="id" label="样品号" width="110"></el-table-column>
        <el-table-column v-for="key in Object.keys(mineSurveyInfos.hollowData[0]).filter(x => x != 'id')" :key="key" :prop="key" :label="key" miniwidth="100"></el-table-column>
      </template>
    </el-table>

    <hr>

    <h3>XRD分析数据</h3>

    <el-table
      :data="mineXRDInfos"
      stripe
      border
      style="width: 100%">
      <template v-if="mineXRDInfos.length">
        <el-table-column prop="id" label="样品编号" width="80"></el-table-column>
        <el-table-column prop="type" label="类型" width="90"></el-table-column>
        <el-table-column prop="quartz" label="石英" miniwidth="100">
          <template slot-scope="scope">
            {{ scope.row.quartz ? scope.row.quartz + '%' : '' }}
          </template>
        </el-table-column>
        <el-table-column prop="albite" label="钠长石" miniwidth="100">
          <template slot-scope="scope">
            {{ scope.row.albite ? scope.row.albite + '%' : '' }}
          </template>
        </el-table-column>
        <el-table-column prop="potashFeldspar" label="钾长石" miniwidth="100">
          <template slot-scope="scope">
            {{ scope.row.potashFeldspar ? scope.row.potashFeldspar + '%' : '' }}
          </template>
        </el-table-column>
        <el-table-column prop="mica" label="云母" miniwidth="100">
          <template slot-scope="scope">
            {{ scope.row.mica ? scope.row.mica + '%' : '' }}
          </template>
        </el-table-column>
        <el-table-column prop="amphibole" label="闪石" miniwidth="100">
          <template slot-scope="scope">
            {{ scope.row.amphibole ? scope.row.amphibole + '%' : '' }}
          </template>
        </el-table-column>
        <el-table-column prop="hematite" label="赤铁矿" miniwidth="100">
          <template slot-scope="scope">
            {{ scope.row.hematite ? scope.row.hematite + '%' : '' }}
          </template>
        </el-table-column>
        <el-table-column prop="magnetite" label="磁铁矿" miniwidth="100">
          <template slot-scope="scope">
            {{ scope.row.magnetite ? scope.row.magnetite + '%' : '' }}
          </template>
        </el-table-column>
        <el-table-column prop="dolomite" label="白云石" miniwidth="100">
          <template slot-scope="scope">
            {{ scope.row.dolomite ? scope.row.dolomite + '%' : '' }}
          </template>
        </el-table-column>
        <el-table-column prop="analcite" label="方沸石" miniwidth="100">
          <template slot-scope="scope">
            {{ scope.row.analcite ? scope.row.analcite + '%' : '' }}
          </template>
        </el-table-column>
        <el-table-column prop="tridymite" label="磷石英" miniwidth="100">
          <template slot-scope="scope">
            {{ scope.row.tridymite ? scope.row.tridymite + '%' : '' }}
          </template>
        </el-table-column>
        <el-table-column prop="cristobalite" label="方石英" miniwidth="100">
          <template slot-scope="scope">
            {{ scope.row.cristobalite ? scope.row.cristobalite + '%' : '' }}
          </template>
        </el-table-column>
        <el-table-column prop="mullite" label="莫来石" miniwidth="100">
          <template slot-scope="scope">
            {{ scope.row.mullite ? scope.row.mullite + '%' : '' }}
          </template>
        </el-table-column>
      </template>
      <template v-else>
        <el-table-column label="样品编号" width="80"></el-table-column>
        <el-table-column label="类型" width="90"></el-table-column>
        <el-table-column label="石英" miniwidth="100"></el-table-column>
        <el-table-column label="钠长石" miniwidth="100"></el-table-column>
        <el-table-column label="钾长石" miniwidth="100"></el-table-column>
        <el-table-column label="云母" miniwidth="100"></el-table-column>
        <el-table-column label="闪石" miniwidth="100"></el-table-column>
        <el-table-column label="赤铁矿" miniwidth="100"></el-table-column>
        <el-table-column label="磁铁矿" miniwidth="100"></el-table-column>
        <el-table-column label="白云石" miniwidth="100"></el-table-column>
        <el-table-column label="方沸石" miniwidth="100"></el-table-column>
        <el-table-column label="磷石英" miniwidth="100"></el-table-column>
        <el-table-column label="方石英" miniwidth="100"></el-table-column>
        <el-table-column label="莫来石" miniwidth="100"></el-table-column>
      </template>
    </el-table>

    <hr>

    <h3>化学成分数据</h3>

    <el-table
      :data="mineChemistryInfos"
      stripe
      border
      style="width: 100%">
      <template v-if="mineChemistryInfos.length">
        <el-table-column prop="id" label="样品号" width="80"></el-table-column>
        <el-table-column prop="type" label="类型" width="90"></el-table-column>
        <el-table-column prop="Na2O" label="Na₂O" miniwidth="100"></el-table-column>
        <el-table-column prop="MgO" label="MgO" miniwidth="100"></el-table-column>
        <el-table-column prop="Al2O3" label="Al₂O₃" miniwidth="100"></el-table-column>
        <el-table-column prop="SiO2" label="SiO₂" miniwidth="100"></el-table-column>
        <el-table-column prop="K2O" label="K₂O" miniwidth="100"></el-table-column>
        <el-table-column prop="CaO" label="CaO" miniwidth="100"></el-table-column>
        <el-table-column prop="Fe2O3" label="Fe₂O₃" miniwidth="100"></el-table-column>
      </template>
      <template v-else>
        <el-table-column label="样品号" width="80"></el-table-column>
        <el-table-column label="类型" width="90"></el-table-column>
        <el-table-column label="Na₂O" miniwidth="100"></el-table-column>
        <el-table-column label="MgO" miniwidth="100"></el-table-column>
        <el-table-column label="Al₂O₃" miniwidth="100"></el-table-column>
        <el-table-column label="SiO₂" miniwidth="100"></el-table-column>
        <el-table-column label="K₂O" miniwidth="100"></el-table-column>
        <el-table-column label="CaO" miniwidth="100"></el-table-column>
        <el-table-column label="Fe₂O₃" miniwidth="100"></el-table-column>
      </template>
    </el-table>

    <h3>热分析</h3>

    <el-table
      :data="mineThermalInfos"
      :span-method="mineThermalSpan"
      stripe
      border
      style="width: 100%">
      <template v-if="mineThermalInfos.length">
        <el-table-column prop="id" label="样品号" width="80"></el-table-column>
        <el-table-column prop="termTemper" label="终止温度" miniwidth="100"></el-table-column>
        <el-table-column prop="fireResis" label="耐火度" miniwidth="100"></el-table-column>
        <el-table-column prop="data" label="热分析数据" miniwidth="100"></el-table-column>
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
      </template>
      <template v-else>
        <el-table-column label="样品号" width="80"></el-table-column>
        <el-table-column label="终止温度" miniwidth="100"></el-table-column>
        <el-table-column label="耐火度" miniwidth="100"></el-table-column>
        <el-table-column label="热分析数据" miniwidth="100"></el-table-column>
        <el-table-column label="热分析曲线" miniwidth="400"></el-table-column>
      </template>
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
export default {
  name: "ExperimentPage",
  props: {
    sampleId: String
  },
  data() {
    return {
      mineContentInfos: [],
      mineSurveyInfos: {
        debrisData: [],
        hollowData: []
      },
      mineXRDInfos: [],
      mineChemistryInfos: [],
      mineThermalInfos: []
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
          var obj = {
            id: '',
            clay: 0,
            debris: 0,
            hollow: 0,
            quartz: 0,
            sampleName: null,
            sand: {
              Ominerals: 0,
              feldspar: 0,
              quartz: 0
            }
          }
          temp.forEach(v => {
            obj.clay += v.clay
            obj.debris += v.debris            
            obj.hollow += v.hollow
            obj.quartz += v.quartz 
            obj.sand.Ominerals += v.sand.Ominerals
            obj.sand.feldspar += v.sand.feldspar
            obj.sand.quartz += v.sand.quartz
          })
          obj.clay /= temp.length
          obj.debris /= temp.length
          obj.hollow /= temp.length
          obj.quartz /= temp.length
          obj.sand.Ominerals /= temp.length
          obj.sand.feldspar /= temp.length
          obj.sand.quartz /= temp.length
          obj.id = '平均值'
          var obj2 = {
            id: '',
            clay: 0,
            debris: 0,
            hollow: 0,
            quartz: 0,
            sampleName: null,
            sand: {
              Ominerals: 0,
              feldspar: 0,
              quartz: 0
            }
          }
          temp.forEach(v => {
            obj2.clay += Math.pow(v.clay - obj.clay, 2)
            obj2.debris += Math.pow(v.debris - obj.debris, 2)
            obj2.hollow += Math.pow(v.hollow - obj.hollow, 2)
            obj2.quartz  += Math.pow(v.quartz  - obj.quartz, 2)
            obj2.sand.Ominerals += Math.pow(v.sand.Ominerals - obj.sand.Ominerals, 2)
            obj2.sand.feldspar += Math.pow(v.sand.feldspar - obj.sand.feldspar, 2)
            obj2.sand.quartz += Math.pow(v.sand.quartz - obj.sand.quartz, 2)
          })
          obj2.clay = Math.pow(obj2.clay / temp.length, 0.5) / obj.clay
          obj2.debris = Math.pow(obj2.debris / temp.length, 0.5) / obj.debris
          obj2.hollow = Math.pow(obj2.hollow / temp.length, 0.5) / obj.hollow
          obj2.quartz  = Math.pow(obj2.quartz  / temp.length, 0.5) / obj.quartz 
          obj2.sand.Ominerals = Math.pow(obj2.sand.Ominerals / temp.length, 0.5) / obj.sand.Ominerals
          obj2.sand.feldspar = Math.pow(obj2.sand.feldspar / temp.length, 0.5) / obj.sand.feldspar
          obj2.sand.quartz = Math.pow(obj2.sand.quartz / temp.length, 0.5) / obj.sand.quartz
          obj2.id = '变异系数'
          temp.push(obj)
          temp.push(obj2)
          this.mineContentInfos = temp
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
        }
        else {
          this.$message.error('出错啦！')
        }
      })
    this.axios.get('/api/minechemistryinfo/' + this.sampleId)
      .then(res => {
        if (res.status == 200 && res.data.status == 200) {
          this.mineChemistryInfos = res.data.data
        }
        else {
          this.$message.error('出错啦！')
        }
      })
    this.axios.get('/api/minethermalinfo/' + this.sampleId)
      .then(res => {
        if (res.status == 200 && res.data.status == 200) {
          this.mineThermalInfos = res.data.data
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
      if (rowIndex == 0 && columnIndex >= 4) {
        // console.log(this.mineThermalInfos.length);
        return {
          rowspan: this.mineThermalInfos.length,
          colspan: 1
        }
      }
      else if (rowIndex > 0 && columnIndex >= 4) {
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
    }
  }
}
</script>
