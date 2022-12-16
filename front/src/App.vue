<template>
  <div id="app">
    <el-container v-if="flag">
      <el-header>
        <el-container direction="horizontal">
          <el-image
            style="width: 60px; height: 60px"
            :src="require('@/assets/logo.png')"
            fit="contain">
            <div slot="error" class="image-slot">
              <i class="el-icon-picture-outline"></i>
            </div>
          </el-image>
          <span>中国古代冶金耐火材料科技信息数据库</span>
          <el-dropdown id="usericon" szie="medium" @command="handleCommand">
            <el-button size="medium" plain icon="el-icon-user-solid">
              {{ username }}
              <i class="el-icon-arrow-down"></i>
            </el-button>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item command="c">修改密码</el-dropdown-item>
              <el-dropdown-item command="l">注销登录</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </el-container>
      </el-header>
      <el-container style="height: 94vh" direction="horizontal">
        <el-aside width="200px">
          <el-menu
            ref="sidemenu"
            default-active="1"
            :default-openeds="['4']"
            @select="handleMenuSelect"
            background-color="#545c64"
            text-color="#fff"
            active-text-color="#ffd04b">
            <el-menu-item index="1">
              <i class="el-icon-document"></i>
              <span slot="title">数据列表</span>
            </el-menu-item>
            <el-menu-item index="2">
              <i class="el-icon-document-add"></i>
              <span slot="title">增加数据</span>
            </el-menu-item>
            <el-menu-item index="3">
              <i class="el-icon-upload"></i>
              <span slot="title">导入数据</span>
            </el-menu-item>
            <el-submenu index="4">
              <template slot="title">
                <i class="el-icon-data-analysis"></i>
                <span>统计信息</span>
              </template>
              <el-menu-item-group>
                <template slot="title">统计</template>
                <!-- <el-menu-item index="4-1">显微组织</el-menu-item> -->
                <el-menu-item index="4-2">矿物含量+矿物测量</el-menu-item>
                <el-menu-item index="4-3">XRD+化学成分</el-menu-item>
                <el-menu-item index="4-4">物理结构+热分析</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
          </el-menu>
        </el-aside>
        <el-container>
          <el-main>
            <router-view @changeSideMenuIndex="changeSideMenuIndex"/>
          </el-main>
          <!-- <el-footer>
            Created By Ablocker © <router-link to="/about">关于</router-link>
          </el-footer> -->
        </el-container>
      </el-container>
    </el-container>
    <div v-else style="height: 100%;">
      <router-view/>
    </div>
  </div>
  <!--
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav>
    <router-view/>
   -->
</template>

<style>
#app {
  height: 100%;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#usericon {
  margin-bottom: auto;
  margin-top: auto;
  margin-left: auto;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

html,
body {
  height: 100%;
}

body {
  margin: 0px;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.el-header {
  background-color: #B3C0D1;
  color: #333;
  text-align: left;
  line-height: 60px;
}

.el-footer {
  background-color: #f7fbfd;
  color: #333;
  text-align: left;
  line-height: 60px;
}

.el-aside {
  background-color: #545c64;
  color: #333;
  text-align: left;
  line-height: 200px;
}

.el-main {
  background-color: #E9EEF3;
  color: #333;
  text-align: center;
  line-height: 25px;
  padding: 0px;
}

body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
</style>

<script>
export default {
  data() {
    return {
      index: '1',
      flag: true,
      username: ''
    }
  },
  watch: {
    index: {
      handler() {
        this.$refs.sidemenu.activeIndex = this.index
      },
      deep: true
    },
    $route(to) {
      if (to.name == 'SignView' || to.name == 'PasswdView') {
      this.flag = false
      }
      else {
        this.flag = true
      }
    }
  },
  mounted() {
    if (this.$cookies.isKey('username')) {
      this.username = this.$cookies.get('username')
    }
    switch (this.$route.name) {
      case 'HomeView':
        this.index = '1'
        break
      case 'AddView':
        this.index = '2'
        break
      case 'ImportView':
        this.index = '3'
        break
      case 'StatisticView1':
        this.index = '4-1'
        break
      case 'StatisticView2':
        this.index = '4-2'
        break
      case 'StatisticView3':
        this.index = '4-3'
        break
      case 'StatisticView4':
        this.index = '4-4'
        break
      case 'SignView':
      case 'PasswdView':
        this.flag = false
        break
    }
  },
  methods: {
    handleCommand(command) {
      switch (command) {
        case 'c':
          this.$router.replace({
            name: 'PasswdView'
          })
          break
        case 'l':
          this.$cookies.remove('token')
          this.$router.replace({
            name: 'SignView'
          })
          break
        default:
          break
      }
    },
    handleMenuSelect(key) {
      this.index = key
      switch (key) {
        case '1':
          this.$router.replace({
            name: 'HomeView'
          })
          break
        case '2':
          this.$router.replace({
            name: 'AddView'
          })
          break
        case '3':
          this.$router.replace({
            name: 'ImportView'
          })
          break
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
            name: 'StatisticView3'
          })
          break
        case '4-4':
          this.$router.replace({
            name: 'StatisticView4'
          })
          break
        default:
          break
      }
    },
    changeSideMenuIndex(key) {
      this.index = key
    }
  }
}
</script>
