<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\Api\ApiController;
use App\Http\Controllers\Api\AlbumController;
use App\Http\Controllers\Api\TrackController;



Route::post('register', [ApiController::class, 'register']);
Route::post('login', [ApiController::class, 'login']);

Route::get('albums', [AlbumController::class, 'albums']);
Route::post('albums', [AlbumController::class, 'search']);
Route::get('album/{id}', [AlbumController::class, 'show']);

Route::get('tracks', [TrackController::class, 'tracks']);
Route::post('tracks', [TrackController::class, 'search']);
Route::get('track/album/{id}', [TrackController::class, 'searchTrackByAlbum']);
Route::get('track/{id}', [TrackController::class, 'show']);


Route::group([
    'middleware' => ['auth:sanctum']
], function(){

    Route::get('profile', [ApiController::class, 'profile']);
    Route::get('logout', [ApiController::class, 'logout']);

    Route::post('album', [AlbumController::class, 'register']);
    Route::put('album/{id}', [AlbumController::class, 'update']);
    Route::delete('album/{id}', [AlbumController::class, 'delete']);

    Route::post('track', [TrackController::class, 'register']);
    Route::put('track/{id}', [TrackController::class, 'update']);
    Route::delete('track/{id}', [TrackController::class, 'delete']);

});