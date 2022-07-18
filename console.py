import pdb
from quopri import decodestring
from models.destination import Destination
from models.traveller import Traveller

import repositories.destination_repository as destination_repository
import repositories.traveller_repository as traveller_repository

destination_repository.delete_all()
traveller_repository.delete_all()


destination1 = Destination('Sydney', 'Australia', 'Australasia')
destination_repository.save(destination1)


traveller1 = Traveller('Joey', 30)
traveller_repository.save(traveller1)


