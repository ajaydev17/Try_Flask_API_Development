from . import inventory_seasonal_event_api_blueprint
from ..schema import SeasonalEventInsertSchema
from apifairy import body, response
from ..models import SeasonalEvent
from .. import database

seasonal_event_insert_schema = SeasonalEventInsertSchema()


@inventory_seasonal_event_api_blueprint.route('/seasonal-event', methods=['POST'])
@body(seasonal_event_insert_schema)
@response(seasonal_event_insert_schema)
def insert_product(kwargs):
    new_seasonal_event = SeasonalEvent(**kwargs)
    database.session.add(new_seasonal_event)
    database.session.commit()
    return new_seasonal_event

