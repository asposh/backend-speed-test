package main

import (
	"github.com/beego/beego/v2/client/orm/migration"
)

// Entity20220410_171320 - DO NOT MODIFY
type Entity20220410_171320 struct {
	migration.Migration
}

// DO NOT MODIFY
func init() {
	m := &Entity20220410_171320{}
	m.Created = "20220410_171320"

	migration.Register("Entity20220410_171320", m)
}

// Up - Run the migrations
func (m *Entity20220410_171320) Up() {
	m.SQL(`
        SET client_encoding = 'UTF8';

        CREATE SEQUENCE public.entity_id_seq
            START WITH 1
            INCREMENT BY 1
            NO MINVALUE
            NO MAXVALUE
            CACHE 1;

        ALTER TABLE public.entity_id_seq OWNER TO bst;

        SELECT pg_catalog.setval('public.entity_id_seq', 1, false);

        CREATE TABLE public.entity (
            id integer NOT NULL DEFAULT nextval('public.entity_id_seq'),
            name character varying(255) NOT NULL,
            number integer NOT NULL
        );

        ALTER TABLE public.entity OWNER TO bst;

        ALTER TABLE ONLY public.entity
            ADD CONSTRAINT entity_pkey PRIMARY KEY (id);

        CREATE UNIQUE INDEX uniq_e2844685e237e06 ON public.entity USING btree (name);
    `)
}

// Down - Reverse the migrations
func (m *Entity20220410_171320) Down() {
	m.SQL(`
        DROP SEQUENCE public.entity_id_seq;
        DROP TABLE public.entity;
    `)
}
