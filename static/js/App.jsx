const App = () => {
    const [auth, setAuth] = useState(false);

    useEffect(() => {
        checkAuth();
    }, [])

    const checkAuth = () => {
        fetch('/user')
        .then(res => res.text())
        .then(data => {
            if (data == 'Authenticated') {
                setAuth(true);
            } else {
                setAuth(false);
            };
        });
    };

    const logOut = () => {
        fetch('/logout')
        .then(res => res.text())
        .then(data => {
            if (data == "Logout Success") {
                setAuth(false);
            }
        })
    }

    return(
       <div>
            <h2>Saveify</h2>
            {auth ?
                <button 
                    type="button" 
                    className="btn btn-light btn-sm" 
                    onClick={logOut}
                >
                    Logout
                </button> : ''}
            {auth ? <PlaylistLib /> : <Login setAuth={setAuth} />}
       </div>
    ) 
}

ReactDOM.render(<App />, document.getElementById('root'));