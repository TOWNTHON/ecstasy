require "wiringpi.rb"
s = WiringPi::GPIO.new

s.mode(18, PWM_OUTPUT)
s.pwmSetMode(0)
s.pwmSetClock(400)
s.pwmSetRange(1024)

s.pwmWrite(18, 100)
