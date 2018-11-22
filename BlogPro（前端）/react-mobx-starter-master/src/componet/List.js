import React from 'react';
import { Link } from 'react-router-dom'

import postService from '../service/post'
import inject from '../inject'
import { observer } from 'mobx-react'

import { List, message } from 'antd';
import 'antd/lib/list/style';
import 'antd/lib/message/style'
import '../css/login.css'


const service = postService;


@inject({ service })
@observer
export default class Lists extends React.Component {
    constructor(props) {
        super(props);
        let parmas = new URLSearchParams(this.props.location.search)
        this.props.service.list(parmas.get('page'), parmas.get('size'))
    }

    render() {
        const data = this.props.service.posts;
        console.log(data.length)
        return (
            <div>
                <List
                    bordered
                    dataSource={data}
                    renderItem={item => (
                        <List.Item>
                            <List.Item.Meta
                                title={<Link to={'/post/' + item.post_id}>{item.title}</Link>}
                            />
                        </List.Item>)}
                />
            </div>
        )
    };
}

