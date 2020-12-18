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
            Playlists
            { playlists.map((playlist, i) => {
                return(
                    <p key={i}>{playlist.name}</p>
                )
            })}
        </div>
    )
}