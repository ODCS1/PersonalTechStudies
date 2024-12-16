import { Swiper, SwiperSlide } from 'swiper/react';

import { EffectCube, Navigation, Pagination, Scrollbar, A11y } from 'swiper';
import 'swiper/swiper.min.css';
import './App.css'
import 'swiper/swiper-bundle.min.css'

interface Slide {
    image: string;
    title: string;
    subTitle: string;
    interval: number;
}

interface SliderProps {
    slides: Slide[];
}

const Slider = ({ slides }: SliderProps) => {
    return (
        <Swiper
            effect={'cube'}
            cubeEffect={{
                shadow: true,
                slideShadows: true,
                shadowOffset: 20,
                shadowScale: 0.94,
            }}
            modules={[EffectCube, Navigation, Pagination, Scrollbar, A11y]}
            spaceBetween={50}
            slidesPerView={1}
            navigation
            pagination={{ clickable: true }}
            scrollbar={{ draggable: true }}
            onSlideChange={() => console.log('slide change')}
            // onSwiper={(swiper) => console.log(swiper)}
            simulateTouch={true}
            grabCursor={true}
        >
            {slides.map((slide) => (
                <SwiperSlide key={slide.image}>
                    <img src={slide.image} alt={slide.title} />
                </SwiperSlide>
            ))}
        </Swiper>
    );
};

export default Slider;
