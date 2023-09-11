import requests
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

# from database import get_async_session

router = APIRouter(
    prefix="/operations",
    tags=["Operations"],
)


@router.get("/")
async def get_problems():
    problems = requests.get('https://codeforces.com/api/problemset.problems').json()
    list_of_problems = []

    for i in range(len(problems['result']['problems'])):
        result_dict = {
            'contest_id': problems['result']['problems'][i]['contestId'],
            'index': problems['result']['problems'][i]['index'],
            'title': problems['result']['problems'][i]['name'],
            'type': problems['result']['problems'][i]['type'],
            'rating': problems['result']['problems'][i].get('rating'),
            'tags': problems['result']['problems'][i]['tags'],
            'solvedCount': problems['result']['problemStatistics'][i]['solvedCount']
        }
        list_of_problems.append(result_dict)

    return list_of_problems


