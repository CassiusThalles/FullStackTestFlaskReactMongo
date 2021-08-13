import React from "react";
import { Card, Container, Button, Modal } from 'react-bootstrap';
import axios from 'axios';
import { useState } from "react";

export default class Home extends React.Component {
    state = {
        news: []
    }

    componentDidMount() {
        axios.get('http://localhost:8000/news')
            .then(res => {
                const news = res.data;
                this.setState({ news });
            })
    }

    render() {
        return (
            <Container>
                {
                    this.state.news.map((value, index) => {
                        return (
                            <Card key={index}>
                                <Card.Body style={{display:'flex', flexDirection:'row', justifyContent:'space-between'}}>
                                    <div>
                                    <Card.Title>{value.title}</Card.Title>
                                    <Card.Text>{value.content}</Card.Text>
                                    </div>
                                    <div>
                                    <Button variant="primary" style={{margin:'5px'}}>Atualizar</Button>
                                    <Button variant="danger" style={{margin:'5px'}}>Deletar</Button>
                                    </div>
                                </Card.Body>
                            </Card>
                        )
                    })
                }
            </Container>
        )
    }
}