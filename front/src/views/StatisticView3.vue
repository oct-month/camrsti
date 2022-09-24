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
    </el-table>

    <hr>

    <h4 align="left">化学成分数据</h4>

    <el-table
      :data="mineChemistryInfos"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="id" label="样品号" width="110"></el-table-column>
      <el-table-column prop="type" label="类型" width="90"></el-table-column>
      <el-table-column prop="Na2O" label="Na₂O" miniwidth="100"></el-table-column>
      <el-table-column prop="MgO" label="MgO" miniwidth="100"></el-table-column>
      <el-table-column prop="Al2O3" label="Al₂O₃" miniwidth="100"></el-table-column>
      <el-table-column prop="SiO2" label="SiO₂" miniwidth="100"></el-table-column>
      <el-table-column prop="K2O" label="K₂O" miniwidth="100"></el-table-column>
      <el-table-column prop="CaO" label="CaO" miniwidth="100"></el-table-column>
      <el-table-column prop="Fe2O3" label="Fe₂O₃" miniwidth="100"></el-table-column>
    </el-table>
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
export default {
  name: 'StatisticView3',
  data() {
    return {
      mineXRDInfos: [],
      mineChemistryInfos: []
    }
  },
  mounted() {
    this.axios.get('/api/minexrdinfo')
      .then(res => {
        if (res.status == 200 && res.data.status == 200) {
          this.mineXRDInfos = res.data.data
        }
        else {
          this.$message.error('出错啦！')
        }
      })
    this.axios.get('/api/minechemistryinfo')
      .then(res => {
        if (res.status == 200 && res.data.status == 200) {
          this.mineChemistryInfos = res.data.data
        }
        else {
          this.$message.error('出错啦！')
        }
      })
  }
}
</script>
