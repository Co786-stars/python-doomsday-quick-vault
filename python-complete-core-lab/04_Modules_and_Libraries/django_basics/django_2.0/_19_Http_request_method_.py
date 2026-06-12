"""
In this module we are discussing:
HTTP request methods (GET and POST),
their characteristics, limitations, and best practices.
"""

# ------------------------------------------------------------------------
# 1. INTRODUCTION TO HTTP METHODS
# ------------------------------------------------------------------------
# - HTTP defines methods to send data between client and server.
# - The two most common methods are GET and POST.
# - Each has its own use cases, advantages, and limitations.

# ------------------------------------------------------------------------
# 2. GET METHOD
# ------------------------------------------------------------------------
# - The GET method sends encoded user information appended to the page request.
# - Data is added to the URL after a '?' and separated by '&' characters.
# - Example: http://example.com/page?name=John&age=24
# - Characteristics:
#     * Limited length (commonly around 2048 characters depending on browser/server).
#     * Data visible in the URL → not secure for sensitive information.
#     * Should NEVER be used for passwords or confidential data.
#     * Cannot send binary data (images, documents).
# - Best use cases:
#     * Retrieving data.
#     * Bookmarkable/searchable URLs.
#     * Non-sensitive queries.

# ------------------------------------------------------------------------
# 3. POST METHOD
# ------------------------------------------------------------------------
# - The POST method transfers information via the HTTP request body.
# - Data is encoded similarly to GET but placed in the request header/body.
# - Characteristics:
#     * No practical length limit (can send large amounts of data).
#     * Safer for sensitive information (not exposed in URL).
#     * Can send binary data (files, images, documents).
# - Best use cases:
#     * Submitting forms with sensitive data (login, signup).
#     * Uploading files.
#     * Complex data transactions.

# ------------------------------------------------------------------------
# 4. DEPENDING UPON HTTP METHOD
# ------------------------------------------------------------------------
# - Choose GET when:
#     * You want quick, bookmarkable queries.
#     * Data is not sensitive.
# - Choose POST when:
#     * You need to send secure or large data.
#     * You are uploading files or performing transactions.

# ------------------------------------------------------------------------
# 5. SUMMARY
# ------------------------------------------------------------------------
# - GET → appends data to URL, limited, insecure for sensitive info, no binary.
# - POST → sends data in body, secure, supports large/binary data.
# - Always select the method based on the type of data and security needs.
# ------------------------------------------------------------------------

