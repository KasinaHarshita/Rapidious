import React from 'react';
import Img2 from '../../assets/biryani/biryani5.jpg';

const ServicesData = [
    {
        id: 1,
        img: Img2,
        name: "Biryani",
        description: "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Consectetur aliquid ipsum quos, nobis dignissimos voluptas.",
    },
    {
        id: 2,
        img: Img2,
        name: "Chicken Curry",
        description: "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Consectetur aliquid ipsum quos, nobis dignissimos voluptas.",
    },
    {
        id: 3,
        img: Img2,
        name: "Cold Coffee",
        description: "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Consectetur aliquid ipsum quos, nobis dignissimos voluptas.",
    },
];

const Services = () => {
  return (
    <>
      <div className='py-10'>
        <div className='container'>
            {/* Header Section  */}
            <div className='text-center mb-20 max-w-[400px] mx-auto'>
                <p className='text-sm bg-clip-text text-transparent bg-gradient-to-r from-primary to-secondary'>Our Services</p>
                <h1 className='text-3xl font-bold'>Services</h1>
                <p className='text-xs text-gray-400'>{" "}Lorem ipsum dolor, sit amet consectetur adipisicing elit. Blanditiis necessitatibus ducimus ipsum minima, aperiam tempore!</p>
            </div>
            {/* Card Section  */}
            <div>
                <div className='grid grid-cols-1 sm:grid-cols-2 md:grip-cols-3 gap-14 md:gap-5 place-items-center'>
                    {
                        ServicesData.map(({id, img, name, description }) => {
                            return (
                                <div key={id} className='max-w-[300px] group rounded-2xl bg-white dark:bg-gray-800 hover:bg-primary hover:text-white duration-300 shadow-xl'>
                                    <div className='h-[100px]'>
                                        <img src={img} alt="" className='max-w-[150px] mx-auto block transform -translate-y-14 group-hover:scale-105 group-hover:rotate-6 duration-300'/>
                                    </div>
                                    <div className='p-4 text-center'>
                                        <h1 className='text-xl font-bold'>{name}</h1>
                                        <p className='text-gray-500 group-hover:text-white duration-300 text-sm line-clamp-2'>{description}</p>
                                    </div>
                                </div>
                            );
                        })
                    }
                </div>
            </div>
        </div>
      </div>
    </>
  );
};

export default Services
