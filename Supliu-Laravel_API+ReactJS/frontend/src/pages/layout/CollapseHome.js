import { useEffect, useState } from 'react';
import axios from 'axios';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Accordion from 'react-bootstrap/Accordion';
import TableHome from './TableHome';



function CollapseHome() {


    const [albums, setAlbums] = useState([]);

    const getAlbums = async() => {

        try{

            const response = await axios.get("http://127.0.0.1:8000/api/albums");
            setAlbums(response.data.data);

        }catch (e){

            console.log(e);

        }

    }

    useEffect(() => {

        getAlbums();

    },[])
    

    return (

    <Container>
        <Row>
            <Accordion>

                {albums.length === 0 ? <p>Carregando os álbuns...</p> : (
                    albums.map((album) => (
                        <Accordion.Item eventKey={album.id}>
                            <Accordion.Header>Disco: {album.name}</Accordion.Header>
                            <Accordion.Body>
                                <TableHome album={album.id} key={album.id} />
                            </Accordion.Body>
                        </Accordion.Item>
                    ))
                )}

            </Accordion>
        </Row>
    </Container>

    );

}

export default CollapseHome;