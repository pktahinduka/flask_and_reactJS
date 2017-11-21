import React from 'react';

const UsersList = (props) => {
  return (
    <div>
      {
        props.users.map((user) => {
          return (
            <h4
              key={user.id}
              className="well"
            >{user.username}<br/>
            <h5>{user.email}</h5>
            </h4>
            
          )
        })
      }
    </div>
  )
};

export default UsersList;
