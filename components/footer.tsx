'use client';

import Image from 'next/image';
import { Link } from 'react-scroll';
import React from 'react';
import Social from '@/components/social';

const Footer = () => {
  return (
    <footer className='bg-gray-50 py-12 border-t border-gray-200'>
      <div className='container mx-auto flex flex-col items-center justify-between gap-6 xl:flex-row'>
        
        {/* Logo Section */}
        <div className='flex items-center'>
          <Link to='home' spy={true} smooth={true} className='cursor-pointer'>
            <Image src='/logo.png' width={60} height={40} alt='Logo' className='rounded-lg shadow-md' />
          </Link>
        </div>

        {/* Footer Text */}
        <p className='text-gray-800 text-lg font-medium tracking-wide text-center xl:text-left'>
          &copy; 2024 Shir Ali
        </p>

        {/* Social Media Icons */}
        <div className='flex space-x-4'>
          <Social />
        </div>
      </div>
    </footer>
  );
};

export default Footer;
