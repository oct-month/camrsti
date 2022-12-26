<template>
  <div id="HomeView">
    <el-tabs type="card" :value="String(activeTab)" @tab-click="transTab" @tab-remove="removeTab">
      <el-tab-pane label="主页" name="0">
        <!-- 数据列表页面 -->
        <el-table v-show="multiModeFlag" stripe border empty-text=" " height="50" style="width:100%">
          <el-table-column width="50">
            <template slot="header" slot-scope="scope">
              <el-button type="danger" icon="el-icon-delete" size="mini" circle plain @click="multiDeletePre"></el-button>
              <el-dialog title="确认" :visible.sync="multiDeleteDialogVisible" width="30%">
                <span>删除{{multiSelectedList}}?</span>
                <span slot="footer" class="dialog-footer">
                  <el-button @click="multiDeleteDialogVisible=false">取 消</el-button>
                  <el-button type="primary" @click="deleteSelectedSample">确 定</el-button>
                </span>
              </el-dialog>
            </template>
          </el-table-column>
          <el-table-column width="50">
            <template slot="header" slot-scope="scope">
              <el-button type="info" icon="el-icon-picture" size="small" circle plain @click="downloadSelectedImages"></el-button>
            </template>
          </el-table-column>
          <el-table-column width="100">
            <template slot="header" slot-scope="scope">
              <el-button type="success" size="small" round plain @click="toStatisticPage('4-1')">矿物含量</el-button>
            </template>
          </el-table-column>
          <el-table-column width="100">
            <template slot="header" slot-scope="scope">
              <el-button type="success" size="small" round plain @click="toStatisticPage('4-2')">矿物测量</el-button>
            </template>
          </el-table-column>
          <el-table-column width="75">
            <template slot="header" slot-scope="scope">
              <el-button type="success" size="small" round plain @click="toStatisticPage('4-3')">XRD</el-button>
            </template>
          </el-table-column>
          <el-table-column width="100">
            <template slot="header" slot-scope="scope">
              <el-button type="success" size="small" round plain @click="toStatisticPage('4-4')">化学成分</el-button>
            </template>
          </el-table-column>
          <el-table-column width="100">
            <template slot="header" slot-scope="scope">
              <el-button type="success" size="small" round plain @click="toStatisticPage('4-5')">物理性能</el-button>
            </template>
          </el-table-column>
          <el-table-column width="88">
            <template slot="header" slot-scope="scope">
              <el-button type="success" size="small" round plain @click="toStatisticPage('4-6')">热分析</el-button>
            </template>
          </el-table-column>
          <el-table-column width="50">
            <template slot="header" slot-scope="scope">
              <el-button type="warning" icon="el-icon-close" size="mini" circle plain @click="cancelMultiMode"></el-button>
            </template>
          </el-table-column>
        </el-table>
        <el-table v-show="!multiModeFlag" stripe border empty-text=" " height="50" style="width:100%">
          <el-table-column width="50">
            <template slot="header" slot-scope="scope">
              检索
            </template>
          </el-table-column>
          <el-table-column width="110">
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
          <el-table-column width="245">
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
          :data="afterTableData"
          @selection-change="handleSelectionChange"
          stripe
          border
          height="80vh"
          style="width:100%">
          <el-table-column key="1" v-if="multiModeFlag" type="selection" width="50"></el-table-column>
          <el-table-column key="2" v-else type="index" width="50">
            <template slot="header">
              <el-button type="success" size="small" circle plain icon="el-icon-s-operation" @click="doMultiOps"></el-button>
            </template>
            <template slot-scope="scope">
              <div style="text-align:center;">{{scope.$index + 1 + pageSize * (currentPage - 1)}}</div>
            </template>
          </el-table-column>
          <el-table-column key="3" sortable prop="id" :label="keyMap['id']" width="110">
            <template slot-scope="scope">
              <el-link type="primary" @click="to_sample_page(scope.row.id)">
                <el-tag type="info" effect="plain" size="small">
                  {{ scope.row.id }}
                </el-tag>
              </el-link>
            </template>
          </el-table-column>
          <el-table-column key="4" sortable prop="type" :label="keyMap['type']" width="110">
            <template slot-scope="scope">
              <el-autocomplete
                class="inline-input"
                v-if="editModel[scope.row.id]"
                v-model="nowEditSampleInfo.type"
                :fetch-suggestions="typeSuggest"
                placeholder="请选择样品类型"
                style="width: 100%">
              </el-autocomplete>
              <!-- <el-select v-if="editModel[scope.row.id]" v-model="nowEditSampleInfo.type" placeholder="请选择样品类型" style="width: 100%">
                <el-option label="炉渣" value="炉渣"></el-option>
                <el-option label="炉壁" value="炉壁"></el-option>
                <el-option label="陶范" value="陶范"></el-option>
                <el-option label="坩埚" value="坩埚"></el-option>
                <el-option label="鼓风管" value="鼓风管"></el-option>
                <el-option label="铜" value="铜"></el-option>
                <el-option label="铁" value="铁"></el-option>
                <el-option label="不明" value="不明"></el-option>
              </el-select> -->
              <span v-else>
                {{ scope.row.type }}
              </span>
            </template>
          </el-table-column>
          <el-table-column key="5" sortable prop="source" :label="keyMap['source']" width="120">
            <template slot-scope="scope">
              <el-input v-if="editModel[scope.row.id]" v-model="nowEditSampleInfo.source"></el-input>
              <span v-else>
                {{ scope.row.source }}
              </span>
            </template>
          </el-table-column>
          <el-table-column key="6" sortable prop="year" :label="keyMap['year']" width="113">
            <template slot-scope="scope">
              <el-date-picker v-if="editModel[scope.row.id]" type="year" placeholder="日期" v-model="nowEditSampleInfo.year" style="width: 100%"></el-date-picker>
              <div v-else-if="scope.row.year">
                <i class="el-icon-time"></i>
                <span style="margin-left: 8px">{{ scope.row.year }}</span>
              </div>
            </template>
          </el-table-column>
          <el-table-column key="7" sortable prop="people" :label="keyMap['people']" width="110">
            <template slot-scope="scope">
              <el-input v-if="editModel[scope.row.id]" v-model="nowEditSampleInfo.people"></el-input>
              <el-tag v-else-if="scope.row.people" size="medium">{{ scope.row.people }}</el-tag>
            </template>
          </el-table-column>
          <el-table-column key="8" prop="imageId" :label="keyMap['imageId']" width="245">
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
          <el-table-column key="9" prop="describe" :label="keyMap['describe']" miniwidth="200">
            <template slot-scope="scope">
              <el-input v-if="editModel[scope.row.id]" type="textarea" autosize v-model="nowEditSampleInfo.describe"></el-input>
              <span v-else>
                {{ scope.row.describe }}
              </span>
            </template>
          </el-table-column>
          <el-table-column key="10" prop="explain" :label="keyMap['explain']" width="300">
            <template slot-scope="scope">
              <el-input v-if="editModel[scope.row.id]" type="textarea" autosize v-model="nowEditSampleInfo.explain"></el-input>
              <span v-else>
                {{ scope.row.explain }}
              </span>
            </template>
          </el-table-column>
          <el-table-column v-if="!multiModeFlag" key="11" label="操作" width="62">
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
        <el-pagination
          background
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="currentPage"
          :page-sizes="[100, 200, 300, 400]"
          :page-size="pageSize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="currentTableData.length">
        </el-pagination>
        <div style="text-align:center; width:100%; display:inline-block;">
          <!-- <span style="float:left;">总计：{{ currentTableData.length }}条</span> -->
          <div style="float:right;">
            导出：
            <el-button size="small" type="success" icon="el-icon-download" @click="exportTableData"></el-button>
          </div>
        </div>
      </el-tab-pane>
      <el-tab-pane closable :label="v.label" :name="v.name" v-for="v in editableTabs" :key="v.sampleId">
        <!-- 详细页面 -->
        <sample-page :ref="el => {if (el) samplePageComs[v.sampleId] = el}" :sampleId="v.sampleId"/>
        <hr><hr>
        <experiment-page :ref="el => {if (el) extPageComs[v.sampleId] = el}" :sampleId="v.sampleId"/>
        <div style="float:right;">
          导出：
          <el-button size="small" type="success" icon="el-icon-download" @click="exportExTableData(v.sampleId)"></el-button>
        </div>
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
import { ref, onBeforeUpdate } from 'vue'
import JSZip from 'jszip'
import { saveAs } from 'file-saver';

import { deepObjCopy } from '@/utils'
import SamplePage from '@/components/SamplePage.vue'
import ExperimentPage from '@/components/ExperimentPage.vue'

export default {
  name: 'HomeView',
  components: {
    SamplePage,
    ExperimentPage
  },
  setup() {
    const samplePageComs = ref({})
    const extPageComs = ref({})
    onBeforeUpdate(() => {
      samplePageComs.value = {}
      extPageComs.value = {}
    })
    return {
      samplePageComs,
      extPageComs
    }
  },
  data() {
    return {
      token: '',
      currentPage: 1,
      pageSize: 100,
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
      afterTableData: [],
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
      uploadFileList: [],
      multiModeFlag: false,
      multiSelectedList: [],
      multiDeleteDialogVisible: false
    }
  },
  watch: {
    sampleInfos: {
      handler() {
        this.inputFilterHandler()
      },
      deep: true
    },
    currentTableData: {
      handler() {
        this.afterTableData = this.currentTableData.slice((this.currentPage - 1) * this.pageSize, this.currentPage * this.pageSize)
      },
      deep: true
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

    this.axios.get('/api/sampleinfo', {
      params: {
        token: this.token
      }
    })
      .then(res => {
        if (res.status ==200) {
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
          this.currentTableData = this.sampleInfos.slice(0, this.pageSize)
          this.afterTableData = this.sampleInfos.slice(0, this.pageSize)
        }
      })
      .catch(() => {
        this.$message.error('出错啦！')
      })
  },
  methods: {
    typeSuggest(qs, cb) {
      if (qs && qs.trim()) {
        cb([])
      }
      else {
        cb([
          {value: '炉渣'},
          {value: '炉壁'},
          {value: '陶范'},
          {value: '坩埚'},
          {value: '鼓风管'},
          {value: '铜'},
          {value: '铁'},
          {value: '不明'}
        ])
      }
    },
    handleCurrentChange(val) {
      this.currentPage = val
      this.afterTableData = this.currentTableData.slice((val - 1) * this.pageSize, val * this.pageSize)
    },
    handleSizeChange(val) {
      this.pageSize = val
      let max_page = Math.ceil(this.currentTableData.length / this.pageSize)
      if (this.currentPage > max_page) {
        this.currentPage = 1
      }
      this.afterTableData = this.currentTableData.slice((this.currentPage - 1) * val, this.currentPage * val)
    },
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
      let flag = false
      this.editableTabs.forEach((v, i) => {
        if (v.sampleId == id) {
          this.activeTab = i + 1
          flag = true
        }
      })
      if (!flag) {
        this.editableTabs.push({
            label: id.trim() + ' 样品信息',
            name: String(this.editableTabs.length + 1),
            sampleId: id.trim()
          })
        this.lastActiveTab = this.activeTab
        this.activeTab = this.editableTabs.length
      }
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
      this.axios.delete('/api/sampleinfo/' + sampleId, {
        params: {
          token: this.token
        }
      })
        .then(res => {
          if (res.status == 200) {
            this.sampleInfos = this.sampleInfos.filter(v => v.id != sampleId)
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
      this.uploadFileList = this.uploadFileList.concat(res.data)
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
      this.axios.put('/api/sampleinfo/' + this.nowEditSampleInfo.id, this.nowEditSampleInfo, {
        params: {
          token: this.token
        }
      })
        .then(res => {
          if (res.status == 200) {
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
    },
    exportTableData() {
      var temp = deepObjCopy(this.currentTableData)
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
    },
    exportExTableData(sampleId) {
      let sp = this.samplePageComs[sampleId]
      let ep = this.extPageComs[sampleId]
      var wb = xlsx.utils.book_new()

      var temp = []
      var si = this.sampleInfos.filter(v => v.id == sampleId)[0]
      var ins = {};
      Object.keys(this.keyMap).forEach(k => {
        ins[this.keyMap[k]] = si[k]
      })
      temp.push(ins)
      var ws = xlsx.utils.json_to_sheet(temp)
      xlsx.utils.book_append_sheet(wb, ws, '1.样品基本信息')
      temp = []
      var temp2 = []
      var temp3 = []
      ins = {
        '金相': sp.jinxiang ? '有' : '无',
        '样品全图': sp.jinxiang ? sp.jinxiang.sampleImage : '',
        '描述': sp.jinxiang ? sp.jinxiang.sampleDescribe : '',
        '设备': sp.jinxiang ? sp.jinxiang.device : ''
      }
      sp.jinxiang?.imageData.forEach((v, i) => {
        ins['放大倍数' + (i + 1)] = v.zoom
        ins['拍摄模式' + (i + 1)] = v.photoMode
        ins['金相照片' + (i + 1)] = v.image
        ins['描述' + (i + 1)] = v.describe
      })
      temp.push(ins)
      ins = {
        '矿相': sp.kuangxiang ? '有' : '无',
        '薄片扫描图': sp.kuangxiang ? sp.kuangxiang.sampleImage : '',
        '描述': sp.kuangxiang ? sp.kuangxiang.sampleDescribe : '',
        '设备': sp.kuangxiang ? sp.kuangxiang.device : ''
      }
      sp.kuangxiang?.imageData.forEach((v, i) => {
        ins['放大倍数' + (i + 1)] = v.zoom
        ins['拍摄模式' + (i + 1)] = v.photoMode
        ins['矿相照片' + (i + 1)] = v.image
        ins['描述' + (i + 1)] = v.describe
      })
      temp2.push(ins)
      ins = {
        '电子显微照片': sp.dianzi ? '有' : '无',
        '样品全图': sp.dianzi ? sp.dianzi.sampleImage : '',
        '描述': sp.dianzi ? sp.dianzi.sampleDescribe : '',
        '设备': sp.dianzi ? sp.dianzi.device : ''
      }
      sp.dianzi?.imageData.forEach((v, i) => {
        ins['放大倍数' + (i + 1)] = v.zoom
        ins['拍摄模式' + (i + 1)] = v.photoMode
        ins['电子显微照片' + (i + 1)] = v.image
        ins['描述' + (i + 1)] = v.describe
      })
      temp3.push(ins)
      ws = xlsx.utils.json_to_sheet(temp)
      xlsx.utils.book_append_sheet(wb, ws, '2.显微组织观察-金相')
      ws = xlsx.utils.json_to_sheet(temp2)
      xlsx.utils.book_append_sheet(wb, ws, '2.显微组织观察-矿相')
      ws = xlsx.utils.json_to_sheet(temp3)
      xlsx.utils.book_append_sheet(wb, ws, '2.显微组织观察-电子显微照片')
      temp = []
      ep.mineContentInfos.forEach(v => {
        temp.push({
          '样品号': v.id,
          '黏土': v.clay,
          '粉砂': v.quartz,
          '砂-石英': v.sand_quartz,
          '砂-长石': v.sand_feldspar,
          '砂-其他矿物': v.sand_other,
          '小计': ep.sum([v.sand_quartz, v.sand_feldspar, v.sand_other]),
          '岩屑': v.debris,
          '空洞-闭气孔': v.hollow_close,
          '空洞-开气孔': v.hollow_open,
          '空洞-贯通气孔': v.hollow_through
        })
      })
      ws = xlsx.utils.json_to_sheet(temp)
      xlsx.utils.book_append_sheet(wb, ws, '3.矿物含量信息')
      temp = []
      temp2 = []
      ep.mineSurveyInfos.forEach(v => {
        temp.push({
          '样品号': v.id,
          '≤67μm': v.debris_0um,
          '67-167μm': v.debris_67um,
          '167-501μm': v.debris_167um,
          '501-1002μm': v.debris_501um,
          '≥1002μm': v.debris_1002um
        })
        temp2.push({
          '样品号': v.id,
          '≤67μm': v.hollow_0um,
          '67-501μm': v.hollow_67um,
          '501-1002μm': v.hollow_501um,
          '1002-2004μm': v.hollow_1002um,
          '≥2004μm': v.hollow_2004um
        })
      })
      ws = xlsx.utils.json_to_sheet(temp)
      xlsx.utils.book_append_sheet(wb, ws, '4.矿物测量数据-岩屑直径分布')
      ws = xlsx.utils.json_to_sheet(temp2)
      xlsx.utils.book_append_sheet(wb, ws, '4.矿物测量数据-空洞长度分布')
      temp = []
      ep.mineXRDInfos.forEach(v => {
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
      })
      ws = xlsx.utils.json_to_sheet(temp)
      xlsx.utils.book_append_sheet(wb, ws, '5.XRD分析数据')
      temp = []
      ep.mineChemistryInfos.forEach(v => {
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
      })
      ws = xlsx.utils.json_to_sheet(temp)
      xlsx.utils.book_append_sheet(wb, ws, '6.化学成分数据(氧化物)')
      temp = []
      ep.mineChemistryInfoSingle.forEach(v => {
        temp.push({
          '样品号': v.id,
          'C': v.C,
          'Na': v.Na,
          'Mg': v.Mg,
          'Al': v.Al,
          'Si': v.Si,
          'P': v.P,
          'S': v.S,
          'Cl': v.Cl,
          'K': v.K,
          'Ca': v.Ca,
          'Ti': v.Ti,
          'V': v.V,
          'Mn': v.Mn,
          'Fe': v.Fe,
          'Co': v.Co,
          'Ni': v.Ni,
          'Cu': v.Cu,
          'Zn': v.Zn,
          'As': v.As,
          'Ag': v.Ag,
          'Sn': v.Sn,
          'Sb': v.Sb,
          'Au': v.Au,
          'Hg': v.Hg,
          'Pb': v.Pb,
          '其他': v.other
        })
      })
      ws = xlsx.utils.json_to_sheet(temp)
      xlsx.utils.book_append_sheet(wb, ws, '6.化学成分数据(单质)')
      temp = []
      temp.push({
        '样品号': sp.physicalInfo ? sp.physicalInfo.id : '',
        '类型': sp.physicalInfo ? sp.physicalInfo.type : '',
        '密度': sp.physicalInfo ? sp.physicalInfo.trueDensity : '',
        '气孔率': sp.physicalInfo ? sp.physicalInfo.apparentPorosity : '',
        '吸水率': sp.physicalInfo ? sp.physicalInfo.waterAbsorption : '',
        '高温抗折强度': sp.physicalInfo ? sp.physicalInfo.bending : '',
        '热震稳定性系数': sp.physicalInfo ? sp.physicalInfo.resistance : '',
        '抗渣性系数': sp.physicalInfo ? sp.physicalInfo.slag : '',
        '耐碱性系数': sp.physicalInfo ? sp.physicalInfo.alkali : '',
        '荷重软化温度': sp.physicalInfo ? sp.physicalInfo.refractoriness : '',
        '导热系数': sp.physicalInfo ? sp.physicalInfo.heat : ''
      })
      ws = xlsx.utils.json_to_sheet(temp)
      xlsx.utils.book_append_sheet(wb, ws, '7.物理性能数据')
      temp = []
      ep.mineThermalInfos.forEach(v => {
        temp.push({
          '样品号': v.id,
          '熔点': v.melting,
          '耐火度': v.fireResis,
          '烧成温度': v.termTemper,
          // '原始数据': v.data,
          // '曲线图': v.surveImage
        })
      })
      ws = xlsx.utils.json_to_sheet(temp)
      xlsx.utils.book_append_sheet(wb, ws, '8.热分析')

      xlsx.writeFileXLSX(wb, `Export-EXP-${new Date().toISOString().split('T')[0]}.xlsx`)
    },
    doMultiOps() {
      this.multiModeFlag = true
    },
    cancelMultiMode() {
      this.multiModeFlag = false
      // this.multiSelectedList = []
    },
    handleSelectionChange(val) {
      this.multiSelectedList = val
      // this.multiSelectedList = []
      // val.forEach(v => {
      //   this.multiSelectedList.push(v.id)
      // })
    },
    multiSelectedListPre() {
      if (this.multiSelectedList.length > 0) {
        if (typeof this.multiSelectedList[0] != 'string') {
          let temp = this.multiSelectedList
          this.multiSelectedList = []
          temp.forEach(v => {
            this.multiSelectedList.push(v.id)
          })
        }
      }
    },
    async downloadSelectedImages() {
      if (this.multiSelectedList.length > 0) {
        this.multiSelectedListPre()
        const zip = new JSZip()
        for (let i in this.multiSelectedList) {
          let ids = this.multiSelectedList[i]
          let si = this.sampleInfos.filter(v => v.id == ids)[0]
          let ims = zip.folder(ids)
          for (let j in si.imageId) {
            let imid
            try {
              imid = si.imageId[j]
              let dt = await this.axios.get('/api/image/' + imid, {
                responseType: 'blob'
              })
              ims.file(imid, dt.data, {
                binary: true
              })
            }
            catch (err) {
              this.$message.error(ids + '/' + imid + ' 下载失败！')
              console.log(err)
            }
          }
        }
        zip.generateAsync({type: 'blob'})
          .then(content => {
            saveAs(content, `Export-IMG-${new Date().toISOString().split('T')[0]}.zip`)
          })
      }
    },
    multiDeletePre() {
      if (this.multiSelectedList.length > 0) {
        this.multiSelectedListPre()
        this.multiDeleteDialogVisible = true
      }
      else {
        this.$message.warning('请选择要删除的样本')
      }
    },
    deleteSelectedSample() {
      this.axios.delete('/api/sampleinfo', {
        data: this.multiSelectedList,
        params: {
          token: this.token
        }
      })
        .then(res => {
          if (res.status == 200) {
            let deleted_list = res.data.deleted_list
            this.sampleInfos = this.sampleInfos.filter(v => !deleted_list.includes(v.id))
            this.multiDeleteDialogVisible = false
            this.$message.success('删除[' + deleted_list + ']成功！')
            this.multiModeFlag = false
          }
          else {
            this.multiDeleteDialogVisible = false
            this.$message.error('出错啦！')
          }
        })
        .catch(err => {
          console.error(err)
          this.multiDeleteDialogVisible = false
          this.$message.error('出错啦！')
        })
    },
    toStatisticPage(key) {
      this.multiSelectedListPre()
      this.$store.commit('setStatisticInfos', this.multiSelectedList)
      this.$emit('changeSideMenuIndex', key)
      switch (key) {
        case '4-1':
          this.$router.replace({
            name: 'StatisticView1'
          })
          break
        case '4-2':
          this.$router.replace({
            name: 'StatisticView2'
          })
          break
        case '4-3':
          this.$router.replace({
            name:'StatisticView3'
          })
          break
        case '4-4':
          this.$router.replace({
            name: 'StatisticView4'
          })
          break
        case '4-5':
          this.$router.replace({
            name: 'StatisticView5'
          })
          break
        case '4-6':
          this.$router.replace({
            name: 'StatisticView6'
          })
          break
        default:
          break
      }
    }
  }
}
</script>