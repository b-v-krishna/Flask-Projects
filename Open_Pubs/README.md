<h2>PubFinder - Find Pubs Near You</h2>

PubFinder is a multi-page web application built with Streamlit that allows users to find pubs in a specific area and to locate the nearest pubs based on their location.

<h3>Data</h3>
The dataset used for this application contains information on pubs located in the United Kingdom. The dataset has the following columns:

<table>
  <thead>
    <tr>
      <th>Column Name</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>fsa_id</td>
      <td>Unique identifier for each pub</td>
    </tr>
    <tr>
      <td>name</td>
      <td>Name of the pub</td>
    </tr>
    <tr>
      <td>address</td>
      <td>Street address of the pub</td>
    </tr>
    <tr>
      <td>postcode</td>
      <td>Postcode of the pub</td>
    </tr>
    <tr>
      <td>easting</td>
      <td>Easting coordinate of the pub</td>
    </tr>
    <tr>
      <td>northing</td>
      <td>Northing coordinate of the pub</td>
    </tr>
    <tr>
      <td>latitude</td>
      <td>Latitude coordinate of the pub</td>
    </tr>
    <tr>
      <td>longitude</td>
      <td>Longitude coordinate of the pub</td>
    </tr>
    <tr>
      <td>local_authority</td>
      <td>Local authority in which the pub is located</td>
    </tr>
  </tbody>
</table>


<h3>Page 1 - Home Page</h3>
The home page displays some basic information and statistics about the dataset. Users can learn more about the dataset and its attributes from this page.

<h3>Page 2 - Pub Locations</h3>
The pub locations page allows users to search for pubs in a specific area by entering a postcode or local authority. The application displays the locations of all the pubs in the area chosen on a map.

<h3>Page 3 - Find the Nearest Pub</h3>
The find the nearest pub page allows users to find the nearest 5 pubs to their current location. Users can enter their latitude and longitude, and the application will use Euclidean distance to find the nearest pubs. The locations of the nearest pubs are displayed on a map.

<h3>APP LINK</h3>
👉 https://b-v-krishna-innomatics-intern-tasks-open-pubshome-0f6lom.streamlit.app/Nearest_pubs
