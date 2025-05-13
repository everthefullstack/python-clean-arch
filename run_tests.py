import subprocess, asyncio, platform, os
from app.presentation.composers.database import create_database


async def _config_event_loop_policy():
    if platform.system() == "Windows":
       asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def _delete_database():
    databases = ["database_testing", 
                 "database_development.db", 
                 "database_production.db"]
    
    for database in databases:
        if os.path.exists(database):
            os.remove(database)

async def _create_database():
    create_database()

async def _run_pytest():
    subprocess.run(["pytest"])

async def _run_test():
    await _config_event_loop_policy()
    await _delete_database()
    await _create_database()
    await _run_pytest()

if __name__ == "__main__":
    asyncio.run(_run_test())
