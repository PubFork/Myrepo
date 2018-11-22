import React from 'react';
import { Link, Redirect } from 'react-router-dom'
import '../css/login.css'
import postService from '../service/post'
import { observer } from 'mobx-react'
import inject from '../inject'
import { Card, message } from 'antd'
import 'antd/lib/card/style'
import 'antd/lib/message/style'

const service = postService;


@inject({ service })
@observer
export default class Post extends React.Component {
    constructor(props) {
        super(props);
        console.log(555555555, this.props.match.params)
        this.props.service.get(this.props.match.params.id)
    }
    render() {
        if (this.props.service.errMsg) {
            message.error(this.props.service.errMsg, 3, () => { this.props.service.errMsg = "" })
            return <div></div>
        }
        let post = this.props.service.post
        return (
            <div style={{ background: 'ECECEC', padding: '30px' }}>
                <Card title={this.props.service.post.title} bordered={true} style={{width:600}}>
                    <p>{post.title} {post.postdate}</p>
                    <p>{post.content}</p>
                    <p>{post.hits}</p>
                </Card>
            </div>
        );
    }
}

