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

    return(
       <div>
           Saveify
            {auth ? <PlaylistLib /> : ''}
           

       </div>
    ) 
}

ReactDOM.render(<App />, document.getElementById('root'));