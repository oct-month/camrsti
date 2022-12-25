<template>
  <div id="StatisticView3">
    <h4 align="left">XRD分析数据</h4>

    <el-table
      :data="mineXRDInfos"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="id" label="样品编号" width="110"></el-table-column>
      <el-table-column prop="type" label="类型" width="90"></el-table-column>
      <el-table-column prop="quartz" label="石英" miniwidth="100"></el-table-column>
      <el-table-column prop="albite" label="钠长石" miniwidth="100"></el-table-column>
      <el-table-column prop="potashFeldspar" label="钾长石" miniwidth="100"></el-table-column>
      <el-table-column prop="mica" label="云母" miniwidth="100"></el-table-column>
      <el-table-column prop="amphibole" label="闪石" miniwidth="100"></el-table-column>
      <el-table-column prop="hematite" label="赤铁矿" miniwidth="100"></el-table-column>
      <el-table-column prop="magnetite" label="磁铁矿" miniwidth="100"></el-table-column>
      <el-table-column prop="dolomite" label="白云石" miniwidth="100"></el-table-column>
      <el-table-column prop="analcite" label="方沸石" miniwidth="100"></el-table-column>
      <el-table-column prop="tridymite" label="磷石英" miniwidth="100"></el-table-column>
      <el-table-column prop="cristobalite" label="方石英" miniwidth="100"></el-table-column>
      <el-table-column prop="mullite" label="莫来石" miniwidth="100"></el-table-column>
      <el-table-column prop="other" label="其他" miniwidth="100"></el-table-column>
    </el-table>

    <div style="float:right;">
      导出：
      <el-button size="small" type="success" icon="el-icon-download" @click="exportExtData"></el-button>
    </div>
  </div>
</template>

<style scoped>
#StatisticView3 {
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
  name: 'StatisticView3',
  data() {
    return {
      token: '',
      mineXRDInfos: []
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
        this.axios.get('/api/minexrdinfo/' + id, {
          params: {
            token: this.token
          }
        })
          .then(res => {
            if (res.status == 200) {
              this.mineXRDInfos.push(res.data.data)
            }
            else {
              this.$message.error('出错啦！')
            }
          })
      })
    }
    else {
      this.axios.get('/api/minexrdinfo', {
        params: {
          token: this.token
        }
      })
        .then(res => {
          if (res.status == 200) {
            this.mineXRDInfos = res.data.data
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
      this.mineXRDInfos.forEach(v => {
        if (v != null) {
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
            '莫来石': v.mullite,
            '其他': v.other
          })
        }
      })
      let ws = xlsx.utils.json_to_sheet(temp)
      xlsx.utils.book_append_sheet(wb, ws, '5.XRD分析数据')
      
      xlsx.writeFileXLSX(wb, `Export-STATISTIC3-${new Date().toISOString().split('T')[0]}.xlsx`)
    }
  }
}
</script>
