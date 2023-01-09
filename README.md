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

## Planetscale

Connect to the organization:

```bash
pscale org switch husker-gym
```

List all branches:

```bash
pscale branch list gymtime
```

Creating a dev branch for local development:

```bash
pscale branch create gymtime dev
```

Access the dev branch of the database with

```bash
pscale shell gymtime dev
```

This opens a mysql shell of the branch `dev`.

Connect to the branch with

```bash
pscale connect gymtime dev
```

This makes the `dev` branch accessible as if it were on localhost.

## Tests

To run all tests, run

```bash
pdm run test
```

Tests are located in the `test/` folder.