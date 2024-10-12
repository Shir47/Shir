'use client';

import { Menu } from 'lucide-react';
import Image from 'next/image';
import Link from 'next/link';
import { Sheet, SheetContent, SheetTrigger } from '@/components/ui/sheet';

export const menu = [
  {
    name: 'Services',
    href: '/#Services',
  },
  {
    name: 'Work',
    href: '/#Work',
  },
  {
    name: 'FAQ',
    href: '/#FAQ',
  },
  {
    name: 'contact',
    href: '/#Contact',
  },
];

const MobileNav = () => {
  return (
    <Sheet>
      <SheetTrigger className="flex items-center p-2">
        <Menu className="h-8 w-8 text-blue-600" />
      </SheetTrigger>
      <SheetContent className="w-full sm:w-auto flex flex-col items-center bg-white p-4 sm:p-6 md:p-8 rounded-lg shadow-lg">
        <div className="mb-4 flex items-center justify-center">
          <Link href="/">
            <Image src="/hero/logo.svg" height={50} width={40} alt="logo" className="rounded-lg shadow-md" />
          </Link>
        </div>
        <nav className="mt-4 flex flex-col items-center justify-center gap-4">
          {menu.map((item, index) => (
            <Link
              href={item.href}
              key={index}
              className="text-base sm:text-lg font-semibold text-gray-800 capitalize transition-colors duration-300 hover:text-blue-600"
            >
              <span className="relative pb-1 transition-all after:absolute after:left-0 after:bottom-0 after:h-1 after:w-full after:bg-blue-600 after:scale-x-0 after:transition-transform after:duration-300 hover:after:scale-x-100">
                {item.name}
              </span>
            </Link>
          ))}
        </nav>
      </SheetContent>
    </Sheet>
  );
};

export default MobileNav;
