# Core imports
from django.db import models


class Player(models.Model):
    id = models.IntegerField(
        primary_key=True
    )
    asset_id = models.IntegerField()
    first_name = models.CharField(
        max_length=100
    )
    last_name = models.CharField(
        max_length=100
    )
    common_name = models.CharField(
        max_length=100
    )
    overall_rating = models.IntegerField(
        blank=True,
        null=True
    )
    card_att1 = models.IntegerField(
        blank=True,
        null=True
    )
    card_att2 = models.IntegerField(
        blank=True,
        null=True
    )
    card_att3 = models.IntegerField(
        blank=True,
        null=True
    )
    card_att4 = models.IntegerField(
        blank=True,
        null=True
    )
    card_att5 = models.IntegerField(
        blank=True,
        null=True
    )
    card_att6 = models.IntegerField(
        blank=True,
        null=True
    )
    card_type = models.IntegerField(
        blank=True,
        null=True
    )
    item_type = models.CharField(
        max_length=100,
        blank=True
    )
    card_set = models.CharField(
        max_length=100,
        blank=True
    )
    club = models.ForeignKey(
        'clubs.Club',
        to_field='asset_id',
        blank=True,
        null=True,
        related_name='players'
    )
    league = models.ForeignKey(
        'leagues.League',
        to_field='asset_id',
        blank=True,
        null=True,
        related_name='players'
    )
    nation = models.ForeignKey(
        'nations.Nation',
        to_field='asset_id',
        blank=True,
        null=True,
        related_name='players'
    )
    shirt_number = models.IntegerField(
        blank=True,
        null=True
    )
    dob = models.DateField(
        blank=True,
        null=True
    )
    join_date = models.DateField(
        blank=True,
        null=True
    )
    height = models.IntegerField(
        blank=True,
        null=True
    )
    weight = models.IntegerField(
        blank=True,
        null=True
    )
    role_line = models.CharField(
        max_length=100
    )
    role = models.CharField(
        max_length=100,
        blank=True
    )
    prefferred_foot = models.CharField(
        max_length=100
    )
    weak_foot = models.IntegerField(
        blank=True,
        null=True
    )
    skill_moves = models.IntegerField(
        blank=True,
        null=True
    )
    att_workrate = models.CharField(
        max_length=100
    )
    def_workrate = models.CharField(
        max_length=100
    )
    acceleration = models.IntegerField(
        blank=True,
        null=True
    )
    sprint_speed = models.IntegerField(
        blank=True,
        null=True
    )
    agility = models.IntegerField(
        blank=True,
        null=True
    )
    balance = models.IntegerField(
        blank=True,
        null=True
    )
    jumping = models.IntegerField(
        blank=True,
        null=True
    )
    stamina = models.IntegerField(
        blank=True,
        null=True
    )
    strength = models.IntegerField(
        blank=True,
        null=True
    )
    reactions = models.IntegerField(
        blank=True,
        null=True
    )
    aggression = models.IntegerField(
        blank=True,
        null=True
    )
    interceptions = models.IntegerField(
        blank=True,
        null=True
    )
    positioning = models.IntegerField(
        blank=True,
        null=True
    )
    vision = models.IntegerField(
        blank=True,
        null=True
    )
    ball_control = models.IntegerField(
        blank=True,
        null=True
    )
    crossing = models.IntegerField(
        blank=True,
        null=True
    )
    dribbling = models.IntegerField(
        blank=True,
        null=True
    )
    finishing = models.IntegerField(
        blank=True,
        null=True
    )
    free_kick_accuracy = models.IntegerField(
        blank=True,
        null=True
    )
    heading_accuracy = models.IntegerField(
        blank=True,
        null=True
    )
    long_passing = models.IntegerField(
        blank=True,
        null=True
    )
    short_passing = models.IntegerField(
        blank=True,
        null=True
    )
    marking = models.IntegerField(
        blank=True,
        null=True
    )
    long_shots = models.IntegerField(
        blank=True,
        null=True
    )
    shot_power = models.IntegerField(
        blank=True,
        null=True
    )
    standing_tackle = models.IntegerField(
        blank=True,
        null=True
    )
    sliding_tackle = models.IntegerField(
        blank=True,
        null=True
    )
    volleys = models.IntegerField(
        blank=True,
        null=True
    )
    curve = models.IntegerField(
        blank=True,
        null=True
    )
    penalties = models.IntegerField(
        blank=True,
        null=True
    )
    gk_diving = models.IntegerField(
        blank=True,
        null=True
    )
    gk_handling = models.IntegerField(
        blank=True,
        null=True
    )
    gk_kicking = models.IntegerField(
        blank=True,
        null=True
    )
    gk_reflexes = models.IntegerField(
        blank=True,
        null=True
    )
    gk_positioning = models.IntegerField(
        blank=True,
        null=True
    )
    desc = models.CharField(
        max_length=100,
        blank=True
    )
    created = models.DateTimeField(
        blank=True,
        null=True
    )
    modified = models.DateTimeField(
        blank=True,
        null=True
    )
    slug = models.CharField(
        max_length=50,
        blank=True
    )

    @models.permalink
    def get_absolute_url(self):
        return 'players:player', (), {
            'slug': self.slug
        }

    class Meta:
        db_table = 'players_14'
        ordering = ['-overall_rating']

    def __unicode__(self):
        return self.common_name

    def card_colour(self):
        if self.card_type == 12:
            return 'player-card-legend'
        elif self.card_type == 5:
            return 'player-card-motm'
        elif self.overall_rating > 74 and self.card_type == 3:
            return 'player-card-gold player-card-tots'
        elif self.overall_rating > 74 and self.card_type == 2:
            return 'player-card-gold player-card-if'
        elif self.overall_rating > 74 and self.card_type == 1:
            return 'player-card-gold player-card-rare'
        elif self.overall_rating > 74 and self.card_type == 0:
            return 'player-card-gold player-card-nonrare'
        elif 65 <= self.overall_rating <= 74 and self.card_type == 3:
            return 'player-card-silver player-card-tots'
        elif 65 <= self.overall_rating <= 74 and self.card_type == 2:
            return 'player-card-silver player-card-if'
        elif 65 <= self.overall_rating <= 74 and self.card_type == 1:
            return 'player-card-silver player-card-rare'
        elif 65 <= self.overall_rating <= 74 and self.card_type == 0:
            return 'player-card-silver player-card-nonrare'
        elif self.overall_rating < 65 and self.card_type == 3:
            return 'player-card-bronze player-card-tots'
        elif self.overall_rating < 65 and self.card_type == 2:
            return 'player-card-bronze player-card-if'
        elif self.overall_rating < 65 and self.card_type == 1:
            return 'player-card-bronze player-card-rare'
        else:
            return 'player-card-bronze player-card-nonrare'

    def card_name(self):
        player_name = self.common_name
        return player_name.rsplit()[-1]

    def position(self):
        role = {
            '0': 'GK',
            '2': 'RWB',
            '3': 'RB',
            '5': 'CB',
            '7': 'LB',
            '8': 'LWB',
            '10': 'CDM',
            '12': 'RM',
            '14': 'CM',
            '16': 'LM',
            '18': 'CAM',
            '21': 'CF',
            '23': 'RW',
            '25': 'ST',
            '27': 'LW'
        }
        if self.role in role:
            return role[self.role]

    def workrate_att(self):
        wr = {
            '0': 'Medium',
            '1': 'Low',
            '2': 'High'
        }
        if self.att_workrate in wr:
            return wr[self.att_workrate]

    def workrate_def(self):
        wr = {
            '0': 'Medium',
            '1': 'Low',
            '2': 'High'
        }
        if self.def_workrate in wr:
            return wr[self.def_workrate]

    def att_1_label(self):
        if self.role == '0':
            return 'DIV'
        else:
            return 'PAC'

    def att_2_label(self):
        if self.role == '0':
            return 'HAN'
        else:
            return 'SHO'

    def att_3_label(self):
        if self.role == '0':
            return 'KIC'
        else:
            return 'PAS'

    def att_4_label(self):
        if self.role == '0':
            return 'REF'
        else:
            return 'DRI'

    def att_5_label(self):
        if self.role == '0':
            return 'SPE'
        else:
            return 'DEF'

    def att_6_label(self):
        if self.role == '0':
            return 'POS'
        else:
            return 'HEA'