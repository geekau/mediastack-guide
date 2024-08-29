# Portainer - Docker GUI

# Collective Docker Compose Installation

## Heading One

!!! Danger "Warning: &nbsp; &nbsp; &nbsp; Page Under Development"

    This page is still under development and may not have accurate information, and should be considered incomplete / inaccurate until this notice is removed.



Basic intro to Docker... embed Docker intro video etc..

Provide steps to install Docker on Windows, Linux, MacOS, Synology NAS and other hosts where possible


## Heading Two

## Heading Three






https://www.synoforum.com/resources/ultimate-starter-docker-portainer-portainer-agents-and-auto-updating-everything-with-watchtower.183/




  
**Deployment via Portainer GUI on Synology / Linux / Windows:**  
  
Deploying the docker compose media stack via Portainer, will be exactly the same on Synology / Linux / Windows, assuming Portainer has already been installed on the Docker Host, and the file paths have been updated in the ENV file for each respective Operating System.  
  
\- Open Portainer at: [https://localhost:9443](https://localhost:9443)  
  
\- Connect to your local Docker environment in the Portainer portal, then select "Stack" in the left menu, then "Add Stack" on the right side of the page.  
  
\- Stack Name: "media\_stack" <-- Must be lowercase and only use underscores or hyphens  
  
\- Select: "Upload" -- Press "Upload File", then select the "docker-compose-mediastack.yaml" file and save.  
  
\- Select: "Load Variables From .ENV File", then select the "docker-compose-mediastack.env" file and save.  
  
\- "Enable access control": Disable this if you do not have multiple users in Portainer (Optional)  
  
\- Select "Deploy The Stack".  
  
\- Go make a coffee if this is the first time downloading the images, it will take a few minutes.  
  
  
**Configuration Persistence for Docker Containers:**  
  
Great care has been taken to make sure all of the configuration settings in each of the docker containers, have been mapped into their individual folders in the **FOLDER\_FOR\_DOCKER\_DATA** location; if you check these folders, they are now full and contained the configuration of each application.  
  
This means you can completely delete all Docker containers, Docker images, uninstall the Docker application, and then rebuild everything again, and as long as you use the same .YAML and .ENV files with their settings, then your whole media stack will be rebuilt and operate exactly how is was running prior to you stopping it.  
  
This also allows you to easily migrate to new servers / host computers, fire up the docker compose media stack, and be up and running again as soon as the docker images have been downloaded.  
  
Back up the **OLDER\_FOR\_DOCKER\_DATA** sub-folders to save you rebuilding after a system failure / migration.  
  
  
**Test Redeploying Your Docker Compose Media Stack:**  
  
Now is the best time to validate your docker compose configuration, open some of the applications using the links at the very top to make sure they're up and running, then:  
  
\- If you used docker compose command at the terminal / PowerShell, go to the .ENV file, then make the following change, and run the docker compose up command again.  
  

Code:

    TP_THEME=dracula

  
\- If you used Portainer, go to "Stacks" -- "media\_stack" -- "Editor", find "TP\_THEME" down the bottom in the variables, and change the value to "dracula", then select "Actions: Update The Stack".  
  
Once you have redeployed the docker compose via the terminal / Portainer, go back into the applications using the links up the top again, and check that your chance has occurred.  
  
**NOTE:** The TP\_THEME is used in all docker containers, except Jellyfin, Jellyseerr, and Whisparr.  
  



