'use client';

import Image from 'next/image';
import { motion, Variants } from 'framer-motion';
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from '@/components/ui/accordion';
import FadeIn from '@/lib/variants';
import { askedQuestions } from '@/lib/data';

const slideVariant: Variants = {
  initial: {
    x: "0%"
  },
  animate: {
    x: "-50%",
    transition: {
      duration: 30,
      repeat: Infinity,
      ease: "linear",
      repeatType: "loop" as const
    }
  }
};

export const tech = [
  { src: '/tech/wordpress.svg', width: 46.14, height: 45.24, alt: 'Wordpress' },
  { src: '/tech/node.svg', width: 106.2, height: 31, alt: 'Node.js' },
  { src: '/tech/ts.svg', width: 46.14, height: 45.24, alt: 'TypeScript' },
  { src: '/tech/shopify.svg', width: 54.98, height: 48.73, alt: 'Shopify' },
  { src: '/tech/framer.svg', width: 47.48, height: 52.48, alt: 'Framer' },
  { src: '/tech/figma.svg', width: 47.48, height: 52.48, alt: 'Figma' },
  { src: '/tech/react.svg', width: 54.98, height: 48.73, alt: 'React' },
  { src: '/tech/angular.svg', width: 47.48, height: 51.23, alt: 'Angular' },
  { src: '/tech/css.svg', width: 54.98, height: 45.24, alt: 'Css' },
  { src: '/tech/js.svg', width: 54.98, height: 51.23, alt: 'Js' },
  { src: '/tech/html.svg', width: 54.98, height: 51.23, alt: 'Html' },
  { src: '/tech/elementor.svg', width: 54.98, height: 51.23, alt: 'elementor' },
  { src: '/tech/git.svg', width: 43.73, height: 51.23, alt: 'Git' },
  { src: '/tech/github.svg', width: 43.73, height: 51.23, alt: 'Github' },
];

const FAQ = () => {
  return (
    <section id='FAQ' className='bg-white py-20'>
      <div className='container mx-auto sm:px-2'>
        <h1 className='text-5xl font-bold text-center text-gray-900 leading-tight'>
          Frequently <br /> <span className='text-gray-600 underline'>Asked</span>
        </h1>

        <motion.div
          variants={FadeIn('up', 0.2)}
          initial='hidden'
          whileInView='show'
          viewport={{ once: true, amount: 0.8 }}
          className='mt-12 mx-auto max-w-2xl bg-white rounded-lg shadow-xl p-6 sm:p-8'
        >
          {askedQuestions.map((qst) => (
            <Accordion
              type='single'
              collapsible
              className='w-full text-left'
              key={qst.id}
            >
              <AccordionItem value={`item-${qst.id}`}>
                <AccordionTrigger className='flex justify-between items-center text-xl font-semibold text-gray-800 py-4 px-2 hover:bg-gray-100 transition duration-200'>
                  {qst.qs}
                </AccordionTrigger>
                <AccordionContent className='px-4 py-2 text-base text-gray-700 border-t'>
                  {qst.answer}
                </AccordionContent>
              </AccordionItem>
            </Accordion>
          ))}
        </motion.div>
      </div>

      <div className='mt-36 relative w-full overflow-hidden'>
        <div className='flex justify-center'>
          <div className='w-full max-w-[1200px] overflow-hidden'>
            <motion.div
              variants={slideVariant}
              initial='initial'
              animate='animate'
              className='flex gap-16 items-center whitespace-nowrap'
            >
              {/* First set of logos */}
              {tech.map((item, index) => (
                <div
                  key={`first-${index}`}
                  className='flex-shrink-0'
                >
                  <Image
                    src={item.src}
                    width={item.width}
                    height={item.height}
                    alt={item.alt}
                    className='transition-transform duration-300 hover:scale-110 shadow-sm filter grayscale hover:filter-none'
                  />
                </div>
              ))}
              {/* Duplicate set of logos for seamless loop */}
              {tech.map((item, index) => (
                <div
                  key={`second-${index}`}
                  className='flex-shrink-0'
                >
                  <Image
                    src={item.src}
                    width={item.width}
                    height={item.height}
                    alt={item.alt}
                    className='transition-transform duration-300 hover:scale-110 shadow-sm filter grayscale hover:filter-none'
                  />
                </div>
              ))}
            </motion.div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default FAQ;