def on_countdown_end():
    game.over(True)
info.on_countdown_end(on_countdown_end)

def on_on_overlap(sprite, otherSprite):
    mySprite.start_effect(effects.spray, 200)
    info.change_score_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

projectile: Sprite = None
mySprite: Sprite = None
_2: Sprite = None
info.set_life(3)
info.set_score(200)
scene.set_background_color(10)
mySprite = sprites.create(assets.image("""
    lemon
"""), SpriteKind.player)
controller.move_sprite(mySprite)
mySprite.set_stay_in_screen(True)
info.start_countdown(30)

def on_update_interval():
    global _2
    _2 = sprites.create(img("""
            . . . . c c c c c c . . . . . . 
                    . . . c 6 7 7 7 7 6 c . . . . . 
                    . . c 7 7 7 7 7 7 7 7 c . . . . 
                    . c 6 7 7 7 7 7 7 7 7 6 c . . . 
                    . c 7 c 6 6 6 6 c 7 7 7 c . . . 
                    . f 7 6 f 6 6 f 6 7 7 7 f . . . 
                    . f 7 7 7 7 7 7 7 7 7 7 f . . . 
                    . . f 7 7 7 7 6 c 7 7 6 f c . . 
                    . . . f c c c c 7 7 6 f 7 7 c . 
                    . . c 7 2 7 7 7 6 c f 7 7 7 7 c 
                    . c 7 7 2 7 7 c f c 6 7 7 6 c c 
                    c 1 1 1 1 7 6 f c c 6 6 6 c . . 
                    f 1 1 1 1 1 6 6 c 6 6 6 6 f . . 
                    f 6 1 1 1 1 1 6 6 6 6 6 c f . . 
                    . f 6 1 1 1 1 1 1 6 6 6 f . . . 
                    . . c c c c c c c c c f . . . .
        """),
        SpriteKind.enemy)
game.on_update_interval(5000, on_update_interval)

def on_forever():
    if info.score() < 0:
        info.change_life_by(-1)
        mySprite.start_effect(effects.fire, 5000)
        pause(5000)
        game.over(False)
forever(on_forever)

def on_update_interval2():
    global projectile
    projectile = sprites.create_projectile_from_side(assets.image("""2"""),
        randint(-50, 50),
        randint(-50, 50))
game.on_update_interval(500, on_update_interval2)
