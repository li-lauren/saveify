const Playlist = ({playlist}) => {
    const [tracks, setTracks] = useState([]);
    const [showTracks, setShowTracks] = useState(false);
    const [showForm, setShowForm] = useState(false);
    
    const getTracks = () => {
        setShowTracks(!showTracks)
        if (showTracks) {
            fetch(`/tracks/${playlist.id}`)
            .then(res => res.json())
            .then(data => {
                console.log(data.items);
                setTracks(data.items);
            });
        }
    }; 

    return(
        <div className="playlist-cont">
            <button 
                type="button" 
                className="save-btn btn btn-light btn-sm" 
                onClick={() => setShowForm(true)}
            >
                +
            </button>
            
            {
                playlist.images.length > 0 ? 
                <img 
                    src={playlist.images[0].url} 
                    alt={playlist.name} 
                    className="pl-cover"
                /> : 
                <img
                    src={"static/imgs/playlist_cover2.png"}
                    alt={playlist.name}
                    className="pl-cover-custom"
                />
            }
            <SavePlaylistForm 
                showForm={showForm}
                setShowForm={setShowForm}
                playlistID={playlist.id} 
            />
            <span onClick={getTracks}>{playlist.name}</span>  
            {showTracks ? tracks.map((track, i) => <p key={i}>{track.track.name}</p>) : ''}
            
        </div>
    )
}