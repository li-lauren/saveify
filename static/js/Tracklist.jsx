const Tracklist = ({selectedPL}) => {
    const [tracks, setTracks] = useState(null);

    const getTracks = () => {
        fetch(`/tracks/${selectedPL}`)
        .then(res => res.json())
        .then(data => {
            setTracks(data.items);
        });
    }; 

    useEffect(() => {
        if (selectedPL) {
            getTracks();
        } 
    }, [selectedPL])

    return (
        <div className="tracks-container">
            {
                tracks ? 
                tracks.map((track, i) => 
                <Track key={i} track={track.track} />) : ''
            }
        </div>
    )
}