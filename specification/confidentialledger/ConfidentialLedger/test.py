from azure.security.confidentialledger import LedgerClient

client = LedgerClient(endpoint="http://localhost")

client.get_current_ledger_entry().transaction_id