<template>
  <div id="AddView">
    <el-form class="form" ref="form" :model="form" label-width="100px" label-position="right" style="width: 800px;">
        <el-form-item label="样品号">
          <el-input v-model="form.sampleId"></el-input>
        </el-form-item>
        <el-form-item label="样品类型">
          <el-select v-model="form.sampleType" placeholder="请选择样品类型" style="width: 100%">
            <el-option label="炉渣" value="炉渣"></el-option>
            <el-option label="炉壁" value="炉壁"></el-option>
            <el-option label="陶范" value="陶范"></el-option>
            <el-option label="坩埚" value="坩埚"></el-option>
            <el-option label="鼓风管" value="鼓风管"></el-option>
            <el-option label="铜" value="铜"></el-option>
            <el-option label="铁" value="铁"></el-option>
            <el-option label="不明" value="不明"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="样品来源">
          <el-input v-model="form.sampleSource"></el-input>
        </el-form-item>
        <el-form-item label="取样年份">
          <el-date-picker type="year" placeholder="选择日期" v-model="form.samplingYear" style="width: 100%"></el-date-picker>
        </el-form-item>
        <el-form-item label="取样人">
          <el-input v-model="form.samplingPeople"></el-input>
        </el-form-item>
        <el-form-item label="照片">
          <!-- <el-input v-model="form.imageId"></el-input> -->
          <el-upload
            drag
            action="http://自建图床"
            multiple
            style="width: 100%">
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
            <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过1Mb</div>
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
          sampleId: '',
          sampleType: '',
          sampleSource: '',
          samplingYear: 0,
          samplingPeople: '',
          imageId: '',
          describe: '',
          explain: ''
        }
    }
  },
  methods: {
    onSubmit() {
      console.log('submit!')
    }
  }
}
</script>
