-- ================
-- INSERTAR CLIENTE
-- ================
CREATE OR REPLACE FUNCTION func_cliente_insertar(
    p_cliente TEXT,
    p_industria TEXT
)
RETURNS INT
LANGUAGE plpgsql
AS $$
DECLARE
    v_clienteid INT;
    v_industriaid INT;
    v_nuevoid INT;
BEGIN

    -- Dar formato a los parametros de tipo texto
	p_cliente := INITCAP(TRIM(p_cliente));
	p_industria := INITCAP(TRIM(p_industria));

    -- Recuperar id de la industria
    SELECT id INTO v_industriaid
    FROM industria
    WHERE nombre = p_industria;

    -- Crear industria si no existe
    IF v_industriaid IS NULL THEN
        INSERT INTO industria(nombre) VALUES(p_industria)
        RETURNING id INTO v_industriaid;
    END IF;

    -- Recuperar id del cliente
    SELECT id INTO v_clienteid
    FROM cliente
    WHERE nombre = p_cliente
        AND industriaid = v_industriaid;

    -- Insertar cliente si no existe
    IF v_clienteid IS NULL THEN
        INSERT INTO cliente(nombre, industriaid) VALUES(p_cliente, v_industriaid)
        RETURNING id INTO v_nuevoid;

        RETURN v_nuevoid;
    -- Lanzar error si existe
    ELSE
        RAISE EXCEPTION 'El cliente ya existe.';
    END IF;

END;
$$;

-- =================
-- RETORNAR CLIENTES
-- =================
CREATE OR REPLACE FUNCTION func_clientes_recuperar()
RETURNS TABLE(
    id INT,
    cliente TEXT,
    industria TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN

    RETURN QUERY
    SELECT c.id, c.nombre, i.nombre FROM cliente c
    INNER JOIN industria i ON c.industriaid = i.id;

END;
$$;

-- ==================
-- ACTUALIZAR CLIENTE
-- ==================
CREATE OR REPLACE PROCEDURE prc_cliente_actualizar(
    p_clienteid INT,
    p_cliente TEXT,
    p_industria TEXT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_clienteid INT;
    v_industriaid INT;
BEGIN

    -- Dar formato a los parámetros de tipo TEXT
    p_cliente := INITCAP(TRIM(p_cliente));
    p_industria := INITCAP(TRIM(p_industria));

    -- Verificar si existe el cliente
    IF NOT EXISTS (SELECT id FROM cliente WHERE id = p_clienteid) THEN
        RAISE EXCEPTION 'El cliente no existe.';
    END IF;

    -- Recuperar id de la industria
    SELECT id INTO v_industriaid
    FROM industria
    WHERE nombre = p_industria;

    -- Crear industria si no existe
    IF v_industriaid IS NULL THEN
        INSERT INTO industria(nombre) VALUES(p_industria)
        RETURNING id INTO v_industriaid;
    END IF;

    -- Recuperar id del cliente
    SELECT id INTO v_clienteid
    FROM cliente
    WHERE nombre = p_cliente
        AND industriaid = v_industriaid;

    -- Actualizar cliente
    IF v_clienteid IS NULL THEN
        UPDATE cliente
        SET nombre = p_cliente,
            industriaid = v_industriaid
        WHERE id = p_clienteid;
    ELSIF v_clienteid != p_clienteid THEN
        RAISE EXCEPTION 'El cliente ya existe.';
    END IF;
END;
$$;

-- ================
-- ELIMINAR CLIENTE
-- ================
CREATE OR REPLACE PROCEDURE prc_cliente_eliminar(
    p_clienteid INT
)
LANGUAGE plpgsql
AS $$
BEGIN

    -- Eliminar cliente si existe
    IF EXISTS (SELECT id FROM cliente WHERE id = p_clienteid) THEN
        DELETE FROM cliente
        WHERE id = p_clienteid;
    ELSE
        RAISE EXCEPTION 'El cliente no existe.';
    END IF;
END;
$$;