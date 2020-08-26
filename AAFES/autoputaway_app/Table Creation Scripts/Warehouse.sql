-- Table: public.Warehouse

-- DROP TABLE public."Warehouse";

CREATE TABLE public."Warehouse"
(
    "Name" character varying COLLATE pg_catalog."default" NOT NULL,
    "Locations" character varying[] COLLATE pg_catalog."default",
    CONSTRAINT "Warehouse_pkey" PRIMARY KEY ("Name")
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Warehouse"
    OWNER to "Charles";

COMMENT ON TABLE public."Warehouse"
    IS 'Holds data on the warehouse and the locations it contains';