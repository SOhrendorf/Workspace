body = {
    "write": {
        "hue": {"value": 100},
        "sat": {"value": 100}
    }
};

fetch('http://192.168.178.68:16021/api/v1/gEnntf1ygTGNOq0b2fxW8mpsLLdc1ymi/effects',{
    methode: 'PUT',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(body)
}).then(res => {
    return res.json()
})