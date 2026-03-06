-- schema.sql


-- users table

CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT UNIQUE NOT NULL,

    email TEXT UNIQUE NOT NULL,

    password TEXT NOT NULL

);


-- symptom prediction history

CREATE TABLE IF NOT EXISTS symptoms (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    symptom TEXT,

    predicted_disease TEXT,

    risk_level TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);


-- pregnancy monitoring records

CREATE TABLE IF NOT EXISTS pregnancy_records (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    mother_name TEXT,

    age INTEGER,

    start_date DATE,

    weeks INTEGER

);


-- hospitals table

CREATE TABLE IF NOT EXISTS hospitals (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT,

    location TEXT,

    contact TEXT

);


-- emergency alerts

CREATE TABLE IF NOT EXISTS emergency_alerts (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    patient_name TEXT,

    location TEXT,

    issue TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);


-- disease reports (outbreak detection)

CREATE TABLE IF NOT EXISTS disease_reports (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    disease_name TEXT,

    location TEXT,

    cases INTEGER,

    report_date DATE

);  