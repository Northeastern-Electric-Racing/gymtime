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

#### Adding gyms to the `main` DB branch

This needs to be run only once:

```bash
pscale connect gymtime main
pdm run db-seed-gyms
```

Once this is done, confirm the data has been added with 

```bash
pscale shell gymtime main

show tables;
select * from gym;
select * from section;
```

### GitHub Actions

Add `DATABASE_URL` to Settings > Secrets and Variables > Actions > Secrets > Repository secrets. Remove the `?sslaccept=strict` from the Planetscale URL.

## Tests

To run all tests, run

```bash
pdm run test
```

Tests are located in the `test/` folder.

## Other

### Local TZ to UTC

([Credits](https://stackoverflow.com/a/69261133/8677167))

```py
from datetime import datetime

# We're using 3.8, but zoneinfo was added in 3.9
from backports.zoneinfo import ZoneInfo

local_tz = ZoneInfo("America/New_York")
utc_tz = ZoneInfo("UTC")

# Boston time
est = datetime(year=2023, month=1, day=15, hour=20, minute=30, second=0)
est = est.replace(tzinfo=local_tz)
# UTC time
utc = est.astimezone(utc_tz)

print(est)
print(utc)
```