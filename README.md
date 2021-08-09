# opnsense ruleswitch

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![pre-commit][pre-commit-shield]][pre-commit]
[![Black][black-shield]][black]

[![hacs][hacsbadge]][hacs]
[![Project Maintenance][maintenance-shield]][user_profile]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

[![Discord][discord-shield]][discord]
[![Community Forum][forum-shield]][forum]

## opnSense Rule Switch Component

This component is written to toggle opnSense firewall rules on (enabled) or off (disabled).  
One my question why in the world would someone want to do this from HA. Simply put, I only use it to change the vpn use by my chromecast.


FORK from https://github.com/dgshue/home-assistant-custom-components and nagyrobi/home-assistant-custom-components-pfsense-ruleswitch
Thanks for their work on that.

### Pre-Reqs

- opnsense 21.0+
- install os-firewall in opnsense to allow api commands
- pyopnsense api 0.0.3 installed
  https://github.com/mtreinish/pyopnsense
- API Key and Secret with appropriate permissions

### Managed rules
With the new plugin on version 20.1.5 for the firewall API, it adds a new menu item under the "Firewall" section called "Automation"  under that is the "Filter" and "Source NAT" menu items.  You create your firewall rule under "Filter", then you need to get the UUID of this rule (I just looked at the config.xml  Although there is a search parameter you can use with the API).  Now, these firewall rules are above all other rules, even floating.  (so the order of execution for the firewall rules goes: Automation->Floating->Interface)

The rules shown here are the one under the automation tab, not the normal rules.

**This component will set up the following platforms.**

| Platform        | Description                                                               |
| --------------- | ------------------------------------------------------------------------- |
| `switch`        | Switch firewall rules on or off.                                          |



## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `opnsense_ruleswitch`.
4. Download _all_ the files from the `custom_components/opnsense_ruleswitch/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "opnsense ruleswitch"

Using your HA configuration directory (folder) as a starting point you should now also have this:

```text
custom_components/opnsense_ruleswitch/translations/en.json
custom_components/opnsense_ruleswitch/translations/fr.json
custom_components/opnsense_ruleswitch/translations/nb.json
custom_components/opnsense_ruleswitch/translations/sensor.en.json
custom_components/opnsense_ruleswitch/translations/sensor.fr.json
custom_components/opnsense_ruleswitch/translations/sensor.nb.json
custom_components/opnsense_ruleswitch/translations/sensor.nb.json
custom_components/opnsense_ruleswitch/__init__.py
custom_components/opnsense_ruleswitch/api.py
custom_components/opnsense_ruleswitch/binary_sensor.py
custom_components/opnsense_ruleswitch/config_flow.py
custom_components/opnsense_ruleswitch/const.py
custom_components/opnsense_ruleswitch/manifest.json
custom_components/opnsense_ruleswitch/sensor.py
custom_components/opnsense_ruleswitch/switch.py
```

## Configuration is done in the UI

<!---->

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

## Credits

This project was generated from [@oncleben31](https://github.com/oncleben31)'s [Home Assistant Custom Component Cookiecutter](https://github.com/oncleben31/cookiecutter-homeassistant-custom-component) template.

Code template was mainly taken from [@Ludeeus](https://github.com/ludeeus)'s [integration_blueprint][integration_blueprint] template

---

[integration_blueprint]: https://github.com/custom-components/integration_blueprint
[black]: https://github.com/psf/black
[black-shield]: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
[buymecoffee]: https://www.buymeacoffee.com/14roiron
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[commits-shield]: https://img.shields.io/github/commit-activity/y/14roiron/home-assistant-custom-components-opnsense-ruleswitch.svg?style=for-the-badge
[commits]: https://github.com/14roiron/home-assistant-custom-components-opnsense-ruleswitch/commits/main
[hacs]: https://hacs.xyz
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[discord]: https://discord.gg/Qa5fW2R
[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?style=for-the-badge
[exampleimg]: example.png
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license-shield]: https://img.shields.io/github/license/14roiron/home-assistant-custom-components-opnsense-ruleswitch.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-%4014roiron-blue.svg?style=for-the-badge
[pre-commit]: https://github.com/pre-commit/pre-commit
[pre-commit-shield]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/14roiron/home-assistant-custom-components-opnsense-ruleswitch.svg?style=for-the-badge
[releases]: https://github.com/14roiron/home-assistant-custom-components-opnsense-ruleswitch/releases
[user_profile]: https://github.com/14roiron
