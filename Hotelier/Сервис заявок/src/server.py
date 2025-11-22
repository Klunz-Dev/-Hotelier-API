from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
from schemes import ServiceRequestSchemes
from schemes import ApplicationUpdate
from db import engine, SessionDep
from model import Base, ApplicationModel
from sqlalchemy import select
from schemes import WorkerAnswear
import uvicorn

app = FastAPI(title='🏨 Hotelier API', debug=True)

@app.post('/setup_db/', tags=['💾 База данных'], summary='Подключаемся к БД')
async def setup_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

        return {'status': 200}


@app.post('/add_application/', tags=['✏️ Новая заявка'], summary='Добавляем заявку')
async def add_application(application: ServiceRequestSchemes, session: SessionDep):
    try:
        new_application = ApplicationModel(
            title = application.title,
            brief_info = application.brief_info,
            room_numb = application.room_numb,
            quest_name = application.quest_name,
            service = application.service,
        )

        session.add(new_application)
        await session.commit()

        return '✅ Ваша заявка отправлена ожидайте ответа'
    except Exception as e:
        return f'❌ Ваша заявка не отправлена ошибка <<{e}>>'
    
@app.post('/application_answear/', tags=['📝 Ответ на заявку'], summary='Работник отвечает на заявку пользователю')
async def application_answear(answear: WorkerAnswear):
    pass
    

@app.get('/get_application/', tags=['📋 Список заявок'], summary='Работник получает данные от пользователя')
async def  get_application(session: SessionDep):
    try:
        quere = select(ApplicationModel)
        result = await session.execute(quere)
        applications = result.scalars().all()
        return applications
    except Exception as e:
        return {f'⚠️ Ошибка сервиса <<{e}>>'}

if __name__ == '__main__':
    uvicorn.run('server:app', reload=True, port=8080, host='127.0.0.8')