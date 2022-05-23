--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1 (Debian 14.1-1.pgdg110+1)
-- Dumped by pg_dump version 14.1 (Debian 14.1-1.pgdg110+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: migrations_status; Type: TYPE; Schema: public; Owner: bst
--

CREATE TYPE public.migrations_status AS ENUM (
    'update',
    'rollback'
);

ALTER TYPE public.migrations_status OWNER TO bst;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: entity_id_seq; Type: SEQUENCE; Schema: public; Owner: bst
--

CREATE SEQUENCE public.entity_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.entity_id_seq OWNER TO bst;

--
-- Name: entity_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bst
--

SELECT pg_catalog.setval('public.entity_id_seq', 1, false);

--
-- Name: entity; Type: TABLE; Schema: public; Owner: bst
--

CREATE TABLE public.entity (
    id integer NOT NULL DEFAULT nextval('public.entity_id_seq'),
    name character varying(255) NOT NULL,
    number integer NOT NULL
);

ALTER TABLE public.entity OWNER TO bst;

--
-- Name: migrations_id_migration_seq; Type: SEQUENCE; Schema: public; Owner: bst
--

CREATE SEQUENCE public.migrations_id_migration_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

--
-- Name: migrations; Type: TABLE; Schema: public; Owner: bst
--

ALTER TABLE public.migrations_id_migration_seq OWNER TO bst;

--
-- Name: migrations_id_migration_seq; Type: SEQUENCE SET; Schema: public; Owner: bst
--

SELECT pg_catalog.setval('public.migrations_id_migration_seq', 1, true);

CREATE TABLE public.migrations (
    id_migration integer NOT NULL DEFAULT nextval('public.migrations_id_migration_seq'),
    name character varying(255) DEFAULT NULL::character varying,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    statements text,
    rollback_statements text,
    status public.migrations_status
);

ALTER TABLE public.migrations OWNER TO bst;

--
-- Name: migrations_id_migration_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bst
--

ALTER SEQUENCE public.migrations_id_migration_seq OWNED BY public.migrations.id_migration;

--
-- Name: migrations id_migration; Type: DEFAULT; Schema: public; Owner: bst
--

ALTER TABLE ONLY public.migrations ALTER COLUMN id_migration SET DEFAULT nextval('public.migrations_id_migration_seq'::regclass);

--
-- Data for Name: entity; Type: TABLE DATA; Schema: public; Owner: bst
--

--
-- Data for Name: migrations; Type: TABLE DATA; Schema: public; Owner: bst
--

INSERT INTO public.migrations VALUES (1, 'Entity_20220410_171320', '2022-04-10 17:44:56', '
        SET client_encoding = ''UTF8'';

        CREATE TABLE public.entity (
            id integer NOT NULL,
            name character varying(255) NOT NULL,
            number integer NOT NULL
        );

        ALTER TABLE public.entity OWNER TO bst;

        CREATE SEQUENCE public.entity_id_seq
            START WITH 1
            INCREMENT BY 1
            NO MINVALUE
            NO MAXVALUE
            CACHE 1;

        ALTER TABLE public.entity_id_seq OWNER TO bst;

        SELECT pg_catalog.setval(''public.entity_id_seq'', 1, false);

        ALTER TABLE ONLY public.entity
            ADD CONSTRAINT entity_pkey PRIMARY KEY (id);

        CREATE UNIQUE INDEX uniq_e2844685e237e06 ON public.entity USING btree (name);
    ', NULL, 'update');


--
-- Name: entity entity_pkey; Type: CONSTRAINT; Schema: public; Owner: bst
--

ALTER TABLE ONLY public.entity
    ADD CONSTRAINT entity_pkey PRIMARY KEY (id);


--
-- Name: migrations migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: bst
--

ALTER TABLE ONLY public.migrations
    ADD CONSTRAINT migrations_pkey PRIMARY KEY (id_migration);


--
-- Name: uniq_e2844685e237e06; Type: INDEX; Schema: public; Owner: bst
--

CREATE UNIQUE INDEX uniq_e2844685e237e06 ON public.entity USING btree (name);

--
-- PostgreSQL database dump complete
--
