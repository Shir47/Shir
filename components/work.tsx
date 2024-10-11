import { projectsData } from '@/lib/data';
import React from 'react';
import { Project } from '@/components/project';

const Work = () => {
  return (
    <section id='work' className='bg-white py-20'> {/* Clean white background */}
      <div className='container mx-auto px-6 md:px-12 lg:px-16'>
        
        {/* Section Title */}
        <div className='text-center mb-16'>
          <h1 className='text-5xl font-bold text-gray-900 tracking-tight'>
            <span className='relative inline-block'>
              Recent Projects
              <span className='absolute left-0 bottom-0 h-1 w-full bg-blue-500 rounded-md'></span> {/* Blue underline effect */}
            </span>
          </h1>
          <p className='mt-4 text-gray-600 text-lg max-w-2xl mx-auto'>
            Explore some of our most recent and impactful work, designed to create lasting impressions.
          </p>
        </div>

        {/* Projects List */}
        <div className='flex flex-col space-y-12'>
          {projectsData.map((project, i) => (
            <div key={i} className={`flex ${i % 2 === 0 ? 'flex-row' : 'flex-row-reverse'} items-center transform transition duration-300 hover:scale-105 shadow-lg hover:shadow-xl rounded-lg overflow-hidden`}>
              <Project {...project} index={i} />
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Work;
