const Track = ({track}) => {
    const artists = track.artists.reduce((acc, artist) => {
        return acc ? acc + ', ' + artist.name : artist.name
    }, '')
   
    return (
        <div className="f track-cont">
            <img className="album-cover" src={track.album.images[0].url} alt=""/>
            <div className="track-dets">
                <p className="track-name">{track.name}</p>
                <p className="artists">{artists}</p>
            </div>
        </div>
    )
}