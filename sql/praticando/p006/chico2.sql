
-- Aeroporto Tabela

CREATE TABLE AIRPORT (
  airport_code VARCHAR(20) PRIMARY KEY,
  name VARCHAR(10) NOT NULL UNIQUE,
  city VARCHAR(20) NOT NULL,
  state VARCHAR(20) NOT NULL,
);

CREATE TABLE FLIGHT (
  flight_number VARCHAR() PRIMARY KEY,
  airlane VARCHAR() NOT NULL,
  weekdays VARCHAR() NOT NULL,
)

CREATE TABLE FLIGHT_LEG (
  flight__number VARCHAR() PRIMARY KEY,
  leg_number VARCHAR() PRIMARY KEY,
  departure_airport_code VARCHAR() NOT NULL UNIQUE,
  scheduled_departure_time VARCHAR() NOT NULL,
  arrival_airport_code VARCHAR() NOT NULL,
  scheduled_arrival_time VARCHAR() NOT NULL UNIQUE
);

CREATE TABLE LEG_INSTANCE (
  flight_number VARCHAR() PRIMARY KEY,
  leg_number VARCHAR() PRIMARY KEY,
  date DATETIME() PRIMARY KEY,
  number_of_avilable_seats INT() PRIMARY KEY,
  airplane_id FOREIGN KEY REFERENCES AIRPLANE(airplane_id),
  departure_airport_code VARCHAR() NOT NULL,
  departure_time time NOT NULL,
  arrival_airport_code VARCHAR() NOT NULL,
  arrival_time time NOT NULL
);

CREATE TABLE FARE (
  flight_number  VARCHAR() PRIMARY KEY,
  FARE_CODE VARCHAR() PRIMARY KEY,
  amount VARCHAR() NOT NULL,
  restrictions VARCHAR()
);

CREATE TABLE AIRPLANE_TYPE (
  airplane_type_name VARCHAR() PRIMARY KEY,
  max_seats INT() NOT NULL,
  company VARCHAR() NOT NULL UNIQUE 
);

CREATE TABLE CAN_LAND (
  airplane_type_name VARCHAR() PRIMARY KEY,
  airport_code VARCHAR(20) PRIMARY KEY
);

CREATE TABLE AIRPLANE (
  airplane_id VARCHAR() PRIMARY KEY,
  total_number_of_seats VARCHAR() NOT NULL,
  airplane_type VARCHAR() NOT NULL
);

CREATE TABLE SEAT_RESERVATION (
  flight_number VARCHAR() PRIMARY KEY,
  leg_number VARCHAR() PRIMARY KEY,
  date datetime() PRIMARY KEY,
  seat_number VARCHAR() PRIMARY KEY,
  customer_name VARCHAR() NOT NULL,
  customer_phone CHAR(11)
);



