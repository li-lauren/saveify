const Playlist = ({playlist}) => {
    const [tracks, setTracks] = useState([]);

    const getTracks = () => {
        fetch(`/tracks/${playlist.id}`)
        .then(res => res.json())
        .then(data => {
            console.log(data.items)
            setTracks(data.items)
        })
    }
    return(
        <div>
            <span onClick={getTracks}>{playlist.name}</span>  
            {tracks.map((track, i) => <p key={i}>{track.track.name}</p>)}
        </div>
    )
}