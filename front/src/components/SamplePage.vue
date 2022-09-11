<template>
  <div id="SampleView">
    <el-descriptions class="margin-top" title="物理结构数据" :column="2" border>
      <template slot="extra">
        <el-button type="primary" size="small">{{ physicalInfo ? '修改' : '增加' }}</el-button>
      </template>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-s-order"></i>
          类型
        </template>
        {{ physicalInfo ? physicalInfo.type : '无' }}
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-document"></i>
          显气孔率（%）
        </template>
        {{ physicalInfo ? physicalInfo.apparentPorosity : '无' }}
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-document"></i>
          真密度（g/cm3）
        </template>
        {{ physicalInfo ? physicalInfo.trueDensity : '无' }}
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-document"></i>
          吸水率%（%）
        </template>
        {{ physicalInfo ? physicalInfo.waterAbsorption : '无' }}
      </el-descriptions-item>
    </el-descriptions>

    <hr>

    <el-descriptions class="margin-top" title="金相" :column="2" border>
      <template slot="extra">
        <el-button type="primary" size="small">{{ jinxiang ? '修改' : '增加' }}</el-button>
      </template>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-check"></i>
          有/无
        </template>
        {{ jinxiang ? '有' : '无' }}
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-picture"></i>
          样品全图
        </template>
        <div v-if="jinxiang">
          <el-popover trigger="hover" placement="top" v-for="iid in jinxiang.sampleImage" :key="iid">
            <el-image
                style="height: 200px"
                :src="'/api/image/' + iid"
                fit="contain">
                <div slot="error" class="image-slot">
                  <i class="el-icon-picture-outline"></i>
                </div>
            </el-image>
            <div slot="reference" class="name-wrapper">
              <span style="text-decoration: underline; color: #409EAF">{{ iid }} </span>
            </div>
          </el-popover>
        </div>
        <span v-else>
          无
        </span>
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-chat-line-square"></i>
          描述
        </template>
        {{ jinxiang ? jinxiang.sampleDescribe : '无' }}
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-camera-solid"></i>
          设备
        </template>
        {{ jinxiang ? jinxiang.device : '无' }}
      </el-descriptions-item>
    </el-descriptions>

    <el-table
      v-if="jinxiang"
      :data="jinxiang.imageData"
      stripe
      border
      style="width: 100%">
      <el-table-column sortable prop="zoom" label="放大倍数" width="200"></el-table-column>
      <el-table-column sortable prop="photoMode" label="拍摄模式" width="110"></el-table-column>
      <el-table-column prop="image" label="金相照片" miniwidth="300">
        <template slot-scope="scope">
          <el-image
            style="height: 200px"
            :src="'/api/image/' + scope.row.image"
            fit="contain">
            <div slot="error" class="image-slot">
              <i class="el-icon-picture-outline"></i>
            </div>
          </el-image>
        </template>
      </el-table-column>
      <el-table-column sortable prop="describe" label="描述" width="110"></el-table-column>
    </el-table>

    <hr>

    <el-descriptions class="margin-top" title="矿相" :column="2" border>
      <template slot="extra">
        <el-button type="primary" size="small">{{ kuangxiang ? '修改' : '增加' }}</el-button>
      </template>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-check"></i>
          有/无
        </template>
        {{ kuangxiang ? '有' : '无' }}
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-picture"></i>
          薄片扫描图
        </template>
        <div v-if="kuangxiang">
          <el-popover trigger="hover" placement="top" v-for="iid in kuangxiang.sampleImage" :key="iid">
            <el-image
                style="height: 200px"
                :src="'/api/image/' + iid"
                fit="contain">
                <div slot="error" class="image-slot">
                  <i class="el-icon-picture-outline"></i>
                </div>
            </el-image>
            <div slot="reference" class="name-wrapper">
              <span style="text-decoration: underline; color: #409EAF">{{ iid }} </span>
            </div>
          </el-popover>
        </div>
        <span v-else>
          无
        </span>
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-chat-line-square"></i>
          描述
        </template>
        {{ kuangxiang ? kuangxiang.sampleDescribe : '无' }}
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-camera-solid"></i>
          设备
        </template>
        {{ kuangxiang ? kuangxiang.device : '无' }}
      </el-descriptions-item>
    </el-descriptions>

    <el-table
      v-if="kuangxiang"
      :data="kuangxiang.imageData"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="zoom" label="放大倍数" width="77"></el-table-column>
      <el-table-column prop="photoMode" label="拍摄模式" width="77"></el-table-column>
      <el-table-column prop="image" label="矿相照片" miniwidth="300">
        <template slot-scope="scope">
          <el-image
            style="height: 200px"
            :src="'/api/image/' + scope.row.image"
            fit="contain">
            <div slot="error" class="image-slot">
              <i class="el-icon-picture-outline"></i>
            </div>
          </el-image>
        </template>
      </el-table-column>
      <el-table-column prop="describe" label="描述" miniwidth="200"></el-table-column>
    </el-table>

    <hr>

    <el-descriptions class="margin-top" title="电子显微照片" :column="2" border>
      <template slot="extra">
        <el-button type="primary" size="small">{{ dianzi ? '修改' : '增加' }}</el-button>
      </template>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-check"></i>
          有/无
        </template>
        {{ dianzi ? '有' : '无' }}
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-picture"></i>
          样品全图
        </template>
        <div v-if="dianzi">
          <el-popover trigger="hover" placement="top" v-for="iid in dianzi.sampleImage" :key="iid">
            <el-image
                style="height: 200px"
                :src="'/api/image/' + iid"
                fit="contain">
                <div slot="error" class="image-slot">
                  <i class="el-icon-picture-outline"></i>
                </div>
            </el-image>
            <div slot="reference" class="name-wrapper">
              <span style="text-decoration: underline; color: #409EAF">{{ iid }} </span>
            </div>
          </el-popover>
        </div>
        <span v-else>
          无
        </span>
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-chat-line-square"></i>
          描述
        </template>
        {{ dianzi ? dianzi.sampleDescribe : '无' }}
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-camera-solid"></i>
          设备
        </template>
        {{ dianzi ? dianzi.device : '无' }}
      </el-descriptions-item>
    </el-descriptions>

    <el-table
      v-if="dianzi"
      :data="dianzi.imageData"
      stripe
      border
      style="width: 100%">
      <el-table-column prop="zoom" label="放大倍数" width="77"></el-table-column>
      <el-table-column prop="photoMode" label="拍摄模式" width="77"></el-table-column>
      <el-table-column prop="image" label="电子显微照片" miniwidth="300">
        <template slot-scope="scope">
          <el-image
            style="height: 200px"
            :src="'/api/image/' + scope.row.image"
            fit="contain">
            <div slot="error" class="image-slot">
              <i class="el-icon-picture-outline"></i>
            </div>
          </el-image>
        </template>
      </el-table-column>
      <el-table-column prop="describe" label="描述" miniwidth="200"></el-table-column>
    </el-table>
  </div>
</template>

<style scoped>
#SampleView {
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
  name: 'SamplePage',
  props: {
    sampleId: String
  },
  data() {
    return {
      // sampleInfo: null,
      physicalInfo: null,
      jinxiang: null,
      kuangxiang: null,
      dianzi: null
    }
  },
  mounted() {
    if (!this.sampleId) {
      this.$message.error('出错啦！')
      return
    }
    // this.sampleInfo = this.$store.getters.getSampleInfo(this.sampleId)
    this.axios.get('/api/microview/' + this.sampleId)
      .then((res) => {
        if (res.status == 200 && res.data.status == 200) {
          var microInfos = res.data.data
          microInfos.forEach(v => {
            switch (v.type) {
              case '金相':
                this.jinxiang = v
                break
              case '矿相':
                this.kuangxiang = v
                break
              case '电子显微照片':
                this.dianzi = v
                break
            }
          })
          // this.$store.commit('setSampleInfos', res.data.data)
        }
        else {
          this.$message.error('出错啦！')
        }
      })
    this.axios.get('/api/minephysicsinfo/' + this.sampleId)
      .then((res) => {
        if (res.status == 200 && res.data.status == 200) {
          this.physicalInfo = res.data.data
        }
        else {
          this.$message.error('出错啦！')
        }
      })
  }
}
</script>
