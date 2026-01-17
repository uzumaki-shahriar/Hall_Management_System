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
import { BsPeople } from "react-icons/bs";
import { MdOutlineMeetingRoom } from "react-icons/md";


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
                    <p className="title">Overview</p>
                    <NavLink style={{ textDecoration: "none" }} to="/dashboard" className={({ isActive }) => isActive ? 'active' : ''}>
                        <li>
                            <LuLayoutDashboard className="icon" />
                            <span>Dashboard</span>
                        </li>
                    </NavLink>
                    <NavLink style={{ textDecoration: "none" }} to="/student-list" className={({ isActive }) => isActive ? 'active' : ''}>
                        <li>
                            <BsPeople className="icon" />
                            <span>Student List</span>
                        </li>
                    </NavLink>
                    {/* <NavLink style={{ textDecoration: "none" }} to="/room-list" className={({ isActive }) => isActive ? 'active' : ''}>
                        <li>
                            <MdOutlineMeetingRoom className="icon" />
                            <span>Room List</span>
                        </li>
                    </NavLink> */}
                    <p className="title">Management</p>
                     <NavLink style={{ textDecoration: "none" }} to="/add-student" className={({ isActive }) => isActive ? 'active' : ''}>
                        <li>
                            <IoPersonAddOutline className='icon'/>
                            <span>Add New Student</span>
                        </li>
                    </NavLink>
                    <NavLink style={{ textDecoration: "none" }} to="/dinning-applications" className={({ isActive }) => isActive ? 'active' : ''}>
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
                    {/* <NavLink style={{ textDecoration: "none" }} to="/edit-hall" className={({ isActive }) => isActive ? 'active' : ''}>
                        <li>
                            <FaRegEdit className='icon'/>
                            <span>Edit Hall Details</span>
                        </li>
                    </NavLink> */}
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




