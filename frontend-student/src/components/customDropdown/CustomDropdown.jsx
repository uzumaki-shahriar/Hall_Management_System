import { useState, useRef, useEffect } from "react";
import './CustomDropdown.scss';

const CustomDropdown = ({ options, value, onChange, placeholder }) => {
    const [open, setOpen] = useState(false);
    const ref = useRef(null);

    useEffect(() => {
        const close = e => !ref.current.contains(e.target) && setOpen(false);
        document.addEventListener("mousedown", close);
        return () => document.removeEventListener("mousedown", close);
    }, []);

    return (
        <div className="dropdown" ref={ref}>
            <div
                className={`dropdown-selected ${open ? "active" : ""}`}
                onClick={() => setOpen(!open)}
            >
                {value || placeholder}
            </div>

            {open && (
                <div className="dropdown-menu">
                    {options.map(opt => (
                        <div
                            key={opt}
                            className="dropdown-option"
                            onClick={() => {
                                onChange(opt);
                                setOpen(false);
                            }}
                        >
                            {opt}
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};

export default CustomDropdown;
