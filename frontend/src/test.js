import React from 'react';
import axios from 'axios';

export default class Teste extends React.Component {
    state = {
        news: []
    }

    componentDidMount() {
        axios('http://localhost:8000/news')
        .then(response => {
            const result = response.data;
            this.setState({news: result});
        })
    }

    render() {
        return(
            <div>
                { JSON.stringify(this.state.news) }
            </div>
        )
    }
}