<template>
  <div id="HomeView">
    <el-table
      :data="sampleInfos"
      stripe
      border
      height="85vh"
      style="width: 100%">
    <el-table-column sortable prop="id" label="样品号" width="87">
      <template slot-scope="scope">
        <el-link type="primary" @click="to_sample_page(scope.row.id)">
          <el-tag type="info" effect="plain" size="small">
            {{ scope.row.id }}
          </el-tag>
        </el-link>
      </template>
    </el-table-column>
    <el-table-column sortable prop="type" label="样品类型" width="110"></el-table-column>
    <el-table-column sortable prop="source" label="样品来源" width="120"></el-table-column>
    <el-table-column sortable prop="year" label="取样年份" width="101">
      <template slot-scope="scope">
        <i class="el-icon-time"></i>
        <span style="margin-left: 8px">{{ scope.row.year }}</span>
      </template>
    </el-table-column>
    <el-table-column sortable prop="people" label="取样人" width="87">
      <template slot-scope="scope">
        <el-tag size="medium">{{ scope.row.people }}</el-tag>
      </template>
    </el-table-column>
    <el-table-column prop="imageId" label="照片号" miniwidth="100">
      <template slot-scope="scope">
          <el-popover trigger="hover" placement="top" v-for="iid in scope.row.imageId" :key="iid">
            <el-image
                style="height: 200px"
                :src="'/api/image/' + iid"
                fit="contain">
                <div slot="error" class="image-slot">
                  <i class="el-icon-picture-outline"></i>
                </div>
            </el-image>
            <div slot="reference" class="name-wrapper">
              <span style="text-decoration: underline; color: #409EAF">{{ iid }}</span>
            </div>
          </el-popover>
        </template>
      </el-table-column>
      <el-table-column prop="describe" label="描述" miniwidth="190"></el-table-column>
      <el-table-column prop="explain" label="样品制备说明" miniwidth="300"></el-table-column>
      <el-table-column prop="experimentId" label="实验编号" miniwidth="160">
        <template slot-scope="scope">
          <el-link type="primary" v-for="sc in scope.row.experimentId" :key="sc">
            <el-tag type="success" effect="plain" size="small">
                {{ sc }}
            </el-tag>
          </el-link>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="62">
        <template slot-scope="scope">
          <span style="display: none;">{{ scope.row.sampleId }}</span>
          <el-button size="mini" round plain type="warning" icon="el-icon-edit"></el-button><br>
          <el-button size="mini" round plain type="danger" icon="el-icon-delete"></el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<style scoped>
#HomeView {
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
  name: 'HomeView',
  data() {
    return {
      sampleInfos: []
    }
  },
  mounted() {
    this.axios.get('/api/sampleinfo')
      .then(res => {
        if (res.status ==200 && res.data.status == 200) {
          this.sampleInfos = res.data.data
          this.$store.commit('setSampleInfos', res.data.data)
        }
        else {
          this.$message.error('出错啦！')
        }
      })
  },
  methods: {
    to_sample_page(id) {
      this.$router.push({path: '/sample', query: {id}})
    }
  }
}
</script>
