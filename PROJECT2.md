Project Specifications

This updated version of the server will feature RPC logic so that clients are able to invoke functions of a remote server, in particular ADD(a, b), SUBTRACT(a, b), MULTIPLY(a, b), and MAX(a, b).

## TCP Issue
TCP streams bytes between client and server, so there is concern of potentially a mix of instructions (like an ADD, then a SUBTRACT jumbled together). As a result we will have a newline (\n) to enforce boundary.

## Request Format
The request format will look like (PROCEDURE, PARAM1, PARAM2) for the client to send to the server, as this is the information needed for the server to choose a function and choose parameters.

## Response format
The response format that the server will use when sending back to the client will look like (COMPLETE, <output>). If there is an error, it will look like (ERR, <reason>).

## Non-integer parameters
We can only use integers for the parameters in this project. If a string or non-integer is used, we will raise an exception.