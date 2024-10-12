import { Download } from 'lucide-react'
import Link from 'next/link'
import Social from '@/components/social'
import Photo from '@/components/photo'

const Hero = () => {
  return (
    <section className='w-full bg-white pt-32'>
      <div className='container mx-auto h-full px-4'>
        <div className='flex flex-col items-center justify-between gap-10 xl:flex-row xl:pt-8'>
          {/* Text Section */}
          <div className='text-center xl:max-w-lg xl:text-left'>
            <span className='text-lg font-medium text-gray-500'>
              Hello, I&apos;m
            </span>
            <h1 className='mt-2 text-4xl font-extrabold leading-tight text-gray-900 md:text-5xl'>
              Shir
              <span className='text-blue-600 underline decoration-blue-400 decoration-4'>
                Ali
              </span>
            </h1>
            <div className='py-6'>
              <p className='text-base leading-relaxed text-gray-600 md:text-lg'>
                I’m a developer with a passion for creating clean, intuitive web
                applications. I love turning ideas into real, functional
                solutions using creativity and technology. I’m always eager to
                learn new tools and skills. Whether working on solo full-stack
                projects or collaborating with teams, I thrive in bringing
                concepts to life through effective communication, project
                management, and teamwork.
              </p>
            </div>
            <div className='mt-8 flex flex-col items-center space-y-4 xl:flex-row xl:space-x-6 xl:space-y-0'>
              <Link
                href='https://drive.google.com/file/d/1Ygeb5ttgLA0mGIiFn7rG2mldDVny0khT/view?usp=drive_link'
                
                target='_blank'
                className='flex items-center space-x-2 rounded-full border-2 border-blue-600 px-6 py-3 font-semibold uppercase text-blue-600 transition duration-300 hover:bg-blue-600 hover:text-white'
              >
                <span className='text-sm'>Download CV</span>
                <Download className='h-5 w-5' />
              </Link>
              <div className='flex py-4 xl:py-0'>
                <Social />
              </div>
            </div>
          </div>

          {/* Image Section */}
          <div className='flex w-full justify-center xl:w-auto xl:justify-end'>
            <Photo />
          </div>
        </div>
      </div>
    </section>
  )
}

export default Hero
