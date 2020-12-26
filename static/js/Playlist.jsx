const Playlist = ({playlist}) => {

    const getTracks = () => {
        fetch('/tracks')
    }
    return(
        <div>
            <span onClick={getTracks}>{playlist.name}</span>  
        </div>
    )
}