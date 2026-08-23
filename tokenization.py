import tiktoken
text = input("Enter text: ")
encodings = ["r50k_base", "p50k_base", "cl100k_base", "o200k_base"]
for enc_name in encodings:
    print("\n" + "="*80)
    print("Tokenizer:", enc_name)
    encoding = tiktoken.get_encoding(enc_name)
    token_ids = encoding.encode(text)
    tokens = []
    for t in token_ids:
        tok = encoding.decode([t])
        tokens.append(tok)
    print("\nOriginal Text: ", text)
    print("\nTokenization: ", tokens)
    print("\nToken IDs: ", token_ids)
    print("\nTotal Tokens: ", len(token_ids))
    print("\nDecoded Text: ",encoding.decode(token_ids))