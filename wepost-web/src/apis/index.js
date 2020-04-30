
import axios from '@/config/axios/axios'


function BackendLookup(method,endpoint,data){
  let JsonData;
  if(data){
    JsonData = JSON.stringify(data)
  }
  const token = localStorage.getItem('logintoken')
  axios({
    method:method,
    url:'${endpoint}',
    headers:{
      Authentication:'token '+ token,
      "Content-Type": "application/json"
    }
  })
}
