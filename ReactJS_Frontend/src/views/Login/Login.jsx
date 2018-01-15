import React, { Component } from 'react';
import App from 'containers/App/App.jsx';
import UserProfile from 'views/UserProfile/UserProfile';
import appRoutes from 'routes/app.jsx';

class Login extends Component{

  constructor() {
    super();
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick(e) {
    e.preventDefault();
    this.props.history.push('/user');
  }

	render(){

		return(
                <div className="cont">   
                  <div className="demo">
                    <div className="login">
                      <div className="login__check"></div>
                         <div className="login__form">
                           <div className="login__row">
                             <svg className="login__icon name svg-icon" viewBox="0 0 20 26">
                               <path d="M0,20 a10,8 0 0,1 20,0z M10,0 a4,4 0 0,1 0,8 a4,4 0 0,1 0,-8" />
                             </svg>
                             <input type="text" className="login__input name" placeholder="Username"/>
                          </div>
                           <div className="login__row">
                             <svg className="login__icon pass svg-icon" viewBox="0 0 20 26">
                               <path d="M0,20 20,20 20,8 0,8z M10,13 10,16z M4,8 a6,8 0 0,1 12,0" />
                             </svg>
                             <input type="password" className="login__input pass" placeholder="Password"/>
                          </div>
                          <button type="button" onClick={this.handleClick} className="login__submit">Sign in</button>
                          <p className="login__signup">Don't have an account? &nbsp;<a>Sign up</a></p>
                         </div>
                      </div>
                    </div>
               </div> );
	        }
        }

export default Login;