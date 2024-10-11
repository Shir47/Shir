'use client'
import { motion } from 'framer-motion'
import FadeIn from '../lib/variants'
import AnimatedCounter from '../lib/animatedCounter'

const Services = () => {
  return (
    <section id='services' className='relative z-30 bg-white py-20'>
      <div className='container mx-auto w-full py-[100px] lg:py-[200px]'>
        <div className='flex flex-col justify-between gap-12 px-4 lg:flex-row lg:px-0'>
          {/* Left Column */}
          <motion.div
            variants={FadeIn('right', 0.2)}
            initial='hidden'
            whileInView={'show'}
            viewport={{ once: true, amount: 0.8 }}
            className='flex flex-col justify-between lg:mr-8 lg:w-1/2'
          >
            <h1 className='pb-4 text-5xl font-extrabold leading-tight text-blue-800'>
              What I Do
            </h1>
            <p className='mb-8 text-xl text-gray-600'>
              I specialize in designing and developing responsive, user-friendly
              websites and web applications. With expertise in HTML, CSS,
              JavaScript, and frameworks like React and Angular, I create clean,
              modern interfaces that deliver seamless user experiences. I also
              focus on UI/UX design, optimizing websites for performance, and
              integrating custom features for platforms like WordPress and
              Shopify. Whether you need a landing page, full website, or app
              interface, I turn your ideas into polished, functional digital
              products.
            </p>

            <div className='flex justify-between space-x-12 py-8'>
              <div className='flex flex-col items-center'>
                <p className='text-lg font-semibold uppercase text-gray-500'>
                  Projects
                </p>
                <p className='text-5xl font-bold text-blue-700'>
                  + <AnimatedCounter from={0} to={50} />
                </p>
              </div>
              <div className='flex flex-col items-center'>
                <p className='text-lg font-semibold uppercase text-gray-500'>
                  Satisfied Clients
                </p>
                <p className='text-5xl font-bold text-blue-700'>
                  <AnimatedCounter from={0} to={25} />
                </p>
              </div>
            </div>
          </motion.div>

          {/* Right Column */}
          <motion.div
            variants={FadeIn('left', 0.4)}
            initial='hidden'
            whileInView={'show'}
            viewport={{ once: true, amount: 0.8 }}
            className='flex flex-col gap-8 lg:w-1/2'
          >
            {[
              {
                title: 'Front-end Development',
                number: '01',
                description:
                  'Convert your Figma/XD design to a fully responsive web app with React/Next.js, Angular, or HTML with Tailwind CSS'
              },
              {
                title: 'WordPress and Shopify',
                number: '02',
                description:
                  'Customization theme , plugin integration, and performance optimization. Whether it’s a landing page, e-commerce store, or complete website, I deliver polished, functional, and SEO-optimized digital solutions tailored to your needs.'
              }
            ].map(service => (
              <div
                key={service.number}
                className='flex transform items-center space-x-6 rounded-lg border-l-4 border-blue-600 bg-white p-6 shadow-lg transition-transform hover:scale-105 hover:shadow-2xl'
              >
                <p className='text-6xl font-extrabold text-blue-700'>
                  {service.number}
                </p>
                <div>
                  <h2 className='mb-2 text-2xl font-semibold text-gray-800'>
                    {service.title}
                  </h2>
                  <p className='text-gray-600'>{service.description}</p>
                </div>
              </div>
            ))}
          </motion.div>
        </div>
      </div>
    </section>
  )
}

export default Services
