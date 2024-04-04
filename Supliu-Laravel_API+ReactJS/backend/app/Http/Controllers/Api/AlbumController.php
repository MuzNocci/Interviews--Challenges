<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Models\Album;



class AlbumController extends Controller
{
    

    public function albums(Request $request){


        $albums = Album::orderByDESC('launch')->get();


        return Response()->json([
            'status' => true,
            'message' => 'Successfully listed albums',
            'data' => $albums,
        ], 200);


    }


    public function search(Request $request){


        $albums = Album::where('name', 'like', '%'.$request->search.'%')->orderByDESC('launch')->get();

        if (count($albums) > 0){


            return Response()->json([
                'status' => true,
                'message' => 'Albums searched successfully',
                'data' => $albums,
            ], 200);

        }


        return Response()->json([
            'status' => false,
            'message' => 'Album not found',
            'data' => [],
        ], 204);


    }


    public function register(Request $request){


        $request->validate([
            'name' => 'required|string',
            'launch' => 'required|integer|min:4'
        ]);

        Album::create([
            'name' => $request->name,
            'launch' => $request->launch,
        ]);
        
        return Response()->json([
            'status' => true,
            'message' => 'Album registered successfully',
            'data' => [],
        ], 201);


    }


    public function show(Request $request, $id){


        $album = Album::find($id);

        if (!empty($album)){


            return Response()->json([
                'status' => true,
                'message' => 'Album show successfully',
                'data' => $album,
            ], 200);

        }


        return Response()->json([
            'status' => false,
            'message' => 'Album not found',
            'data' => [],
        ], 204);


    }


    public function update(Request $request, $id){


        $request->validate([
            'name' => 'string',
            'launch' => 'integer|min:4'
        ]);

        $album = Album::find($id);

        if (!empty($album)){

            $album->update($request->all());


            return Response()->json([
                'status' => true,
                'message' => 'Album updated successfully',
                'data' => [],
            ], 200);

        }


        return Response()->json([
            'status' => false,
            'message' => 'Album not found',
            'data' => [],
        ], 204);


    }


    public function delete(Request $request, $id){

        
        $album = Album::find($id);

        if (!empty($album)){

            $album->delete();


            return Response()->json([
                'status' => true,
                'message' => 'Album deleted successfully',
                'data' => [],
            ], 200);

        }


        return Response()->json([
            'status' => false,
            'message' => 'Album not found',
            'data' => [],
        ], 204);

    }


}