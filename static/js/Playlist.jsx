const Playlist = ({playlist, setSelectedPL}) => {
    const showSaveForm = () => {
        setSelectedPL(playlist);
    }

    return(
        <div className="playlist-cont col-center">
            <button 
                type="button" 
                className="save-btn btn" 
                onClick={showSaveForm}
            >
                ...
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
            <span>{playlist.name}</span>     
        </div>
    )
}