const SavedPlaylist = ({playlist, setSelectedPL}) => {
    
    return (
        <div 
            className="f saved-playlist-cont" 
            onClick={() => setSelectedPL(playlist.id)}
        >
            <img 
                src={playlist.images[0].url} 
                alt={playlist.name} 
                className="pl-cover"
            />
            <span>
                {playlist.name}
            </span>  
        </div>
    )
}