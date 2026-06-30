<script>
import { PiRogueSectionBase } from 'pirogue-admin-vue';
import { Button } from 'primevue';
export default {
  extends: PiRogueSectionBase,
  components: { Button },
  created() {
    this.$logger(this, 'Logout');
    this.$debug('Created');
  },
  mounted() {
    this.$debug('My parent is', this.$parent, this.$root);
  },
  methods: {
    async proceed_logout() {
      this.$root.logout();
    },
  },
}
</script>
<template>
  <p>To logout from <strong>PiRogue Admin Web</strong>, you can safely close this webpage or click the following button.</p>
  <Button @click="proceed_logout" label="Confirm logout" severity="warn" size="small" />
</template>