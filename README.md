# eventNote
This Api allow to create, display and delete events.
So the Api has 3 endpoints:
   * /add_event
   * /list_events
   * /remove_events
  
An event has 3 informations:
   - start(date format)
   - stop (date format but optional)
   - tag (name of event)

### Structure of project:
```
eventNote
├── client.py
├── README.md
├── server.py
├── test_ConnectionToMongoDB.py
└── templates
    └── index.html
```

### Database architecture:
Atlas MongoDB is used here to manage event Data.
Click in this link to access database (https://account.mongodb.com/account/login?signedOut=true)
- login : emericbankole@gmail.com
- pwd   : ***************** (A envoyer par mail)

```
DataBase's name -> "db_events"
        └── Collection's name -> "collection_event"
```
  
### USAGE:
  ### 0. To check the connection to your Mongo DataBase run this following command:
      python test_ConnectionToMongoDB.py
      
  ### 1. Run the server in a terminal
      python server.py
      Use this Url http://127.0.0.1:5000 to check if the server is ready to be used.
  ### 2. In a another terminal run CLI client to manage events
       python client.py [add|list|remove] [arguments...]

  ### 3. To add an event run the following code example:
      python client.py add <start> <tag> [stop]
      Example:
         python client.py add '27-09-2024' 'Mariage' '27-09-2024'

  ### 4. To display all events saved in database run the following code examle:
      python client.py list

  ### 5. To delete an event run the following code example:
      python client.py remove <event_id>
      Example:
         python client.py remove 66ab553e269bb7424551a561

