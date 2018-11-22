import React from 'react';
import { Link, Redirect } from 'react-router-dom'
import '../css/login.css'
import userService from '../service/user'
import { observer } from 'mobx-react'
import inject from '../inject'

const service = userService;


@inject({service})
@observer
export default class Login extends React.Component{
    handlerClick(event) {
        event.preventDefault();
        let fm = event.target.form;
        this.props.service.login(fm[0].value, fm[1].value)
    }

    render() {
        if (this.props.service.succeed) {
            return <Redirect to="/" />
        };

        return (
            <div className="login-page">
                <div className="form">
                    <form className="login-form">
                        <input type="text" placeholder="邮箱" />
                        <input type="password" placeholder="密码" />
                        <button onClick={this.handlerClick.bind(this)}>登录</button>
                        <p className="message">Already registered? <Link to="/reg">申请注册</Link></p>
                    </form>
                </div>
            </div>
        );
    }
}