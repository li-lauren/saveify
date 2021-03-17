const PlaylistScrollBox = ({playlists}) => {
    const [selectedPL, setSelectedPL] = useState(null);

    // const getTracks = () => {
    //     fetch(`/tracks/${selectedPL}`)
    //     .then(res => res.json())
    //     .then(data => {
    //         setTracks(data.items);
    //     });
    // }; 

    useEffect(() => {
        if (playlists && playlists.length > 0 && !selectedPL) {
            setSelectedPL(playlists[0].id)
        } 
    }, [playlists])

    return(
        <div className="saved-section">
            <Tracklist selectedPL={selectedPL} />
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