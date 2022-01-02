import pygame as pg

def createCard(username, xp, totalXp, level):

  pg.font.init()
  #
  white = (255, 255, 255)
  black = (0,0,0)
  limeGreen = (50,205,50)
  neonPink = (236, 156, 245)

  width = 1000
  height = 400


  #create a font object which can be rendered
  myUsernameFont = pg.font.Font("VT323/VT323-Regular.ttf", 60)
  myXpFont = pg.font.SysFont('"VT323/VT323-Regular.ttf"', 35)

  # create the display window
  win = pg.display.set_mode((width, height))
  # optional title bar caption
  pg.display.set_caption("Pygame draw levelcard and save")


  # default background is black, so make it white
  background = pg.image.load("assets/gradient.png")
  background = pg.transform.scale(background, (1000,500))
  win.blit(background, (0,0))

  #username
  textsurface = myUsernameFont.render(username, False, (0, 0, 0))
  #display username onto screen
  win.blit(textsurface,(260,40))

  #levelText
  levelText = myUsernameFont.render(f"Level {level}", False, (0, 0, 0))
  win.blit(levelText,(260, 120))

  #draws background rect for profile picture
  pg.draw.rect(win, black, pg.Rect(54, 43, 132, 132))
  pg.draw.rect(win, neonPink, pg.Rect(57, 47, 126, 126))

  #avatar
  avatar = pg.image.load("assets/profilepicture.png")
  avatar = pg.transform.scale(avatar, (120,120))

  #avatarRect = avatar.get_rect()
  win.blit(avatar, (60,50))

  #xp bar back
  pg.draw.rect(win, black, pg.Rect(60, 230, 870, 80))

  #xp bar bar
  barLength = (int(xp)/int(totalXp))*850
  pg.draw.rect(win, limeGreen, pg.Rect(70, 240, barLength, 60))

  #totalXp
  xpText = myXpFont.render(f"{xp}/{totalXp} xp", False, (0, 0, 0))
  win.blit(xpText,(800, 200))

 

  # now save the drawing
  # can save as .bmp .tga .png or .jpg
  fname = "assets/levelcard.png"
  pg.image.save(win, fname)
  print("file {} has been saved".format(fname))

  # update the display window to show the drawing
  pg.display.flip()

  pg.quit()





