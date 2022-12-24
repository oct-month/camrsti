<template>
  <div id="StatisticView2">
    <h4 align="left">矿物测量数据</h4>

    <el-table
      :data="mineSurveyInfos"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="id" label="样品号" width="110"></el-table-column>
      <!-- 岩屑直径分布 -->
      <el-table-column label="岩屑直径分布">
        <el-table-column prop="debrisData.≤67μm" label="≤67μm" miniwidth="100"></el-table-column>
        <el-table-column prop="debrisData.67-167μm" label="67-167μm" miniwidth="100"></el-table-column>
        <el-table-column prop="debrisData.167-501" label="167-501" miniwidth="100"></el-table-column>
        <el-table-column prop="debrisData.501-1002" label="501-1002" miniwidth="100"></el-table-column>
        <el-table-column prop="debrisData.≥1002" label="≥1002" miniwidth="100"></el-table-column>
      </el-table-column>
      <!-- 空洞长度分布 -->
      <el-table-column label="空洞长度分布">
        <el-table-column prop="hollowData.≤167" label="≤167" miniwidth="100"></el-table-column>
        <el-table-column prop="hollowData.167-501" label="167-501" miniwidth="100"></el-table-column>
        <el-table-column prop="hollowData.501-1002" label="501-1002" miniwidth="100"></el-table-column>
        <el-table-column prop="hollowData.1002-2004" label="1002-2004" miniwidth="100"></el-table-column>
        <el-table-column prop="hollowData.＞2004" label="＞2004" miniwidth="100"></el-table-column>
      </el-table-column>
    </el-table>

    <div style="float:right;">
      导出：
      <el-button size="small" type="success" icon="el-icon-download" @click="exportExtData"></el-button>
    </div>
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
import xlsx from 'xlsx'

export default {
  name: 'StatisticView2',
  data() {
    return {
      token: '',
      mineSurveyInfos: []
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

    let ids = this.$store.state.statisticInfos
    if (ids.length > 0) {
      ids.forEach(id => {
        this.axios.get('/api/minesurveyinfo/' + id, {
          params: {
            token: this.token
          }
        })
          .then(res => {
            if (res.status == 200) {
              this.mineSurveyInfos.push.apply(this.mineSurveyInfos, res.data.data)
            }
            else {
              this.$message.error('出错啦！')
            }
          })
      })
    }
    else {
      this.axios.get('/api/minesurveyinfo', {
        params: {
          token: this.token
        }
      })
        .then(res => {
          if (res.status == 200) {
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
    exportExtData() {
      var wb = xlsx.utils.book_new()
      let temp = []
      let temp2 = []
      this.mineSurveyInfos.forEach(v => {
        if (v != null) {
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
        }
      })
      let ws = xlsx.utils.json_to_sheet(temp)
      xlsx.utils.book_append_sheet(wb, ws, '4.矿物测量数据-岩屑直径分布')
      ws = xlsx.utils.json_to_sheet(temp2)
      xlsx.utils.book_append_sheet(wb, ws, '4.矿物测量数据-空洞长度分布')
      xlsx.writeFileXLSX(wb, `Export-STATISTIC2-${new Date().toISOString().split('T')[0]}.xlsx`)
    }
  }
}
</script>
