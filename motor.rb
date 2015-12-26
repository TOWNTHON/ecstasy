require "wiringpi.rb"

s = WiringPi::GPIO.new

s.mode(18, PWM_OUTPUT)

s.pwmSetMode(PWM_MODE_MS)
s.pwmSetClock(400)
s.pwmSetRange(1024)

s.pwmWrite(1, 100)
