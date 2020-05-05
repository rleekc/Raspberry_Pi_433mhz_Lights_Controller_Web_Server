# Raspberry_Pi_433mhz_Lights_Controller_Web_Server
Made a raspberry pi flask web server that controls my backyard lights using 433 MHz transmitter

I used this instructable to help me set up the circuit for the 433 mhz transmitter and receiver https://www.instructables.com/id/Super-Simple-Raspberry-Pi-433MHz-Home-Automation/

I used ninjablocks' 433utils for copying the signal of the remote control https://github.com/ninjablocks/433Utils

I used a simple flask server to use the command codesend from 433utils to transmit the signal to turn on the lights in the backyard.

I had to use a faraday blanket to isolate the 433 mhz signal from the remote control since there was a lot of interference in the air. https://www.amazon.com/gp/product/B01M294MGK/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1

The 433 mhz modules can be found here: https://www.amazon.com/gp/product/B07B9TVMW3/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1

The light switch can be found here: https://www.amazon.com/gp/product/B07J4TPSM8/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1
