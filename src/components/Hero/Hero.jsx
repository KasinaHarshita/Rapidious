import React from 'react';
import bgImg from '../../assets/website/vector3.jpg';
import Food1 from '../../assets/biryani/biryani2.jpeg';
import Food2 from '../../assets/biryani/biryani3.jpeg';
import Food3 from '../../assets/biryani/biryani5.jpg';

const ImageList = [
  {
    id: 1,
    img: Food1, 
  },
  {
    id: 2,
    img: Food2,
  },
  {
    id: 3,
    img: Food3,
  },
];

const bgImage = {
  backgroundImage: `url(${bgImg})`,
  backgroundPosition: "center",
  backgroundSize: "cover",
  backgroundRepeat: "no-repeat",
  width: "100%",
  height: "100%",
};

const Hero = () => {
  const [imageId, setImageId] = React.useState(Food1);
  return ( 
    <>
    <div style={bgImage} className='min-h-[550px] sm:min-h-[600px] bg-gray-100 dark:bg-gray-950 dark:text-white duration-200 flex justify-center items-center'>
      <div className='container pb-8 sm:pb-0'>
        <div className='grid grid-cols-1 sm:grid-cols-2'>
          {/* text content section  */}
          <div className='flex flex-col justify-center gap-4 pt-12 sm:pt-0 text-center sm:text-left order-2 sm:order-1'>
            <h1 className='text-5xl sm:text-6xl lg:text-7xl font-bold'>
              Welcome to the Recipe App
            </h1>
            <p className='text-sm'>
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Id cum corrupti repellendus illum voluptatem, vero dolorem quaerat nisi iste nihil animi veniam esse rerum. Non iusto sit tempore sed eaque.
            </p>
          </div>
          {/* Image section  */}
          <div>

          </div>
        </div>
      </div>
    </div>
    </>
  );
};

export default Hero;
