<template>
  <div id="ExperimentView">
    <h3>矿物含量信息</h3>
    <el-table
      v-if="mineContentInfos.length"
      :data="mineContentInfos"
      :span-method="mineContentSpan"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="id" label="样品号" width="200"></el-table-column>
      <el-table-column prop="sampleName" label="样品名称" width="110"></el-table-column>
      <el-table-column prop="clay" label="黏土基质" width="110"></el-table-column>
      <el-table-column prop="quartz" label="石英粉砂" width="110"></el-table-column>
      <el-table-column label="砂" width="110">
        <el-table-column prop="sand.quartz" label="石英" width="110"></el-table-column>
        <el-table-column prop="sand.feldspar" label="长石" width="110"></el-table-column>
        <el-table-column prop="sand.Ominerals" label="其他矿物" width="110"></el-table-column>
        <el-table-column label="小计" width="110">
          <template slot-scope="scope">
            {{ sum(Object.values(scope.row.sand)) }}
          </template>
        </el-table-column>
      </el-table-column>
      <el-table-column prop="debris" label="岩屑" width="110"></el-table-column>
      <el-table-column prop="hollow" label="空洞" width="110"></el-table-column>
    </el-table>

    <hr>

    <h3>矿物测量数据</h3>

    岩屑直径分布
    <el-table
      v-if="mineSurveyInfos.debrisData.length"
      :data="mineSurveyInfos.debrisData"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="id" label="样品号" width="110"></el-table-column>
      <el-table-column v-for="key in Object.keys(mineSurveyInfos.debrisData[0]).filter(x => x != 'id')" :key="key" :prop="key" :label="key" width="200"></el-table-column>
    </el-table>
    空洞长度分布
    <el-table
      v-if="mineSurveyInfos.hollowData.length"
      :data="mineSurveyInfos.hollowData"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="id" label="样品号" width="110"></el-table-column>
      <el-table-column v-for="key in Object.keys(mineSurveyInfos.hollowData[0]).filter(x => x != 'id')" :key="key" :prop="key" :label="key" width="200"></el-table-column>
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
  name: "ExperimentView",
  data() {
    return {
      mineContentInfos: [],
      mineSurveyInfos: {
        debrisData: [],
        hollowData: []
      }
    }
  },
  mounted() {
    if (!this.$route.query.id) {
      this.$router.push('/')
      return
    }
    this.axios.get('/api/minecontentinfo/' + this.$route.query.id)
      .then((res) => {
        if (res.status == 200 && res.data.status == 200) {
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
    this.axios.get('/api/minesurveyinfo/' + this.$route.query.id)
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
    }
  }
}
</script>
