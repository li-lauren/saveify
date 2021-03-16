const PlaylistScrollBox = ({playlists}) => {
    const [tracks, setTracks] = useState([]);
    const [selectedPL, setSelectedPL] = useState(null);

    const getTracks = () => {
        fetch(`/tracks/${selectedPL}`)
        .then(res => res.json())
        .then(data => {
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
                    tracks.map((track, i) => <Track key={i} track={track.track} />) 
                }
            </div>
            <div className="f scroll-box">
           
                {playlists.map((playlist, i) => 
                    <SavedPlaylist 
                        key={i} 
                        playlist={playlist}
                        selectedPL={selectedPL}
                        setSelectedPL={setSelectedPL}
                    />
                )}
                
            </div>

        </div>
        
    )
}