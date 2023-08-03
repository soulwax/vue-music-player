import axios from 'axios'

const api = axios.create({
  baseURL: 'https://api.echoelysium.tech/api'
})

export default api
