Steps:

1. Upload Files

2. Apply Patterns

3. Finalize Categories

4. Review

Tables:

PendingBatch:

- status:
  - open: can have files attached
  - loaded: files have been parsed
  - final: all transactions have categories
- user

Batch:

- completion date
- user

ImportFileUpload:

- name
- location
- batch_id
- import_def_id

PendingTransaction:

- batch_id

- POST /batches - open batch - same response as get
- GET /batches/{id}
  - id
  - status
  - files: {id, name, import_def_id?, status, tran_count?}[]
  - transactions: {id, date, amount, summary, category_id, account_id}[]
  - category_patterns: {id, pattern, category_id, save}[]

- POST /batches/{id}/files
  - request: {file_name, file_contents}
  - response: {id, name, import_def_id?, status, tran_count?}[]

- PATCH /batches/{id}/files{id}
  - request: {import_def_id}
  - response: {id, name, import_def_id?, status, tran_count?}[]

- DELETE /batches/{id}/files/{id}

- POST /batches/{id}/loadfiles
  - no body
  - response: {id, date, amount, summary, category_id, account_id}[]

- POST /batches/{id}/categorypatterns
  - request: {pattern, category, save}
  - response: {id, {transaction_id, category_id}[]}

- DELETE /batches/{id}/categorypatterns/{id}
  - response: {id, {transaction_id, category_id}[]}

- PATCH /batches/{id}/transactions{id}
  - request: { transaction_category_id }

- POST /batches/{id}/submit
