<template>
  <div id="AddView">
    <el-form class="form" ref="form" :model="form" :rules="rules" label-width="100px" label-position="right" style="width: 800px;">
        <el-form-item label="样品号" prop="id">
          <el-input v-model="form.id" placeholder="必填"></el-input>
        </el-form-item>
        <el-form-item label="样品类型">
          <el-autocomplete
            class="inline-input"
            v-model="form.type"
            :fetch-suggestions="typeSuggest"
            placeholder="请输入内容"
            style="width: 100%">
          </el-autocomplete>
          <!-- <el-select v-model="form.type" placeholder="请选择样品类型" style="width: 100%">
            <el-option label="炉渣" value="炉渣"></el-option>
            <el-option label="炉壁" value="炉壁"></el-option>
            <el-option label="陶范" value="陶范"></el-option>
            <el-option label="坩埚" value="坩埚"></el-option>
            <el-option label="鼓风管" value="鼓风管"></el-option>
            <el-option label="铜" value="铜"></el-option>
            <el-option label="铁" value="铁"></el-option>
            <el-option label="不明" value="不明"></el-option>
          </el-select> -->
        </el-form-item>
        <el-form-item label="样品来源">
          <el-input v-model="form.source"></el-input>
        </el-form-item>
        <el-form-item label="取样年份">
          <el-date-picker type="year" placeholder="选择日期" v-model="form.year" style="width: 100%"></el-date-picker>
        </el-form-item>
        <el-form-item label="取样人">
          <el-input v-model="form.people"></el-input>
        </el-form-item>
        <el-form-item label="照片">
          <!-- <el-input v-model="form.imageId"></el-input> -->
          <el-upload
            action="/api/image"
            accept="image/png, image/jpeg"
            ref="upload"
            name="upload"
            multiple
            drag
            :on-success="handleUploadSuccess"
            :on-error="handleUploadError"
            :auto-upload="true"
            style="width: 100%">
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
            <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过4MB</div>
          </el-upload>
        </el-form-item>
        <el-form-item label="描述">
          <el-input type="textarea" autosize v-model="form.describe"></el-input>
        </el-form-item>
        <el-form-item label="样品制备说明">
          <el-input type="textarea" autosize v-model="form.explain"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">立即增加</el-button>
          <el-button>取消</el-button>
        </el-form-item>
    </el-form>
  </div>
</template>

<style scoped>
#AddView {
  background: #fff;
  padding-top: 20px;
  padding-left: 10px;
  padding-bottom: 10px;
}
</style>

<script>
export default {
  name: 'AddView',
  data() {
    return {
      form: {
        id: '',
        type: '',
        source: '',
        year: 0,
        people: '',
        imageId: [],
        describe: '',
        explain: ''
      },
      rules: {
        id: [
          {required: true, message: '请输入样品号', trigger: 'blur'}
        ]
      },
      uploadFileList: []
    }
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
    handleUploadSuccess(res) {
      if (res.status == 200) {
        this.uploadFileList = this.uploadFileList.concat(res.data)
      }
    },
    handleUploadError(err, file) {
      this.$message.error(file.name + '没有上传成功：' + JSON.parse(err.message).msg)
    },
    onSubmit() {
      this.$refs.form.validate(valid => {
        if (valid) {
          if (this.form.year){
            this.form.year = this.form.year.getFullYear()
          }
          if (this.uploadFileList.length > 0) {
            this.form.imageId = this.uploadFileList
          }
          this.uploadFileList = []
          this.axios.post('/api/sampleinfo', this.form)
            .then(res => {
              if (res.status == 200 && res.data.status == 200) {
                this.$message.success('添加成功!')
                this.$refs.form.resetFields()
                this.form = {
                  id: '',
                  type: '',
                  source: '',
                  year: 0,
                  people: '',
                  imageId: [],
                  describe: '',
                  explain: ''
                }
                this.uploadFileList = []
                this.$refs.upload.clearFiles()
              }
              else {
                this.$message.error('出错啦！')
              }
            })
        }
      })
    }
  }
}
</script>
