const SavePlaylistForm = ({showForm, setShowForm, playlistID}) => {
    const [title, setTitle] = useState('');
    const [interval, setInterval] = useState('once');

    const savePlaylist = e => {
        e.preventDefault();

        const reqOptions = {
            method: 'POST', 
            headers: {'Content-Type' : 'application/json'}, 
            body: JSON.stringify({
                'title': title, 
                'interval': interval,
                'playlist_id': playlistID
            })
        };

        fetch('/save', reqOptions)
        .then(res => res.json())
        .then(data => {
            console.log(data)
        });
    };

    const handleRadio = e => setInterval(e.target.value);

    return (
        <div className="save-cont">
            {
                showForm ? 
                <div>
                    <button onClick={() => setShowForm(false)}>
                        Cancel
                    </button>
                
                    <form>
                        <div className="form-group">
                            <label>Playlist name:</label>
                            <input 
                                className="form-control"
                                type="text" 
                                placeholder="Name"
                                value={title}
                                onChange={e => setTitle(e.target.value)}
                            />
                        </div>
                

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
                </div> : ''
            }
        </div>
    )
}