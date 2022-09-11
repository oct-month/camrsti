<template>
  <div id="HomeView">
    <el-tabs type="card" :value="String(activeTab)" @tab-click="transTab" @tab-remove="removeTab">
      <el-tab-pane label="主页" name="0">
        <el-table
          :data="sampleInfos"
          stripe
          border
          height="85vh"
          style="width: 100%">
          <el-table-column sortable prop="id" label="样品号" width="100" :filters="sampleFilters.id" :filter-method="filterHandler('id')">
            <template slot-scope="scope">
              <el-link type="primary" @click="to_sample_page(scope.row.id)">
                <el-tag type="info" effect="plain" size="small">
                  {{ scope.row.id }}
                </el-tag>
              </el-link>
            </template>
          </el-table-column>
          <el-table-column sortable prop="type" label="样品类型" width="120" :filters="sampleFilters.type" :filter-method="filterHandler('type')">
            <template slot-scope="scope">
              <el-select v-if="editModel[scope.row.id]" v-model="nowEditSampleInfo.type" placeholder="请选择样品类型" style="width: 100%">
                <el-option label="炉渣" value="炉渣"></el-option>
                <el-option label="炉壁" value="炉壁"></el-option>
                <el-option label="陶范" value="陶范"></el-option>
                <el-option label="坩埚" value="坩埚"></el-option>
                <el-option label="鼓风管" value="鼓风管"></el-option>
                <el-option label="铜" value="铜"></el-option>
                <el-option label="铁" value="铁"></el-option>
                <el-option label="不明" value="不明"></el-option>
              </el-select>
              <span v-else>
                {{ scope.row.type }}
              </span>
            </template>
          </el-table-column>
          <el-table-column sortable prop="source" label="样品来源" width="120" :filters="sampleFilters.source" :filter-method="filterHandler('source')">
            <template slot-scope="scope">
              <el-input v-if="editModel[scope.row.id]" v-model="nowEditSampleInfo.source"></el-input>
              <span v-else>
                {{ scope.row.source }}
              </span>
            </template>
          </el-table-column>
          <el-table-column sortable prop="year" label="取样年份" width="120" :filters="sampleFilters.year" :filter-method="filterHandler('year')">
            <template slot-scope="scope">
              <el-date-picker v-if="editModel[scope.row.id]" type="year" placeholder="选择日期" v-model="nowEditSampleInfo.year" style="width: 100%"></el-date-picker>
              <div v-else>
                <i class="el-icon-time"></i>
                <span style="margin-left: 8px">{{ scope.row.year }}</span>
              </div>
            </template>
          </el-table-column>
          <el-table-column sortable prop="people" label="取样人" width="100" :filters="sampleFilters.people" :filter-method="filterHandler('people')">
            <template slot-scope="scope">
              <el-input v-if="editModel[scope.row.id]" v-model="nowEditSampleInfo.people"></el-input>
              <el-tag v-else size="medium">{{ scope.row.people }}</el-tag>
            </template>
          </el-table-column>
          <el-table-column prop="imageId" label="照片号" miniwidth="100">
            <template slot-scope="scope">
              <el-upload
                v-if="editModel[scope.row.id]"
                action="/api/image"
                accept="image/png, image/jpeg"
                ref="upload"
                name="upload"
                multiple
                :on-success="handleUploadSuccess"
                :on-error="handleUploadError"
                :auto-upload="false">
                <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
                <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器</el-button>
                <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过4MB</div>
              </el-upload>
              <el-popover v-else trigger="hover" placement="top" v-for="iid in scope.row.imageId" :key="iid">
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
          <el-table-column prop="describe" label="描述" miniwidth="190">
            <template slot-scope="scope">
              <el-input v-if="editModel[scope.row.id]" type="textarea" autosize v-model="nowEditSampleInfo.describe"></el-input>
              <span v-else>
                {{ scope.row.describe }}
              </span>
            </template>
          </el-table-column>
          <el-table-column prop="explain" label="样品制备说明" miniwidth="300">
            <template slot-scope="scope">
              <el-input v-if="editModel[scope.row.id]" type="textarea" autosize v-model="nowEditSampleInfo.explain"></el-input>
              <span v-else>
                {{ scope.row.explain }}
              </span>
            </template>
          </el-table-column>
          <el-table-column prop="experimentId" label="实验编号" miniwidth="160">
            <template slot-scope="scope">
              <el-link type="primary" @click="to_experiment_page(scope.row.id)">
                <el-tag type="success" effect="plain" size="small" v-for="sc in scope.row.experimentId" :key="sc">
                    {{ sc }}
                </el-tag>
              </el-link>
            </template>
          </el-table-column>
          <el-table-column label="操作" width="62">
            <template slot-scope="scope">
              <!-- <span style="display: none;">{{ scope.row.id }}</span> -->
              <div v-if="editModel[scope.row.id]" style="text-align:center;">
                <el-button size="small" type="success" icon="el-icon-check" circle @click="submitEdit(scope.row.id)"></el-button><br>
                <el-button size="mini" type="danger" icon="el-icon-close" circle @click="cancelEdit(scope.row.id)"></el-button>
              </div>
              <div v-else style="text-align:center;">
                <el-button size="mini" round plain type="warning" icon="el-icon-edit" @click="editSampleInfo(scope.row.id)"></el-button><br>
                <el-button size="mini" round plain type="danger" icon="el-icon-delete" @click="deleteDialogVisible[scope.row.id]=true"></el-button>
                <el-dialog title="确认" :visible.sync="deleteDialogVisible[scope.row.id]" width="30%">
                  <span>删除{{ scope.row.id }}?</span>
                  <span slot="footer" class="dialog-footer">
                    <el-button @click="deleteDialogVisible[scope.row.id]=false">取 消</el-button>
                    <el-button type="primary" @click="deleteSampleInfo(scope.row.id)">确 定</el-button>
                  </span>
                </el-dialog>
              </div>
            </template>
          </el-table-column>
        </el-table>
        <span style="text-align:left; width:100%; display:inline-block;">总计：{{ sampleInfos.length }}条</span>
      </el-tab-pane>
      <el-tab-pane closable :label="v.label" :name="v.name" v-for="v in editableTabs" :key="v">
        <sample-page v-if="v.type" :sampleId="v.sampleId"/>
        <experiment-page v-else :sampleId="v.sampleId"/>
      </el-tab-pane>
    </el-tabs>
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

::v-deep .el-tabs__nav {
  background: #ddd;
}
</style>

<script>
import SamplePage from '@/components/SamplePage.vue'
import ExperimentPage from '@/components/ExperimentPage.vue'

export default {
  name: 'HomeView',
  components: {
    SamplePage,
    ExperimentPage
  },
  data() {
    return {
      sampleInfos: [],
      editableTabs: [],
      lastActiveTab: 0,
      activeTab: 0,
      sampleFilters: {
        id: [],
        type: [],
        source: [],
        year: [],
        people: []
      },
      deleteDialogVisible: {},
      editModel: {},
      nowEditSampleInfo: null,
      uploadFileList: []
    }
  },
  mounted() {
    this.axios.get('/api/sampleinfo')
      .then(res => {
        if (res.status ==200 && res.data.status == 200) {
          this.sampleInfos = res.data.data
          this.$store.commit('setSampleInfos', res.data.data)
          this.sampleInfos.forEach(v => {
            this.$set(this.deleteDialogVisible, v.id, false)
            this.$set(this.editModel, v.id, false)
          })
          var temp = {
            id: new Set(),
            type: new Set(),
            source: new Set(),
            year: new Set(),
            people: new Set()
          }
          this.sampleInfos.forEach(v => {
            temp.id.add(v.id)
            temp.type.add(v.type)
            temp.source.add(v.source)
            temp.year.add(v.year)
            temp.people.add(v.people)
          })
          temp.id.forEach(v => {
            this.sampleFilters.id.push({
              text: String(v),
              value: v
            })
          })
          temp.type.forEach(v => {
            this.sampleFilters.type.push({
              text: String(v),
              value: v
            })
          })
          temp.source.forEach(v => {
            this.sampleFilters.source.push({
              text: String(v),
              value: v
            })
          })
          temp.year.forEach(v => {
            this.sampleFilters.year.push({
              text: String(v),
              value: v
            })
          })
          temp.people.forEach(v => {
            this.sampleFilters.people.push({
              text: String(v),
              value: v
            })
          })
        }
        else {
          this.$message.error('出错啦！')
        }
      })
  },
  methods: {
    transTab({ name }) {
      if (name != this.activeTab) {
        this.lastActiveTab = this.activeTab
        this.activeTab = name
      }
    },
    removeTab(targetName) {
      for (let i = 0; i < this.editableTabs.length; ++ i) {
        if (this.editableTabs[i].name == targetName) {
          this.editableTabs.splice(i, 1)
          break
        }
      }
      this.activeTab = this.lastActiveTab
    },
    to_sample_page(id) {
      this.editableTabs.push({
          label: id.trim() + ' 样品信息',
          name: String(this.editableTabs.length + 1),
          sampleId: id.trim(),
          type: 1
        })
      this.lastActiveTab = this.activeTab
      this.activeTab = this.editableTabs.length
    },
    to_experiment_page(id) {
      this.editableTabs.push({
        label: id.trim() + ' 实验信息',
        name: String(this.editableTabs.length + 1),
        sampleId: id.trim(),
        type: 0
      })
      this.lastActiveTab = this.activeTab
      this.activeTab = this.editableTabs.length
    },
    filterHandler: property => (value, row) => {
      return value === row[property]
    },
    deleteSampleInfo(sampleId) {
      this.axios.delete('/api/sampleinfo/' + sampleId)
        .then(res => {
          if (res.status == 200 && res.data.status == 200) {
            this.sampleInfos = this.sampleInfos.filter(v => v.id != sampleId)
            this.$message.warning('删除' + sampleId + '成功！')
          }
          else {
            this.$message.error('出错啦！')
          }
        })
      this.deleteDialogVisible[sampleId] = false
    },
    editSampleInfo(sampleId) {
      if (!this.nowEditSampleInfo) {
        var temp = this.sampleInfos.filter(v => v.id === sampleId)
        if (temp.length > 0) {
          this.nowEditSampleInfo = JSON.parse(JSON.stringify(temp[0]))
          this.nowEditSampleInfo.year = new Date(this.nowEditSampleInfo.year, 1)
        }
        this.editModel[sampleId] = true
      }
      else {
        this.$message.warning('您正在编辑' + this.nowEditSampleInfo.id + '，请优先完成')
      }
    },
    handleUploadSuccess(res) {
      if (res.status == 200) {
        this.uploadFileList = this.uploadFileList.concat(res.data)
      }
      // else {
      //   this.$message.error(file.name + '没有上传成功：' + res.data.msg)
      // }
    },
    handleUploadError(err, file) {
      this.$message.error(file.name + '没有上传成功：' + JSON.parse(err.message).msg)
    },
    submitUpload() {
      this.$refs.upload.submit()
    },
    submitEdit(sampleId) {
      this.nowEditSampleInfo.year = this.nowEditSampleInfo.year.getFullYear()
      this.nowEditSampleInfo.imageId = this.uploadFileList
      this.uploadFileList = []
      this.axios.put('/api/sampleinfo', this.nowEditSampleInfo)
        .then(res => {
          if (res.status == 200 && res.data.status == 200) {
            this.sampleInfos.forEach((v, i) => {
              if (v.id == sampleId) {
                this.$set(this.sampleInfos, i, this.nowEditSampleInfo)
              }
            })
            this.nowEditSampleInfo = null
            this.editModel[sampleId] = false
          }
          else {
            this.$message.error('出错啦！')
          }
        })
    },
    cancelEdit(sampleId) {
      this.nowEditSampleInfo = null
      this.editModel[sampleId] = false
    }
  }
}
</script>
