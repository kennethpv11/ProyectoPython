from fastapi import APIRouter, Header
from models.schema.Measure import Measure
from config.DbHandler import conn
from models.Dao.MeasureDao import MeasureDao
from fastapi.responses import JSONResponse
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from middlewares.verify_token_route import VerifyTokenRoute

simulator = APIRouter(route_class=VerifyTokenRoute)


@simulator.post('/')
def save_measure(data: Measure, Authorization: str = Header(None)):
    data = {'Device': data.device, 'Measure': data.measure, 'Magnitude': data.magnitude,
            'Timestamp': data.timestamp}

    response = conn.execute(MeasureDao.insert().returning(MeasureDao.c.id).values(data))
    return JSONResponse(status_code=HTTP_200_OK, content={"id_generado": response.first()[0]})


@simulator.get('/')
def get_all_measure(Authorization: str = Header(None)):
    try:
        return conn.execute(MeasureDao.select()).fetchall()
    except Exception as e:
        return JSONResponse(content="error en la consulta", status_code=HTTP_400_BAD_REQUEST)


@simulator.get('/{id}')
def get_measure(id: int, Authorization: str = Header(None)):
    result = conn.execute(MeasureDao.select().where(MeasureDao.c.id == id)).first()
    if result:
        return result
    else:
        return JSONResponse(status_code=HTTP_400_BAD_REQUEST, content={"data not found": id})


@simulator.put('/{id}')
def update_measure(id: int, data: Measure , Authorization: str = Header(None)):
    data = {'Device': data.device, 'Measure': data.measure, 'Magnitude': data.magnitude,
            'Timestamp': data.timestamp}
    result = conn.execute(MeasureDao.update().returning(MeasureDao.c.id)
    .values(data).where(
        MeasureDao.c.id == id))
    if result.fetchall():
        return conn.execute(MeasureDao.select().where(MeasureDao.c.id == id)).first()
    else:
        return JSONResponse(status_code=HTTP_400_BAD_REQUEST, content={"data not found": id})


@simulator.delete('/{id}')
def delete_measure(id: int , Authorization: str = Header(None)):
    result = conn.execute(MeasureDao.delete().returning(MeasureDao.c.id).where(MeasureDao.c.id == id))
    if result.fetchall():
        return JSONResponse(status_code=HTTP_200_OK, content={"person deleted": id})
    else:
        return JSONResponse(status_code=HTTP_204_NO_CONTENT, content={"data not found": id})
