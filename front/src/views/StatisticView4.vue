<template>
  <div id="StatisticView4">
    <h4 align="left">物理结构数据</h4>
    
    <el-table
      :data="minePhysicalInfos"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="id" label="样品编号" width="110"></el-table-column>
      <el-table-column prop="type" label="类型" width="120"></el-table-column>
      <el-table-column prop="apparentPorosity" label="显气孔率" miniwidth="100"></el-table-column>
      <el-table-column prop="trueDensity" label="真密度" miniwidth="100"></el-table-column>
      <el-table-column prop="waterAbsorption" label="吸水率" miniwidth="100"></el-table-column>
    </el-table>

    <hr>

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
export default {
  name: 'StatisticView4',
  data() {
    return {
      minePhysicalInfos: [],
      mineThermalInfos: []
    }
  },
  mounted() {
    this.axios.get('/api/minephysicsinfo')
      .then(res => {
        if (res.status == 200 && res.data.status == 200) {
          this.minePhysicalInfos = res.data.data
        }
        else {
          this.$message.error('出错啦！')
        }
      })
    this.axios.get('/api/minethermalinfo')
      .then(res => {
        if (res.status == 200 && res.data.status == 200) {
          this.mineThermalInfos = res.data.data
        }
        else {
          this.$message.error('出错啦！')
        }
      })
  }
}
</script>
