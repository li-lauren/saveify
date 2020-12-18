const PlaylistLib = () => {
    const [playlists, setPlaylists] = useState(null)
    
    const getPlaylists = () => {
        fetch('/playlists')
        .then(res => res.json())
        .then(data => console.log(data))
    }

    return(
        <div>
            Playlists
        </div>
    )
}