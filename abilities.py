class ability(object):

    """Contain information about abilities"""

    def __init__(self, name, type, cooldown, damage=None, stun_damage=None,
                 stuns=False, bleeds=False):
        """Setup ability name, type, cooldown, and damage is applicable

        Parameters
        ----------
        name : string
            Name of the ability
        type : {'Melee', 'Range', 'Magic', 'Defensive'}
            Describes the type of ability
        cooldown : int
            Number of seconds the ability has for a cooldown
        damage : (optional) float
            Average damage value for the ability
        stun_damage : (optional) float
            Average damage value for the ability when the target is stunned
        stuns : (optional) boolean
            true if the ability stuns or binds the opponent, false otherwise
        bleeds : (optional) boolean
            true if the ability applies a bleed, false otherwise
        """

        self._name = name
        self._type = type.lower()
        self._cooldown = cooldown
        self._damage = damage
        self._stun_damage = stun_damage
        self._stuns = stuns
        self._bleeds = bleeds

    def get_damage(self, is_stunned):
        """Returns the average damage of the ability

        Parameters
        ----------
        is_stunned : boolean
            true if the target is stunned, false otherwise

        Returns
        -------
        float : average damage of the Ability
        """
        if(is_stunned):
            return(self._stun_damage)
        return(self._damage)
