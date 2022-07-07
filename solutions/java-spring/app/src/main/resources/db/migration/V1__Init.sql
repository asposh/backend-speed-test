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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: bst_entity; Type: TABLE; Schema: public; Owner: bst
--

CREATE TABLE public.bst_entity (
    id bigint NOT NULL,
    name character varying(255),
    number integer NOT NULL
);


ALTER TABLE public.bst_entity OWNER TO bst;

--
-- Name: hibernate_sequence; Type: SEQUENCE; Schema: public; Owner: bst
--

CREATE SEQUENCE public.hibernate_sequence
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hibernate_sequence OWNER TO bst;

--
-- Data for Name: bst_entity; Type: TABLE DATA; Schema: public; Owner: bst
--



--
-- Name: hibernate_sequence; Type: SEQUENCE SET; Schema: public; Owner: bst
--

SELECT pg_catalog.setval('public.hibernate_sequence', 1, false);


--
-- Name: bst_entity bst_entity_pkey; Type: CONSTRAINT; Schema: public; Owner: bst
--

ALTER TABLE ONLY public.bst_entity
    ADD CONSTRAINT bst_entity_pkey PRIMARY KEY (id);


--
-- Name: bst_entity uk_f94v0t1nyoh9jf8j2oko5hir6; Type: CONSTRAINT; Schema: public; Owner: bst
--

ALTER TABLE ONLY public.bst_entity
    ADD CONSTRAINT uk_f94v0t1nyoh9jf8j2oko5hir6 UNIQUE (name);


--
-- Name: idxf94v0t1nyoh9jf8j2oko5hir6; Type: INDEX; Schema: public; Owner: bst
--

CREATE INDEX idxf94v0t1nyoh9jf8j2oko5hir6 ON public.bst_entity USING btree (name);


--
-- PostgreSQL database dump complete
--

