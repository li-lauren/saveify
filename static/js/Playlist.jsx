const Playlist = ({playlist}) => {
    const [tracks, setTracks] = useState([]);

    const getTracks = () => {
        fetch(`/tracks/${playlist.id}`)
        .then(res => res.json())
        .then(data => {
            console.log(data)
            setTracks(data)
        })
    }
    return(
        <div>
            <span onClick={getTracks}>{playlist.name}</span>  
            {tracks.map(track => <span>{}</span>)}
        </div>
    )
}