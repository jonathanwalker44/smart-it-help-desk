10/4/26
Created the GitHub repository, added the initial Flask application and requirements file. Connected GitHub repository to Redner and successfully deployed the first version of the web app. URL is https://smart-it-help-desk.onrender.com Created Supabse project. Configured the project to use PostgreSQL for persistent cloud database storage, disabled Data API because flask will be connecting directly to PostgreSQL from server side. Enabled automatic Row Level Security as security measure. Created the tickets table in Supabase PostgreSQl with fields for: requestor information, issue description, category, priorirty, status, technician assignment, resolution notes, and date created. 
Connected the Flask application hosted on Render to the Supabase PostgreSQL database. The initial connection failed because of an IPv6 compatibility issue. I fixed this by switching to the Supabase Session Pooler connection string. The \test-db route confirmed all was working 

10/7/26
Added the technician dashboard and ticket editing function. IT staff can view submitted tickets, and update category, priority, status, technician assignment, and resolution notes. Tested and it works properly. Added a login page to the application. Credentials are securely stored as Render environment variable. Login was successful and redirects authorized user to tech dashboard. Had error with login screen originially, this was rectified by moving login.html to its proper place under templates.

10/11/2026
Updated application so that tech dashboard and ticketing editing pages now require authentication. If user is not logged in they will be redirected to the login page. Ticket submission remains public. Added search functionality to the technician dashboard. This allows staff to search tickets by requestor, email, issue description, category, priority, status, and assigned technician. 
Added simple automated ticket triage. This uses keywords in the submitted issue description to automatically assign category and priority for common issues. All tested and working.

10/12/2026
Continued development and refinement of the IT Help Desk Application. I added dashboard summary statistics which show total tickets, open tickets, in-progress tickets, resolved tickets, and high-priority tickets. I tested to make sure that these work properly and match the tickets that are currently there.
I added the logout functionality, so that techs can securely end their sessions. Tested and confirmed that protected pages will redirect back to the login page after logged out.
Improved the tech dashboard by using Bootstrap. The dashboard now has a professional looking navigation bar, statistics card, a cleaner search bar, responsive ticket table, priority/status badges, cleanly formatted timestamps, create ticket function (so techs can create a ticket without going to the public page), and just an improved layout in general.
I updated the public ticket submission page, technician login page, and ticket-editing page with consistent Bootstrap styling, to ensure a clean, professional, and easy to navigate layout.
I made a ticket submission confirmation message, which also allows the user to click to submit another ticket as well.
Confirmed that the application continues to operate as intended after changes were made. 
