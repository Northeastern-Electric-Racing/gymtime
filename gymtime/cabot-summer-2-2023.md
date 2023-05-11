SQL for adding Cabot gyms:

```sql
INSERT INTO gym (slug, name, short_name) VALUES ('cabot', 'Cabot Center', 'Cabot');

INSERT INTO section (slug, name, short_name, c2c_name, description, gym_id)
VALUES ('cabot-weight-room', 'Cabot Weight Room', 'Weight Room', 'Cabot Center - Weight Room', 'Athletes Weight Room', 3);

INSERT INTO section (slug, name, short_name, c2c_name, description, gym_id)
VALUES ('cabot-basketball-court', 'Cabot Basketball Court', 'Basketball', 'Cabot Center - Basketball Court', 'Basketball Court @ Cabot Center', 3);
```

Seems like this made a typo:

```sql
UPDATE section SET c2c_name = 'Cabot Center - Baseketball Court' WHERE id = 10;
```

DO NOT tell them about this! It will break the scraping workflow.

Adding FTA:

```sql
INSERT INTO section (slug, name, short_name, c2c_name, description, gym_id)
VALUES ('squash-fta', 'Squashbusters Functional Training Area', 'Squash FTA', 'Functional Training Area', 'First Floor', 2);
```