# DISCAILMER  i used AI to generate the code, template, tests, and readme. Python, being a very large language, is not in it's entirety familiar to me. 
# Thus, my approach was to use the AI fro suggestions, libraries, structure and code. I then checked the code and the libraris status, then made the necessary changes to make it work, leveraging my knowledge of Python, SWE and good old Google.
# i run tests, checked output integrity, and made sure the code was readable and maintainable.

# CSV Transformer Tool

This is a production-ready Python CLI application to transform CSV files by reordering columns and applying transformations to specific fields.

## ✅ Features

- Input and output in **CSV** format.
- Output can have **custom column order**.
- **Three built-in transformations**:
  - `uuid_seq`: Convert UUIDs into a unique integer sequence.
  - `redact`: Redact sensitive data into fake but similar-looking values.
  - `date_fmt`: Convert timestamps into a standard `YYYY-MM-DD` or custom format with timezone adjustments.

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the CLI

### 🔧 Basic Syntax

```bash
python cli.py <input.csv> <output.csv> --columns col1,col2,... --transform col1=transform,col2=transform [--tz-source=...] [--tz-target=...] [--date-format=...]
```

---

## 🧪 Sample Input (`user_sample.csv`)

```csv
user_id,manager_id,name,email_address,start_date,last_login
EFEABEA5-981B-4E45-8F13-425C456BF7F6,CDD3AA5D-F8BF-40BB-B220-36147E1B75F7,Ashley Hernandez,ashley.hernandez@live.com,2025-Mar-01,2025-03-23 16:54:43 CET
```

---

## 🧭 Examples

### 1. 🔀 Reorder columns only

```bash
python cli.py user_sample.csv out1.csv --columns name,email_address,user_id
```

🟠 Output:

```csv
name,email_address,user_id
Ashley Hernandez,ashley.hernandez@live.com,EFEABEA5-981B-4E45-8F13-425C456BF7F6
```

---

### 2. 🔐 Redact sensitive info

```bash
python cli.py user_sample.csv out2.csv --columns name,email_address --transform name=redact,email_address=redact
```

🟠 Output:

```csv
name,email_address
Svbkef Pvgkjjfef,ashmbi.uebmxjix@nrht.eqb
```

---

### 3. 🔢 Convert UUIDs to unique integers

```bash
python cli.py user_sample.csv out3.csv --columns user_id,manager_id --transform user_id=uuid_seq,manager_id=uuid_seq
```

🟠 Output:

```csv
user_id,manager_id
1,2
```

---

### 4. 🕓 Convert timezones & format dates

```bash
python cli.py user_sample.csv out4.csv --columns last_login --transform last_login=date_fmt --tz-source=CET --tz-target=UTC --date-format="%Y-%m-%d %H:%M:%S"
```

🟠 Output:

```csv
last_login
2025-03-23 15:54:43
```

---

### 5. 🦪 Combine everything

```bash
python cli.py user_sample.csv out5.csv --columns user_id,email_address,last_login --transform user_id=uuid_seq,email_address=redact,last_login=date_fmt --tz-source=CET --tz-target=UTC --date-format="%Y-%m-%d %H:%M:%S"
```

🟠 Output:

```csv
user_id,email_address,last_login
1,hxipbw.abplppdf@lmno.apr,2025-03-23 15:54:43
```

---

## 🧑‍💻 Development

Run tests using:

```bash
pytest tests/
```

---

## 📁 Project Structure

```
.
├── cli.py
├── config.py
├── main.py
├── reader.py
├── writer.py
├── tests/
│   ├── ...
├── transformers/
│   ├── base.py
│   ├── uuid_seq.py
│   ├── redact.py
│   ├── date_fmt.py
│   └── __init__.py
├── requirements.txt
├── tests/
├── user_sample.csv
└── README.md
```




Release input files with about 1 million lines and make use of the available machine resources by utilizing the strategies below:

Streaming I/O (the current approach): We already read and write CSV row-by-row without loading the entire file into memory, ensuring low peak RAM usage even for mega-gigabyte files.

Chunked Processing: If the transformations become CPU- or memory-intensive, process rows in configurable chunks tp balance memory use and throughput.
Parallel Transformation Pipelines: Use Python’s multiprocessing or joblib to distribute independent row transformations across multiple CPU cores. For example:
Read chunks of rows in the main process.
Dispatch each chunk to a worker pool to apply transformations in parallel.

Parallel Transformation Pipelines: Use Python's multiprocessing or joblib to distribute independent row transformations over multiple CPU cores easily. For example: The main process reads chunks of rows. Each chunk is dispatched to a worker pool to apply transformations in parallel. Results are collected and written according to the order or via chunk numbering. Asynchronous I/O: In cases where reading/writing is a bottleneck (e.g., network-mounted storage), instead of using synchronous file I/O, use asynchronous file I/O (via aiofiles) to which extra CPU time is devoted to the disk operations without the need of the transforming code.

Batch UUID Mapping && & Caching Baptism For very large datasets with repeated UUIDs, it is already using an in-memory cache (e.g., a dict) efficient. If UUID space is huge, consider a disk-backed or LRU-cached store (e.g., SQLite or shelve) to avoid unbounded memory growth.

Profiling Systems "&" Optimization: Use tools like cProfile or py-spy to identify hotspots (e.g., date parsing) and optimize them:

Replace dateutil parsing with faster specialized parsers (e.g., ciso8601) if needed.

Precompile regular expressions or transformers .