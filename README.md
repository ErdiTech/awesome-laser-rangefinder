# Awesome laser rangefinder [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of **laser rangefinder and single-point LiDAR distance modules**, the drivers that talk to them, flight-controller integration docs, guides and safety standards. For drones, robots, industrial gauging, surveying and IoT.

Scope: modules and software for measuring distance to one point with a laser (time-of-flight, phase-shift, triangulation). Scanning LiDAR has its own lists; see [awesome-lidar](https://github.com/szenergy/awesome-lidar).

## Contents

- [Module manufacturers](#module-manufacturers)
- [Drivers and libraries](#drivers-and-libraries)
- [Flight controller integration](#flight-controller-integration)
- [Guides](#guides)
- [Tools and datasets](#tools-and-datasets)
- [Standards and safety](#standards-and-safety)

## Module manufacturers

- [ERDI LASER (ERDI TECH LTD)](https://erdilrf.com/) — 905 nm and 1535 nm laser rangefinder modules, UART/I2C, from 12 g down to 1.3 g; open drivers, public price list and model pages.
- [Benewake](https://en.benewake.com/) — TFmini, TF-Luna, TF02 and TF03 single-point LiDAR for drones and robots.
- [LightWare Optoelectronics](https://lightwarelidar.com/) — SF and LW series laser altimeters and rangefinders with serial and I2C output.
- [Garmin LIDAR-Lite](https://www.garmin.com/en-US/p/557294) — LIDAR-Lite v3 / v3HP optical distance sensors (I2C, PWM).
- [Nooploop](https://www.nooploop.com/) — TOFSense time-of-flight ranging sensors.
- [Lumispot Tech](https://www.lumispot-tech.com/) — Laser rangefinder modules and laser sources.
- [Terabee](https://www.terabee.com/) — TeraRanger Evo time-of-flight distance sensors.
- [DFRobot](https://www.dfrobot.com/) — Hobby and education laser range sensors and breakouts.
- [STMicroelectronics FlightSense](https://www.st.com/en/imaging-and-photonics-solutions/time-of-flight-sensors.html) — VL53 family time-of-flight ranging ICs.

## Drivers and libraries

- [ErdiTech/erdi-lrf-drivers](https://github.com/ErdiTech/erdi-lrf-drivers) — Python and Arduino drivers for ERDI modules, every constant cited to the manual.
- [ErdiTech/erdi_lrf_driver](https://github.com/ErdiTech/erdi_lrf_driver) — ROS 2 driver node (`sensor_msgs/Range`), builds on Jazzy and Humble.
- [erdi-lrf on PyPI](https://pypi.org/project/erdi-lrf/) — pip install erdi-lrf.
- [ErdiLRF Arduino library](https://github.com/ErdiTech/ErdiLRF) — Arduino / ESP32 library for ERDI modules.
- [erdi-lrf-esp32-micropython](https://github.com/ErdiTech/erdi-lrf-esp32-micropython) — MicroPython driver for ESP32 and RP2040.
- [erdi-lrf-stm32-hal](https://github.com/ErdiTech/erdi-lrf-stm32-hal) — STM32 HAL driver with circular DMA.
- [erdi-lrf-home-assistant](https://github.com/ErdiTech/erdi-lrf-home-assistant) — ESPHome external component for Home Assistant.
- [erdi-lrf-raspberry-pi-python](https://github.com/ErdiTech/erdi-lrf-raspberry-pi-python) — Raspberry Pi logger, MQTT publisher and MAVLink bridge.
- [erdi-lrf-ros2-examples](https://github.com/ErdiTech/erdi-lrf-ros2-examples) — ROS 2 launch files, RViz config and filters.
- [budryerson/TFMini-Plus](https://github.com/budryerson/TFMini-Plus) — Arduino library for Benewake TFmini-Plus.
- [budryerson/TFLuna-I2C](https://github.com/budryerson/TFLuna-I2C) — Arduino library for the Benewake TF-Luna over I2C.
- [garmin/LIDARLite_Arduino_Library](https://github.com/garmin/LIDARLite_Arduino_Library) — Arduino library for LIDAR-Lite.
- [pololu/vl53l1x-arduino](https://github.com/pololu/vl53l1x-arduino) — Arduino library for the VL53L1X.
- [adafruit/Adafruit_VL53L1X](https://github.com/adafruit/Adafruit_VL53L1X) — Adafruit library for the VL53L1X.

## Flight controller integration

- [ArduPilot rangefinders](https://ardupilot.org/copter/docs/common-rangefinder-landingpage.html) — Supported rangefinders, wiring and parameters for ArduPilot.
- [PX4 distance sensors](https://docs.px4.io/main/en/sensor/rangefinders.html) — Rangefinder drivers and setup for PX4.
- [MAVLink DISTANCE_SENSOR](https://mavlink.io/en/messages/common.html#DISTANCE_SENSOR) — Message used by companion computers to feed a rangefinder to the autopilot.
- [ArduPilot Lua scripting](https://ardupilot.org/copter/docs/common-lua-scripts.html) — Writing serial rangefinder drivers as Lua scripts.
- [AP_RangeFinder source](https://github.com/ArduPilot/ardupilot/tree/master/libraries/AP_RangeFinder) — ArduPilot rangefinder backends.
- [PX4 distance sensor drivers](https://github.com/PX4/PX4-Autopilot/tree/main/src/drivers/distance_sensor) — PX4 rangefinder drivers.
- [ArduPilot PR #34983: ERDI VB and H series](https://github.com/ArduPilot/ardupilot/pull/34983) — Open pull request adding a native serial driver for the 0x5C stream modules.
- [erdi-lrf-pixhawk-ardupilot](https://github.com/ErdiTech/erdi-lrf-pixhawk-ardupilot) — Wiring, RNGFND parameters and bench logs for using a laser rangefinder as an ArduPilot altimeter.

## Guides

- [drone-altimeter-laser-rangefinder-guide](https://github.com/ErdiTech/drone-altimeter-laser-rangefinder-guide) — Selection guide for drone laser altimeters and obstacle sensors.
- [ERDI: 905 nm vs 1535 nm](https://github.com/ErdiTech/erdi-lrf-drivers/blob/main/docs/905nm-vs-1535nm.md) — Wavelength trade-offs and laser safety scope.
- [ERDI: laser rangefinder evaluation checklist](https://github.com/ErdiTech/erdi-lrf-drivers/blob/main/docs/evaluation-checklist.md) — What to test before design freeze.
- [ERDI: field troubleshooting](https://github.com/ErdiTech/erdi-lrf-drivers/blob/main/docs/field-troubleshooting.md) — Symptom-to-cause table for serial rangefinders.

## Tools and datasets

- [laser-rangefinder-module-database](https://github.com/ErdiTech/laser-rangefinder-module-database) — Open dataset of laser rangefinder module specifications with source URLs and capture dates; sortable table.
- [lrf-uart-protocol-decoder](https://github.com/ErdiTech/lrf-uart-protocol-decoder) — WebSerial and Python UART frame decoder for rangefinder modules.
- [erdi-lrf-pixhawk-ardupilot](https://github.com/ErdiTech/erdi-lrf-pixhawk-ardupilot) — Pixhawk wiring, parameters and a Lua driver.

## Standards and safety

- [REP 117: Informational Distance Measurements](https://www.ros.org/reps/rep-0117.html) — How ROS represents out-of-range and invalid distance readings.
- [sensor_msgs/Range](https://docs.ros.org/en/humble/p/sensor_msgs/interfaces/msg/Range.html) — ROS 2 message for single-point range sensors.
- [IEC 60825-1](https://webstore.iec.ch/en/publication/3587) — Safety of laser products: equipment classification and requirements.

## Contributing

Open a PR with the link, a one-line description and which section it belongs in. Manufacturer entries need a public product page with specifications; driver entries need a README that says which modules and interfaces they support. Links are checked with a script before merge.

## Support / 打赏

If this project saved you time, you can buy the author a coffee in crypto. Thank you!
如果这个项目帮到了你，欢迎用加密货币打赏支持，谢谢！

| Network | Asset | Address |
|---|---|---|
| TRON (TRC20) | USDT | `TNGdTwE6opH6rmUyoG1JUR7FSyEb4k273R` |
| Ethereum / BNB Chain / Polygon | USDT | `0x59c43144a862b351fa1086ae842d1327c9d91613` |
| Ethereum / Arbitrum / Base | ETH | `0x59c43144a862b351fa1086ae842d1327c9d91613` |
| Bitcoin | BTC | `1RS6tWXHregLfEsiPzVUCUBuhgDg5uTSV` |
| Solana | USDT | `HZguEXfTtLChNdJTxAYCbcGscaqikz8JYrEpUhEyeVd9` |

Please send only the listed asset on the listed network — other tokens or networks may be lost.
请按表中对应的网络转对应的币种，转错币种或网络可能无法找回。


## License

MIT — see [LICENSE](LICENSE).
