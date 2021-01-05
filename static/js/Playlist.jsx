const Playlist = ({playlist}) => {
    const [tracks, setTracks] = useState([]);
    const [showForm, setShowForm] = useState(false);
    const [title, setTitle] = useState('');

    const getTracks = () => {
        fetch(`/tracks/${playlist.id}`)
        .then(res => res.json())
        .then(data => {
            console.log(data.items);
            setTracks(data.items);
        });
    };

    const savePlaylist = () => {
        fetch(`/save/${playlist.id}`)
        .then(res => res.json())
        .then(data => {
            console.log(data)
        });
    };

    return(
        <div>
            <span onClick={getTracks}>{playlist.name}</span>  
            {tracks.map((track, i) => <p key={i}>{track.track.name}</p>)}
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
                        <input type="radio" name="interval" value="once"/>
                        <label>Once</label>

                        <input type="radio" name="interval" value="weekly"/>
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