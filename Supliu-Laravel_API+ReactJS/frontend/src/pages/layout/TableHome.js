import { useEffect, useState } from 'react';
import React from 'react'
import axios from 'axios';
import Table from 'react-bootstrap/Table';
import './components/table/TableHome.css'



function TableHome(props) {


    const [tracks, setTracks] = useState([]);

    const getTracks = async(props) => {

        try{

            const response = await axios.get({
                toString: function() {
                    // return 'http://127.0.0.1:8000/api/track/album/5'; // Assim funciona
                    // return 'http://127.0.0.1:8000/api/track/album/'+props.album; // Não funciona com a variável props
                    return `http://127.0.0.1:8000/api/track/album/${props.album}`; // Não funciona com a variável props
                    }
                });
            setTracks(response.data);


        }catch (e){

            console.log(e);

        }

    }

    useEffect((props) => {

        getTracks(props);

    },[])
    

    return (

        <div>
            <Table responsive="lg">
                <thead>
                    <tr>
                        <th>#</th>
                        <th className="p-2 ms-auto">Nome da Faixa</th>
                        <th>Duração</th>
                    </tr>
                </thead>
                <tbody>
                {tracks.length === 0 ? 
                    <tr>
                        <td colSpan="3">Carregando os álbuns...</td>
                    </tr>
                : (
                    tracks.data.map((track) => (
                    <tr key={track.id}>
                        <td># { track.track }</td>
                        <td className="p-2 ms-auto">{ track.name }</td>
                        <td>{ track.duration }</td>
                    </tr>
                    ))
                )}
                </tbody>
            </Table>
        </div>

    );

}

export default TableHome;