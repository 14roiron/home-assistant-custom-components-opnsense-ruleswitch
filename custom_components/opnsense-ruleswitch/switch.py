"""
Switch Platform support for opnSense firewall rules.

For more details please refer to
https://github.com/dgshue/home-assistant-custom-components

Example usage:

configuration.yaml

---------------------------------------

switch:
  - platform: opnsense_rule
    host: 192.168.1.1
    api_key: PFFA1QDKsakjied21
    access_token: AectmzLxeTS413I6FtLyA3xhFxs3Y80n3bZEu6gzboxd5adUbbrejFZae1u5
    rule_filter: HomeAssistant


---------------------------------------

"""
import logging
import subprocess
import voluptuous as vol
import homeassistant.helpers.config_validation as cv

try:
    from homeassistant.components.switch import SwitchEntity as SwitchDevice
except ImportError:
    from homeassistant.components.switch import SwitchDevice

from homeassistant.components.switch import (
        PLATFORM_SCHEMA, ENTITY_ID_FORMAT)
from homeassistant.const import (
    CONF_FRIENDLY_NAME, CONF_SWITCHES, CONF_VALUE_TEMPLATE, CONF_HOST, CONF_API_KEY, CONF_ACCESS_TOKEN)

CONF_RULE_FILTER = 'rule_filter'

DOMAIN = "switch"
DEFAULT_ICON_ENABLED = 'mdi:check-network-outline'
DEFAULT_ICON_DISABLED = 'mdi:close-network-outline'

REQUIREMENTS = ['pyopnsense==0.0.3']


_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_HOST): cv.string,
    vol.Required(CONF_API_KEY): cv.string,
    vol.Required(CONF_ACCESS_TOKEN): cv.string,
    vol.Optional(CONF_FRIENDLY_NAME): cv.string,
    vol.Optional(CONF_VALUE_TEMPLATE): cv.template,
    vol.Optional(CONF_RULE_FILTER): cv.string,
})


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Initialize the platform"""

    """Setup the opnSense Rules platform."""
    import pprint, sys
    from pyopnsense import client

    # Assign configuration variables. The configuration check takes care they are
    # present.
    host = config.get(CONF_HOST)
    api_key = config.get(CONF_API_KEY)
    access_token = config.get(CONF_ACCESS_TOKEN)
    rule_prefix = config.get(CONF_RULE_FILTER)

    _LOGGER.debug("Connecting to opnSense firewall to collect rules to add as switches.")

    try:
        
        apiLib = client.OPNClient(api_key, access_token,host)

        filters = apiLib._get('firewall/filter/searchRule')

        _LOGGER.debug("Found %s rules in opnSense automation tab", (filters['total']))

        if rule_prefix:
            _LOGGER.debug("Filter for rules starting with %s being applied", rule_prefix)

        rules = []
        # Iterate through and find rules
        i = 0
        for rule in filters['rows']:
            tracker = rule.get('uuid')
            if tracker == None:
                _LOGGER.warning("Skipping rule (no tracker_id): " + rule['description'])
            else:
                if rule_prefix:
                    if (rule['description'].startswith(rule_prefix)):
                        _LOGGER.debug("Found rule %s", rule['description'])
                        new_rule = opnSense('opnSense_'+rule['description'], rule['description'], tracker, host, api_key, access_token, rule_prefix)
                        rules.append(new_rule)
                else:
                    _LOGGER.debug("Found rule %s", rule['description'])
                    new_rule = opnSense('opnSense_'+rule['description'], rule['description'], tracker, host, api_key, access_token, rule_prefix)
                    rules.append(new_rule)
            i=i+1

        # Add devices
        add_entities(rules)
    except Exception as e:
        _LOGGER.error("Problem getting rule set from opnSense host: %s.  Likely due to API key or secret. More Info:" + str(e), host)

class opnSense(SwitchDevice):
    """Representation of an opnSense Rule."""

    def __init__(self, name, rule_name, tracker_id, host, api_key, access_token, rule_prefix):
        _LOGGER.info("Initialized opnSense Rule SWITCH %s", name)
        """Initialize an opnSense Rule as a switch."""
        self._name = name
        self._rule_name = rule_name
        self._state = None
        self._host = host
        self._api_key = api_key
        self._access_token = access_token
        self._tracker_id = tracker_id
        self._rule_prefix = rule_prefix

    @property
    def name(self):
        return self._name

    @property
    def is_on(self):
        return self._state

    @property
    def icon(self):
        if self._state:
            return DEFAULT_ICON_ENABLED
        else:
            return DEFAULT_ICON_DISABLED

    def turn_on(self, **kwargs):
        self.set_rule_state(True)

    def turn_off(self, **kwargs):
        self.set_rule_state(False)

    def update(self):
        """Check the current state of the rule in pfSense"""
        import pprint, sys
        from pyopnsense import client

        if self._rule_prefix:
            if (self._rule_name.startswith(self._rule_prefix)):
                self._name = self._rule_name.replace(self._rule_prefix,'').strip()
        else:
            self._name = self._rule_name

        _LOGGER.debug("Getting opnSense current rule state for %s", self._rule_name)
        try:
            # Setup connection with devices/cloud
            apiLib = client.OPNClient(self._api_key, self._access_token,self._host)

            # Get the current set of filters
            rule = apiLib._get(f'firewall/filter/getRule/{self._tracker_id}')
            _LOGGER.debug("Found rule with tracker %s, updating state.", self._tracker_id)
            if ('1' in rule['rule']['enabled']):
                self._state = True
            else:
                self._state = False
        except:
            _LOGGER.error("Problem retrieving rule set from pfSense host: %s.  Likely due to API key or secret, or rule name", self._host)

    def set_rule_state(self, action):
        """Setup the pfSense Rules platform."""
        import pprint, sys
        from pyopnsense import client

        _LOGGER.debug("Connecting to opnSense firewall to change rule states.")
        try:
            # Setup connection with devices/cloud
            apiLib = client.OPNClient(self._api_key, self._access_token,self._host)

            # Get the current set of filters
            rule = apiLib._get(f'firewall/filter/getRule/{self._tracker_id}')
        except:
            _LOGGER.error("Problem retrieving rule set from pfSense host: %s.  Likely due to API key or secret.", self._host)

        i = 0
        
        _LOGGER.info("Found rule changing state rule: %s", self._rule_name)
        if (action == True):
            if ('0' in rule['rule']['enabled']):
                filters = apiLib._post(f'firewall/filter/toggleRule//{self._tracker_id}','')
                _LOGGER.debug("Rule %s enabled in config", self._rule_name)
        elif (action == False):
            if ('1' in rule['rule']['enabled']):
                filters = apiLib._post(f'firewall/filter/toggleRule//{self._tracker_id}','')
                _LOGGER.debug("Rule %s disabled in config", self._rule_name)
        i=i+1

        try:
            _LOGGER.debug("Sending updated rule set to pfSense firewall")
            # Push the config back to pfSense
            filters = apiLib._post(f'firewall/filter/apply/','')
        except:
            _LOGGER.error("Problem sending & reloading rule set from opnSense host: %s.  Likely due to API key or secret.", self._host)
