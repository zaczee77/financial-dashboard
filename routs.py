from fastapi import APIRouter
import pandas as pd

router = APIRouter()

@router.get("/data")
async def get_data():
    # Example of using pandas
    data = {"Name": ["Alice", "Bob"], "Balance": [100, 200]}
    df = pd.DataFrame(data)
    return df.to_dict(orient="records")
