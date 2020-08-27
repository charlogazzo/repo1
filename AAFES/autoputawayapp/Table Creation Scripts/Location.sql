-- Table: public.Location

-- DROP TABLE public."Location";

CREATE TABLE public."Location"
(
    "Name" character varying COLLATE pg_catalog."default" NOT NULL,
    "Height" integer NOT NULL,
    "Loads" character varying[] COLLATE pg_catalog."default",
    "Location_CRC" character varying COLLATE pg_catalog."default",
    "Status" character varying COLLATE pg_catalog."default" DEFAULT 'Empty'::character varying,
    "Number_Of_Cases" integer DEFAULT 0,
    CONSTRAINT "Location_pkey" PRIMARY KEY ("Name")
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Location"
    OWNER to postgres;

COMMENT ON TABLE public."Location"
    IS 'This holds data on all each location';