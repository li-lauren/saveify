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

    const regPlaylistComps = regPlaylists.map((playlist, i) =>
        <Playlist key={i} playlist={playlist} />)

    const savedPlaylistComps = savedPlaylists.map((playlist, i) => 
        <SavedPlaylist key={i} playlist={playlist}/>)

    return(
        <div className="container">
            <h1>Spotify Playlists</h1>
            <div id="spotify-pl-cont">
                <PlaylistCarousel playlists={regPlaylistComps} n={4} />
            </div>

            <h1>Saveify Playlists</h1>
            <div id="saveify-pl-cont">
                <PlaylistCarousel playlists={savedPlaylistComps} n={4} />
            </div>
        </div>
    )
}