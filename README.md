## Database

### Create database

```bash
pdm run db-create
```

### Seed

```bash
pdm run db-test-drop-all
pdm run db-test-seed
```

> **Warning**
> Running `pdm run db-drop-all` will delete all rows in the database.

## Tests

To run all tests, run

```bash
pdm run test
```

Tests are located in the `test/` folder.