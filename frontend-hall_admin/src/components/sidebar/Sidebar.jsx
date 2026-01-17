import React from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import './Sidebar.scss';
import { LuLayoutDashboard } from "react-icons/lu";
import { FaWpforms } from "react-icons/fa";
import { VscFeedback } from "react-icons/vsc";
import { VscAccount } from "react-icons/vsc";
import { RiLogoutBoxRLine } from "react-icons/ri";
import { FaRegEdit } from "react-icons/fa";
import { IoPersonAddOutline } from "react-icons/io5";


export default function Sidebar() {
    const navigate = useNavigate();

    const handleLogout = () => {
        // TODO: clear auth token or context here
        navigate('/login'); // redirect to login
    };

    return (
        <div className="sidebar">
            <div className="top">
                <h2 className="sidebar-title">HallMate</h2>
            </div>
            <div className="bottom">
                <ul>
                    <p className="title">Main</p>
                    <NavLink style={{ textDecoration: "none" }} to="/dashboard" className={({ isActive }) => isActive ? 'active' : ''}>
                        <li>
                            <LuLayoutDashboard className="icon" />
                            <span>Dashboard</span>
                        </li>
                    </NavLink>
                    <p className="title">My Work</p>
                     <NavLink style={{ textDecoration: "none" }} to="/add_new_student" className={({ isActive }) => isActive ? 'active' : ''}>
                        <li>
                            <IoPersonAddOutline className='icon'/>
                            <span>Add New Student</span>
                        </li>
                    </NavLink>
                    <NavLink style={{ textDecoration: "none" }} to="/appointments" className={({ isActive }) => isActive ? 'active' : ''}>
                        <li>
                            <FaWpforms className='icon'/>
                            <span>Dinning Applications</span>
                        </li>
                    </NavLink>
                    <NavLink style={{ textDecoration: "none" }} to="/feedbacks" className={({ isActive }) => isActive ? 'active' : ''}>
                        <li>
                            <VscFeedback className='icon'/>
                            <span>Feedbacks</span>
                        </li>
                    </NavLink>
                    <NavLink style={{ textDecoration: "none" }} to="/edit_hall" className={({ isActive }) => isActive ? 'active' : ''}>
                        <li>
                            <FaRegEdit className='icon'/>
                            <span>Edit Hall Info.</span>
                        </li>
                    </NavLink>
                    <p className="title">Account</p>
                    <NavLink style={{ textDecoration: "none" }} to="/profile" className={({ isActive }) => isActive ? 'active' : ''}>
                        <li>
                            <VscAccount className="icon" />
                            <span>Profile</span>
                        </li>
                    </NavLink>
                    <NavLink
                        style={{ textDecoration: "none" }}
                        to="/"
                        className={({ isActive }) => isActive ? 'active' : ''}
                        onClick={handleLogout}
                    >
                        <li>
                            <RiLogoutBoxRLine className="icon" />
                            <span>Logout</span>
                        </li>
                    </NavLink>
                </ul>
            </div>
        </div>
    );
}




