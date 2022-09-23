<template>
  <div id="HomeView">
    <el-tabs type="card" :value="String(activeTab)" @tab-click="transTab" @tab-remove="removeTab">
      <el-tab-pane label="主页" name="0">
        <el-table stripe border empty-text=" " height="50" style="width:100%">
          <el-table-column width="50">
            <template slot="header" slot-scope="scope">
              检索
            </template>
          </el-table-column>
          <el-table-column width="90">
            <template slot="header" slot-scope="scope">
              <el-input size="mini" placeholder="样品号" v-model="filterItems.id" @input="forceUpdate" @change="inputFilterHandler"></el-input>
            </template>
          </el-table-column>
          <el-table-column width="110">
            <template slot="header" slot-scope="scope">
              <el-input size="mini" placeholder="样品类型" v-model="filterItems.type" @input="forceUpdate" @change="inputFilterHandler"></el-input>
            </template>
          </el-table-column>
          <el-table-column width="120">
            <template slot="header" slot-scope="scope">
              <el-input size="mini" placeholder="样品来源" v-model="filterItems.source" @input="forceUpdate" @change="inputFilterHandler"></el-input>
            </template>
          </el-table-column>
          <el-table-column width="113">
            <template slot="header" slot-scope="scope">
              <el-input size="mini" placeholder="取样年份" v-model="filterItems.year" @input="forceUpdate" @change="inputFilterHandler"></el-input>
            </template>
          </el-table-column>
          <el-table-column width="110">
            <template slot="header" slot-scope="scope">
              <el-input size="mini" placeholder="取样人" v-model="filterItems.people" @input="forceUpdate" @change="inputFilterHandler"></el-input>
            </template>
          </el-table-column>
          <el-table-column width="240">
            <template slot="header" slot-scope="scope">
              <el-input size="mini" placeholder="照片号" v-model="filterItems.imageId" @input="forceUpdate" @change="inputFilterHandler"></el-input>
            </template>
          </el-table-column>
          <el-table-column width="78">
            <template slot="header" slot-scope="scope">
              模糊检索
            </template>
          </el-table-column>
          <el-table-column miniwidth="100">
            <template slot="header" slot-scope="scope">
              <el-input size="mini" placeholder="请输入关键字搜索" v-model="filterItems.keyWord" @input="forceUpdate" @change="inputFilterHandler"></el-input>
            </template>
          </el-table-column>
        </el-table>

        <el-table
          :data="currentTableData"
          stripe
          border
          height="80vh"
          style="width:100%">
          <el-table-column type="index" width="50">
            <template slot-scope="scope">
              <div style="text-align:center;">{{scope.$index + 1}}</div>
            </template>
          </el-table-column>
          <el-table-column sortable prop="id" :label="keyMap['id']" width="90">
            <template slot-scope="scope">
              <el-link type="primary" @click="to_sample_page(scope.row.id)">
                <el-tag type="info" effect="plain" size="small">
                  {{ scope.row.id }}
                </el-tag>
              </el-link>
            </template>
          </el-table-column>
          <el-table-column sortable prop="type" :label="keyMap['type']" width="110">
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
          <el-table-column sortable prop="source" :label="keyMap['source']" width="120">
            <template slot-scope="scope">
              <el-input v-if="editModel[scope.row.id]" v-model="nowEditSampleInfo.source"></el-input>
              <span v-else>
                {{ scope.row.source }}
              </span>
            </template>
          </el-table-column>
          <el-table-column sortable prop="year" :label="keyMap['year']" width="113">
            <template slot-scope="scope">
              <el-date-picker v-if="editModel[scope.row.id]" type="year" placeholder="日期" v-model="nowEditSampleInfo.year" style="width: 100%"></el-date-picker>
              <div v-else-if="scope.row.year">
                <i class="el-icon-time"></i>
                <span style="margin-left: 8px">{{ scope.row.year }}</span>
              </div>
            </template>
          </el-table-column>
          <el-table-column sortable prop="people" :label="keyMap['people']" width="110">
            <template slot-scope="scope">
              <el-input v-if="editModel[scope.row.id]" v-model="nowEditSampleInfo.people"></el-input>
              <el-tag v-else-if="scope.row.people" size="medium">{{ scope.row.people }}</el-tag>
            </template>
          </el-table-column>
          <el-table-column prop="imageId" :label="keyMap['imageId']" width="240">
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
                :auto-upload="true">
                <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
                <!-- <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器</el-button> -->
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
          <el-table-column prop="describe" :label="keyMap['describe']" miniwidth="190">
            <template slot-scope="scope">
              <el-input v-if="editModel[scope.row.id]" type="textarea" autosize v-model="nowEditSampleInfo.describe"></el-input>
              <span v-else>
                {{ scope.row.describe }}
              </span>
            </template>
          </el-table-column>
          <el-table-column prop="explain" :label="keyMap['explain']" miniwidth="300">
            <template slot-scope="scope">
              <el-input v-if="editModel[scope.row.id]" type="textarea" autosize v-model="nowEditSampleInfo.explain"></el-input>
              <span v-else>
                {{ scope.row.explain }}
              </span>
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
        <div style="text-align:center; width:100%; display:inline-block;">
          <span style="float:left;">总计：{{ currentTableData.length }}条</span>
          <div style="float:right;">
            导出：
            <el-button size="small" type="success" icon="el-icon-download" @click="exportTableData"></el-button>
          </div>
        </div>
      </el-tab-pane>
      <el-tab-pane closable :label="v.label" :name="v.name" v-for="v in editableTabs" :key="v.label">
        <sample-page :sampleId="v.sampleId"/>
        <hr><hr>
        <experiment-page :sampleId="v.sampleId"/>
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

:deep(.el-tabs__nav) {
  background: #ddd;
}
/* ::v-deep .el-table__cell {
  text-align: center;
} */
</style>

<script>
import xlsx from 'xlsx'

import { deepObjCopy } from '@/utils'
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
      keyMap: {
        id: '样品号',
        type: '样品类型',
        source: '样品来源',
        year: '取样年份',
        people: '取样人',
        imageId: '照片号',
        describe: '描述',
        explain: '样品制备说明'
      },
      currentTableData: [],
      filterItems: {
        id: '',
        type: '',
        source: '',
        year: '',
        people: '',
        imageId: '',
        keyWord: ''
      },
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
          this.sampleInfos = res.data.data.reverse()
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
          this.currentTableData = this.sampleInfos
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
          sampleId: id.trim()
        })
      this.lastActiveTab = this.activeTab
      this.activeTab = this.editableTabs.length
    },
    filterHandler: property => (value, row) => {
      return value === row[property]
    },
    forceUpdate() {
      this.$forceUpdate()
    },
    inputFilterHandler() {
      this.currentTableData = deepObjCopy(this.sampleInfos)
      if (this.filterItems.id.trim()) {
        for (let i = this.currentTableData.length - 1; i >=0 ; -- i) {
          if (this.currentTableData[i].id.indexOf(this.filterItems.id.trim()) < 0) {
            this.currentTableData.splice(i, 1)
          }
        }
      }
      if (this.filterItems.type.trim()) {
        for (let i = this.currentTableData.length - 1; i >=0 ; -- i) {
          if (this.currentTableData[i].type.indexOf(this.filterItems.type.trim()) < 0) {
            this.currentTableData.splice(i, 1)
          }
        }
      }
      if (this.filterItems.source.trim()) {
        for (let i = this.currentTableData.length - 1; i >=0 ; -- i) {
          if (this.currentTableData[i].source.indexOf(this.filterItems.source.trim()) < 0) {
            this.currentTableData.splice(i, 1)
          }
        }
      }
      if (this.filterItems.year.trim()) {
        for (let i = this.currentTableData.length - 1; i >=0 ; -- i) {
          if (String(this.currentTableData[i].year).indexOf(this.filterItems.year.trim()) < 0) {
            this.currentTableData.splice(i, 1)
          }
        }
      }
      if (this.filterItems.people.trim()) {
        for (let i = this.currentTableData.length - 1; i >=0 ; -- i) {
          if (this.currentTableData[i].people.indexOf(this.filterItems.people.trim()) < 0) {
            this.currentTableData.splice(i, 1)
          }
        }
      }
      if (this.filterItems.imageId.trim()) {
        for (let i = this.currentTableData.length - 1; i >=0 ; -- i) {
          let flag = false
          this.currentTableData[i].imageId.forEach(v => {
            if (v.indexOf(this.filterItems.imageId.trim()) >= 0) {
              flag = true
            }
          })
          if (!flag) {
            this.currentTableData.splice(i, 1)
          }
        }
      }
      if (this.filterItems.keyWord.trim()) {
        for (let i = this.currentTableData.length - 1; i >=0 ; -- i) {
          if (JSON.stringify(this.currentTableData[i]).indexOf(this.filterItems.keyWord) < 0) {
            this.currentTableData.splice(i, 1)
          }
        }
      }
    },
    deleteSampleInfo(sampleId) {
      this.axios.delete('/api/sampleinfo/' + sampleId)
        .then(res => {
          if (res.status == 200 && res.data.status == 200) {
            this.sampleInfos = this.sampleInfos.filter(v => v.id != sampleId)
            this.currentTableData = this.currentTableData.filter(v => v.id != sampleId)
            this.$message.success('删除' + sampleId + '成功！')
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
          this.nowEditSampleInfo = deepObjCopy(temp[0])
          if (this.nowEditSampleInfo.year) {
            this.nowEditSampleInfo.year = new Date(this.nowEditSampleInfo.year, 1)
          }
          else {
            this.nowEditSampleInfo.year = 0
          }
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
      if (this.nowEditSampleInfo.year) {
        this.nowEditSampleInfo.year = this.nowEditSampleInfo.year.getFullYear()
      }
      else {
        this.nowEditSampleInfo.year = 0
      }
      if (this.uploadFileList.length > 0) {
        this.nowEditSampleInfo.imageId = this.uploadFileList
      }
      this.uploadFileList = []
      this.axios.put('/api/sampleinfo', this.nowEditSampleInfo)
        .then(res => {
          if (res.status == 200 && res.data.status == 200) {
            this.sampleInfos.forEach((v, i) => {
              if (v.id == sampleId) {
                this.$set(this.sampleInfos, i, this.nowEditSampleInfo)
              }
            })
            this.currentTableData.forEach((v, i) => {
              if (v.id == sampleId) {
                this.$set(this.currentTableData, i, this.nowEditSampleInfo)
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
    },
    exportTableData() {
      var temp = deepObjCopy(this.currentTableData)
      temp.forEach((v, i) => {
        temp[i].imageId = v.imageId.join('、')
      })
      var exData = [];
      temp.forEach(v => {
        let obj = {};
        Object.keys(this.keyMap).forEach(k => {
          obj[this.keyMap[k]] = v[k]
        })
        exData.push(obj)
      })
      var ws = xlsx.utils.json_to_sheet(exData)
      var wb = xlsx.utils.book_new()
      xlsx.utils.book_append_sheet(wb, ws, 'Sheet')
      xlsx.writeFileXLSX(wb, `Export-${new Date().toISOString().split('T')[0]}.xlsx`)
    }
  }
}
</script>