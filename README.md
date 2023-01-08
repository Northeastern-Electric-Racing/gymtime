## Database

### Create database

```bash
pdm run db-create
```

### Seed

```bash
pdm run db-dev-drop-all
pdm run db-dev-seed
```

> **Warning**
> Running `pdm run db-dev-drop-all` will delete all rows in the database.

## Tests

To run all tests, run

```bash
pdm run test
```

Tests are located in the `test/` folder.