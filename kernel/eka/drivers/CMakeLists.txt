cmake_minimum_required(VERSION 3.20)

# Optional: print out extra messages to see what is going on. Comment it to have less verbose messages
set(CMAKE_VERBOSE_MAKEFILE ON)

add_subdirectory(adc)
add_subdirectory(display)
add_subdirectory(iic)
#add_subdirectory(dma)
add_subdirectory(ecomm)
#add_subdirectory(hcr)