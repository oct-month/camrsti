<template>
  <div id="ImportView">
    <!-- TODO -->
    <el-form class="form" ref="form" label-width="100px" label-position="right" style="width: 800px;">
      <el-form-item label="数据导入">
        <el-upload
          action="/api/import"
          accept=".xlsx"
          ref="upload"
          name="upload"
          drag
          :on-success="handleUploadSuccess"
          :on-error="handleUploadError"
          :auto-upload="true"
          style="width: 100%">
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
          <div class="el-upload__tip" slot="tip">只能上传xlsx文件</div>
        </el-upload>
      </el-form-item>
    </el-form>
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
    }
  },
  methods: {
    submitUpload() {
      this.$refs.upload.submit()
    },
    handleUploadSuccess(res) {
      if (res.status == 200) {
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
