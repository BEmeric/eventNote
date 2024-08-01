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

USAGE:
   python client.py [add|list|remove] [arguments...]

   ## To add an event run the following code example:
      python client.py add <start> <tag> [stop]
      Example:
         python client.py add '27-09-2024' 'Mariage' '27-09-2024'

   ## To display all events saved in database run the following code examle:
      python client.py list

   ## To delete an event run the following code example:
      python client.py remove <event_id>
      Example:
         python client.py remove 66ab553e269bb7424551a561

