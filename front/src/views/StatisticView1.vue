<template>
  <div id="StatisticView1">
    <h4 align="left">矿物含量信息</h4>
    <el-table
      :data="mineContentInfos"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="id" label="样品号" width="110"></el-table-column>
      <el-table-column prop="clay" label="黏土基质" miniwidth="100"></el-table-column>
      <el-table-column prop="quartz" label="石英粉砂" miniwidth="100"></el-table-column>
      <el-table-column label="砂">
        <el-table-column prop="sand_quartz" label="石英" miniwidth="100"></el-table-column>
        <el-table-column prop="sand_feldspar" label="长石" miniwidth="100"></el-table-column>
        <el-table-column prop="sand_other" label="其他矿物" miniwidth="100"></el-table-column>
        <!-- <el-table-column label="小计" miniwidth="100">
          <template slot-scope="scope">
            {{ sum([scope.row.sand_quartz, ...]) }}
          </template>
        </el-table-column> -->
      </el-table-column>
      <el-table-column prop="debris" label="岩屑" miniwidth="100"></el-table-column>
      <el-table-column label="空洞">
        <el-table-column prop="hollow_close" label="闭气孔" miniwidth="100"></el-table-column>
        <el-table-column prop="hollow_open" label="开气孔" miniwidth="100"></el-table-column>
        <el-table-column prop="hollow_through" label="贯通气孔" miniwidth="100"></el-table-column>
      </el-table-column>
    </el-table>

    <div style="float:right;">
      导出：
      <el-button size="small" type="success" icon="el-icon-download" @click="exportExtData"></el-button>
    </div>
  </div>
</template>

<style scoped>
#StatisticView1 {
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
  name: 'StatisticView1',
  data() {
    return {
      token: '',
      mineContentInfos: []
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
        this.axios.get('/api/minecontentinfo/' + id, {
          params: {
            token: this.token
          }
        })
          .then(res => {
            if (res.status == 200) {
              this.mineContentInfos.push(res.data.data)
            }
            else {
              this.$message.error('出错啦！')
            }
          })
      })
    }
    else {
      this.axios.get('/api/minecontentinfo', {
        params: {
          token: this.token
        }
      })
        .then(res => {
          if (res.status == 200) {
            this.mineContentInfos = res.data.data
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
    exportExtData() {
      var wb = xlsx.utils.book_new()
      let temp = []
      this.mineContentInfos.forEach(v => {
        if (v != null) {
          temp.push({
            '样品号': v.id,
            '黏土': v.clay,
            '粉砂': v.quartz,
            '砂-石英': v.sand_quartz,
            '砂-长石': v.sand_feldspar,
            '砂-其他矿物': v.sand_other,
            '小计': this.sum([v.sand_quartz, v.sand_feldspar, v.sand_other]),
            '岩屑': v.debris,
            '空洞-闭气孔': v.hollow_close,
            '空洞-开气孔': v.hollow_open,
            '空洞-贯通气孔': v.hollow_through
          })
        }
      })
      let ws = xlsx.utils.json_to_sheet(temp)
      xlsx.utils.book_append_sheet(wb, ws, '3.矿物含量信息')
      
      xlsx.writeFileXLSX(wb, `Export-STATISTIC1-${new Date().toISOString().split('T')[0]}.xlsx`)
    }
  }
}
</script>
