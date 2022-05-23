--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1 (Debian 14.1-1.pgdg110+1)
-- Dumped by pg_dump version 14.1 (Ubuntu 14.1-2.pgdg20.04+1)

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: doctrine_migration_versions; Type: TABLE; Schema: public; Owner: bst
--

CREATE TABLE public.doctrine_migration_versions (
    version character varying(191) NOT NULL,
    executed_at timestamp(0) without time zone DEFAULT NULL::timestamp without time zone,
    execution_time integer
);


ALTER TABLE public.doctrine_migration_versions OWNER TO bst;

--
-- Name: entity; Type: TABLE; Schema: public; Owner: bst
--

CREATE TABLE public.entity (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    number integer NOT NULL
);


ALTER TABLE public.entity OWNER TO bst;

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
-- Data for Name: doctrine_migration_versions; Type: TABLE DATA; Schema: public; Owner: bst
--



--
-- Data for Name: entity; Type: TABLE DATA; Schema: public; Owner: bst
--



--
-- Name: entity_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bst
--

SELECT pg_catalog.setval('public.entity_id_seq', 1, false);


--
-- Name: doctrine_migration_versions doctrine_migration_versions_pkey; Type: CONSTRAINT; Schema: public; Owner: bst
--

ALTER TABLE ONLY public.doctrine_migration_versions
    ADD CONSTRAINT doctrine_migration_versions_pkey PRIMARY KEY (version);


--
-- Name: entity entity_pkey; Type: CONSTRAINT; Schema: public; Owner: bst
--

ALTER TABLE ONLY public.entity
    ADD CONSTRAINT entity_pkey PRIMARY KEY (id);


--
-- Name: uniq_e2844685e237e06; Type: INDEX; Schema: public; Owner: bst
--

CREATE UNIQUE INDEX uniq_e2844685e237e06 ON public.entity USING btree (name);


--
-- PostgreSQL database dump complete
--

