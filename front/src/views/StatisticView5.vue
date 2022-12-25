<template>
  <div id="StatisticView5">
    <h4 align="left">物理性能数据</h4>
    
    <el-table
      :data="minePhysicalInfos"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="id" label="样品号" width="110"></el-table-column>
      <el-table-column prop="type" label="类型" width="120"></el-table-column>
      <el-table-column prop="trueDensity" label="密度" miniwidth="100"></el-table-column>
      <el-table-column prop="apparentPorosity" label="气孔率" miniwidth="100"></el-table-column>
      <el-table-column prop="waterAbsorption" label="吸水率" miniwidth="100"></el-table-column>
      <el-table-column prop="bending" label="高温抗折强度" miniwidth="100"></el-table-column>
      <el-table-column prop="resistance" label="热震稳定性系数" miniwidth="100"></el-table-column>
      <el-table-column prop="slag" label="抗渣性系数" miniwidth="100"></el-table-column>
      <el-table-column prop="alkali" label="耐碱性系数" miniwidth="100"></el-table-column>
      <el-table-column prop="refractoriness" label="荷重软化温度" miniwidth="100"></el-table-column>
      <el-table-column prop="heat" label="导热系数" miniwidth="100"></el-table-column>
    </el-table>

    <div style="float:right;">
      导出：
      <el-button size="small" type="success" icon="el-icon-download" @click="exportExtData"></el-button>
    </div>
  </div>
</template>

<style scoped>
#StatisticView5 {
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
  name: 'StatisticView5',
  data() {
    return {
      token: '',
      minePhysicalInfos: []
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
        this.axios.get('/api/minephysicsinfo/' + id, {
          params: {
            token: this.token
          }
        })
          .then(res => {
            if (res.status == 200) {
              this.minePhysicalInfos.push(res.data.data)
            }
            else {
              this.$message.error('出错啦！')
            }
          })
      })
    }
    else {
      this.axios.get('/api/minephysicsinfo', {
        params: {
          token: this.token
        }
      })
        .then(res => {
          if (res.status == 200) {
            this.minePhysicalInfos = res.data.data
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
      this.minePhysicalInfos.forEach(v => {
        if (v != null) {
          temp.push({
            '样品编号': v.id,
            '类型': v.type,
            '密度': v.trueDensity,
            '气孔率': v.apparentPorosity,
            '吸水率': v.waterAbsorption,
            '高温抗折强度': v.bending,
            '热震稳定性系数': v.resistance,
            '抗渣性系数': v.slag,
            '耐碱性系数': v.alkali,
            '荷重软化温度': v.refractoriness,
            '导热系数': v.heat
          })
        }
      })
      let ws = xlsx.utils.json_to_sheet(temp)
      xlsx.utils.book_append_sheet(wb, ws, '7.物理性能数据')
      
      xlsx.writeFileXLSX(wb, `Export-STATISTIC5-${new Date().toISOString().split('T')[0]}.xlsx`)
    }
  }
}
</script>
