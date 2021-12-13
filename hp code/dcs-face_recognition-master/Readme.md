Running the script <br />

Python version: 3

Install the dependencies 
`pip install -r requirements.txt`

Execute the script
`python dcs_video_face_detection.py <video_file_path>`

_**It is recommended to just create a docker image using provided Dockerfile,
as it will be much cleaner and eliminate number of issue that may come
with dependency installation :-**_

#### Executing script better way</br>
After cloning the repository build the image: <br />
 `docker build -t <image_name> .`

Starting the container and executing the script inside the container [replace the \<placeholders\>]<br />
 `docker run --rm -it -v <path_to_this_repo_where_it's_cloned>:/usr/workspace --name <container_name> <image_name_as given in previous step> python dcs_video_face_detection.py <video_file_path>`<br/>
 <br />Note, the container provides just the envriornment for the script to execute, and 
 thus the '-v' option we mount the cloned codebase into the
 working directory of the container. The command that is getting executed inside 
 the container is 'python dcs_video_face_detection.py <video_file_path>'  
 
 
