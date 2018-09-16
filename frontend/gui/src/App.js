import React, { Component } from 'react';
import './App.css';
import 'antd/dist/antd.css';

import CustomLayout from './containers/Layout';
import ArticleList from './containers/ArticleListView';

class App extends Component {
  render() {
    return (
      <div className="App">
        <CustomLayout>
          <ArticleList/> 
        </CustomLayout>
      </div>
    );
  }
}

export default App;
