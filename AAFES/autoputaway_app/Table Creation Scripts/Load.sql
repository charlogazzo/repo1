-- Table: public.Load

-- DROP TABLE public."Load";

CREATE TABLE public."Load"
(
    "Load_Number" character varying COLLATE pg_catalog."default" NOT NULL,
    "Product" character varying COLLATE pg_catalog."default",
    "Number_Of_Cases" integer,
    "Location" character varying COLLATE pg_catalog."default" DEFAULT 'Receiving'::character varying,
    CONSTRAINT "Load_pkey" PRIMARY KEY ("Load_Number"),
    CONSTRAINT "FKey_Product" FOREIGN KEY ("Product")
        REFERENCES public."Product" ("Product_CRC") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Load"
    OWNER to postgres;

COMMENT ON TABLE public."Load"
    IS 'This holds data for every load';