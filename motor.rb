require 'bundler'
Bundler.setup
Bundler.require

io = WiringPi::GPIO.new do |gpio|
  gpio.pin_mode(18, WiringPi::OUTPUT)
  gpio.pwm_set_mode(0) # PWM_MODE_MS
  gpio.pwm_set_clock(400)
  gpio.pwm_set_range(1024)
end

io.soft_pwm_write(18, 100)
