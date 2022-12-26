<template>
  <div id="SignView" class="text-center">
    <form class="form-signin" ref="form" v-on:submit.prevent="handleSubmit">
      <img class="mb-4" :src="require('@/assets/logo.png')" alt="" width="72" height="72">
      <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
      <label for="inputUsername" class="sr-only">Username</label>
      <input v-model="username" type="text" id="inputUsername" name="username" class="form-control" placeholder="用户名" required autofocus>
      <label for="inputPassword" class="sr-only">Password</label>
      <input v-model="passwd" type="password" id="inputPassword" name="password" class="form-control" placeholder="密码" required>
      <div class="checkbox mb-3">
        <label>
          <input v-model="remember" type="checkbox"> Remember me
        </label>
      </div>
      <button class="btn btn-lg btn-primary btn-block" type="submit">登 录</button>
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

#SignView {
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
.form-signin input[type="text"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
</style>

<script>
export default {
  name: 'SignView',
  data() {
    return {
      username: '',
      passwd: '',
      remember: true,
      token: ''
    }
  },
  methods: {
    handleSubmit() {
      this.doLogin()
      return false
    },
    resetFields() {
      this.username = ''
      this.passwd = ''
    },
    doLogin() {
      if (this.username && this.passwd) {
        this.axios.post('/api/login', {
          username: this.username,
          passwd: this.passwd
        })
          .then(res => {
            if (res.status == 200) {
              this.token = res.data.token
              this.$message.success('登录成功!')
              this.$cookies.set('username', this.username)
              this.$parent.$data.username = this.username
              // 记住登录状态
              if (this.remember) {
                this.$cookies.set('token', this.token)
                this.$router.replace({
                  name: 'HomeView'
                })
              }
              // 不记住
              else {
                this.$router.replace({
                  name: 'HomeView',
                  query: {
                    token: this.token
                  }
                })
              }
            }
            else {
              this.$message.error(res.data.msg)
              this.resetFields()
            }
          })
          .catch(err => {
            this.$message.error(err.response.data.msg)
            this.resetFields()
          })
      }
    }
  }
}
</script>
