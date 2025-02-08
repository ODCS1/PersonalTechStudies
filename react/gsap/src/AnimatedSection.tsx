"use client";

import React, { useEffect, useRef } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

const AnimatedSection: React.FC = () => {
  const sectionRef = useRef<HTMLDivElement | null>(null);
  const textRef = useRef<HTMLDivElement | null>(null);
  const imageRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    gsap.to(sectionRef.current, {
      backgroundColor: "#3B2C22",
      scrollTrigger: {
        trigger: sectionRef.current,
        start: "top top",
        end: "bottom top",
        scrub: 1,
      },
    });

    if (textRef.current?.children) {
      gsap.fromTo(
        textRef.current.children,
        { opacity: 0, y: 50 },
        {
          opacity: 1,
          y: 0,
          stagger: 0.5,
          scrollTrigger: {
            trigger: textRef.current,
            start: "top center",
            end: "bottom center",
            scrub: 1,
          },
        }
      );
    }

    if (imageRef.current?.children) {
      gsap.fromTo(
        imageRef.current.children,
        { opacity: 0, y: 50 },
        {
          opacity: 1,
          y: 0,
          stagger: 0.8,
          scrollTrigger: {
            trigger: imageRef.current,
            start: "top center",
            end: "bottom top",
            scrub: 1,
          },
        }
      );
    }
  }, []);

  return (
    <section
      ref={sectionRef}
      className="h-screen flex items-center justify-center p-10 transition-colors duration-500"
    >

      <div ref={textRef} className="w-1/2 text-white">
        <h2 className="text-4xl font-bold">Whisky Cellar</h2>
        <p className="text-lg mt-4">Work Office Brown</p>
      </div>

      <div ref={imageRef} className="w-1/2 relative">
        <img
          src="/image1.jpg"
          alt="Image 1"
          className="absolute top-0 left-0 w-full h-full object-cover transition-opacity duration-700"
        />
        <img
          src="/image2.jpg"
          alt="Image 2"
          className="absolute top-0 left-0 w-full h-full object-cover transition-opacity duration-700"
        />
        <img
          src="/image3.jpg"
          alt="Image 3"
          className="absolute top-0 left-0 w-full h-full object-cover transition-opacity duration-700"
        />
      </div>
    </section>
  );
};

export default AnimatedSection;
