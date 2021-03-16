const SavedPlaylist = ({playlist, selectedPL, setSelectedPL}) => {
    const [isSelected, setIsSelected] = useState(false);

    useEffect(() => {
        setIsSelected(playlist.id === selectedPL);
    }, [selectedPL])

    return (
        <div 
            className={"f saved-playlist-cont" + (isSelected ? " selected" : "") } 
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