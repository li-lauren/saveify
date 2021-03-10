const SavedPlaylist = ({playlist}) => {
    const [tracks, setTracks] = useState([]);
    const [showTracks, setShowTracks] = useState(false);
   
    const getTracks = () => {
        setShowTracks(!showTracks)
        if (showTracks) {
            fetch(`/tracks/${playlist.id}`)
            .then(res => res.json())
            .then(data => {
                console.log(data.items);
                setTracks(data.items);
            });
        };
    };

    return (
        <div className="saved-playlist-cont">
            <img 
                src={playlist.images[0].url} 
                alt={playlist.name} 
                className="pl-cover"
            />
            <span onClick={getTracks}>
                {playlist.name}
            </span>  
            {showTracks ? 
                tracks.map((track, i) => <p key={i}>{track.track.name}</p>) 
                : ''
            }
        </div>
    )
}