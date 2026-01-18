import { useState, useEffect } from "react";

export default function TypingEffect({ text, speed = 100, cls }) {
  const [displayed, setDisplayed] = useState("");

  useEffect(() => {
    let index = 0;
    const interval = setInterval(() => {
      if (index < text.length-1) {
        setDisplayed((prev) => prev + text[index]);
        index++;
      } else {
        clearInterval(interval);
      }
    }, speed);

    return () => clearInterval(interval);
  }, [text, speed]);

  return <h2 className={cls}>{displayed}</h2>;
}
