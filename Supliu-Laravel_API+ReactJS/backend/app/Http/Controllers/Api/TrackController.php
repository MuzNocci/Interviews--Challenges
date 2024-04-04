<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Models\Album;
use App\Models\Track;



class TrackController extends Controller
{

    
    public function tracks(Request $request){


        $tracks = Track::orderByDESC('album_id')->orderby('track')->get();


        return Response()->json([
            'status' => true,
            'message' => 'Tracks listed successfully',
            'data' => $tracks,
        ], 200);


    }


    public function search(Request $request){


        $tracks = Track::where('name', 'like', '%'.$request->search.'%')->orderByDESC('album_id')->orderby('track')->get();

        if (count($tracks) > 0){


            return Response()->json([
                'status' => true,
                'message' => 'Tracks searched successfully',
                'data' => $tracks,
            ], 200);

        }


        return Response()->json([
            'status' => false,
            'message' => 'Track not found',
            'data' => [],
        ], 204);


    }


    public function searchTrackByAlbum(Request $request, $id){


        $tracks = Track::where('album_id', $id)->orderby('track')->get();

        if (count($tracks) > 0){


            return Response()->json([
                'status' => true,
                'message' => 'Tracks searched successfully',
                'data' => $tracks,
            ], 200);

        }


        return Response()->json([
            'status' => false,
            'message' => 'Track not found',
            'data' => [],
        ], 204);


    }


    public function register(Request $request){


        $request->validate([
            'album' => 'required|integer',
            'track' => 'required|integer|max:4',
            'name' => 'required|string|min:2|max:50',
            'duration' => 'required',
        ]);

        if (!empty(Album::find($request->album))){

            Track::create([
                'album_id' => $request->album,
                'track' => $request->track,
                'name' => $request->name,
                'duration' => $request->duration,
            ]);


            return Response()->json([
                'status' => true,
                'message' => 'Track registered successfully',
                'data' => [],
            ], 201);

        }else{


            return Response()->json([
                'status' => false,
                'message' => 'Album does not exist',
                'data' => [],
            ], 422);


        }


    }


    public function show(Request $request, $id){


        $track = Track::find($id);

        if (!empty($track)){


            return Response()->json([
                'status' => true,
                'message' => 'Track show successfully',
                'data' => $track,
            ], 200);

        }


        return Response()->json([
            'status' => false,
            'message' => 'Track not found',
            'data' => [],
        ], 204);


    }


    public function update(Request $request, $id){


        $request->validate([
            'album_id' => 'required|integer',
            'track' => 'required|integer|max:4',
            'name' => 'required|string|min:2|max:50',
            'duration' => 'required',
        ]);

        $track = Track::find($id);

        if (!empty($track)){

            $track->update($request->all());


            return Response()->json([
                'status' => true,
                'message' => 'Track updated successfully',
                'data' => [],
            ], 200);

        }


        return Response()->json([
            'status' => false,
            'message' => 'Track not found',
            'data' => [],
        ], 204);


    }


    public function delete(Request $request, $id){


        $track = Track::find($id);
        
        if (!empty($track)){

            $track->delete();


            return Response()->json([
                'status' => true,
                'message' => 'Track deleted successfully',
                'data' => [],
            ], 200);

        }


        return Response()->json([
            'status' => false,
            'message' => 'Track not found',
            'data' => [],
        ], 204);

    }


}
