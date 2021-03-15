const PlaylistCarousel = ({playlists, n}) => {
    // n = number of slides to display at one time
    const [pos, setPos] = useState(0);
    const [hidePrev, setHidePrev] = useState(false);
    const [hideNext, setHideNext] = useState(false);
    
    const checkBounds = () => {
        const numPlaylists = playlists.length;
        console.log(`Current POS: ${pos}`);

        pos == 0 ? setHidePrev(true) : setHidePrev(false);
        pos + n >= numPlaylists ? setHideNext(true) : setHideNext(false);
    };

    const showPrevPL = () => setPos(pos - n);
    const showNextPL = () => setPos(pos + n);
   

    useEffect(() => {
        checkBounds();
    }, [playlists, pos]);

    return(
        <div className="f carousel">
            {
                hidePrev ? '' : 
                <button 
                    className="btn btn-sm"
                    onClick={showPrevPL}>
                    &larr;
                </button>
            }
            <div className="f carousel-slides">
                {playlists.slice(pos, pos + n)}
            </div>
            
            {
                hideNext ? '' :  
                <button 
                    className="btn btn-sm"
                    onClick={showNextPL}>
                    &rarr;
                </button>
            }
        </div>
    )
}