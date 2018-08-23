import Vue from 'vue'
import VeeValidate from 'vee-validate'
import ContactList from './components/ContactList.vue'
import router from './router'
import store from './store'

import './filters'

import './assets/styles.css'

Vue.config.productionTip = false
Vue.use(VeeValidate)

new Vue({
  router,
  store,
  render: h => h(ContactList)
}).$mount('#app')
