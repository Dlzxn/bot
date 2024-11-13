--
-- ‘айл сгенерирован с помощью SQLiteStudio v3.4.4 в —р но€ 6 12:32:24 2024
--
-- »спользованна€ кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- “аблица: users
CREATE TABLE IF NOT EXISTS users (user_id INTEGER UNIQUE, user_name TEXT, user_surname TEXT, username TEXT, para_id INTEGER, progr_otn INTEGER DEFAULT (0), lvl_otn INTEGER DEFAULT (0), chmok_stat INTEGER DEFAULT (0), seks_stat INTEGER DEFAULT (0), obn_stat INTEGER DEFAULT (0));
INSERT INTO users (user_id, user_name, user_surname, username, para_id, progr_otn, lvl_otn, chmok_stat, seks_stat, obn_stat) VALUES (7136047862, 'Ж?????ы? ?????Ж', NULL, 'sonuuuuuks', NULL, 0, 0, 0, 0, 0);
INSERT INTO users (user_id, user_name, user_surname, username, para_id, progr_otn, lvl_otn, chmok_stat, seks_stat, obn_stat) VALUES (1007130027, 'Int', 'Text_Massage?{Alex??}', 'illgettomorow', 1007130027, 0, 0, 0, 0, 0);
INSERT INTO users (user_id, user_name, user_surname, username, para_id, progr_otn, lvl_otn, chmok_stat, seks_stat, obn_stat) VALUES (7031632607, 'Luni', 'Top', 'drilli2', NULL, 0, 0, 0, 0, 0);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
