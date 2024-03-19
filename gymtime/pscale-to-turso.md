Run

```
pscale database dump gymtime main
```

Recreate the local SQLite DB:

```
pdm run db-create
```

Run all files:

```
sqlite3 ./local-db.sqlite < ./gymtime/pscale_dump_gymtime_main/gymtime.gym.00001.sql
sqlite3 ./local-db.sqlite < ./gymtime/pscale_dump_gymtime_main/gymtime.section.00001.sql
sqlite3 ./local-db.sqlite < ./gymtime/pscale_dump_gymtime_main/gymtime.record.00001.sql
```

On turso, set up the DB, then install the libsql adapter:

```
pdm add sqlalchemy-libsql
```
