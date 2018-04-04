import Vue from 'vue'
import axios from 'axios'
import Example from './components/Example.vue'

Vue.prototype.$http = axios

new Vue(Example).$mount('.example')