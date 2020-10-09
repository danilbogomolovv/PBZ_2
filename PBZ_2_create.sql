CREATE DATABASE IF NOT EXISTS lab_2;
use lab_2;

CREATE TABLE IF NOT EXISTS medical_statistics_card (
  id int NOT NULL AUTO_INCREMENT,
  fullname varchar(50) DEFAULT NULL,
  sex varchar(1) DEFAULT NULL,
  age int DEFAULT NULL,
  provisional_diagnosis varchar(50) DEFAULT NULL,
  admission varchar(50) DEFAULT NULL,
  date_of_admission date DEFAULT NULL,
  height int DEFAULT NULL,
  weight int DEFAULT NULL,
  hair_color varchar(15) DEFAULT NULL,
  special_signs varchar(60) DEFAULT NULL,
  room_number int DEFAULT NULL,
  reason_for_discharge varchar(50) DEFAULT NULL,
  discharge_date date DEFAULT NULL,
  PRIMARY KEY (id)
);


CREATE TABLE IF NOT EXISTS transfer(
id int NOT NULL AUTO_INCREMENT,
fullname varchar(50) DEFAULT NULL,
previous_room_number int DEFAULT NULL,
next_room_number int DEFAULT NULL,
next_room_phone varchar(15) DEFAULT NULL,
transfer_date date DEFAULT NULL,
PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS ward_phone(
id int NOT NULL AUTO_INCREMENT,
room_number int DEFAULT NULL,
room_phone varchar(50) DEFAULT NULL,
PRIMARY KEY (id));

/*INSERT INTO ward_phone(room_number, room_phone) VALUES
(212, '323-43-65'),
(214, '456-23-23'),
(216, '128-34-98'),
(218, '178-45-78'),
(312, '778-28-92'),
(314, '565-66-43'),
(316, '888-66-34'),
(318, '656-77-90'),
(412, '127-09-45'),
(414, '878-87-78'),
(416, '456-78-90'),
(418, '990-56-65');


INSERT INTO medical_statistics_card(fullname, sex, age, provisional_diagnosis, admission, date_of_admission, height, weight, hair_color, special_signs, room_number, reason_for_discharge, discharge_date) VALUES
('Богомолов Данил Владимирович', 'М', '19', 'Перелом руки', 'Скорая помощь', '2020-01-21', '183', '64', 'Каштановый', 'Татуировка на пальце', '212', 'Выздоровление', '2020-02-12'), 
('Кузин Алексей Тарасович', 'М', '20', 'Коронавирус', 'Скорая помощь', '2020-03-05', '180', '73', 'Русый', 'Короткая стрижка, алкоголик', '318', 'Смерть', '2020-03-08'), 
('Дубно Анастасия Дмитриевна', 'Ж', '53', 'Мигрень', 'Направление поликлиники', '2020-10-07', '175', '54', 'Русый', '-', '216', '-', NULL), 
('Шепко Матвей Тарасович', 'М', '27', 'Коронавирус', 'Скорая помощь', '2020-03-05', '185', '78', 'Черный', 'Курит', '318', 'Смерть', '2020-03-09'), 
('Янкова Кристина Васильевна', 'Ж', '31', 'Отравление', 'Направление поликлиники', '2020-01-21', '173', '64', 'Блонидинистый', '-', '412', 'Выздоровление', '2020-02-12'), 
('Самаль Алина Викторовна', 'Ж', '19', 'Перелом ключицы', 'Скорая помощь', '2020-01-25', '169', '50', 'Каштановый', 'Сирота', '214', 'Перевод в другую больницу', '2020-02-20'), 
('Хмелинко Павел Сергеевич', 'М', '74', 'Варикоз', 'Направление поликлиники', '2020-01-11', '190', '70', 'Русый', 'Татуировка на шее', '312', 'Выздоровление', '2020-02-01'), 
('Варавко Ксения Дмитриевна', 'Ж', '47', 'Коронавирус', 'Скорая помощь', '2020-03-05', '167', '52', 'Блондинистый', '-', '318', 'Выздоровление', '2020-03-19'), 
('Шадрин Евгений Владимирович', 'М', '24', 'Ангидроз', 'Скорая помощь', '2020-10-08', '183', '68', 'Блондинистый', '-', '314', '-', NULL), 
('Коваленко Антон Викторович', 'М', '56', 'Аденома бронха', 'Скорая помощь', '2020-10-06', '180', '71', 'Черный', 'Иностранец', '314', '-', NULL), 
('Хмарик Данила Сергеевич', 'М', '24', 'Сепсис', 'Скорая помощь', '2020-05-16', '186', '69', 'Каштановый', '-', '316', 'Перевод в другую больницу', '2020-06-02'), 
('Яблонь Алина Андреевна', 'Ж', '35', 'Отравление', 'Направление поликлиники', '2020-03-16', '172', '59', 'Каштановый', '-', '414', 'Выздоровление', '2020-04-01');
*/

