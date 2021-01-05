const PlaylistLib = () => {
    const [playlists, setPlaylists] = useState([]);

    const getPlaylists = () => {
        fetch('/playlists')
        .then(res => res.json())
        .then(data => {
            console.log(data);
            console.log(data.items);
            setPlaylists(data.items);    
        });
    }

    useEffect(() => {
        getPlaylists();
    }, [])

    return(
        <div>
            <h1>Playlists</h1>
            { playlists.map((playlist, i) => {
                return(
                    <Playlist key={i} playlist={playlist}/>
                )
            })}
        </div>
    )
}