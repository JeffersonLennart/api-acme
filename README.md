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
DB_PORT=5433
DB_NAME=ACME 
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

</details>

