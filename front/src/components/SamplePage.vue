<template>
  <div id="SampleView">
    <!-- 物理结构数据 -->
    <el-descriptions class="margin-top" title="物理结构数据" :column="2" border>
      <template slot="extra">
        <div v-if="physicalInfoFlag" style="text-align:center;">
          <el-button size="small" type="success" icon="el-icon-check" circle @click="submitPhysicalInfoEdit"></el-button>
          <el-button size="mini" type="danger" icon="el-icon-close" circle @click="cancelPhysicalInfoEdit"></el-button>
        </div>
        <el-button v-else type="primary" size="small" @click="setPhysicalInfo">{{ physicalInfo ? '修改' : '增加' }}</el-button>
      </template>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-s-order"></i>
          类型
        </template>
        <el-input v-if="physicalInfoFlag" v-model="physicalInfo_E.type"></el-input>
        <span v-else>{{ physicalInfo ? physicalInfo.type : '无' }}</span>
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-document"></i>
          显气孔率（%）
        </template>
        <el-input v-if="physicalInfoFlag" v-model="physicalInfo_E.apparentPorosity" @change="phyInputValid('apparentPorosity')"></el-input>
        <span v-else>{{ physicalInfo ? physicalInfo.apparentPorosity : '无' }}</span>
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-document"></i>
          真密度（g/cm3）
        </template>
        <el-input v-if="physicalInfoFlag" v-model="physicalInfo_E.trueDensity" @change="phyInputValid('trueDensity')"></el-input>
        <span v-else>{{ physicalInfo ? physicalInfo.trueDensity : '无' }}</span>
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-document"></i>
          吸水率%（%）
        </template>
        <el-input v-if="physicalInfoFlag" v-model="physicalInfo_E.waterAbsorption" @change="phyInputValid('waterAbsorption')"></el-input>
        <span v-else>{{ physicalInfo ? physicalInfo.waterAbsorption : '无' }}</span>
      </el-descriptions-item>
    </el-descriptions>

    <hr>

    <!-- 金相 -->
    <el-descriptions class="margin-top" title="金相" :column="2" border>
      <template slot="extra">
        <div v-if="jinxiangFlag" style="text-align:center;">
          <el-button size="small" type="success" icon="el-icon-check" circle @click="submitjinxiangEdit"></el-button>
          <el-button size="mini" type="danger" icon="el-icon-close" circle @click="canceljinxiangEdit"></el-button>
        </div>
        <el-button v-else type="primary" size="small" @click="setjinxiang">{{ jinxiang ? '修改' : '增加' }}</el-button>
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
        <el-upload
          v-if="jinxiangFlag"
          action="/api/image"
          accept="image/png, image/jpeg"
          ref="upload"
          name="upload"
          multiple
          :on-success="jinxiangHandleUploadSuccess"
          :on-error="handleUploadError"
          :auto-upload="true">
          <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
          <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过4MB</div>
        </el-upload>
        <div v-else-if="jinxiang">
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
        <el-input v-if="jinxiangFlag" v-model="jinxiang_E.sampleDescribe"></el-input>
        <span v-else>{{ jinxiang ? jinxiang.sampleDescribe : '无' }}</span>
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-camera-solid"></i>
          设备
        </template>
        <el-input v-if="jinxiangFlag" v-model="jinxiang_E.device"></el-input>
        <span v-else>{{ jinxiang ? jinxiang.device : '无' }}</span>
      </el-descriptions-item>
    </el-descriptions>

    <div v-if="jinxiang">
      <el-table
        :data="jinxiang.imageData"
        stripe
        border
        style="width: 100%">
        <el-table-column prop="zoom" label="放大倍数" width="100">
          <template slot-scope="scope">
            <el-input v-if="jinxiangItemFlag && scope.row.temp" v-model="jinxiangItem_E.zoom" @change="zoomInputValid('jinxiangItem_E')"></el-input>
            <el-input v-else-if="editItemModel[scope.row.id]" v-model="nowEditItem.zoom" @change="zoomInputValid('nowEditItem')"></el-input>
            <span v-else>{{ scope.row.zoom }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="photoMode" label="拍摄模式" width="100">
          <template slot-scope="scope">
            <el-select v-if="jinxiangItemFlag && scope.row.temp" v-model="jinxiangItem_E.photoMode">
              <el-option label="明场" value="明场"></el-option>
              <el-option label="暗场" value="暗场"></el-option>
            </el-select>
            <el-select v-else-if="editItemModel[scope.row.id]" v-model="nowEditItem.photoMode">
              <el-option label="明场" value="明场"></el-option>
              <el-option label="暗场" value="暗场"></el-option>
            </el-select>
            <span v-else>{{ scope.row.photoMode }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="image" label="金相照片" miniwidth="300">
          <template slot-scope="scope">
            <el-upload
              v-if="jinxiangItemFlag && scope.row.temp"
              action="/api/image"
              accept="image/png, image/jpeg"
              ref="upload"
              name="upload"
              :on-success="jinxiangItemHandleUploadSuccess"
              :on-error="handleUploadError"
              :auto-upload="true">
              <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
              <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过4MB</div>
            </el-upload>
            <el-upload
              v-if="editItemModel[scope.row.id]"
              action="/api/image"
              accept="image/png, image/jpeg"
              ref="upload"
              name="upload"
              :on-success="itemHandleUploadSuccess"
              :on-error="handleUploadError"
              :auto-upload="true">
              <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
              <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过4MB</div>
            </el-upload>
            <el-image
              v-else
              style="height: 200px"
              :src="'/api/image/' + scope.row.image"
              fit="contain">
              <div slot="error" class="image-slot">
                <i class="el-icon-picture-outline"></i>
              </div>
            </el-image>
          </template>
        </el-table-column>
        <el-table-column prop="describe" label="描述" miniwidth="200">
          <template slot-scope="scope">
            <el-input v-if="jinxiangItemFlag && scope.row.temp" type="textarea" autosize v-model="jinxiangItem_E.describe"></el-input>
            <el-input v-else-if="editItemModel[scope.row.id]" type="textarea" autosize v-model="nowEditItem.describe"></el-input>
            <span v-else>{{ scope.row.describe }}</span>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="62">
          <template slot-scope="scope">
            <div v-if="editItemModel[scope.row.id] && !scope.row.temp" style="text-align:center;">
              <el-button size="small" type="success" icon="el-icon-check" circle @click="submitItemEdit(scope.row.id)"></el-button><br>
              <el-button size="mini" type="danger" icon="el-icon-close" circle @click="cancelItemEdit(scope.row.id)"></el-button>
            </div>
            <div v-else-if="!scope.row.temp" style="text-align:center;">
              <el-button size="mini" round plain type="warning" icon="el-icon-edit" @click="editItem(scope.row.id)"></el-button><br>
              <el-button size="mini" round plain type="danger" icon="el-icon-delete" @click="$set(deleteDialogVisible, scope.row.id, true)"></el-button>
              <el-dialog title="确认" :visible.sync="deleteDialogVisible[scope.row.id]" width="30%">
                <span>删除?</span>
                <span slot="footer" class="dialog-footer">
                  <el-button @click="deleteDialogVisible[scope.row.id]=false">取 消</el-button>
                  <el-button type="primary" @click="deleteItem(scope.row.id)">确 定</el-button>
                </span>
              </el-dialog>
            </div>
          </template>
        </el-table-column>
      </el-table>
      <div style="text-align:center; width:100%; display:inline-block;">
        <span style="float:left;">总计：{{ jinxiang.imageData.length - jinxiangItemFlag }}条</span>
        <div v-if="jinxiangItemFlag" style="float:right;">
          <el-button size="small" type="success" icon="el-icon-check" circle @click="submitjinxiangItemEdit"></el-button>
          <el-button size="mini" type="danger" icon="el-icon-close" circle @click="canceljinxiangItemEdit"></el-button>
        </div>
        <el-button v-else style="float:right;" size="small" type="success" icon="el-icon-plus" @click="jinxiangItemAdd"></el-button>
      </div>
    </div>

    <hr>

    <!-- 矿相 -->
    <el-descriptions class="margin-top" title="矿相" :column="2" border>
      <template slot="extra">
        <div v-if="kuangxiangFlag" style="text-align:center;">
          <el-button size="small" type="success" icon="el-icon-check" circle @click="submitkuangxiangEdit"></el-button>
          <el-button size="mini" type="danger" icon="el-icon-close" circle @click="cancelkuangxiangEdit"></el-button>
        </div>
        <el-button v-else type="primary" size="small" @click="setkuangxiang">{{ kuangxiang ? '修改' : '增加' }}</el-button>
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
        <el-upload
          v-if="kuangxiangFlag"
          action="/api/image"
          accept="image/png, image/jpeg"
          ref="upload"
          name="upload"
          multiple
          :on-success="kuangxiangHandleUploadSuccess"
          :on-error="handleUploadError"
          :auto-upload="true">
          <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
          <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过4MB</div>
        </el-upload>
        <div v-else-if="kuangxiang">
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
        <el-input v-if="kuangxiangFlag" v-model="kuangxiang_E.sampleDescribe"></el-input>
        <span v-else>{{ kuangxiang ? kuangxiang.sampleDescribe : '无' }}</span>
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-camera-solid"></i>
          设备
        </template>
        <el-input v-if="kuangxiangFlag" v-model="kuangxiang_E.device"></el-input>
        <span v-else>{{ kuangxiang ? kuangxiang.device : '无' }}</span>
      </el-descriptions-item>
    </el-descriptions>

    <div v-if="kuangxiang">
      <el-table
        :data="kuangxiang.imageData"
        stripe
        border
        style="width: 100%">
        <el-table-column prop="zoom" label="放大倍数" width="100">
          <template slot-scope="scope">
            <el-input v-if="kuangxiangItemFlag && scope.row.temp" v-model="kuangxiangItem_E.zoom" @change="zoomInputValid('kuangxiangItem_E')"></el-input>
            <el-input v-else-if="editItemModel[scope.row.id]" v-model="nowEditItem.zoom" @change="zoomInputValid('nowEditItem')"></el-input>
            <span v-else>{{ scope.row.zoom }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="photoMode" label="拍摄模式" width="100">
          <template slot-scope="scope">
            <el-select v-if="kuangxiangItemFlag && scope.row.temp" v-model="kuangxiangItem_E.photoMode">
              <el-option label="XPL" value="XPL"></el-option>
              <el-option label="PPL" value="PPL"></el-option>
            </el-select>
            <el-select v-else-if="editItemModel[scope.row.id]" v-model="nowEditItem.photoMode">
              <el-option label="XPL" value="XPL"></el-option>
              <el-option label="PPL" value="PPL"></el-option>
            </el-select>
            <span v-else>{{ scope.row.photoMode }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="image" label="矿相照片" miniwidth="300">
          <template slot-scope="scope">
            <el-upload
              v-if="kuangxiangItemFlag && scope.row.temp"
              action="/api/image"
              accept="image/png, image/jpeg"
              ref="upload"
              name="upload"
              :on-success="kuangxiangItemHandleUploadSuccess"
              :on-error="handleUploadError"
              :auto-upload="true">
              <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
              <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过4MB</div>
            </el-upload>
            <el-upload
              v-if="editItemModel[scope.row.id]"
              action="/api/image"
              accept="image/png, image/jpeg"
              ref="upload"
              name="upload"
              :on-success="itemHandleUploadSuccess"
              :on-error="handleUploadError"
              :auto-upload="true">
              <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
              <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过4MB</div>
            </el-upload>
            <el-image
              v-else
              style="height: 200px"
              :src="'/api/image/' + scope.row.image"
              fit="contain">
              <div slot="error" class="image-slot">
                <i class="el-icon-picture-outline"></i>
              </div>
            </el-image>
          </template>
        </el-table-column>
        <el-table-column prop="describe" label="描述" miniwidth="200">
          <template slot-scope="scope">
            <el-input v-if="kuangxiangItemFlag && scope.row.temp" type="textarea" autosize v-model="kuangxiangItem_E.describe"></el-input>
            <el-input v-else-if="editItemModel[scope.row.id]" type="textarea" autosize v-model="nowEditItem.describe"></el-input>
            <span v-else>{{ scope.row.describe }}</span>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="62">
          <template slot-scope="scope">
            <div v-if="editItemModel[scope.row.id] && !scope.row.temp" style="text-align:center;">
              <el-button size="small" type="success" icon="el-icon-check" circle @click="submitItemEdit(scope.row.id)"></el-button><br>
              <el-button size="mini" type="danger" icon="el-icon-close" circle @click="cancelItemEdit(scope.row.id)"></el-button>
            </div>
            <div v-else-if="!scope.row.temp" style="text-align:center;">
              <el-button size="mini" round plain type="warning" icon="el-icon-edit" @click="editItem(scope.row.id)"></el-button><br>
              <el-button size="mini" round plain type="danger" icon="el-icon-delete" @click="$set(deleteDialogVisible, scope.row.id, true)"></el-button>
              <el-dialog title="确认" :visible.sync="deleteDialogVisible[scope.row.id]" width="30%">
                <span>删除?</span>
                <span slot="footer" class="dialog-footer">
                  <el-button @click="deleteDialogVisible[scope.row.id]=false">取 消</el-button>
                  <el-button type="primary" @click="deleteItem(scope.row.id)">确 定</el-button>
                </span>
              </el-dialog>
            </div>
          </template>
        </el-table-column>
      </el-table>
      <div style="text-align:center; width:100%; display:inline-block;">
        <span style="float:left;">总计：{{ kuangxiang.imageData.length - kuangxiangItemFlag }}条</span>
        <div v-if="kuangxiangItemFlag" style="float:right;">
          <el-button size="small" type="success" icon="el-icon-check" circle @click="submitkuangxiangItemEdit"></el-button>
          <el-button size="mini" type="danger" icon="el-icon-close" circle @click="cancelkuangxiangItemEdit"></el-button>
        </div>
        <el-button v-else style="float:right;" size="small" type="success" icon="el-icon-plus" @click="kuangxiangItemAdd"></el-button>
      </div>
    </div>

    <hr>

    <!-- 电子显微照片 -->
    <el-descriptions class="margin-top" title="电子显微照片" :column="2" border>
      <template slot="extra">
        <div v-if="dianziFlag" style="text-align:center;">
          <el-button size="small" type="success" icon="el-icon-check" circle @click="submitdianziEdit"></el-button>
          <el-button size="mini" type="danger" icon="el-icon-close" circle @click="canceldianziEdit"></el-button>
        </div>
        <el-button v-else type="primary" size="small" @click="setdianzi">{{ dianzi ? '修改' : '增加' }}</el-button>
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
        <el-upload
          v-if="dianziFlag"
          action="/api/image"
          accept="image/png, image/jpeg"
          ref="upload"
          name="upload"
          multiple
          :on-success="dianziHandleUploadSuccess"
          :on-error="handleUploadError"
          :auto-upload="true">
          <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
          <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过4MB</div>
        </el-upload>
        <div v-else-if="dianzi">
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
        <el-input v-if="dianziFlag" v-model="dianzi_E.sampleDescribe"></el-input>
        <span v-else>{{ dianzi ? dianzi.sampleDescribe : '无' }}</span>
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-camera-solid"></i>
          设备
        </template>
        <el-input v-if="dianziFlag" v-model="dianzi_E.device"></el-input>
        <span v-else>{{ dianzi ? dianzi.device : '无' }}</span>
      </el-descriptions-item>
    </el-descriptions>

    <div v-if="dianzi">
      <el-table
        :data="dianzi.imageData"
        stripe
        border
        style="width: 100%">
        <el-table-column prop="zoom" label="放大倍数" width="100">
          <template slot-scope="scope">
            <el-input v-if="dianziItemFlag && scope.row.temp" v-model="dianziItem_E.zoom" @change="zoomInputValid('dianziItem_E')"></el-input>
            <el-input v-else-if="editItemModel[scope.row.id]" v-model="nowEditItem.zoom" @change="zoomInputValid('nowEditItem')"></el-input>
            <span v-else>{{ scope.row.zoom }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="photoMode" label="拍摄模式" width="100">
          <template slot-scope="scope">
            <el-select v-if="dianziItemFlag && scope.row.temp" v-model="dianziItem_E.photoMode">
              <el-option label="SE" value="SE"></el-option>
              <el-option label="BSE" value="BSE"></el-option>
            </el-select>
            <el-select v-else-if="editItemModel[scope.row.id]" v-model="nowEditItem.photoMode">
              <el-option label="SE" value="SE"></el-option>
              <el-option label="BSE" value="BSE"></el-option>
            </el-select>
            <span v-else>{{ scope.row.photoMode }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="image" label="电子显微照片" miniwidth="300">
          <template slot-scope="scope">
            <el-upload
              v-if="dianziItemFlag && scope.row.temp"
              action="/api/image"
              accept="image/png, image/jpeg"
              ref="upload"
              name="upload"
              :on-success="dianziItemHandleUploadSuccess"
              :on-error="handleUploadError"
              :auto-upload="true">
              <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
              <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过4MB</div>
            </el-upload>
            <el-upload
              v-if="editItemModel[scope.row.id]"
              action="/api/image"
              accept="image/png, image/jpeg"
              ref="upload"
              name="upload"
              :on-success="itemHandleUploadSuccess"
              :on-error="handleUploadError"
              :auto-upload="true">
              <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
              <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过4MB</div>
            </el-upload>
            <el-image
              v-else
              style="height: 200px"
              :src="'/api/image/' + scope.row.image"
              fit="contain">
              <div slot="error" class="image-slot">
                <i class="el-icon-picture-outline"></i>
              </div>
            </el-image>
          </template>
        </el-table-column>
        <el-table-column prop="describe" label="描述" miniwidth="200">
          <template slot-scope="scope">
            <el-input v-if="dianziItemFlag && scope.row.temp" type="textarea" autosize v-model="dianziItem_E.describe"></el-input>
            <el-input v-else-if="editItemModel[scope.row.id]" type="textarea" autosize v-model="nowEditItem.describe"></el-input>
            <span v-else>{{ scope.row.describe }}</span>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="62">
          <template slot-scope="scope">
            <div v-if="editItemModel[scope.row.id] && !scope.row.temp" style="text-align:center;">
              <el-button size="small" type="success" icon="el-icon-check" circle @click="submitItemEdit(scope.row.id)"></el-button><br>
              <el-button size="mini" type="danger" icon="el-icon-close" circle @click="cancelItemEdit(scope.row.id)"></el-button>
            </div>
            <div v-else-if="!scope.row.temp" style="text-align:center;">
              <el-button size="mini" round plain type="warning" icon="el-icon-edit" @click="editItem(scope.row.id)"></el-button><br>
              <el-button size="mini" round plain type="danger" icon="el-icon-delete" @click="$set(deleteDialogVisible, scope.row.id, true)"></el-button>
              <el-dialog title="确认" :visible.sync="deleteDialogVisible[scope.row.id]" width="30%">
                <span>删除?</span>
                <span slot="footer" class="dialog-footer">
                  <el-button @click="deleteDialogVisible[scope.row.id]=false">取 消</el-button>
                  <el-button type="primary" @click="deleteItem(scope.row.id)">确 定</el-button>
                </span>
              </el-dialog>
            </div>
          </template>
        </el-table-column>
      </el-table>
      <div style="text-align:center; width:100%; display:inline-block;">
        <span style="float:left;">总计：{{ dianzi.imageData.length - dianziItemFlag }}条</span>
        <div v-if="dianziItemFlag" style="float:right;">
          <el-button size="small" type="success" icon="el-icon-check" circle @click="submitdianziItemEdit"></el-button>
          <el-button size="mini" type="danger" icon="el-icon-close" circle @click="canceldianziItemEdit"></el-button>
        </div>
        <el-button v-else style="float:right;" size="small" type="success" icon="el-icon-plus" @click="dianziItemAdd"></el-button>
      </div>
    </div>
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
import { deepObjCopy } from '@/utils'

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
      dianzi: null,
      physicalInfoFlag: false,
      physicalInfo_E: null,
      jinxiangFlag: false,
      jinxiang_E: null,
      jinxiang_E_up1: [],
      jinxiangItemFlag: false,
      jinxiangItem_E: null,
      kuangxiangFlag: false,
      kuangxiang_E: null,
      kuangxiang_E_up1: [],
      kuangxiangItemFlag: false,
      kuangxiangItem_E: null,
      dianziFlag: false,
      dianzi_E: null,
      dianzi_E_up1: [],
      dianziItemFlag: false,
      dianziItem_E: null,
      editItemModel: {},
      deleteDialogVisible: {},
      nowEditItem: null
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
            this.$set(this.deleteDialogVisible, v.id, false)
            this.$set(this.editItemModel, v.id, false)
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
  },
  methods: {
    setPhysicalInfo() {
      if (this.physicalInfo) {
        this.physicalInfo_E = deepObjCopy(this.physicalInfo)
      }
      else {
        this.physicalInfo_E = {
          id: this.sampleId,
          type: '',
          apparentPorosity: '',
          trueDensity: '',
          waterAbsorption: ''
        }
      }
      this.physicalInfoFlag = true
    },
    phyInputValid(key) {
      if (typeof this.physicalInfo_E[key] == 'number') {
        return
      }
      this.physicalInfo_E[key] = this.physicalInfo_E[key].trim()
      var point_flag = false
      for (let i = 0; i < this.physicalInfo_E[key].length; ++ i) {
        if (this.physicalInfo_E[key][i] == '.' && !point_flag) {
          point_flag = true
        }
        else if (this.physicalInfo_E[key][i] < '0' || this.physicalInfo_E[key][i] > '9') {
          this.physicalInfo_E[key] = this.physicalInfo_E[key].substring(0, i)
          break
        }
      }
    },
    submitPhysicalInfoEdit() {
      this.physicalInfo_E.type = this.physicalInfo_E.type.trim()
      this.physicalInfo_E.apparentPorosity = Number(this.physicalInfo_E.apparentPorosity)
      this.physicalInfo_E.trueDensity = Number(this.physicalInfo_E.trueDensity)
      this.physicalInfo_E.waterAbsorption = Number(this.physicalInfo_E.waterAbsorption)
      this.axios.put('/api/minephysicsinfo', this.physicalInfo_E)
        .then(res => {
          if (res.status == 200 && res.data.status == 200) {
            this.physicalInfo =this.physicalInfo_E
            this.physicalInfo_E = null
            this.$message.success('修改' + this.sampleId+ '物理结构数据成功！')
          }
          else {
            this.$message.error('出错啦！')
          }
        })
      this.physicalInfoFlag = false
    },
    cancelPhysicalInfoEdit() {
      this.physicalInfo_E = null
      this.physicalInfoFlag = false
    },
    setjinxiang() {
      if (this.jinxiang) {
        this.jinxiang_E = deepObjCopy(this.jinxiang)
      }
      else {
        this.jinxiang_E = {
          type: '金相',
          sampleImage: [],
          sampleDescribe: '',
          device: '',
          imageData: [],
          sampleId: this.sampleId
        }
      }
      this.jinxiangFlag = true
    },
    submitjinxiangEdit() {
      this.jinxiang_E.sampleDescribe = this.jinxiang_E.sampleDescribe.trim()
      this.jinxiang_E.device = this.jinxiang_E.device.trim()
      if (this.jinxiang_E_up1.length) {
        this.jinxiang_E.sampleImage = this.jinxiang_E_up1
        this.jinxiang_E_up1 = []
      }
      this.axios.put('/api/microview', this.jinxiang_E)
        .then(res => {
          if (res.status == 200 && res.data.status == 200) {
            this.jinxiang = this.jinxiang_E
            this.jinxiang.id = res.data.id
            this.jinxiang_E = null
            this.$message.success('修改' + this.sampleId+ '金相数据成功！')
          }
          else {
            this.$message.error('出错啦！')
          }
        })
      this.jinxiangFlag = false
    },
    canceljinxiangEdit() {
      this.jinxiang_E = null
      this.jinxiangFlag = false
    },
    jinxiangHandleUploadSuccess(res) {
      if (res.status == 200) {
        this.jinxiang_E_up1 = this.jinxiang_E_up1.concat(res.data)
      }
    },
    handleUploadError(err, file) {
      this.$message.error(file.name + '没有上传成功：' + JSON.parse(err.message).msg)
    },
    setkuangxiang() {
      if (this.kuangxiang) {
        this.kuangxiang_E = deepObjCopy(this.kuangxiang)
      }
      else {
        this.kuangxiang_E = {
          type: '矿相',
          sampleImage: [],
          sampleDescribe: '',
          device: '',
          imageData: [],
          sampleId: this.sampleId
        }
      }
      this.kuangxiangFlag = true
    },
    submitkuangxiangEdit() {
      this.kuangxiang_E.sampleDescribe = this.kuangxiang_E.sampleDescribe.trim()
      this.kuangxiang_E.device = this.kuangxiang_E.device.trim()
      if (this.kuangxiang_E_up1.length) {
        this.kuangxiang_E.sampleImage = this.kuangxiang_E_up1
        this.kuangxiang_E_up1 = []
      }
      this.axios.put('/api/microview', this.kuangxiang_E)
        .then(res => {
          if (res.status == 200 && res.data.status == 200) {
            this.kuangxiang = this.kuangxiang_E
            this.kuangxiang.id = res.data.id
            this.kuangxiang_E = null
            this.$message.success('修改' + this.sampleId+ '矿相数据成功！')
          }
          else {
            this.$message.error('出错啦！')
          }
        })
      this.kuangxiangFlag = false
    },
    cancelkuangxiangEdit() {
      this.kuangxiang_E = null
      this.kuangxiangFlag = false
    },
    kuangxiangHandleUploadSuccess(res) {
      if (res.status == 200) {
        this.kuangxiang_E_up1 = this.kuangxiang_E_up1.concat(res.data)
      }
    },
    setdianzi() {
      if (this.dianzi) {
        this.dianzi_E = deepObjCopy(this.dianzi)
      }
      else {
        this.dianzi_E = {
          type: '电子显微照片',
          sampleImage: [],
          sampleDescribe: '',
          device: '',
          imageData: [],
          sampleId: this.sampleId
        }
      }
      this.dianziFlag = true
    },
    submitdianziEdit() {
      this.dianzi_E.sampleDescribe = this.dianzi_E.sampleDescribe.trim()
      this.dianzi_E.device = this.dianzi_E.device.trim()
      if (this.dianzi_E_up1.length) {
        this.dianzi_E.sampleImage = this.dianzi_E_up1
        this.dianzi_E_up1 = []
      }
      this.axios.put('/api/microview', this.dianzi_E)
        .then(res => {
          if (res.status == 200 && res.data.status == 200) {
            this.dianzi = this.dianzi_E
            this.dianzi.id = res.data.id
            this.dianzi_E = null
            this.$message.success('修改' + this.sampleId+ '电子显微照片数据成功！')
          }
          else {
            this.$message.error('出错啦！')
          }
        })
      this.dianziFlag = false
    },
    canceldianziEdit() {
      this.dianzi_E = null
      this.dianziFlag = false
    },
    dianziHandleUploadSuccess(res) {
      if (res.status == 200) {
        this.dianzi_E_up1 = this.dianzi_E_up1.concat(res.data)
      }
    },
    jinxiangItemAdd() {
      if (this.jinxiangFlag) {
        this.$message.warning('您正在编辑金相基本信息，请优先完成')
        return
      }
      this.jinxiangItem_E = {
        zoom: '',
        photoMode: '',
        image: '',
        describe: '',
        microId: this.jinxiang.id
      }
      this.jinxiang.imageData.push({
        temp: true,
        zoom: '',
        photoMode: '',
        image: '',
        describe: ''
      })
      this.jinxiangItemFlag = true
    },
    jinxiangItemHandleUploadSuccess(res) {
      if (res.status == 200) {
        this.jinxiangItem_E.image = res.data[0]
      }
    },
    submitjinxiangItemEdit() {
      this.jinxiangItem_E.zoom = Number(this.jinxiangItem_E.zoom)
      this.axios.post('/api/microview/' + this.jinxiang.id, this.jinxiangItem_E)
        .then(res => {
          if (res.status == 200 && res.data.status == 200) {
            this.jinxiangItem_E.id = res.data.id
            this.jinxiang.imageData.push(this.jinxiangItem_E)
            this.jinxiangItem_E = null
            this.$message.success('增加' + this.sampleId+ '金相数据成功！')
          }
          else {
            this.$message.error('出错啦！')
          }
        })
      this.jinxiang.imageData = this.jinxiang.imageData.filter(v=>!v.temp)
      this.jinxiangItemFlag = false
    },
    canceljinxiangItemEdit() {
      this.jinxiangItem_E = null
      this.jinxiang.imageData = this.jinxiang.imageData.filter(v=>!v.temp)
      this.jinxiangItemFlag = false
    },
    kuangxiangItemAdd() {
      if (this.kuangxiangFlag) {
        this.$message.warning('您正在编辑矿相基本信息，请优先完成')
        return
      }
      this.kuangxiangItem_E = {
        zoom: '',
        photoMode: '',
        image: '',
        describe: '',
        microId: this.kuangxiang.id
      }
      this.kuangxiang.imageData.push({
        temp: true,
        zoom: '',
        photoMode: '',
        image: '',
        describe: ''
      })
      this.kuangxiangItemFlag = true
    },
    kuangxiangItemHandleUploadSuccess(res) {
      if (res.status == 200) {
        this.kuangxiangItem_E.image = res.data[0]
      }
    },
    submitkuangxiangItemEdit() {
      this.kuangxiangItem_E.zoom = Number(this.kuangxiangItem_E.zoom)
      this.axios.post('/api/microview/' + this.kuangxiang.id, this.kuangxiangItem_E)
        .then(res => {
          if (res.status == 200 && res.data.status == 200) {
            this.kuangxiangItem_E.id = res.data.id
            this.kuangxiang.imageData.push(this.kuangxiangItem_E)
            this.kuangxiangItem_E = null
            this.$message.success('增加' + this.sampleId+ '矿相数据成功！')
          }
          else {
            this.$message.error('出错啦！')
          }
        })
      this.kuangxiang.imageData = this.kuangxiang.imageData.filter(v=>!v.temp)
      this.kuangxiangItemFlag = false
    },
    cancelkuangxiangItemEdit() {
      this.kuangxiangItem_E = null
      this.kuangxiang.imageData = this.kuangxiang.imageData.filter(v=>!v.temp)
      this.kuangxiangItemFlag = false
    },
    dianziItemAdd() {
      if (this.dianziFlag) {
        this.$message.warning('您正在编辑电子显微照片基本信息，请优先完成')
        return
      }
      this.dianziItem_E = {
        zoom: '',
        photoMode: '',
        image: '',
        describe: '',
        microId: this.dianzi.id
      }
      this.dianzi.imageData.push({
        temp: true,
        zoom: '',
        photoMode: '',
        image: '',
        describe: ''
      })
      this.dianziItemFlag = true
    },
    dianziItemHandleUploadSuccess(res) {
      if (res.status == 200) {
        this.dianziItem_E.image = res.data[0]
      }
    },
    submitdianziItemEdit() {
      this.dianziItem_E.zoom = Number(this.dianziItem_E.zoom)
      this.axios.post('/api/microview/' + this.dianzi.id, this.dianziItem_E)
        .then(res => {
          if (res.status == 200 && res.data.status == 200) {
            this.dianziItem_E.id = res.data.id
            this.dianzi.imageData.push(this.dianziItem_E)
            this.dianziItem_E = null
            this.$message.success('增加' + this.sampleId+ '电子显微照片数据成功！')
          }
          else {
            this.$message.error('出错啦！')
          }
        })
      this.dianzi.imageData = this.dianzi.imageData.filter(v=>!v.temp)
      this.dianziItemFlag = false
    },
    canceldianziItemEdit() {
      this.dianziItem_E = null
      this.dianzi.imageData = this.dianzi.imageData.filter(v=>!v.temp)
      this.dianziItemFlag = false
    },
    zoomInputValid(key) {
      this[key].zoom = this[key].zoom.trim()
      var point_flag = false
      for (let i = 0; i < this[key].zoom.length; ++ i) {
        if (this[key].zoom[i] == '.' && !point_flag) {
          point_flag = true
        }
        else if (this[key].zoom[i] < '0' || this[key].zoom[i] > '9') {
          this[key].zoom = this[key].zoom.substring(0, i)
          break
        }
      }
    },
    findItem(id) {
      let res = null
      let temp = []
      if (this.jinxiang) {
        temp = temp.concat(this.jinxiang.imageData)
      }
      if (this.kuangxiang) {
        temp = temp.concat(this.kuangxiang.imageData)
      }
      if (this.dianzi) {
        temp = temp.concat(this.dianzi.imageData)
      }
      for (let i = 0; i < temp.length; ++ i) {
        if (temp[i].id == id) {
          res = temp[i]
          break
        }
      }
      return res
    },
    removeItem(id) {
      if (this.jinxiang) {
        this.jinxiang.imageData = this.jinxiang.imageData.filter(v => v.id != id)
      }
      if (this.kuangxiang) {
        this.kuangxiang.imageData = this.kuangxiang.imageData.filter(v => v.id != id)
      }
      if (this.dianzi) {
        this.dianzi.imageData = this.dianzi.imageData.filter(v => v.id != id)
      }
    },
    setItem(item) {
      let flag = true
      if (this.jinxiang) {
        this.jinxiang.imageData.forEach((v, i) => {
          if (flag && v.id == item.id) {
            this.$set(this.jinxiang.imageData, i, item)
            flag = false
          }
        })
      }
      if (this.kuangxiang && flag) {
        this.kuangxiang.imageData.forEach((v, i) => {
          if (flag && v.id == item.id) {
            this.$set(this.kuangxiang.imageData, i, item)
            flag = false
          }
        })
      }
      if (this.dianzi && flag) {
        this.dianzi.imageData.forEach((v, i) => {
          if (flag && v.id == item.id) {
            this.$set(this.dianzi.imageData, i, item)
            flag = false
          }
        })
      }
    },
    editItem(id) {
      if (this.nowEditItem) {
        this.$message.warning('请优先完成正在编辑的条目。')
        return
      }
      this.nowEditItem = deepObjCopy(this.findItem(id))
      this.$set(this.editItemModel, id, true)
    },
    cancelItemEdit(id) {
      this.nowEditItem = null
      this.editItemModel[id] = false
    },
    deleteItem(id) {
      this.axios.delete('/api/microview/' + id)
        .then(res => {
          if (res.status == 200 && res.data.status == 200) {
            this.deleteDialogVisible[id] = false
            this.removeItem(id)
            this.$message.success('删除成功！')
          }
          else {
            this.$message.error('出错啦！')
          }
        })
    },
    submitItemEdit(id) {
      this.nowEditItem.zoom = Number(this.nowEditItem.zoom)
      this.axios.put('/api/microview/' + id, this.nowEditItem)
        .then(res => {
          if (res.status == 200 && res.data.status == 200) {
            this.setItem(this.nowEditItem)
            this.nowEditItem = null
            this.editItemModel[id] = false
            this.$message.success('修改成功！')
          }
          else {
            this.$message.error('出错啦！')
          }
        })
    },
    itemHandleUploadSuccess(res) {
      if (res.status == 200) {
        this.nowEditItem.image = res.data[0]
      }
    }
  }
}
</script>
