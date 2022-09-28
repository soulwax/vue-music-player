import axios from "axios";

const api = axios.create({
  baseURL: "https://music.madtec.org/api"
});

export default api;
