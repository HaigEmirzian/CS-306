# S/KEY One-Time Password

(Server) Key Generation

         i) For random key K, generate H1(K), H2(K), ... , Hn(K), Hn+1(K).

         ii)Send Hn(K), Hn-1(K), ..., H1(K) (in reverse order) to the Client and delete everything except Server_Key = Hn+1(K) from the server.

(Client) Sends Client_Key = Hi(n) for i from n to 1 sequentially.

         (Server)Authentication

                 i)  For Client_Key received from the client, 

                          if(Server_Key == H(Client_Key):

                                   print(authenticated) and update Server_Key = Client_Key

                           Otherwise

                                    print(not authenticated)
