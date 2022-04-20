# PhenotyposDB/InfrafrontierGR

### PhenotyposDB Development, Design and Features

The current database architecture is built to support all phenotyping protocols (SOPS) designed by BSRC Alexander Fleming researchers and Phenotyping Services Unit members. To date we have developed more than 40 SOPs on monitoring procedures/assays in the areas of microCT imaging, ultrasound Imaging, optical/X-ray imaging, endoscopy imaging, FACS, Histopathology, Biochemical, Hematology and Clinical Analyses, and Proteomics. 25 of the aforementioned assays participate in 7 phenotyping pipelines that have been developed to monitor disease models and provide a protocol guide for disease areas screened. The data are mainly xlsx or csv files with a specific format. The user through the platform uploads the raw data of the experiment as well as the xlsx, csv files with the general information of the experiment (environmental conditions, mice information, etc.) and can also store other data such as images.

### Database Design and Implementation

#### i.      User Types and privileges
PhenotyposDB supports 4 different levels of security for users which include: scientific staff, scientists in charge, clients and visitors (privilege depicted in Figure 1 below). Visitors (“Clients”) only acquire access to specific data following permission granted by a user of higher level (eg. Administrator of Scientist in charge). “Lab members” have access to assay data of their own Lab/Facility only. “Scientists in charge” monitor pipelines and supervise the experimental procedures within their pipelines.

#### ii. Implementation & Technology
The backend section of the framework manages the data and executes the analysis pipelines. Data are stored on a file server using NGINX proxy server and PostgreSQL database. Access to the data and analysis pipelines is managed through RESTful API of the Django application framework. Django REST framework contains needed tools for implementation of the RESTful API such as serializers, pagination, permissions, etc.
On the client (web browser) side, the framework includes the application of data management (upload file, store to database) and the interactive assay/pipeline analysis (data visualization, export reports). The front-end is implemented using JavaScript, HTML5 and CSS3. For the data visualization we used some of the following JavaScript libraries: Bootstrap, version 4.2.0, (http://getbootstrap.com/); c3, version 0.4.10, (http://c3js.org/); d3, version 3.5.5, (https://d3js.org/); report-labs, JavaScript Datatables v1.11.3, jQuery UI v1.12.1, Highcharts.

#### iii. Data deposition
Raw data of a single assay or an entire pipeline may be uploaded, via an xlsx or csv file with a specific format based on each measurement type. Depending on a specific field in the submission form (field “type”) the particular experimental data are linked to the respective supported SOP  and to an existing experiment pipeline. Data can only be uploaded by the user type ‘Scientific staff’ or ‘lab members’. 
