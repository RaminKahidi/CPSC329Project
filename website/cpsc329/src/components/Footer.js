import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faFacebook,
  faInstagram,
  faGoogle,
} from "@fortawesome/free-brands-svg-icons";

const Footer = () => {
  return (
    <footer>
      <div id="socials">
        <h2>Social Media</h2>
        <ul>
          <li>
            <a
              href="https://www.facebook.com/universityofcalgary/"
              target="_blank"
            >
              <FontAwesomeIcon icon={faFacebook} />
            </a>
          </li>
          <li>
            <a href="https://www.instagram.com/ucalgary/?hl=en" target="_blank">
              <FontAwesomeIcon icon={faInstagram} />
            </a>
          </li>
          <li>
            <a href="mailto: uofc@gmail.com" target="_blank">
              <FontAwesomeIcon icon={faGoogle} />
            </a>
          </li>
        </ul>
        <p>403-345-3589</p>
      </div>
      <div id="contact">
        <p>
          Designed By{" "}
          <a
            href="https://github.com/RaminKahidi/CPSC329Project"
            target="_blank"
          >
            Project Group 27
          </a>
        </p>
      </div>
    </footer>
  );
};

export default Footer;
