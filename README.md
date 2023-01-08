## Database

### Create database

```bash
pdm run db-create
```

### Seed

```bash
pdm run db-drop-all
pdm run db-seed-gyms
pdm run db-seed-test-data
```

> **Warning**
> Running `pdm run db-drop-all` will delete all rows in the database. Only run in locally.

## Tests

To run all tests, run

```bash
pdm run test
```

Tests are located in the `test/` folder.