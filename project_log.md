10/4/26
Created the GitHub repository, added the initial Flask application and requirements file. Connected GitHub repository to Redner and successfully deployed the first version of the web app. URL is https://smart-it-help-desk.onrender.com Created Supabse project. Configured the project to use PostgreSQL for persistent cloud database storage, disabled Data API because flask will be connecting directly to PostgreSQL from server side. Enabled automatic Row Level Security as security measure. Created the tickets table in Supabase PostgreSQl with fields for: requestor information, issue description, category, priorirty, status, technician assignment, resolution notes, and date created. 
Connected the Flask application hosted on Render to the Supabase PostgreSQL database. The initial connection failed because of an IPv6 compatibility issue. I fixed this by switching to the Supabase Session Pooler connection string. The \test-db route confirmed all was working 

10/7/26
Added the technician dashboard and ticket editing function. IT staff can view submitted tickets, and update category, priority, status, technician assignment, and resolution notes. Tested and it works properly. 
