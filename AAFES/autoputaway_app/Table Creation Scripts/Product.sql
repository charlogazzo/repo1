-- Table: public.Product

-- DROP TABLE public."Product";

CREATE TABLE public."Product"
(
    "Name" character varying COLLATE pg_catalog."default" NOT NULL,
    "Product_CRC" character varying(7) COLLATE pg_catalog."default" NOT NULL,
    "Cases_Per_Layer" integer NOT NULL,
    "Case_Height" integer NOT NULL,
    CONSTRAINT "Product_pkey" PRIMARY KEY ("Product_CRC")
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Product"
    OWNER to "Charles";

COMMENT ON TABLE public."Product"
    IS 'Contains data about the products that can be stored in the locations';