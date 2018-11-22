import React from 'react';
import axios from 'axios'
import store from 'store'
import {observable} from 'mobx'


class UserService {
    @observable succeed = false

    login(email, pwd) {
        console.log(email, pwd)
        axios.post('/api/user/login', {
            email: email,
            password: pwd 
        }).then( response=> {
            console.log(response);
            store.set('token',response.data.token,(new Date()).getTime()+8*3600*1000);
            this.succeed = true;

        }).catch(error=>{
                console.log(error);
        });
    }

    reg(name,email,pwd) {
        axios.post('/api/user/reg', {
            name: name,
            email: email,
            password: pwd
        }).then(response=>{
                console.log(response.data);
                store.set('token',response.data.token,(new Date()).getTime()+8*3600*1000);
                this.succeed = true;

        }).catch(error=>{
                console.log(error);
        });
    }
}
const userSerivce = new UserService()
export default userSerivce