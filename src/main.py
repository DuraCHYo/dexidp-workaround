from fastapi import FastAPI
import requests
#from dotenv import load_dotenv
import os

#load_dotenv()

app = FastAPI()

@app.get("/dex_changed_uri")
def dex_changed_jwks():
    r = requests.get(os.getenv("ENDPOINT"))
    data = r.json()

    if os.getenv("ENABLE_ALL") == "True":
        for key, value in data.items():
            if isinstance(value, str) and os.getenv('USE_KUBE_SVC') == 'True':
                data[key] = value.replace(
                    os.getenv('URL_TO_CHANGE'),
                    os.getenv("KUBE_SVC_ADDRESS")
                )
    else:
        for key, value in data.items():
            if key == 'jwks_uri':
                if os.getenv("REPLACE_ONLY_JWKS_URI"):
                    data[key] = os.getenv("REPLACE_ONLY_JWKS_URI")

    return data

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)