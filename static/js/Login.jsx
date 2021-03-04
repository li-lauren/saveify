const Login = ({checkAuth, setAuth}) => {
    const authenticate = () => {
        fetch('/authorize')
        .then(res => res.json())
        .then(data => checkAuth())
    }
    
    return (
        <div>
            Starting saving --
            <button type="button" className="btn btn-light btn-sm" 
             onClick={authenticate}>
                Sync With Spotify
            </button>
        </div>
    )
}