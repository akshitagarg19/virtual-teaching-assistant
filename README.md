# Virtual TA for TDS Jan 2025

A virtual assistant that answers student questions based on course material and Discourse discussions.

## Endpoint

POST `/api/`

```json
{
  "question": "Why do we use a tokenizer in GA5?",
  "image": "BASE64_STRING_OPTIONAL"
}
