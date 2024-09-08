import React from 'react';
import FooterLogo from '../../assets/logo.png';
// import {
//     FaFacebook,
//     FaInstagram,
//     FaLinkedIn,
//     FaLocationArrow,
//     FaMobileAlt,
// } from "react-icons/fa";
// import footerLogo from '../../assets/logo.png';

const Footer = () => {
  return (
    <>
      <div className='bg-gray-100 dark:bg-gray-950'>
        <div className='max-w-[1200px] mx-auto'>
            <div className="grid md:grid-cols-3 py-5">
                <div className='py-8 px-4 dark:text-white'>
                    <h1 className='flex items-center gap-3 text-xl sm:text-3xl font-bold text-justify sm:text-left'>
                    <img src={FooterLogo} alt="" className='max-w-[100px]'/>RECIPE</h1>
                    <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ab reiciendis suscipit, molestiae numquam quos provident!</p>
                    <br />
                    {/* <div>
                        <FaLocationArrow />
                        <p>Hyderbad, Telangana</p>
                    </div>
                    <div className='flex items-center gap-3 mt-3'>
                        <FaMobileAlt />
                        <p>+91 987654321</p>
                    </div> */}
                </div>
                <div className='grid grid-cols-2 sm:grid-cols-3 col-span-2 md:pl-10'></div>
            </div>
        </div>
      </div>
    </>
  );
};

export default Footer;
