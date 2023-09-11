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


# def problems_to_db(args):
#     for problem in args:
#         new_tags = Theme.objects.filter(theme__in=problem.get('tags')) # Новые значения тегов
#         if not Problem.objects.filter(
#                 contest_id=problem.get('contest_id'),
#                 index=problem.get('index')
#                 ).exists():
#             create_ = Problem.objects.create(
#                         contest_id=problem.get('contest_id'),
#                         index=problem.get('index'),
#                         title=problem.get('title'),
#                         difficulty=problem.get('rating'),
#                         solve_count=problem.get('solvedCount')
#                         )
#
#             create_.theme.set(new_tags)  # Используйте метод set() для установки новых значений
#             create_.save()
