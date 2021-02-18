const Playlist = ({playlist}) => {
    const [tracks, setTracks] = useState([]);
    const [showTracks, setShowTracks] = useState(false);
    const [showForm, setShowForm] = useState(false);
    const [title, setTitle] = useState('');
    const [interval, setInterval] = useState('once');

    const getTracks = () => {
        setShowTracks(!showTracks)
        if (showTracks) {
            fetch(`/tracks/${playlist.id}`)
            .then(res => res.json())
            .then(data => {
                console.log(data.items);
                setTracks(data.items);
            });
        }
    };

    const savePlaylist = e => {
        e.preventDefault();

        const reqOptions = {
            method: 'POST', 
            headers: {'Content-Type' : 'application/json'}, 
            body: JSON.stringify({
                'title': title, 
                'interval': interval,
                'playlist_id': playlist.id
            })
        };

        fetch('/save', reqOptions)
        .then(res => res.json())
        .then(data => {
            console.log(data)
        });
    };

    const handleRadio = e => {
        setInterval(e.target.value);
    };

    return(
        <div>
            <span onClick={getTracks}>{playlist.name}</span>  
            {showTracks ? tracks.map((track, i) => <p key={i}>{track.track.name}</p>) : ''}
            {
                showForm ? 
                <div>
                    <button onClick={() => setShowForm(false)}>Cancel</button>
                
                    <form>
                        <label>Come up with a title:</label>
                        <input 
                            type="text" 
                            placeholder="Title"
                            value={title}
                            onChange={e => setTitle(e.target.value)}
                        />
                        <br/>

                        Choose when to save:
                        <br/>
                        <input 
                            type="radio" 
                            name="interval" 
                            value="once" 
                            onClick={handleRadio}
                        />
                        <label>Once</label>

                        <input 
                            type="radio" 
                            name="interval" 
                            value="weekly" 
                            onClick={handleRadio}
                        />
                        <label>Weekly</label>
                        <br/>
                        <button onClick={savePlaylist}>Save</button>
                    </form>
                </div> :
                <div>
                    <button onClick={() => setShowForm(true)}>Save</button>
                </div>
            }
        </div>
    )
}