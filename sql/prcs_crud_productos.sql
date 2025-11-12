-- =================
-- INSERTAR PRODUCTO
-- =================
CREATE OR REPLACE FUNCTION func_producto_insertar(
	p_producto TEXT,
	p_categoria TEXT,
	p_marca TEXT,
	p_empresa TEXT
)
RETURNS INT
LANGUAGE plpgsql
AS $$
DECLARE
	v_productoid INT;
	v_categoriaid INT;
	v_marcaid INT;
	v_empresaid INT;
	v_empresa_categoria_id INT;
	v_nuevoid INT;
BEGIN

	-- Dar formato a los parametros de tipo texto
	p_producto := INITCAP(TRIM(p_producto));
	p_categoria := INITCAP(TRIM(p_categoria));
	p_marca := INITCAP(TRIM(p_marca));
	p_empresa := INITCAP(TRIM(p_empresa));
	
	-- Recuperar id de la categoria
	SELECT id INTO v_categoriaid
	FROM categoria 
	WHERE nombre = p_categoria;

	-- Crear categoria si no existe
	IF v_categoriaid IS NULL THEN
		INSERT INTO categoria(nombre) VALUES(p_categoria)
		RETURNING id INTO v_categoriaid;
	END IF;

	-- Recuperar id de la marca
	SELECT id INTO v_marcaid
	FROM marca
	WHERE nombre = p_marca;

	-- Crear marca si no existe
	IF v_marcaid IS NULL THEN
		INSERT INTO marca(nombre) VALUES(p_marca)
		RETURNING id INTO v_marcaid;
	END IF;

	-- Recuperar id de la empresa
	SELECT id INTO v_empresaid
	FROM empresa
	WHERE nombre = p_empresa;

	-- Crear empresa si no existe
	IF v_empresaid IS NULL THEN
		INSERT INTO empresa(nombre, escompetidor)
		VALUES(p_empresa,
			CASE
				WHEN p_empresa = 'Acme' THEN False
				ELSE True
			END)
		RETURNING id INTO v_empresaid;
	END IF;

	-- Recuperar id de la relacion empresa_categoria
	SELECT id INTO v_empresa_categoria_id
	FROM empresa_categoria
	WHERE categoriaid = v_categoriaid
		AND empresaid = v_empresaid;

	-- Crear la relacion empresa_categoria si no existe
	IF v_empresa_categoria_id IS NULL THEN
		INSERT INTO empresa_categoria(categoriaid, empresaid)
		VALUES(v_categoriaid, v_empresaid)
		RETURNING id INTO v_empresa_categoria_id;
	END IF;

	-- Recuperar id del producto
	SELECT id INTO v_productoid
	FROM producto
	WHERE nombre = p_producto
		AND categoriaid = v_categoriaid
		AND marcaid = v_marcaid
		AND empresaid = v_empresaid;

	-- Crear Producto si no existe
	IF v_productoid IS NULL THEN
		INSERT INTO producto(nombre, categoriaid, marcaid, empresaid) 
		VALUES(p_producto, v_categoriaid, v_marcaid, v_empresaid)
		RETURNING id INTO v_nuevoid;

		RETURN v_nuevoid;
	-- Si el producto ya existe lanzar un error
	ELSE
		RAISE EXCEPTION 'El producto ya existe.';
	END IF;
END;
$$;

-- ==================
-- RETORNAR PRODUCTOS
-- ==================
CREATE OR REPLACE FUNCTION func_productos_recuperar()
RETURNS TABLE (
	id INT,
	producto TEXT,
	categoria TEXT,
	marca TEXT,
	empresa TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
	RETURN QUERY
	SELECT p.id,
		p.nombre,
		c.nombre,
		m.nombre,
		e.nombre
	FROM producto p
	INNER JOIN categoria c ON p.categoriaid = c.id
	INNER JOIN marca m ON p.marcaid = m.id
	INNER JOIN empresa e ON p.empresaid = e.id
	ORDER BY p.id;
END;
$$;

-- =================
-- ACTUALIZAR PRODUCTO
-- =================
CREATE OR REPLACE PROCEDURE prc_producto_actualizar(
	p_productoid INT,
	p_producto TEXT,
	p_categoria TEXT,
	p_marca TEXT,
	p_empresa TEXT
)
LANGUAGE plpgsql
AS $$
DECLARE
	v_productoid INT;
	v_categoriaid INT;
	v_marcaid INT;
	v_empresaid INT;
	v_empresa_categoria_id INT;
BEGIN

	-- Dar formato a los parametros de tipo texto
	p_producto := INITCAP(TRIM(p_producto));
	p_categoria := INITCAP(TRIM(p_categoria));
	p_marca := INITCAP(TRIM(p_marca));
	p_empresa := INITCAP(TRIM(p_empresa));

	-- Validar que existe el producto
	IF NOT EXISTS (SELECT id FROM producto WHERE id = p_productoid) THEN
		RAISE EXCEPTION 'El producto no existe.';
	END IF;
	
	-- Recuperar id de la categoria
	SELECT id INTO v_categoriaid
	FROM categoria 
	WHERE nombre = p_categoria;

	-- Crear categoria si no existe
	IF v_categoriaid IS NULL THEN
		INSERT INTO categoria(nombre) VALUES(p_categoria)
		RETURNING id INTO v_categoriaid;
	END IF;

	-- Recuperar id de la marca
	SELECT id INTO v_marcaid
	FROM marca
	WHERE nombre = p_marca;

	-- Crear marca si no existe
	IF v_marcaid IS NULL THEN
		INSERT INTO marca(nombre) VALUES(p_marca)
		RETURNING id INTO v_marcaid;
	END IF;

	-- Recuperar id de la empresa
	SELECT id INTO v_empresaid
	FROM empresa
	WHERE nombre = p_empresa;

	-- Crear empresa si no existe
	IF v_empresaid IS NULL THEN
		INSERT INTO empresa(nombre, escompetidor)
		VALUES(p_empresa,
			CASE
				WHEN p_empresa = 'Acme' THEN False
				ELSE True
			END)
		RETURNING id INTO v_empresaid;
	END IF;

	-- Recuperar id de la relacion empresa_categoria
	SELECT id INTO v_empresa_categoria_id
	FROM empresa_categoria
	WHERE categoriaid = v_categoriaid
		AND empresaid = v_empresaid;

	-- Crear la relacion empresa_categoria si no existe
	IF v_empresa_categoria_id IS NULL THEN
		INSERT INTO empresa_categoria(categoriaid, empresaid)
		VALUES(v_categoriaid, v_empresaid)
		RETURNING id INTO v_empresa_categoria_id;
	END IF;

	-- Recuperar id del producto
	SELECT id INTO v_productoid
	FROM producto
	WHERE nombre = p_producto
		AND categoriaid = v_categoriaid
		AND marcaid = v_marcaid
		AND empresaid = v_empresaid;

	-- Actualizar Producto si no existe
	IF v_productoid IS NULL THEN
		UPDATE producto
		SET nombre = p_producto,
			categoriaid = v_categoriaid,
			marcaid = v_marcaid,
			empresaid = v_empresaid
		WHERE id = p_productoid;			
	-- Si el producto ya existe lanzar un error
	ELSIF v_productoid != p_productoid THEN
		RAISE EXCEPTION 'El producto ya existe.';
	END IF;
END;
$$;

-- =================
-- ELIMINAR PRODUCTO
-- =================
CREATE OR REPLACE PROCEDURE prc_producto_eliminar(
	p_productoid INT
)
LANGUAGE plpgsql
AS $$
BEGIN

	-- Eliminar el producto si existe
	IF EXISTS (SELECT id FROM producto WHERE id = p_productoid) THEN
		DELETE FROM producto WHERE id = p_productoid;
	ELSE
		RAISE EXCEPTION 'El producto no existe.';
	END IF;
END;
$$;