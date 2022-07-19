import pdb
from quopri import decodestring
from models.destination import Destination
from models.traveller import Traveller

import repositories.destination_repository as destination_repository
import repositories.traveller_repository as traveller_repository

destination_repository.delete_all()
traveller_repository.delete_all()

traveller1 = Traveller('Joey', 30)
traveller_repository.save(traveller1)

traveller2 = Traveller('Rachel', 28)
traveller_repository.save(traveller2)

destination1 = Destination(traveller1, 'Sydney', 'Australia', 30, False)
destination_repository.save(destination1)



