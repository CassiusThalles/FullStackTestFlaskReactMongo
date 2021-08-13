import React from 'react';
import { useForm } from 'react-hook-form';
import { Form, Button } from 'react-bootstrap';
import axios from 'axios';

export default function Create() {
  const { register, handleSubmit, formState: { errors } } = useForm();
  const onSubmit = data => axios.post('http://localhost:8000/news', data)
                                .then(res => {
                                    console.log(res);
                                    console.log(res.data);
                                });
  console.log(errors);

  return (
      <Form style={{marginLeft:'30px', marginRight:'30px', marginTop:'15px'}} onSubmit={handleSubmit(onSubmit)}>
          <Form.Label>Título</Form.Label>
          <Form.Control type="text" placeholder="Digite aqui o Título" {...register("title", {required: true, maxLength: 199})} />
          <br/>
          <Form.Label>Conteúdo da Matéria</Form.Label>
          <Form.Control as="textarea" rows={5} {...register("content", {required: true})} />
          <br/>
          <Button variant="primary" type="submit">
              Submit
          </Button>
      </Form>
  )
}