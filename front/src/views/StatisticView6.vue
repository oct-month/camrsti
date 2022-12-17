<template>
  <div id="StatisticView4">
    <h4 align="left">热分析</h4>
    
    <el-table
      :data="mineThermalInfos"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="id" label="样品号" width="110"></el-table-column>
      <el-table-column prop="termTemper" label="终止温度" miniwidth="100"></el-table-column>
      <el-table-column prop="fireResis" label="耐火度" miniwidth="100"></el-table-column>
      <el-table-column prop="data" label="热分析数据" miniwidth="100">
        <template slot-scope="scope">
          <el-link type="primary" target="_blank" :href="'/api/txt/'+scope.row.data" :download="scope.row.data">
            {{ scope.row.data }}
          </el-link>
        </template>
      </el-table-column>
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
      mineThermalInfos: []
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
        this.axios.get('/api/minethermalinfo/' + id, {
          params: {
            token: this.token
          }
        })
          .then(res => {
            if (res.status == 200 && res.data.status == 200) {
              this.mineThermalInfos.push.apply(this.mineThermalInfos, res.data.data)
            }
            else {
              this.$message.error('出错啦！')
            }
          })
      })
    }
    else {
      this.axios.get('/api/minethermalinfo', {
        params: {
          token: this.token
        }
      })
        .then(res => {
          if (res.status == 200 && res.data.status == 200) {
            this.mineThermalInfos = res.data.data
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
      this.mineThermalInfos.forEach(v => {
        if (v != null) {
          temp.push({
            '样品号': v.id,
            '终止温度': v.termTemper,
            '耐火度': v.fireResis,
            '热分析数据': v.data,
            '热分析曲线': '' //v.surveImage
          })
        }
      })
      let ws = xlsx.utils.json_to_sheet(temp)
      xlsx.utils.book_append_sheet(wb, ws, '8.热分析')
      xlsx.writeFileXLSX(wb, `Export-STATISTIC6-${new Date().toISOString().split('T')[0]}.xlsx`)
    }
  }
}
</script>
