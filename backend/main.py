from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from hackathon import answer_question


app = FastAPI()

# Allow frontend (Vite) to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

"""@app.post("/ask")
def ask_question(query: Query):
    answer = answer_question(query.question)
    return {"answer": answer}"""

@app.post("/ask")
async def ask_question(
    question: str | None = Form(None),
    image: UploadFile | None = File(None),
    audio: UploadFile | None = File(None),
):
    image_path = audio_path = None

    if image:
        image_path = f"temp_{image.filename}"
        with open(image_path, "wb") as f:
            f.write(await image.read())

    if audio:
        audio_path = f"temp_{audio.filename}"
        with open(audio_path, "wb") as f:
            f.write(await audio.read())

    answer = answer_question(
        question=question or "",
        image_path=image_path,
        audio_path=audio_path,
    )

    for p in [image_path, audio_path]:
        if p and os.path.exists(p):
            os.remove(p)

    return {"answer": answer}
