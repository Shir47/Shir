'use client'; 

import { useRef } from 'react';
import Image from 'next/image';
import Link from 'next/link';
import { projectsData } from '@/lib/data';
import { useScroll, useTransform, motion } from 'framer-motion';

// Define the type for a single project using the data structure
type ProjectProps = (typeof projectsData)[number];

export const Project = ({
  title,
  image,
  category,
  description,
  index // Added index to alternate layout
}: ProjectProps & { index: number }) => {
  // Ref for tracking the DOM element
  const ref = useRef<HTMLDivElement>(null);

  // Get scroll progress and apply it to animations
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ['0 1', '1.33 1'],
  });

  // Create scale and opacity transformations
  const scaleProgress = useTransform(scrollYProgress, [0, 1], [0.95, 1]);
  const opacityProgress = useTransform(scrollYProgress, [0, 1], [0.75, 1]);

  // Project links based on the index
  const projectLinks = [
    "https://shir.framer.website/", // First project link
    "https://afgweb.com.au/",         // Second project link
    "https://42adelaide.netlify.app/" // Third project link
  ];

  return (
    <motion.div
      ref={ref}
      style={{
        scale: scaleProgress,
        opacity: opacityProgress,
      }}
      className='flex flex-col items-center bg-white rounded-xl shadow-lg p-8 transition-transform hover:-translate-y-2 hover:shadow-xl xl:flex-row xl:justify-between'
    >
      {/* Text content */}
      <div className={`text-center xl:text-left xl:w-1/2 ${index % 2 === 0 ? 'xl:pr-8' : 'xl:pl-8'}`}>
        <h5 className='text-sm font-bold text-blue-600 uppercase tracking-wide'>{category}</h5>
        <h3 className='mt-4 text-2xl font-semibold text-gray-800 leading-tight'>{title}</h3>
        <p className='mt-4 text-base text-gray-600 max-w-lg leading-relaxed'>{description}</p>
        <Link 
          href={projectLinks[index]} 
          target="_blank" 
          rel="noopener noreferrer" 
          className="mt-6 inline-block text-sm font-medium text-blue-600 hover:underline"
        >
          View Details
        </Link>
      </div>

      {/* Image with hover effect */}
      <div className="relative mt-6 w-full xl:w-1/2 h-80 xl:h-96">
        <Image
          src={image}
          width={384}
          height={384}
          alt={`${title} project image`}
          className="rounded-lg object-cover transition-transform duration-500 ease-in-out hover:scale-105 shadow-md"
        />
      </div>
    </motion.div>
  );
};
