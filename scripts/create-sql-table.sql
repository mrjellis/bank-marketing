CREATE TABLE public.bank
(
    id real NOT NULL,
    age integer,
    job text COLLATE pg_catalog."default",
    marital text COLLATE pg_catalog."default",
    education text COLLATE pg_catalog."default",
    "default" text COLLATE pg_catalog."default",
    balance real,
    housing text COLLATE pg_catalog."default",
    loan text COLLATE pg_catalog."default",
    contact text COLLATE pg_catalog."default",
    day real,
    month text COLLATE pg_catalog."default",
    duration real,
    campaign real,
    pdays real,
    previous real,
    poutcome text COLLATE pg_catalog."default",
    y text COLLATE pg_catalog."default",
    CONSTRAINT bank_pkey PRIMARY KEY (id)
)


