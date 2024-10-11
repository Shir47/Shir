import { Link } from 'react-scroll';

const menu = [
  {
    name: 'Services',
    href: 'services',
  },
  {
    name: 'Work',
    href: 'work',
  },
  {
    name: 'FAQ',
    href: 'FAQ', // Ensure this matches the id of your FAQ section
  },
  {
    name: 'Contact',
    href: 'Contact',
  },
];

const Nav = () => {
  return (
    <nav className='z-50 flex gap-10'>
      {menu.map((item, index) => (
        <Link
          to={item.href}
          spy={true}
          smooth={true}
          key={index}
          className='relative cursor-pointer text-lg font-semibold text-gray-800 transition-colors duration-300 ease-in-out hover:text-blue-600'
        >
          <span className='pb-1 transition-all duration-300 ease-in-out border-b-2 border-transparent hover:border-blue-600'>
            {item.name}
          </span>
        </Link>
      ))}
    </nav>
  );
};

export default Nav;
