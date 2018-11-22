import React from 'react';
import axios from 'axios';
import { observable } from 'mobx';


class PostService {
    @observable posts = [];
    @observable page_info = { page: 1, size: 20, count: 0, pages: 0 }
    @observable post = {};

    list(page = 1, size = 20) {
        axios.get(
            '/api/post/' + "?page=" + page + "&size=" + size
        )
            .then(response => {
                this.posts = response.data.posts;
                this.page_infos = response.data.page_infos;
            })
            .catch(error => {
                console.log(error);
                this.errMsg = "异常"
            });
    };

    get(psot_id) {
        axios.get(
            '/api/post/' + psot_id
            )
            .then(response => {
                this.post = response.data.post;
                this.page_infos = response.data.page_infos;
            })
            .catch(error => {
                console.log(error);
                this.errMsg = "异常"
            });
    }
};

const postSerivce = new PostService()
export default postSerivce


 /**
 * jsonify(post={
            'post_id':post.id,
            'title':post.title,
            'author':post.author.name,
            'postdate':post.postdate.timestamp(),
            'content':post.content.content,
            'hits':post.hits
        },diginfo=diginfo,buryinfo=buryinfo,tags=tags)
 */