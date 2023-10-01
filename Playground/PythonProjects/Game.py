def setup(self):
    """ Set up the game and initialize the variables. """

    # Create the sprite lists
    self.player_list = arcade.SpriteList()
    self.coin_list = arcade.SpriteList()

    # Score
    self.score = 0

    # Set up the player
    # Character image from kenney.nl
    self.player_sprite = arcade.Sprite("images/character.png", SPRITE_SCALING_PLAYER)
    self.player_sprite.center_x = 50 # Starting position
    self.player_sprite.center_y = 50
    self.player_list.append(self.player_sprite)

    # Create the coins
    for i in range(COIN_COUNT):

        # Create the coin instance
        # Coin image from kenney.nl
        coin = arcade.Sprite("images/coin_01.png", SPRITE_SCALING_COIN)

        # Position the coin
        coin.center_x = random.randrange(SCREEN_WIDTH)
        coin.center_y = random.randrange(SCREEN_HEIGHT)

        # Add the coin to the lists
        self.coin_list.append(coin)
def on_draw(self):
    arcade.start_render()
    self.coin_list.draw()
    self.player_list.draw()
self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)    
MOVEMENT_SPEED = 5

def on_key_press(self, key, modifiers):
    """Called whenever a key is pressed. """

    if key == arcade.key.UP:
        self.player_sprite.change_y = MOVEMENT_SPEED
    elif key == arcade.key.DOWN:
        self.player_sprite.change_y = -MOVEMENT_SPEED
    elif key == arcade.key.LEFT:
        self.player_sprite.change_x = -MOVEMENT_SPEED
    elif key == arcade.key.RIGHT:
        self.player_sprite.change_x = MOVEMENT_SPEED

def on_key_release(self, key, modifiers):
    """Called when the user releases a key. """

    if key == arcade.key.UP or key == arcade.key.DOWN:
        self.player_sprite.change_y = 0
    elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
        self.player_sprite.change_x = 0
    def update(self, delta_time):

     self.physics_engine.update()
self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                     self.wall_list,
                                                     gravity_constant=GRAVITY)