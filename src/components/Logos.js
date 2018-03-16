import React, { Component } from 'react';
import '../styles/Logos.css';
import logo1 from '../images/Sanford_logo_01.svg';
import logo2 from '../images/Sanford_logo_02.svg';
import logo3 from '../images/Sanford_logo_10.svg';


class Logos extends Component {
    render() {
      return (
        <div>
            <img src={logo1} alt="logo1" class='style4'/>
            <br />
            <img src={logo2} alt="logo1" class='style4'/>
            <br />
            <img src={logo3} alt="logo1" class='style4'/>
            <br />

            <img src={logo1} alt="logo1" class='style1'/>
            <br />
            <img src={logo2} alt="logo1" class='style1'/>
            <br />
            <img src={logo3} alt="logo1" class='style1'/>
            <br />

            <img src={logo1} alt="logo1" class='style2'/>
            <br />
            <img src={logo2} alt="logo1" class='style2'/>
            <br />
            <img src={logo3} alt="logo1" class='style2'/>
            <br />

            <img src={logo1} alt="logo1" class='style3'/>
            <br />
            <img src={logo2} alt="logo1" class='style3'/>
            <br />
            <img src={logo3} alt="logo1" class='style3'/>
            <br />
        </div>
      )
    }
}

export default Logos;