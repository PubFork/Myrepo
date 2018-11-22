import React from 'react';
import {Link,Redirect} from 'react-router-dom'
import '../css/login.css'
import userService from '../service/user'
import inject from '../inject'
import {observer} from 'mobx-react'

const service = userService;


@inject({service})
@observer
export default class Reg extends React.Component {

    handlerClick(event){
        event.preventDefault();
        let fm = event.target.form;
        console.log(fm[0].value,fm[1].value,fm[2].value)
        this.props.service.reg(fm[0].value,fm[1].value,fm[2].value)
    }
    render() {
        if (this.props.service.succeed) {
            return <Redirect to="/" />
        };
        return (
        <div className="login-page">
            <div className="form">
                <form className="register-form">
                    <input type="text" placeholder="昵称" />
                    <input type="email address" placeholder="邮箱地址" />
                    <input type="password1" placeholder="密码" />
                    <input type="password2" placeholder="确认密码" />
                    <button onClick={this.handlerClick.bind(this)}>申请注册</button>
                    <p className="message">Already registered? <Link to="/login">登录</Link></p>
                </form>
            </div>
        </div>
        );
    }
}