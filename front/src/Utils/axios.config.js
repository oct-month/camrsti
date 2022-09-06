import axios from "axios";

// const remote = 'http://1.13.21.160:5001/'
const urlPrefix = 'http://localhost:5000/'

export const httpGet = axios.create({
  baseURL: urlPrefix,
  timeout: 3000
});

export const httpPost = axios.create({
  method: 'POST',
  baseURL: urlPrefix,
  timeout: 3000
})

export const httpImg = urlPrefix