<template>
  <div id="PassView" class="text-center">
    <form class="form-signin" ref="form" v-on:submit.prevent="handleSubmit">
      <img class="mb-4" :src="require('@/assets/logo.png')" alt="" width="72" height="72">
      <h1 class="h3 mb-3 font-weight-normal">更改密码</h1>
      <label for="inputUsername" class="sr-only">用户名</label>
      <input v-model="username" type="text" id="inputUsername" class="form-control" placeholder="用户名" disabled>
      <label for="inputPassword" class="sr-only">原密码</label>
      <input v-model="passwd" type="password" id="inputPassword" class="form-control" placeholder="原密码" required autofocus style="margin-bottom: 10px;">
      <label for="inputNPassword" class="sr-only">新密码</label>
      <input v-model="npasswd" type="password" id="inputNPassword" class="form-control" placeholder="新密码" required>
      <label for="inputNPassword2" class="sr-only">再次输入</label>
      <input v-model="npasswd2" type="password" id="inputNPassword2" class="form-control" placeholder="再次输入新密码" required>
      <button class="btn btn-lg btn-primary btn-block" type="submit">修 改</button>
      <p class="mt-5 mb-3 text-muted">&copy; 2022-2023</p>
    </form>
  </div>
</template>

<style src="@/assets/bootstrap.min.css" scoped></style>
<style scoped>
.bd-placeholder-img {
  font-size: 1.125rem;
  text-anchor: middle;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

@media (min-width: 768px) {
  .bd-placeholder-img-lg {
    font-size: 3.5rem;
  }
}

#PassView {
  height: 100%;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  background-color: #f5f5f5;
}

.form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: auto;
}
.form-signin .checkbox {
  font-weight: 400;
}
.form-signin .form-control {
  position: relative;
  box-sizing: border-box;
  height: auto;
  padding: 10px;
  font-size: 16px;
}
.form-signin .form-control:focus {
  z-index: 2;
}
.form-signin input {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

button {
  margin-top: 12px;
}
</style>

<script>
export default {
  name: 'PassView',
  data() {
    return {
      token: '',
      username: '',
      passwd: '',
      npasswd: '',
      npasswd2: ''
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
    if (this.$cookies.isKey('username')) {
      this.username = this.$cookies.get('username')
    }
  },
  methods: {
    handleSubmit() {
      this.doChange()
      return false
    },
    resetFields() {
      // this.username = ''
      this.passwd = ''
      this.npasswd = ''
      this.npasswd2 = ''
    },
    doChange() {
      if (this.username && this.passwd && this.npasswd) {
        if (this.npasswd != this.npasswd2) {
          this.$message.error('两次密码不一致，请重新输入')
        }
        else {
          this.axios.put('/api/passwd', {
            username: this.username,
            passwd: this.passwd,
            npasswd: this.npasswd
          }, {
            params: {
              token: this.token
            }
          })
            .then(res => {
              if (res.status == 200 && res.data.status == 200) {
                this.$message.success('修改成功！')
                this.$router.replace({
                  name: 'SignView'
                })
              }
              else {
                this.$message.error('修改失败！')
                this.resetFields()
              }
            })
            .catch(() => {
              this.$message.error('出错啦！')
              this.resetFields()
            })
        }
      }
    }
  }
}
</script>
