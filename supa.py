import os
from supabase import create_client

url = "https://ksamafybltajrgrhmgzw.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtzYW1hZnlibHRhanJncmhtZ3p3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDIzNDgzOTIsImV4cCI6MjAxNzkyNDM5Mn0.MIBSPCNyXHc45nmKneZewUzDDRU4mh9-NyUKI_beR50"

supabase = create_client(url, key)

datas = supabase.table("data").select("*").execute()
print(datas)