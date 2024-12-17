from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

SENSOR_ID_MAX_LENGTH = 16
TEST_TYPE_NAME_MAX_LENGTH = 8
TEST_DATA_FILE_PATH_MAX_LENGTH = 255

Base = declarative_base()


class Sensor(Base):
    __tablename__ = 'sensors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sensor_id = Column(String(SENSOR_ID_MAX_LENGTH),
                       unique=True,
                       nullable=False,
                       index=True)

    tests = relationship('Test', back_populates='sensor')

    def __repr__(self):
        return f"<SensorData(id={self.id}, sensor_id='{self.sensor_id}')>"


class TestType(Base):
    __tablename__ = 'test_types'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(TEST_TYPE_NAME_MAX_LENGTH),
                  nullable=False,
                  unique=True,
                  index=True)

    tests = relationship('Test', back_populates='test_type')

    def __repr__(self):
        return f"<TestType(id={self.id}, name='{self.name}')>"


class Test(Base):
    __tablename__ = 'tests'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sensor_id = Column(String(SENSOR_ID_MAX_LENGTH),
                       ForeignKey('sensors.sensor_id'),
                       nullable=False)
    test_name = Column(String(TEST_TYPE_NAME_MAX_LENGTH),
                       ForeignKey('test_types.name'),
                       nullable=False)
    timestamp = Column(DateTime, nullable=False)
    test_data_file = Column(String(TEST_DATA_FILE_PATH_MAX_LENGTH),
                            nullable=False)

    sensor = relationship('Sensor', back_populates='tests')
    test_type = relationship('TestType', back_populates='tests')

    def __repr__(self):
        return (f"<Test(id={self.id}, sensor_id={self.sensor_id}, "
                f"test_name={self.test_name}, timestamp='{self.timestamp}', "
                f"test_data_file='{self.test_data_file}')>")
