sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Food, function (sprite, otherSprite) {
    mySprite.startEffect(effects.bubbles, 2000)
    sprite.destroy()
})
info.onCountdownEnd(function () {
    game.over(true)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function (sprite, otherSprite) {
    mySprite.startEffect(effects.spray, 200)
    info.changeScoreBy(-1)
})
let projectile: Sprite = null
let mySprite: Sprite = null
info.setLife(3)
info.setScore(200)
let mySprite2 = sprites.create(img`
    . . . b b b b b b b b b . . . . 
    . . b 1 d d d d d d d 1 b . . . 
    . b 1 1 1 1 1 1 1 1 1 1 1 b . . 
    . b d b c c c c c c c b d b . . 
    . b d c 6 6 6 6 6 6 6 c d b . . 
    . b d c 6 d 6 6 6 6 6 c d b . . 
    . b d c 6 6 6 6 6 6 6 c d b . . 
    . b d c 6 6 6 6 6 6 6 c d b . . 
    . b d c 6 6 6 6 6 6 6 c d b . . 
    . b d c c c c c c c c c d b . . 
    . c b b b b b b b b b b b c . . 
    c b c c c c c c c c c c c b c . 
    c 1 d d d d d d d d d d d 1 c . 
    c 1 d 1 1 d 1 1 d 1 1 d 1 1 c . 
    c b b b b b b b b b b b b b c . 
    c c c c c c c c c c c c c c c . 
    `, SpriteKind.Food)
scene.setBackgroundColor(10)
mySprite = sprites.create(assets.image`lemon`, SpriteKind.Player)
controller.moveSprite(mySprite)
mySprite.setStayInScreen(true)
info.startCountdown(30)
forever(function () {
    if (info.score() < 0) {
        info.changeLifeBy(-1)
        mySprite.startEffect(effects.fire, 5000)
        mySprite.destroy()
        pause(5000)
        game.over(false)
    }
    if (info.score() < 100) {
        mySprite.startEffect(effects.starField)
    }
})
game.onUpdateInterval(500, function () {
    projectile = sprites.createProjectileFromSide(assets.image`2`, randint(-50, 50), randint(-50, 50))
})
