DROP TABLE IF EXISTS fire;
CREATE TABLE fire (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  name        TEXT NOT NULL UNIQUE,
  title       TEXT NOT NULL,
  description TEXT
);

DROP TABLE IF EXISTS flame;
CREATE TABLE flame (
  id      INTEGER PRIMARY KEY AUTOINCREMENT,
  fire    INTEGER NOT NULL,
  fuel    INTEGER             DEFAULT 1,
  title   TEXT    NOT NULL,
  content TEXT    NOT NULL,
  FOREIGN KEY (fire) REFERENCES fire (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

INSERT INTO fire VALUES (0, 'python', 'Python', 'Let''s talk about Python!');
INSERT INTO flame VALUES (0, 0, 1, 'I <3 python', 'Python really is a great language!');
INSERT INTO flame VALUES (0, 0, 1, 'Monty Python', 'Always look on the bright side of life.');
