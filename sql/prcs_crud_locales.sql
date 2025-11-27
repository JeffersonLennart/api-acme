-- ==============
-- INSERTAR LOCAL
-- ==============
CREATE OR REPLACE FUNCTION func_local_insertar(
	p_local TEXT,
	p_cliente TEXT,
	p_territorio TEXT
)
RETURNS INT
LANGUAGE plpgsql
AS $$
DECLARE
	v_localid INT;
	v_clienteid INT;
	v_territorioid INT;
	v_nuevoid INT;
BEGIN

	-- Dar formato a los parametros de tipo texto
	p_local := INITCAP(TRIM(p_local));
	p_cliente := INITCAP(TRIM(p_cliente));
	p_territorio := INITCAP(TRIM(p_territorio));
	
	-- Recuperar id del cliente
	SELECT id INTO v_clienteid
	FROM cliente
	WHERE nombre = p_cliente;

	-- Validar si existe el cliente
	IF v_clienteid IS NULL THEN
		RAISE EXCEPTION 'El Cliente no existe.';
	END IF;
	
	-- Recuperar id del territorio
	SELECT id INTO v_territorioid
	FROM territorio
	WHERE nombre = p_territorio;

	-- Crear territorio si no existe
	IF v_territorioid IS NULL THEN
		INSERT INTO territorio(nombre) VALUES(p_territorio)
		RETURNING id INTO v_territorioid;
	END IF;
	
	-- Recuperar id del local
	SELECT id INTO v_localid
	FROM locaL
	WHERE nombre = p_local
		AND clienteid = v_clienteid
		AND territorioid = v_territorioid;		
	
	-- Crear local si no existe
	IF v_localid IS NULL THEN
		INSERT INTO local(nombre, clienteid, territorioid)
		VALUES(p_local, v_clienteid, v_territorioid)
		RETURNING id INTO v_nuevoid;

		RETURN v_nuevoid;
	-- Si el local ya existe lanzar un error
	ELSE
		RAISE EXCEPTION 'El local ya existe.';
	END IF;
END;
$$;

-- ================
-- RETORNAR LOCALES
-- ================
CREATE OR REPLACE FUNCTION func_locales_recuperar()
RETURNS TABLE (
	id INT,
	local TEXT,
	cliente TEXT,
	territorio TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
	RETURN QUERY
	SELECT l.id,
		l.nombre,
		c.nombre,
		t.nombre
	FROM local l
	INNER JOIN cliente c ON l.clienteid = c.id
	INNER JOIN territorio t ON l.territorioid = t.id
	ORDER BY l.id;
END;
$$;

-- ================
-- ACTUALIZAR LOCAL
-- ================
CREATE OR REPLACE PROCEDURE prc_local_actualizar(
	p_localid INT,
	p_local TEXT,
	p_cliente TEXT,
	p_territorio TEXT
)
LANGUAGE plpgsql
AS $$
DECLARE
	v_localid INT;
	v_clienteid INT;
	v_territorioid INT;
BEGIN

	-- Dar formato a los parametros de tipo texto
	p_local := INITCAP(TRIM(p_local));
	p_cliente := INITCAP(TRIM(p_cliente));
	p_territorio := INITCAP(TRIM(p_territorio));
	
	-- Validar que existe el local
	IF NOT EXISTS (SELECT id FROM local WHERE id = p_localid) THEN
		RAISE EXCEPTION 'El local no existe.';
	END IF;

	-- Recuperar id del cliente
	SELECT id INTO v_clienteid
	FROM cliente
	WHERE nombre = p_cliente;

	-- Validar que exista el cliente
	IF v_clienteid IS NULL THEN
		RAISE EXCEPTION 'El cliente no existe.';
	END IF;

	-- Recuperar id del territorio
	SELECT id INTO v_territorioid
	FROM territorio
	WHERE nombre = p_territorio;

	-- Crear territorio si no existe
	IF v_territorioid IS NULL THEN
		INSERT INTO territorio(nombre) VALUES(p_territorio)
		RETURNING id INTO v_territorioid;
	END IF;

	-- Recuperar id del local
	SELECT id INTO v_localid
	FROM local
	WHERE nombre = p_local
		AND clienteid = v_clienteid
		AND territorioid = v_territorioid;

	-- actualizar local si no existe
	IF v_localid IS NULL THEN
		UPDATE local
		SET nombre = p_local, clienteid = v_clienteid, territorioid = v_territorioid
		WHERE id = p_localid;
	ELSIF v_localid != p_localid THEN
		RAISE EXCEPTION 'El local ya existe.';
	END IF;	
END;
$$;

-- ==============
-- ELIMINAR LOCAL
-- ==============
CREATE OR REPLACE PROCEDURE prc_local_eliminar(
	p_localid INT
)
LANGUAGE plpgsql
AS $$
BEGIN

	-- Eliminar el local si existe
	IF EXISTS (SELECT id FROM local WHERE id = p_localid) THEN
		DELETE FROM local WHERE id = p_localid;
	ELSE
		RAISE EXCEPTION 'El local no existe.';
	END IF;
END;
$$;