import 'bootstrap/dist/css/bootstrap.css';
import 'primeicons/primeicons.css';
import './assets/styles.css';
import PrimeVue from 'primevue/config';
import { createApp } from 'vue';
import App from './App.vue';
import {
  default as PirogueAdminClientVuePlugin,
  LoggerPlugin,
  DesignSystemConfig as PACVueConfig} from 'pirogue-admin-vue';
import 'pirogue-admin-vue/assets/style.scss';

import {register_section} from 'pirogue-admin-vue';
import Logout from './sections/Logout.vue';

import PiRogueAdminWebTheme from './theme-preset';

register_section({
    group: 'Administration',
    label: 'Logout',
    icon: 'pi pi-sign-out',
    component: Logout,
});

let app = createApp(App);
app.use(LoggerPlugin, {
    logLevel: 6,
});
app.use(PirogueAdminClientVuePlugin);
app.use( PACVueConfig, {
    ripple: true,
    theme: {
        preset: PiRogueAdminWebTheme,
    }
} );
app.use(PrimeVue, {
    ripple: true,
    theme: {
        preset: PiRogueAdminWebTheme,
    }
 });
app.mount('#app');