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
        <el-table-column prop="debris_0um" label="≤67μm" miniwidth="100"></el-table-column>
        <el-table-column prop="debris_67um" label="67-167μm" miniwidth="100"></el-table-column>
        <el-table-column prop="debris_167um" label="167-501μm" miniwidth="100"></el-table-column>
        <el-table-column prop="debris_501um" label="501-1002μm" miniwidth="100"></el-table-column>
        <el-table-column prop="debris_1002um" label="≥1002μm" miniwidth="100"></el-table-column>
      </el-table-column>
      <!-- 空洞长度分布 -->
      <el-table-column label="空洞长度分布">
        <el-table-column prop="hollow_0um" label="≤67μm" miniwidth="100"></el-table-column>
        <el-table-column prop="hollow_67um" label="67-501μm" miniwidth="100"></el-table-column>
        <el-table-column prop="hollow_501um" label="501-1002μm" miniwidth="100"></el-table-column>
        <el-table-column prop="hollow_1002um" label="1002-2004μm" miniwidth="100"></el-table-column>
        <el-table-column prop="hollow_2004um" label="≥2004μm" miniwidth="100"></el-table-column>
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
              this.mineSurveyInfos.push(res.data.data)
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
            '≤67μm': v.debris_0um,
            '67-167μm': v.debris_67um,
            '167-501μm': v.debris_167um,
            '501-1002μm': v.debris_501um,
            '≥1002μm': v.debris_1002um
          })
          temp2.push({
            '样品号': v.id,
            '≤67μm': v.hollow_0um,
            '67-501μm': v.hollow_67um,
            '501-1002μm': v.hollow_501um,
            '1002-2004μm': v.hollow_1002um,
            '≥2004μm': v.hollow_2004um
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
