[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]][license]

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

| Platform        | Description                         |
| --------------- | ----------------------------------- |
| `switch`        | Switch something `True` or `False`. |

![example][exampleimg]

{% if not installed %}

## Installation

1. Click install.
1. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "opnsense ruleswitch".

{% endif %}

## Configuration is done in the UI

<!---->

## Credits

This project was generated from [@oncleben31](https://github.com/oncleben31)'s [Home Assistant Custom Component Cookiecutter](https://github.com/oncleben31/cookiecutter-homeassistant-custom-component) template.

Code template was mainly taken from [@Ludeeus](https://github.com/ludeeus)'s [integration_blueprint][integration_blueprint] template

---

[integration_blueprint]: https://github.com/custom-components/integration_blueprint
[buymecoffee]: https://www.buymeacoffee.com/ludeeus
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[commits-shield]: https://img.shields.io/github/commit-activity/y/14roiron/opnsense-ruleswitch.svg?style=for-the-badge
[commits]: https://github.com/14roiron/opnsense-ruleswitch/commits/main
[hacs]: https://hacs.xyz
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[discord]: https://discord.gg/Qa5fW2R
[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?style=for-the-badge
[exampleimg]: example.png
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license]: https://github.com/14roiron/opnsense-ruleswitch/blob/main/LICENSE
[license-shield]: https://img.shields.io/github/license/14roiron/opnsense-ruleswitch.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-%4014roiron-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/14roiron/opnsense-ruleswitch.svg?style=for-the-badge
[releases]: https://github.com/14roiron/opnsense-ruleswitch/releases
[user_profile]: https://github.com/14roiron
