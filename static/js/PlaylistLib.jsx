const PlaylistLib = () => {
    const [regPlaylists, setRegPlaylists] = useState([]);
    const [savedPlaylists, setSavedPlaylists] = useState([]);

    const getPlaylists = () => {
        fetch('/playlists')
        .then(res => res.json())
        .then(data => {
            console.log(data);
            
            setRegPlaylists(data.regPlaylistData);  
            setSavedPlaylists(data.savedPlaylistData);

            console.log(`SAVED PLAYLISTS ${savedPlaylists}`)
        });
    }

    useEffect(() => {
        getPlaylists();
    }, [])

    return(
        <div>
            <h1>Spotify Playlists</h1>
            { regPlaylists.map((playlist, i) => 
                <Playlist key={i} playlist={playlist}/>)}

            <h1>Saveify Playlists</h1>
            { savedPlaylists.map((playlist, i) => 
                <SavedPlaylist key={i} playlist={playlist}/>)}
        </div>
    )
}