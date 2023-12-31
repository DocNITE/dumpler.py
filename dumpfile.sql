--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1
-- Dumped by pg_dump version 16.1

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
-- Name: onemore; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.onemore (
    id integer
);


ALTER TABLE public.onemore OWNER TO postgres;

--
-- Data for Name: onemore; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.onemore (id) FROM stdin;
5
5
2
1
\.


--
-- PostgreSQL database dump complete
--

