from flask import Flask      

app = Flask(__name__)

def get_data():
    return '''[
    {
        "id": 11,
        "sigla": "RO",
        "data": [124.87,
            120.42,
            124.99,
            120.36,
            127.39,
            123.42,
            190.24,
            120.42,
            119.99]
    },
    {
        "id": 12,
        "sigla": "AC",
        "data": [249.87,
            214.42,
            296.99,
            286.36,
            293.39,
            239.42,
            217.24,
            256.42,
            275.99]
    },
    {
        "id": 13,
        "sigla": "AM",
        "data": [124.87,
            120.42,
            124.99,
            120.36,
            127.39,
            123.42,
            190.24,
            120.42,
            119.99]
    },
    {
        "id": 14,
        "sigla": "RR",
        "data": [249.87,
            214.42,
            296.99,
            286.36,
            293.39,
            239.42,
            217.24,
            256.42,
            275.99]
    },
    {
        "id": 15,
        "sigla": "PA",
        "data": [124.87,
            120.42,
            124.99,
            120.36,
            127.39,
            123.42,
            190.24,
            120.42,
            119.99]
    },
    {
        "id": 16,
        "sigla": "AP",
        "data": [124.87,
            120.42,
            124.99,
            120.36,
            127.39,
            123.42,
            190.24,
            120.42,
            119.99]
    },
    {
        "id": 17,
        "sigla": "TO",
        "data": [249.87,
            214.42,
            296.99,
            286.36,
            293.39,
            239.42,
            217.24,
            256.42,
            275.99]
    },
    {
        "id": 21,
        "sigla": "MA",
        "data": [124.87,
            120.42,
            124.99,
            120.36,
            127.39,
            123.42,
            190.24,
            120.42,
            119.99]
    },
    {
        "id": 22,
        "sigla": "PI",
        "data": [249.87,
            214.42,
            296.99,
            286.36,
            293.39,
            239.42,
            217.24,
            256.42,
            275.99]
    },
    {
        "id": 23,
        "sigla": "CE",
        "data": [124.87,
            120.42,
            124.99,
            120.36,
            127.39,
            123.42,
            190.24,
            120.42,
            119.99]
    },
    {
        "id": 24,
        "sigla": "RN",
        "data": [249.87,
            214.42,
            296.99,
            286.36,
            293.39,
            239.42,
            217.24,
            256.42,
            275.99]
    },
    {
        "id": 25,
        "sigla": "PB",
        "data": [124.87,
            120.42,
            124.99,
            120.36,
            127.39,
            123.42,
            190.24,
            120.42,
            119.99]
    },
    {
        "id": 26,
        "sigla": "PE",
        "data": [249.87,
            214.42,
            296.99,
            286.36,
            293.39,
            239.42,
            217.24,
            256.42,
            275.99]
    },
    {
        "id": 27,
        "sigla": "AL",
        "data": [124.87,
            120.42,
            124.99,
            120.36,
            127.39,
            123.42,
            190.24,
            120.42,
            119.99]
    },
    {
        "id": 28,
        "sigla": "SE",
        "data": [249.87,
            214.42,
            296.99,
            286.36,
            293.39,
            239.42,
            217.24,
            256.42,
            275.99]
    },
    {
        "id": 29,
        "sigla": "BA",
        "data": [124.87,
            120.42,
            124.99,
            120.36,
            127.39,
            123.42,
            190.24,
            120.42,
            119.99]
    },
    {
        "id": 31,
        "sigla": "MG",
        "data": [249.87,
            214.42,
            296.99,
            286.36,
            293.39,
            239.42,
            217.24,
            256.42,
            275.99]
    },
    {
        "id": 32,
        "sigla": "ES",
        "data": [124.87,
            120.42,
            124.99,
            120.36,
            127.39,
            123.42,
            190.24,
            120.42,
            119.99]
    },
    {
        "id": 33,
        "sigla": "RJ",
        "data": [249.87,
            214.42,
            296.99,
            286.36,
            293.39,
            239.42,
            217.24,
            256.42,
            275.99]
    },
    {
        "id": 35,
        "sigla": "SP",
        "data": [124.87,
            120.42,
            124.99,
            120.36,
            127.39,
            123.42,
            190.24,
            120.42,
            119.99]
    },
    {
        "id": 41,
        "sigla": "PR",
        "data": [249.87,
            214.42,
            296.99,
            286.36,
            293.39,
            239.42,
            217.24,
            256.42,
            275.99]
    },
    {
        "id": 42,
        "sigla": "SC",
        "data": [124.87,
            120.42,
            124.99,
            120.36,
            127.39,
            123.42,
            190.24,
            120.42,
            119.99]
    },
    {
        "id": 43,
        "sigla": "RS",
        "data": [249.87,
            214.42,
            296.99,
            286.36,
            293.39,
            239.42,
            217.24,
            256.42,
            275.99]
    },
    {
        "id": 50,
        "sigla": "MS",
        "data": [124.87,
            120.42,
            124.99,
            120.36,
            127.39,
            123.42,
            190.24,
            120.42,
            119.99]
    },
    {
        "id": 51,
        "sigla": "MT",
        "data": [249.87,
            214.42,
            296.99,
            286.36,
            293.39,
            239.42,
            217.24,
            256.42,
            275.99]
    },
    {
        "id": 52,
        "sigla": "GO",
        "data": [124.87,
            120.42,
            124.99,
            120.36,
            127.39,
            123.42,
            190.24,
            120.42,
            119.99]
    },
    {
        "id": 53,
        "sigla": "DF",
        "data": [249.87,
            214.42,
            296.99,
            286.36,
            293.39,
            239.42,
            217.24,
            256.42,
            275.99]
    }
]'''


@app.route("/", methods=['GET'])
def home():
    return str(get_data())

if __name__ == "__main__":
    app.run(host='0.0.0.0')
