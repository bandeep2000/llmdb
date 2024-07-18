from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session
from datetime import datetime

Base = declarative_base()

class Server(Base):
    __tablename__ = 'servers'
    id = Column(Integer, primary_key=True)
    hostname = Column(String, unique=True, nullable=False)
    ip_address = Column(String, unique=True, nullable=False)
    operating_system = Column(String, nullable=False)
    os_version = Column(String, nullable=False)
    cpu_cores = Column(Integer)
    ram_gb = Column(Integer)
    disk_gb = Column(Integer)
    location = Column(String)
    environment = Column(String)
    last_updated = Column(DateTime, default=datetime.utcnow)

    applications = relationship("Application", back_populates="server")
    network_interfaces = relationship("NetworkInterface", back_populates="server")

class Application(Base):
    __tablename__ = 'applications'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    version = Column(String)
    install_date = Column(DateTime)
    server_id = Column(Integer, ForeignKey('servers.id'))

    server = relationship("Server", back_populates="applications")

class NetworkInterface(Base):
    __tablename__ = 'network_interfaces'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    mac_address = Column(String)
    ip_address = Column(String)
    server_id = Column(Integer, ForeignKey('servers.id'))

    server = relationship("Server", back_populates="network_interfaces")

def create_and_populate_db():
    engine = create_engine("sqlite:///cmdb.db", echo=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    # Sample data
    servers = [
        Server(hostname="win-srv-01", ip_address="192.168.1.10", operating_system="Windows", os_version="Server 2019", cpu_cores=8, ram_gb=64, disk_gb=1000, location="NYC", environment="Production"),
        Server(hostname="ubuntu-srv-01", ip_address="192.168.1.20", operating_system="Ubuntu", os_version="20.04 LTS", cpu_cores=4, ram_gb=32, disk_gb=500, location="NYC", environment="Production"),
        Server(hostname="win-srv-02", ip_address="192.168.1.11", operating_system="Windows", os_version="Server 2016", cpu_cores=4, ram_gb=32, disk_gb=500, location="LA", environment="Development"),
        Server(hostname="ubuntu-srv-02", ip_address="192.168.1.21", operating_system="Ubuntu", os_version="22.04 LTS", cpu_cores=8, ram_gb=64, disk_gb=1000, location="LA", environment="Staging"),
    ]
    session.add_all(servers)
    session.commit()

    applications = [
        Application(name="SQL Server", version="2019", install_date=datetime(2021, 1, 1), server_id=1),
        Application(name="IIS", version="10", install_date=datetime(2021, 1, 1), server_id=1),
        Application(name="MySQL", version="8.0", install_date=datetime(2021, 2, 1), server_id=2),
        Application(name="Apache", version="2.4", install_date=datetime(2021, 2, 1), server_id=2),
        Application(name="SQL Server", version="2016", install_date=datetime(2020, 6, 1), server_id=3),
        Application(name="Nginx", version="1.18", install_date=datetime(2022, 3, 1), server_id=4),
    ]
    session.add_all(applications)
    session.commit()

    network_interfaces = [
        NetworkInterface(name="eth0", mac_address="00:1A:2B:3C:4D:5E", ip_address="192.168.1.10", server_id=1),
        NetworkInterface(name="eth0", mac_address="00:1A:2B:3C:4D:5F", ip_address="192.168.1.20", server_id=2),
        NetworkInterface(name="eth0", mac_address="00:1A:2B:3C:4D:60", ip_address="192.168.1.11", server_id=3),
        NetworkInterface(name="eth0", mac_address="00:1A:2B:3C:4D:61", ip_address="192.168.1.21", server_id=4),
    ]
    session.add_all(network_interfaces)
    session.commit()

    print("Database created and populated successfully.")

if __name__ == "__main__":
    create_and_populate_db()
