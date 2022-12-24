<template>
  <div id="ImportView">
    <!-- <h3 align="left">数据导入模块</h3>
    <p align="left">在此处下载导入模板：<el-link href="/api/txt/导入模板.xlsx" type="primary" icon="el-icon-document-copy">导入模板.xlsx</el-link></p> -->
    <h3 align="left">注意事项</h3>
    <p align="left">1. 导入功能需要确保各sheet命名正确</p>
    <p align="left">2. 导入功能需要各sheet内的表格规范放置</p>
    <p align="left">3. 表头请加粗，表格内数据请不要加粗</p>
    <p align="left">4. 表格数据的样品编号中的中文括号"（）"及内容将被忽略</p>
    <p align="left">5. 表格内的数据请不要使用合并单元格，表头也尽量减少合并单元格的使用</p>
    <p align="left">6. 一个sheet内可放置多个表格，请注意按照<el-link href="/api/excel/导入模板.xlsx" type="primary" icon="el-icon-document-copy">导入模板.xlsx</el-link>的样式排版</p>
    <p align="left">7. 仅支持<b>.xlsx</b>格式的文件，<b>.xls</b>旧格式不支持</p>

    <el-divider></el-divider>

    <el-form inline class="form" ref="form" label-width="100px" label-position="right" style="text-align:left;width:800px;">
      <el-form-item label="数据导入">
        <el-upload
          :action="'/api/import?token='+token"
          accept=".xlsx"
          ref="upload"
          name="upload"
          drag
          :on-success="handleUploadSuccess"
          :on-error="handleUploadError"
          :auto-upload="true"
          :data="{cover: cover}"
          style="width: 100%">
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
          <div class="el-upload__tip" slot="tip">只能上传xlsx文件</div>
        </el-upload>
      </el-form-item>
      <el-form-item label="覆盖模式">
         <el-checkbox v-model="cover">{{ cover ? '已启用' : '已关闭' }}</el-checkbox>
      </el-form-item>
    </el-form>

    <el-divider></el-divider>

    <div v-if="history.length > 0">
      <h3 align="left">导入历史</h3>
      <p align="left" v-for="h in history" :key="h">
        <el-link :href="'/api/import/'+h+'?token='+token" type="primary" icon="el-icon-document-copy">{{ h }}</el-link>
      </p>
    </div>
  </div>
</template>

<style scoped>
#ImportView {
  background: #fff;
  padding-top: 20px;
  padding-left: 10px;
  padding-bottom: 10px;
}
</style>

<script>
export default {
  name: "ImportView",
  data() {
    return {
      token: '',
      history: [],
      cover: false
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

    this.axios.get('/api/import', {
      params: {
        token: this.token
      }
    })
      .then(res => {
        if (res.status == 200) {
          this.history = res.data.data
        }
        else {
          this.$message.error('出错啦！')
        }
      })
  },
  methods: {
    submitUpload() {
      this.$refs.upload.submit()
    },
    handleUploadSuccess(res) {
      if (res.status == 200) {
        this.history.unshift(res.data)
        this.$message.success(res.msg)
      }
      else {
        this.$message.error(res.msg)
      }
    },
    handleUploadError(error, file) {
      this.$message.error(file.name + '没有上传成功')
    }
  }
}
</script>
