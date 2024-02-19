from fastapi import APIRouter

router = APIRouter()

@router.get("/getAll", tags=["Capstone"])
async def read_capstone():
    return {"message": "Hello World Capstone"}

@router.get("/sample1Nicholas", tags=["Capstone"])
async def read_capstone():
    return {"message": "Hello World Capstone"}

@router.get("/sample2", tags=["Capstone"])
async def read_capstone():
    sample_device = {
        'serial_number' :"12345ABC",
        'device_type' :"Sensor",
        'owner' :"John Doe",
        'location' :"Warehouse 1",
        'status' : "Active"
    }
    return sample_device
