from azure.cosmosdb.table.models import Entity, TablePermissions
from azure.cosmosdb.table.sharedaccesssignature import (
    TableSharedAccessSignature,
)
from azure.cosmosdb.table.tableservice import (
    TableService,
)

from datetime import datetime, timedelta
import json
import uuid

account_name='hackhr'
account_key = 'LxVyv4khX6NsL+67nsghixU9fK/IsTOjW1l27KZ0eJQeRZFKT5Ew/HwMBZcUXPQV24gGJxOnVIS4sBTsA5/VIQ=='
table_service = TableService(account_name=account_name,account_key=account_key)
table_name = "skillstore"

def store_feedback_skills(job_id,hm_id,cand_id,skills_scores,recommendation,org):
    try:
        task = Entity()
        task.PartitionKey = str(uuid.uuid4())
        task.HmId = hm_id
        task.RowKey = str(cand_id)
        now = datetime.now()
        task.LastUpdated = str(now)
        task.SkillScores = json.dumps(skills_scores)
        task.JobId = str(job_id)
        table_service.insert_or_replace_entity(table_name, task)
    except:
        raise

# def get_compute_data(org,result,hm_id):
#     if org and result and hm_id:
#         query = "HmId eq {hm_id} and result eq {result} and org eq {org}"
#         query.format(hm_id= hm_id)

