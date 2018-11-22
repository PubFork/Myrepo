import React from 'react';
import ReactDom from 'react-dom';
import 'antd/lib/menu/style';
import 'antd/lib/icon/style';
import Login from './componet/Login'
import Reg from './componet/Reg'
import Lists from './componet/List'
import Post from './componet/Post'
import { Layout, Menu, Breadcrumb, Icon } from 'antd';
import { Row, Col } from 'antd';


const { Header, Content, Footer, Sider } = Layout;
const SubMenu = Menu.SubMenu;

import {
  BrowserRouter as Router,
  Route,
  Link
} from 'react-router-dom'


const Home = () => (
  <div>
    <h2>Home</h2>
  </div>
);

const About = () => (
  <div>
    <h2>About</h2>
  </div>
);



class SiderDemo extends React.Component {
  state = {
    collapsed: false,
  };

  onCollapse = (collapsed) => {
    console.log(collapsed);
    this.setState({ collapsed });
  }

  render() {
    return (
      <Router>
        <Row>
          <Layout>
            <Col span={6} push={1}>
              <Sider
                collapsible
                collapsed={this.state.collapsed}
                onCollapse={this.onCollapse}
              >
                <div className="logo" />

                <div>
                  <Menu theme="dark" mode="inline">
                    <Menu.Item key='home'>
                      <Link to="/"><Icon type='home' />主页</Link>
                    </Menu.Item>
                    <Menu.Item key='login'>
                      <Link to="/login"><Icon type='login' />登录</Link>
                    </Menu.Item>
                    <Menu.Item key='reg'>
                      <Link to="/reg"><Icon type='reg' />注册</Link>
                    </Menu.Item>
                    <Menu.Item key='list'>
                      <Link to="/post"><Icon type='list' />文章列表</Link>
                    </Menu.Item>
                    <Menu.Item key='about'>
                      <Link to="/about"><Icon type='about' />关于</Link>
                    </Menu.Item>
                  </Menu>
                </div>

              </Sider>
            </Col>
            <Col span={18} pull={1}>
              <Layout>
                <Content>
                  <Route path="/about" component={About} />
                  <Route exact path="/" component={Home} />
                  <Route path="/login" component={Login} />
                  <Route path="/reg" component={Reg} />
                  <Route exact path="/post" component={Lists} />
                  <Route path="/post/:id" component={Post} />
                </Content>
              </Layout>
            </Col>
          </Layout>
        </Row>
      </Router>
    );
  }
}

ReactDom.render(<SiderDemo />, document.getElementById('root'))