import tiktoken

# Using the get_encoding function from tiktoken module
enc = tiktoken.get_encoding("cl100k_base")
assert enc.decode(enc.encode("hello world")) == "hello world"

# Using the encoding_for_model function from tiktoken module
enc = tiktoken.encoding_for_model("gpt-4")