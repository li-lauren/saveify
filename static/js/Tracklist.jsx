const Tracklist = ({playlistID}) => {
    const [tracks, setTracks] = useState(null);

    const getTracks = () => {
        fetch(`/tracks/${playlistID}`)
        .then(res => res.json())
        .then(data => {
            setTracks(data.items);
        });
    }; 

    useEffect(() => {
        if (playlistID) {
            getTracks();
        } 
    }, [playlistID])

    return (
        <div className="f tracks-container">
            <div>
                {
                    tracks ? 
                    tracks.map((track, i) => 
                    <Track key={i} track={track.track} />) : ''
                }
            </div>
            <div className="f tracklist-h-cont">
                <span className="tracklist-h">
                    Tracks
                </span>
            </div>
            
        </div>
    )
}