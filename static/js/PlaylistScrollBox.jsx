const PlaylistScrollBox = ({playlists}) => {
    const [tracks, setTracks] = useState([]);
    const [selectedPL, setSelectedPL] = useState(null);

    const getTracks = () => {
        fetch(`/tracks/${selectedPL}`)
        .then(res => res.json())
        .then(data => {
            console.log(data.items);
            setTracks(data.items);
        });
    }; 

    useEffect(() => {
        if (selectedPL) {
            getTracks()
        } else {
            setSelectedPL(playlists[0].id)
        }
    }, [selectedPL, playlists])

    return(
        <div className="saved-section">
            <div className="tracks-container">
                {
                    tracks.map((track, i) => <p key={i}>{track.track.name}</p>) 
                }
            </div>
            <div className="f scroll-box">
           
                {playlists.map((playlist, i) => 
                    <SavedPlaylist 
                        key={i} 
                        playlist={playlist}
                        setSelectedPL={setSelectedPL}
                    />
                )}
                
            </div>

        </div>
        
    )
}