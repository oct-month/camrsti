<template>
  <div id="StatisticView4">
    <h4 align="left">化学成分数据</h4>

    <el-table
      :data="mineChemistryInfos"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="id" label="样品号"></el-table-column>
      <el-table-column prop="Na2O" label="Na₂O"></el-table-column>
      <el-table-column prop="MgO" label="MgO"></el-table-column>
      <el-table-column prop="Al2O3" label="Al₂O₃"></el-table-column>
      <el-table-column prop="SiO2" label="SiO₂"></el-table-column>
      <el-table-column prop="P2O5" label="P₂O₅"></el-table-column>
      <el-table-column prop="SO2" label="SO₂"></el-table-column>
      <el-table-column prop="K2O" label="K₂O"></el-table-column>
      <el-table-column prop="CaO" label="CaO"></el-table-column>
      <el-table-column prop="TiO2" label="TiO₂"></el-table-column>
      <el-table-column prop="MnO" label="MnO"></el-table-column>
      <el-table-column prop="FeO" label="FeO"></el-table-column>
      <el-table-column prop="CuO" label="CuO"></el-table-column>
      <el-table-column prop="ZnO" label="ZnO"></el-table-column>
      <el-table-column prop="As2O3" label="As₂O₃"></el-table-column>
      <el-table-column prop="SnO2" label="SnO₂"></el-table-column>
      <el-table-column prop="PbO" label="PbO"></el-table-column>
      <el-table-column prop="other" label="其他"></el-table-column>
    </el-table>

    <div style="float:right;">
      导出：
      <el-button size="small" type="success" icon="el-icon-download" @click="exportExtData"></el-button>
    </div>
  </div>
</template>

<style scoped>
#StatisticView4 {
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
  name: 'StatisticView4',
  data() {
    return {
      token: '',
      mineChemistryInfos: []
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
        this.axios.get('/api/minechemistryinfo/' + id, {
          params: {
            token: this.token
          }
        })
          .then(res => {
            if (res.status == 200) {
              this.mineChemistryInfos.push(res.data.data)
            }
            else {
              this.$message.error('出错啦！')
            }
          })
      })
    }
    else {
      this.axios.get('/api/minechemistryinfo', {
        params: {
          token: this.token
        }
      })
        .then(res => {
          if (res.status == 200) {
            this.mineChemistryInfos = res.data.data
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
      this.mineChemistryInfos.forEach(v => {
        if (v != null) {
          temp.push({
            '样品号': v.id,
            'Na₂O': v.Na2O,
            'MgO': v.MgO,
            'Al₂O₃': v.Al2O3,
            'SiO₂': v.SiO2,
            'P₂O₅': v.P2O5,
            'SO₂': v.SO2,
            'K₂O': v.K2O,
            'CaO': v.CaO,
            'TiO₂': v.TiO2,
            'MnO': v.MnO,
            'FeO': v.FeO,
            'CuO': v.CuO,
            'ZnO': v.ZnO,
            'As₂O₃': v.As2O3,
            'SnO₂': v.SnO2,
            'PbO': v.PbO,
            '其他': v.other
          })
        }
      })
      let ws = xlsx.utils.json_to_sheet(temp)
      xlsx.utils.book_append_sheet(wb, ws, '6.化学成分数据')
      xlsx.writeFileXLSX(wb, `Export-STATISTIC4-${new Date().toISOString().split('T')[0]}.xlsx`)
    }
  }
}
</script>
