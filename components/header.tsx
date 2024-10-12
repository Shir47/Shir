'use client'

import { Link } from 'react-scroll'
import Image from 'next/image'
import Nav from '@/components/nav'
import MobileNav from '@/components/mobileNav'

const Header = () => {
  return (
    <header className='fixed z-50 w-full bg-white py-4 shadow-md xl:py-6'>
      <div className='container mx-auto flex items-center justify-between px-6 md:px-12 lg:px-16'>
         {/* logo */}
         <Link to='/' spy={true} smooth={true} className='cursor-pointer'>
          <Image src='/hero/logo.svg' height={54.53} width={41.35} alt='logo' />
        </Link>

        {/* Desktop Navigation */}
        <div className='hidden items-center gap-x-8 xl:flex'>
          <Nav />
          <Link
            to='/'
            spy={true}
            smooth={true}
            className='text-md rounded-full bg-blue-600 px-6 py-2 font-semibold text-white shadow-lg transition-all duration-300 hover:bg-blue-700 hover:shadow-xl'
          >
            Hire Me
          </Link>
        </div>

        {/* Mobile Navigation */}
        <div className='z-50 xl:hidden'>
          <MobileNav />
        </div>
      </div>
    </header>
  )
}

export default Header