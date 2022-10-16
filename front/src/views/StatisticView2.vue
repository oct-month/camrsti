<template>
  <div id="StatisticView2">
    <h4 align="left">矿物含量信息</h4>
    <el-table
      :data="mineContentInfos"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="id" label="样品号" width="110"></el-table-column>
      <el-table-column prop="sampleName" label="样品名称" width="90"></el-table-column>
      <el-table-column prop="clay" label="黏土基质" miniwidth="100"></el-table-column>
      <el-table-column prop="quartz" label="石英粉砂" miniwidth="100"></el-table-column>
      <el-table-column label="砂">
        <el-table-column prop="sand.quartz" label="石英" miniwidth="100"></el-table-column>
        <el-table-column prop="sand.feldspar" label="长石" miniwidth="100"></el-table-column>
        <el-table-column prop="sand.Ominerals" label="其他矿物" miniwidth="100"></el-table-column>
        <!-- <el-table-column label="小计" miniwidth="100">
          <template slot-scope="scope">
            {{ sum(Object.values(scope.row.sand)) }}
          </template>
        </el-table-column> -->
      </el-table-column>
      <el-table-column prop="debris" label="岩屑" miniwidth="100"></el-table-column>
      <el-table-column prop="hollow" label="空洞" miniwidth="100"></el-table-column>
      <el-table-column prop="other" label="其他" miniwidth="100"></el-table-column>
    </el-table>

    <hr>

    <h4 align="left">矿物测量数据</h4>

    岩屑直径分布
    <el-table
      :data="mineSurveyInfos"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="id" label="样品号" width="110"></el-table-column>
      <el-table-column prop="debrisData.≤67μm" label="≤67μm" miniwidth="100"></el-table-column>
      <el-table-column prop="debrisData.67-167μm" label="67-167μm" miniwidth="100"></el-table-column>
      <el-table-column prop="debrisData.167-501" label="167-501" miniwidth="100"></el-table-column>
      <el-table-column prop="debrisData.501-1002" label="501-1002" miniwidth="100"></el-table-column>
      <el-table-column prop="debrisData.≥1002" label="≥1002" miniwidth="100"></el-table-column>
    </el-table>

    空洞长度分布
    <el-table
      :data="mineSurveyInfos"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="id" label="样品号" width="110"></el-table-column>
      <el-table-column prop="hollowData.≤167" label="≤167" miniwidth="100"></el-table-column>
      <el-table-column prop="hollowData.167-501" label="167-501" miniwidth="100"></el-table-column>
      <el-table-column prop="hollowData.501-1002" label="501-1002" miniwidth="100"></el-table-column>
      <el-table-column prop="hollowData.1002-2004" label="1002-2004" miniwidth="100"></el-table-column>
      <el-table-column prop="hollowData.＞2004" label="＞2004" miniwidth="100"></el-table-column>
    </el-table>
  </div>
</template>

<style scoped>
#StatisticView2 {
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
  name: 'StatisticView2',
  data() {
    return {
      mineContentInfos: [],
      mineSurveyInfos: []
    }
  },
  mounted() {
    let ids = this.$store.state.statisticInfos
    if (ids.length > 0) {
      ids.forEach(id => {
        this.axios.get('/api/minecontentinfo/' + id)
          .then(res => {
            if (res.status == 200 && res.data.status == 200) {
              this.mineContentInfos.push.apply(this.mineContentInfos, res.data.data)
            }
            else {
              this.$message.error('出错啦！')
            }
          })
        this.axios.get('/api/minesurveyinfo/' + id)
          .then(res => {
            if (res.status == 200 && res.data.status == 200) {
              this.mineSurveyInfos.push.apply(this.mineSurveyInfos, res.data.data)
            }
            else {
              this.$message.error('出错啦！')
            }
          })
      })
    }
    else {
      this.axios.get('/api/minecontentinfo')
        .then(res => {
          if (res.status == 200 && res.data.status == 200) {
            this.mineContentInfos = res.data.data
          }
          else {
            this.$message.error('出错啦！')
          }
        })
      this.axios.get('/api/minesurveyinfo')
        .then(res => {
          if (res.status == 200 && res.data.status == 200) {
            this.mineSurveyInfos = res.data.data
          }
          else {
            this.$message.error('出错啦！')
          }
        })
    }
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
  }
}
</script>
