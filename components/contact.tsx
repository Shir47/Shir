'use client';

import { Send } from 'lucide-react';
import React, { useState } from 'react';
import { motion } from 'framer-motion';
import FadeIn from '@/lib/variants';
import emailjs from 'emailjs-com';

const Contact = () => {
  const [formData, setFormData] = useState({
    name: '',
    subject: '',
    message: ''
  });

  // Proper typing for handleChange event (React.ChangeEvent<HTMLInputElement> or React.ChangeEvent<HTMLTextAreaElement>)
  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  // Proper typing for handleSubmit event (React.FormEvent<HTMLFormElement>)
  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    emailjs
      .send(
        'service_jnkcmsn', // replace with your EmailJS service ID
        'template_ch3lr07', // replace with your EmailJS template ID
        {
          from_name: formData.name,
          subject: formData.subject,
          message: formData.message,
          to_email: 'shiralimohammadi47@gmail.com', // replace with the email where submissions should go
        },
        'YOUR_USER_ID' // replace with your EmailJS user ID
      )
      .then(
        (result) => {
          console.log('Message sent: ', result.text);
        },
        (error) => {
          console.log('Failed to send: ', error.text);
        }
      );

    setFormData({ name: '', subject: '', message: '' });
  };

  return (
    <section id='Contact' className='bg-white py-28'>
      <div className='container flex flex-col justify-between px-6 md:flex-row'>
        {/* Heading Section */}
        <motion.div
          variants={FadeIn('right', 0.2)}
          initial='hidden'
          whileInView='show'
          viewport={{ once: true, amount: 0.8 }}
          className='mb-12 mr-6 flex items-center py-6'
        >
          <h1 className='text-4xl font-extrabold leading-tight text-gray-800'>
            Let&apos;s Work <br /> <span className='text-blue-600 underline'>Together</span>
          </h1>
        </motion.div>

        {/* Form Section */}
        <motion.form
          onSubmit={handleSubmit}
          variants={FadeIn('left', 0.2)}
          initial='hidden'
          whileInView='show'
          viewport={{ once: true, amount: 0.8 }}
          className='flex max-w-xl flex-1 flex-col items-start gap-y-6 rounded-lg bg-white shadow-md p-10 transition-transform duration-300 hover:shadow-lg'
        >
          {/* Name Input */}
          <input
            type='text'
            name='name'
            value={formData.name}
            onChange={handleChange}
            placeholder='Your Name'
            required
            className='w-full border-b-2 border-gray-300 bg-transparent py-3 outline-none text-gray-800 transition-all placeholder:text-gray-500 focus:border-blue-500 focus:ring-0'
          />

          {/* Subject Input */}
          <input
            type='text'
            name='subject'
            value={formData.subject}
            onChange={handleChange}
            placeholder='Subject'
            required
            className='w-full border-b-2 border-gray-300 bg-transparent py-3 outline-none text-gray-800 transition-all placeholder:text-gray-500 focus:border-blue-500 focus:ring-0'
          />

          {/* Message Input */}
          <textarea
            name='message'
            id='message'
            value={formData.message}
            onChange={handleChange}
            placeholder='Your Message'
            required
            className='mb-6 w-full resize-none border-b-2 border-gray-300 bg-transparent py-3 outline-none text-gray-800 transition-all placeholder:text-gray-500 focus:border-blue-500 focus:ring-0'
          ></textarea>

          {/* Submit Button */}
          <button
            type='submit'
            className='flex items-center justify-between gap-x-2 rounded-full bg-blue-600 px-6 py-3 text-white transition-all duration-300 hover:bg-blue-700'
          >
            <p className='text-md font-semibold capitalize'>Send Message</p>
            <Send className='h-5 w-5' />
          </button>
        </motion.form>
      </div>
    </section>
  );
};

export default Contact;
