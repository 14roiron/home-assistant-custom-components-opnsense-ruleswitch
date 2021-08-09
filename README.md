## opnSense Rule Switch Component

This component is written to toggle opnSense firewall rules on (enabled) or off (disabled).  
One my question why in the world would someone want to do this from HA. Simply put, I only use it to change the vpn use by my chromecast.


FORK from https://github.com/dgshue/home-assistant-custom-components and nagyrobi/home-assistant-custom-components-pfsense-ruleswitch
Thanks for their work on that.
### Pre-Reqs

- opnsense 21.0+
- pyopnsense api 0.0.3 installed
  https://github.com/mtreinish/pyopnsense
- API Key and Secret with appropriate permissions

### Installation

- Copy directory `opnsense_rule` to your `<config dir>/custom_components` directory.
- Configure with config below.
- Restart Home-Assistant.

### Usage
To use this component in your installation, add the following to your `configuration.yaml` file:

```yaml
# Example configuration.yaml entry

switch:
  - platform: opnsense_rule
    host: 192.168.1.1
    api_key: PFFA1QDKsakjied21 -or- !secret fauxapi-key
    access_token: AectmzLxeTS413I6FtLyA3xhFxs3Y80n3bZEu6gzboxd5adUbbrejFZae1u5 -or- !secret fauxapi-secret
    rule_filter: HomeAssistant
```

Configuration variables:

- **host** (*Required*): The hostname or IP address of the pfSense firewall, ideally the LAN IP
- **api_key** (*Required*): The API Key from FauxAPI
- **access_token** (*Required*): The API Secret from FauxAPI
- **rule_filter** (*Optional*): Used to create switches only on certain rules.  Rule description must start with filter to match (ie. HomeAssisant-BlockTraffic1)
