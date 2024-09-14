# Documentation

1) **Frontend Development**
  - Opened the terminal. Changed the directory to Desktop
  - Went to Vite ( https://vitejs.dev/guide/ ). Typed npm create vite@latest command
  - Select framework: React, Select a variant: JavaScript
  - Run the following commands: cd rapidious and npm install. Npm install installs dependencies 
  - Once that is done, type code .
  - First step is to setup tailwind. Went to Tailwindcss website, under Frameworks Guide, went to Vite. Copied npm install -D tailwindcss postcss autoprefixer (this installs 3 dependencies, postcss, autoprefixer,   tailwind)
  - Then ran this command: npx tailwindcss init -p 
  content: [
  
     "./index.html",
  
     "./src/**/*.{js,ts,jsx,tsx}",
  
   ], this code is replaced in place of content in tailwind.config.js file in vs code
  @tailwind base;
  @tailwind components;
  @tailwind utilities; this code is replaced in the index.css file present in the scr folder in vs code
  - Npm run dev in the vs code terminal to open the app
  - Delete App.css, in App.jsx, type this command: rafce
  - Typed this into the return: 
  <>
  <Navbar/>
  </>
  - Created a folder in src, called components, and another folder in that called Navbar. Created a file called Navbar.jsx in it.
  - After creating the folder, the code present in the repository was used to build a website.
  - After that was done, I pushed the code into the repository by typing the following commands:
  git init
  git commit -m "first commit"
  git remote add origin https://github.com/KasinaHarshita/Rapidious.git
  git push -u origin main
  - Then I modified the code later and the commits were to be made in the repository which were done using the following:
  git add .
  git commit -m "initial changes"
  git push origin main


2) **OpenSearch Installation and Setup**
  - Installed Docker Desktop ( https://www.docker.com/products/docker-desktop/ )
  - Installed OpenSearch with Docker Compose ( https://opensearch.org/downloads.html )
  - Download docker-compose.yml file into the desired directory
  - Before installing, setting the OPENSEARCH_INITIAL_ADMIN_PASSWORD to the desired password. It can be done in 2 ways. 
  - Using set OPENSEARCH_INITIAL_ADMIN_PASSWORD = password
  - Making changes directly in docker-compose.yml file.
  - Open a terminal in location where the docker-compose.yml file was saved and type in docker-compose up command
  - Initially I had faced challenges with localhost 5601. I tried checking the logs of opensearch-node1, openearch-node2, opensearch-dashboards using the command: docker logs opensearch-node1, opensearch-node2,     opensearch-dashboards. Upon using Google and ChatGPT, I was able to rectife the error.
  - Then navigate to http://localhost:5601/ for OpenSearch Dashboards
  - Login with the default username (admin) and password (<custom-admin-password>)
  - I tried to curl localhost 9200 but faced errors with connecting to the port. Watched YouTube video on how to curl localhost 9200.
  - I cloned the OpenSearch Repository onto my GitHub account and then I ran the following commands:
  git clone https://github.com/KasinaHarshita/OpenSearch.git
  cd OpenSearch
  ./gradlew assemble
  ./gradlew run - During this command process, I had faced an issue and when Googled, told me to do the following:
  ./gradlew precommit
  ./gradlew run - I faced the same error again
  - Then I checked the port status using this command: netstat -aon | findstr :9200. And the port was being listened by Docker and WSL.
  - After a few hours, I ran the following commands again:
  ./gradlew run and netstat -aon | findstr :9200
  - Checked the logs of opensearch-node1, opensearch-node2 and opensearch-dashboards. 
  - At the end, I was able to navigate to http://localhost:9200/ 
  - Local host 9200 contained the following content:
  {
    "name" : "runTask-0",
    "cluster_name" : "runTask",
    "cluster_uuid" : "h0gxeu2_Q5m7b_GVv3u-tg",
    "version" : {
      "distribution" : "opensearch",
      "number" : "3.0.0-SNAPSHOT",
      "build_type" : "zip",
      "build_hash" : "19aedcd896c060db9028b2055e03d7f3e239e59c",
      "build_date" : "2024-09-10T17:52:28.327629200Z",
      "build_snapshot" : true,
      "lucene_version" : "9.12.0",
      "minimum_wire_compatibility_version" : "2.18.0",
      "minimum_index_compatibility_version" : "2.0.0"
    },
    "tagline" : "The OpenSearch Project: https://opensearch.org/"
  }


3) **Backend Development**
   - For this, I have decided to go with FastAPI due to its efficiency and speed for building RESTful APIs. FastAPI is modern, asynchronous, and has excellent performance, making it well-suited for handling both     small and large-scale APIs. It also has great integration capabilities with search engines like OpenSearch.
   - For this, I have installed PostgreSQL to store the data. I installed the software but the psql.exe file was missing in my bin folder so I couldn't proceed further.
   - Then I proceeded with FastAPI and ran the following command in the command prompt pip install fastapi uvicorn opensearch-py
   - I made a folder which consists of the following files: main.py, routes.py, models.py, databse.py
   - Then I typed the codes into the files which can be seen on the Repository
