import React, { useEffect, useState } from 'react';

const API_BASE_URL = 'https://super-duper-carnival-q9grvg57g7fv7v-8000.app.github.dev/api/activities/';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch(`${API_BASE_URL}`)
      .then(response => response.json())
      .then(data => setActivities(data))
      .catch(error => console.error('Error fetching activities:', error));
  }, []);

  return (
    <div>
      <h1 className="display-4">Activities</h1>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Activity Type</th>
            <th>Duration</th>
          </tr>
        </thead>
        <tbody>
          {activities.map(activity => (
            <tr key={activity._id}>
              <td>{activity.activity_type}</td>
              <td>{activity.duration}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Activities;
