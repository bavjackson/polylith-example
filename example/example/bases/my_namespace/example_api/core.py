from fastapi import FastAPI

from my_namespace.example_api.rabbit_router import rabbit_router

app = FastAPI(
    title='example_api',
    openapi_url='/api/openapi.json',
    lifespan=rabbit_router.lifespan_context
)


@rabbit_router.get('/')
async def example_get():
    await rabbit_router.broker.publish({'message': 'event from event'}, 'example')
    return {'message': 'reponse from route'}

@rabbit_router.get('/another')
async def example_get():
    await rabbit_router.broker.publish({'message': 'event from another event'}, 'another_example')
    return {'message': 'reponse from route'}

app.include_router(rabbit_router, prefix='/api')


