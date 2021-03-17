const SavePlaylistForm = ({showForm, setShowForm, playlist}) => {
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
                'playlist_id': playlist.id
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
                <div className="f save-form">
                    <img 
                        src={playlist.images[0].url} 
                        alt={playlist.name} 
                        className="pl-cover"
                    />
                    <form>
                        <div className="form-group">
                            <label>
                                Save <strong>{playlist.name}</strong> as:
                            </label>
                            <input 
                                className="form-control input-sm"
                                type="text" 
                                placeholder="Name"
                                value={title}
                                onChange={e => setTitle(e.target.value)}
                            />
                        </div>
                            
                        <label className="radio-inline">
                            <input 
                                // className="form-check-input" 
                                type="radio" 
                                name="interval" 
                                value="once"
                                onClick={handleRadio} />
                            Once
                        </label>
                    

                        <label className="radio-inline">
                            <input 
                                // className="form-check-input" 
                                type="radio" 
                                name="interval" 
                                value="weekly"
                                onClick={handleRadio} 
                            />
                            Weekly
                        </label>
                        
                        <br/>
                        <button 
                            onClick={savePlaylist}
                            className="btn btn-sm"
                        >
                            Save
                        </button>
                        <span onClick={() => setShowForm(false)}>
                            Cancel
                        </span>
                    </form>
                </div> : ''
            }
        </div>
    )
}