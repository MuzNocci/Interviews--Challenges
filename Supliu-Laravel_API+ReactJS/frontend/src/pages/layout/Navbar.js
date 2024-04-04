import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import NavbarReact from 'react-bootstrap/Navbar';



function Navbar(){


    return (

        <NavbarReact collapseOnSelect expand="lg" className="bg-body-tertiary">
            <Container>
                <NavbarReact.Brand href="/">Tião Carreiro e Pardinho</NavbarReact.Brand>
                <NavbarReact.Toggle aria-controls="responsive-navbarReact-nav" />
                <NavbarReact.Collapse id="responsive-navbarReact-nav">
                    <Nav className="me-auto">
                    </Nav>
                    <Nav>
                        <Nav.Link href="/">Home</Nav.Link>
                        <Nav.Link eventKey={2} href="/login">Login</Nav.Link>
                    </Nav>
                </NavbarReact.Collapse>
            </Container>
        </NavbarReact>

    );

}

export default Navbar;