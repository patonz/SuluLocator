# SuluLocator
Indoor Localization Lib

run the following command:
```pip install .```

now check the examples folder.

- [ ] Pozyx wrapper
  - [x] windows test: download the Driver from [https://www.st.com/en/development-tools/stsw-stm32102.html]
  - [ ] ubuntu test:

        1. Make sure you have permissions set to use the serial device.
        2. To get permission once (given your device is on port ACM0) you can run sudo chmod 666 /dev/ttyACM0
        3. To get permission forever you can run sudo adduser $USER dialout or the relevant group for your distro.
        
- [ ] esp wrapper
- [ ] bitcraze wrapper
