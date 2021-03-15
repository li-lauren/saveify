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

    return(
        <div className="f pl-lib-cont">
            <h1 id="pl-h-top">Your</h1>
            <h1 id="pl-h">Playlists</h1>
            <div id="spotify-pl-cont">
                <PlaylistCarousel playlists={regPlaylistComps} n={4} />
            </div>

            <h1 id="saved-h">Saved</h1> 
            {
                savedPlaylists.length > 0 ? 
                <PlaylistScrollBox playlists={savedPlaylists} /> : ''
            }    
            
        </div>
    )
}