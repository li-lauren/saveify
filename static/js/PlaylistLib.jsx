const PlaylistLib = () => {

    const getPlaylists = () => {
        fetch('/playlists')
        .then(res => res.json())
        .then(data => console.log(data))
    }
}