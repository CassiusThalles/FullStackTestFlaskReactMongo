import React from 'react';
import axios from 'axios';

export default class Teste extends React.Component {
    state = {
        news: []
    }

    componentDidMount() {
        axios.get('https://pokeapi.co/api/v2/pokemon/ditto')
            .then(res => {
                const news = res.data;
                this.setState({ news });
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