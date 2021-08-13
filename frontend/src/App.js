import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import React from "react";
import { Container, Nav, Navbar } from "react-bootstrap";

import Home from "./pages/Home/Home";
import Create from "./pages/Create/Create";
import Update from "./pages/Update/Update";

function App() {
  return (
    <Router>
      <div >
        <Navbar bg="light">
          <Container>
            <Nav className="me-auto">
              <Nav.Link><Link to="/">Home</Link></Nav.Link>
              <Nav.Link><Link to="/create">Create</Link></Nav.Link>
            </Nav>
          </Container>
        </Navbar>
      </div>
      <Switch>
        <Route path="/create">
          <Create />
        </Route>
        <Route path="/">
          <Home />
        </Route>
      </Switch>
    </Router>
  );
}


function Users() {
  return <h2>Users</h2>
}

export default App;
