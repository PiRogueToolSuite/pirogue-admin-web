<script>
import { Button, Dialog, Fluid, IftaLabel, Message, Password, ProgressSpinner } from 'primevue';
export default {
  components: {
    Button,
    Dialog,
    Fluid,
    IftaLabel,
    Message,
    Password,
    ProgressSpinner,
  },
  data() {
    return {
      need_login: true,
      logged_in: false,
      token: null,
      loginError: null,
    };
  },
  created() {
    this.$logger(this, 'PiRogueAdminWebApp');
    this.$debug('Created');
  },
  expose: [ 'logout' ],
  methods: {
    async login() {
      this.loginError = null;
      this.need_login = false;
      let res = await fetch('./login-with-token', {
        method: 'GET',
        headers: {
          "X-CSRFToken": this.token,
          "Content-Type": "application/json",
        },
      });
      if (!res.ok) {
        this.loginError = "Unable to login. Please try again.";
        this.reset_but_error();
        return;
      }
      let answer = await res.json();
      if (!answer.success) {
        this.loginError = "Unable to login. Please try again.";
        this.reset_but_error();
        return;
      }
      setTimeout(() => {
        this.logged_in = true;
      }, 1000);
    },
    logout() {
      this.reset();
    },
    reset() {
      this.reset_but_error();
      this.loginError = null;
    },
    reset_but_error() {
      this.token = null;
      this.logged_in = false;
      this.need_login = true;
    },
  },
  computed: {
  },
};
</script>
<template>
  <Dialog v-model:visible="need_login"
          modal :closable="false" :draggable="false" :closeOnEscape="false">
    <template #header>
      <strong>Welcome to PiRogue Admin</strong>
    </template>
    <p>In order to access the configuration page, you need to provide an access token.</p>
    <IftaLabel>
      <Password id="token" v-model="token"
                variant="filled" fluid toggleMask :feedback="false"
                :invalid="loginError"
                @keyup.enter="login"/>
      <label for="token">Token</label>
    </IftaLabel>
    <Message v-if="loginError" severity="error"
             variant="simple" size="small">{{ loginError }}</Message>
    <template #footer>
      <Button label="Login" size="small" @click="login"/>
    </template>

  </Dialog>
  <PiRogueConfigurator v-if="logged_in"
                       :dataCsrfToken="token"
                       dataEndpoint="."></PiRogueConfigurator>
  <div id="login-loading" v-else>
    <ProgressSpinner/>
  </div>
</template>
<style>
body {
  margin: 1rem;
  background-color: #EEE;
  position: relative;
}

#app
{
  min-height: calc(100vh - 2rem);
}

#login-loading
{
  position: absolute;
  display: inline-block;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

#app > .row > .col > .p-panel
{
  min-height: calc(100vh - 2rem);
}
</style>