# ACME API Project

## ETL Process
This project complements the ETL process defined in the [ETL repository](https://github.com/JeffersonLennart/importador-acme). It details the necessary steps to ingest data from Excel files into the database, covering both the business problem description and the database design.

## API Description
This RESTful API is built using the **FastAPI** framework (Python). It is designed specifically to handle CRUD operations by directly calling **PostgreSQL Stored Procedures**, intentionally bypassing the use of an ORM system for direct database management.

## Database Configuration
The SQL scripts are located in the `sql` folder. You must execute the scripts corresponding to the CRUD processes for each table, such as `prcs_crud_clientes.sql`, `prcs_crud_locales.sql`, and `prcs_crud_productos.sql`.

The connection settings are defined in the `.env` file, as explained below.

## Local Installation and Configuration

### 1. Clone the Repository

```
git clone https://github.com/JeffersonLennart/api-acme.git
cd api-acme
```

### 2. Create Virtual Environment and Install Dependencies

```
python -m venv env
source env/bin/activate  # Linux/macOS
# env\Scripts\activate   # Windows

pip install -r requirements.txt
```

### 3. Environment Configuration
Create a `.env` file in the project root and set the environment variables. 
You can use `.env.example` as a template (you only need to update `DB_PASSWORD`).

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=acme 
DB_USER=postgres
DB_PASSWORD=**YOUR PASSWORD**
```

### 4. Execution

Run the server using Uvicorn:

```
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Implementation in AWS
*(Pending implementation details)*

## API Usage and Documentation
FastAPI automatically generates interactive documentation based on the Swagger standard. You can access it via the following URL: 
`http://127.0.0.1:8000/docs`

Additionally, a breakdown of the endpoints is provided below:

<details markdown="1">
<summary>Locations Endpoints</summary>

| Method | Route | Description | Body (JSON) |
|--------|-------|-------------|-------------|
| GET | `/locals` | Retrieve a list of all locations | N/A |
| GET | `/locals/{id}` | Retrieve details of a specific location | N/A |
| POST | `/locals` | Create a new location | `{ "local": "...", "cliente": "...", "territorio": "..." }` |
| PUT | `/locals/{id}` | Update the data of a specific location | `{ "local": "...", "cliente": "...", "territorio": "..." }` |
| DELETE | `/locals/{id}` | Remove a specific location | N/A |

#### 1. Retrieve a list of all locations (`GET /locals`)

**Request Example**

```bash
curl --request GET \
  --url http://127.0.0.1:8000/locals/
```

**Success Response (HTTP 200 OK)**

```json
[
   {
      "id": 1,
      "local": "Planta Principal",
      "cliente": "La Viga",
      "territorio": "Zona Norte"
   },
   {
      "id": 2,
      "local": "Planta Ancash",
      "cliente": "La Viga",
      "territorio": "Zona Centro"
   }
]
```

#### 2. Retrieve details of a specific location (`GET /locals/{id}`)

**Request Example**

```bash
curl --request GET \
  --url http://127.0.0.1:8000/locals/1
```

**Success Response (HTTP 200 OK)**

```json
{
  "id": 1,
  "local": "Planta Principal",
  "cliente": "La Viga",
  "territorio": "Zona Norte"
}
```

#### 3. Create a new location (`POST /locals`)

**Request Example**

```bash
curl --request POST \
  --url http://127.0.0.1:8000/locals/ \
  --header 'Content-Type: application/json' \
  --data '{
  "local": "Bodega Nueva Arequipa",
  "cliente": "La Viga",
  "territorio": "Zona Sur"
}'
```

**Success Response (HTTP 200 OK)**

```json
{
  "success": true,
  "message": "Local creado correctamente.",
  "id": 47
}
```

#### 4. Update the data of a specific location (`PUT /locals/{id}`)

**Request Example**

```bash
curl --request PUT \
  --url http://127.0.0.1:8000/locals/1 \
  --header 'Content-Type: application/json' \
  --data '{
  "local": "Planta Principal",
  "cliente": "La Viga",
  "territorio": "Zona Sur"
}'
```

**Success Response (HTTP 200 OK)**

```json
{
  "success": true,
  "message": "Local actualizado correctamente."
}
```

#### 5. Remove a specific location (`DELETE /locals/{id}`)

**Request Example**

```bash
curl --request DELETE \
  --url http://127.0.0.1:8000/locals/1
```

**Success Response (HTTP 200 OK)**

```json
{
  "success": true,
  "message": "Local eliminado correctamente."
}
```
</details>

<details markdown="1">
<summary>Products Endpoints</summary>

| Method | Route | Description | Body (JSON) |
|--------|-------|-------------|-------------|
| GET | `/products` | Retrieve a list of all products | N/A |
| GET | `/products/{id}` | Retrieve details of a specific product | N/A |
| POST | `/products` | Create a new product | `{ "producto": "...", ..., "empresa": "..." }` |
| PUT | `/products/{id}` | Update the data of a specific product | `{ "producto": "...", ..., "empresa": "..." }` |
| DELETE | `/products/{id}` | Remove a specific product | N/A |


#### 1. Retrieve a list of all products (`GET /products`)

**Request Example**

```bash
curl --request GET \
  --url http://127.0.0.1:8000/products/
```

**Success Response (HTTP 200 OK)**

```json
[
  {
  	"id": 1,
  	"producto": "Motobomba Lite De 10Hp",
  	"categoria": "Motobombas",
  	"marca": "Power Flow",
  	"empresa": "Acme"
  },
  {
  	"id": 2,
  	"producto": "Valvula De Corte Recto",
  	"categoria": "Valvulas",
  	"marca": "Power Flow",
  	"empresa": "Acme"
  }
]
```

#### 2. Retrieve details of a specific product (`GET /products/{id}`)

**Request Example**

```bash
curl --request GET \
  --url http://127.0.0.1:8000/products/1
```

**Success Response (HTTP 200 OK)**

```json
{
  "id": 1,
  "producto": "Motobomba Lite De 10Hp",
  "categoria": "Motobombas",
  "marca": "Power Flow",
  "empresa": "Acme"
}
```

#### 3. Create a new product (`POST /products`)

**Request Example**

```bash
curl --request POST \
  --url http://127.0.0.1:8000/products/ \
  --header 'Content-Type: application/json' \
  --data '{	
	"producto": "Caldera Corriente Fast",
	"categoria": "Calderas",
	"marca": "Cartago",
	"empresa": "Acme"	
}'
```

**Success Response (HTTP 200 OK)**

```json
{
  "success": true,
  "message": "Producto creado correctamente.",
  "id": 24
}
```

#### 4. Update the data of a specific product (`PUT /products/{id}`)

**Request Example**

```bash
curl --request PUT \
  --url http://127.0.0.1:8000/products/1 \
  --header 'Content-Type: application/json' \
  --data '{
	"producto": "Caldera Corriente Oregon",
	"categoria": "Calderas",
	"marca": "Cartamio",
	"empresa": "Acme"
}'
```

**Success Response (HTTP 200 OK)**

```json
{
  "success": true,
  "message": "Producto actualizado correctamente."
}
```

#### 5. Remove a specific product (`DELETE /products/{id}`)

**Request Example**

```bash
curl --request DELETE \
  --url http://127.0.0.1:8000/products/1
```

**Success Response (HTTP 200 OK)**

```json
{
  "success": true,
  "message": "Producto eliminado correctamente."
}
```
</details>

<details markdown="1">
<summary>Clients Endpoints</summary>

| Method | Route | Description | Body (JSON) |
|--------|-------|-------------|-------------|
| GET | `/clients` | Retrieve a list of all clients | N/A |
| GET | `/clients/{id}` | Retrieve details of a specific client | N/A |
| POST | `/clients` | Create a new client | `{ "cliente": "...", "industria": "..." }` |
| PUT | `/clients/{id}` | Update the data of a specific client | `{ "cliente": "...", "industria": "..." }` |
| DELETE | `/clients/{id}` | Remove a specific client | N/A |


#### 1. Retrieve a list of all clients (`GET /clients`)

**Request Example**

```bash
curl --request GET \
  --url http://127.0.0.1:8000/clients/
```

**Success Response (HTTP 200 OK)**

```json
[
  {
  	"id": 1,
  	"cliente": "Pesquera San Miguel",
  	"industria": "Pesca"
  },
  {
  	"id": 2,
  	"cliente": "Pesquera San Antonio",
  	"industria": "Pesca"
  }
]
```

#### 2. Retrieve details of a specific client (`GET /clients/{id}`)

**Request Example**

```bash
curl --request GET \
  --url http://127.0.0.1:8000/clients/1
```

**Success Response (HTTP 200 OK)**

```json
{
  "id": 1,
  "cliente": "Pesquera San Miguel",
  "industria": "Pesca"
}
```

#### 3. Create a new client (`POST /clients`)

**Request Example**

```bash
curl --request POST \
  --url http://127.0.0.1:8000/clients/ \
  --header 'Content-Type: application/json' \
  --data '{	
	"cliente": "Gold Investments Plasma",
	"industria": "Mineria"
}'
```

**Success Response (HTTP 200 OK)**

```json
{
  "success": true,
  "message": "Cliente creado correctamente.",
  "id": 13
}
```

#### 4. Update the data of a specific client (`PUT /clients/{id}`)

**Request Example**

```bash
curl --request PUT \
  --url http://127.0.0.1:8000/clients/1 \
  --header 'Content-Type: application/json' \
  --data '{	
	"cliente": "Golden Investments Fast",
	"industria": "Mineria"
}'
```

**Success Response (HTTP 200 OK)**

```json
{
  "success": true,
  "message": "Cliente actualizado correctamente."
}
```

#### 5. Remove a specific client (`DELETE /clients/{id}`)

**Request Example**

```bash
curl --request DELETE \
  --url http://127.0.0.1:8000/clients/1
```

**Success Response (HTTP 200 OK)**

```json
{
  "success": true,
  "message": "Cliente eliminado correctamente."
}
```
</details>

