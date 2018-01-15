
import UserProfile from 'views/UserProfile/UserProfile';
import Login from 'views/Login/Login';

const appRoutes = [
    { path: "/user", name: "User Profile", icon: "pe-7s-user", component: UserProfile },
    { path: "/login", name: "User Login", icon: "pe-7s-user", component: Login },
    { redirect: true, path: "/", to: "/login", name: "User Login" }
];

export default appRoutes;