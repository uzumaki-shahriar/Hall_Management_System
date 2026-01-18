import React from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import './Sidebar.scss';
import { LuLayoutDashboard } from "react-icons/lu";
import { GiPayMoney } from "react-icons/gi";
import { VscFeedback } from "react-icons/vsc";
import { VscAccount } from "react-icons/vsc";
import { RiLogoutBoxRLine } from "react-icons/ri";
import { GiForkKnifeSpoon } from "react-icons/gi";


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
                    <NavLink style={{ textDecoration: "none" }} to="/payment" className={({ isActive }) => isActive ? 'active' : ''}>
                        <li>
                            <GiPayMoney className='icon' />
                            <span>Payment</span>
                        </li>
                    </NavLink>
                    <NavLink style={{ textDecoration: "none" }} to="/write-feedback" className={({ isActive }) => isActive ? 'active' : ''}>
                        <li>
                            <VscFeedback className='icon' />
                            <span>Write Feedback</span>
                        </li>
                    </NavLink>
                    <p className="title">Management</p>
                    <NavLink style={{ textDecoration: "none" }} to="/dining-mangement" className={({ isActive }) => isActive ? 'active' : ''}>
                        <li>
                            <GiForkKnifeSpoon className='icon' />
                            <span>Dining Mangement</span>
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




