from fastapi import FastAPI, status
import uvicorn

api = FastAPI(
    title="ETICApi"
)

@api.get("/" , status_code=status.HTTP_200_OK)
def health_check():


if __name__ == "__main__":
    uvicorn.run(
        app=api
        host="0.0.0.0",
        port=8000,
    )

