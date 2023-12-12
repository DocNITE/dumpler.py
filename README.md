# dumpler.py
PostgreSQL dumpler - for making dump reports and easy loading

# Usage
- For making archive dump:
`py d_make.py <-U username|-h ip_address|-p port> DB_NAME OUTPUT_FILE_NAME`

- For uploading dump on server:
`py d_load.py <-U username|-h ip_address|-p port> DB_NAME INPUT_ARCHIVE_NAME`

# d_init
It should be run for Windows users for initializing PATH for `psql` and (TODO: binary files)
