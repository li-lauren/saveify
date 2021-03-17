const PlaylistScrollBox = ({playlists}) => {
    const [selectedPL, setSelectedPL] = useState(null);

    useEffect(() => {
        if (playlists && playlists.length > 0 && !selectedPL) {
            setSelectedPL(playlists[0].id);
        } 
    }, [playlists]);

    return(
        <div className="f saved-section">
            <Tracklist playlistID={selectedPL} />
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