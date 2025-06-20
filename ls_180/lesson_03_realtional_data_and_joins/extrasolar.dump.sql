--
-- PostgreSQL database dump
--

-- Dumped from database version 16.9 (Ubuntu 16.9-0ubuntu0.24.04.1)
-- Dumped by pg_dump version 16.9 (Ubuntu 16.9-0ubuntu0.24.04.1)

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
-- Name: spectral_type_enum; Type: TYPE; Schema: public; Owner: nicolo-bencini
--

CREATE TYPE public.spectral_type_enum AS ENUM (
    'O',
    'B',
    'A',
    'F',
    'G',
    'K',
    'M'
);


ALTER TYPE public.spectral_type_enum OWNER TO "nicolo-bencini";

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: moons; Type: TABLE; Schema: public; Owner: nicolo-bencini
--

CREATE TABLE public.moons (
    id integer NOT NULL,
    designation integer NOT NULL,
    semi_major_axis numeric,
    mass numeric,
    planet_id integer,
    CONSTRAINT moons_mass_check CHECK ((mass >= (0)::numeric)),
    CONSTRAINT moons_semi_major_axis_check CHECK ((semi_major_axis >= (0)::numeric))
);


ALTER TABLE public.moons OWNER TO "nicolo-bencini";

--
-- Name: moons_id_seq; Type: SEQUENCE; Schema: public; Owner: nicolo-bencini
--

CREATE SEQUENCE public.moons_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.moons_id_seq OWNER TO "nicolo-bencini";

--
-- Name: moons_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nicolo-bencini
--

ALTER SEQUENCE public.moons_id_seq OWNED BY public.moons.id;


--
-- Name: planets; Type: TABLE; Schema: public; Owner: nicolo-bencini
--

CREATE TABLE public.planets (
    id integer NOT NULL,
    designation character(1) NOT NULL,
    mass numeric NOT NULL,
    star_id integer NOT NULL,
    semi_major_axis numeric NOT NULL,
    CONSTRAINT mass_constraint CHECK ((mass >= (0)::numeric))
);


ALTER TABLE public.planets OWNER TO "nicolo-bencini";

--
-- Name: planets_id_seq; Type: SEQUENCE; Schema: public; Owner: nicolo-bencini
--

CREATE SEQUENCE public.planets_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.planets_id_seq OWNER TO "nicolo-bencini";

--
-- Name: planets_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nicolo-bencini
--

ALTER SEQUENCE public.planets_id_seq OWNED BY public.planets.id;


--
-- Name: stars; Type: TABLE; Schema: public; Owner: nicolo-bencini
--

CREATE TABLE public.stars (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    distance numeric NOT NULL,
    spectral_type public.spectral_type_enum,
    companions integer NOT NULL,
    CONSTRAINT companions_constraint CHECK ((companions >= 0)),
    CONSTRAINT distance_constraint CHECK (((distance)::double precision > (0)::double precision))
);


ALTER TABLE public.stars OWNER TO "nicolo-bencini";

--
-- Name: stars_id_seq; Type: SEQUENCE; Schema: public; Owner: nicolo-bencini
--

CREATE SEQUENCE public.stars_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.stars_id_seq OWNER TO "nicolo-bencini";

--
-- Name: stars_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nicolo-bencini
--

ALTER SEQUENCE public.stars_id_seq OWNED BY public.stars.id;


--
-- Name: moons id; Type: DEFAULT; Schema: public; Owner: nicolo-bencini
--

ALTER TABLE ONLY public.moons ALTER COLUMN id SET DEFAULT nextval('public.moons_id_seq'::regclass);


--
-- Name: planets id; Type: DEFAULT; Schema: public; Owner: nicolo-bencini
--

ALTER TABLE ONLY public.planets ALTER COLUMN id SET DEFAULT nextval('public.planets_id_seq'::regclass);


--
-- Name: stars id; Type: DEFAULT; Schema: public; Owner: nicolo-bencini
--

ALTER TABLE ONLY public.stars ALTER COLUMN id SET DEFAULT nextval('public.stars_id_seq'::regclass);


--
-- Data for Name: moons; Type: TABLE DATA; Schema: public; Owner: nicolo-bencini
--



--
-- Data for Name: planets; Type: TABLE DATA; Schema: public; Owner: nicolo-bencini
--



--
-- Data for Name: stars; Type: TABLE DATA; Schema: public; Owner: nicolo-bencini
--

INSERT INTO public.stars VALUES (3, 'Alpha Centauri B', 4, 'K', 3);
INSERT INTO public.stars VALUES (4, 'Alpha Orionis', 643, 'M', 9);


--
-- Name: moons_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nicolo-bencini
--

SELECT pg_catalog.setval('public.moons_id_seq', 1, false);


--
-- Name: planets_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nicolo-bencini
--

SELECT pg_catalog.setval('public.planets_id_seq', 1, false);


--
-- Name: stars_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nicolo-bencini
--

SELECT pg_catalog.setval('public.stars_id_seq', 4, true);


--
-- Name: moons moons_pkey; Type: CONSTRAINT; Schema: public; Owner: nicolo-bencini
--

ALTER TABLE ONLY public.moons
    ADD CONSTRAINT moons_pkey PRIMARY KEY (id);


--
-- Name: planets planets_pkey; Type: CONSTRAINT; Schema: public; Owner: nicolo-bencini
--

ALTER TABLE ONLY public.planets
    ADD CONSTRAINT planets_pkey PRIMARY KEY (id);


--
-- Name: stars stars_name_key; Type: CONSTRAINT; Schema: public; Owner: nicolo-bencini
--

ALTER TABLE ONLY public.stars
    ADD CONSTRAINT stars_name_key UNIQUE (name);


--
-- Name: stars stars_pkey; Type: CONSTRAINT; Schema: public; Owner: nicolo-bencini
--

ALTER TABLE ONLY public.stars
    ADD CONSTRAINT stars_pkey PRIMARY KEY (id);


--
-- Name: moons moons_planet_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nicolo-bencini
--

ALTER TABLE ONLY public.moons
    ADD CONSTRAINT moons_planet_id_fkey FOREIGN KEY (planet_id) REFERENCES public.planets(id);


--
-- Name: planets planets_star_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nicolo-bencini
--

ALTER TABLE ONLY public.planets
    ADD CONSTRAINT planets_star_id_fkey FOREIGN KEY (star_id) REFERENCES public.stars(id);


--
-- PostgreSQL database dump complete
--

