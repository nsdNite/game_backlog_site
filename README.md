# Games backlog

Website for tracking your backlog of PC video games available on Steam.

## Credits

- Soft UI Design System for a perfect template: [GitHub Repo](https://github.com/app-generator/django-soft-ui-design)
- RDNE Stock project for background: [Pexels](https://www.pexels.com/photo/a-woman-playing-a-video-game-7915289/)
- Leinstay for a great Steam games database: [GitHub Repo](https://github.com/leinstay/steamdb/)

## Overview of Functionality

1. **Great index page thanks to the template.**<br>
   ![Image 1](img.png)

2. **Game list with user level separation.**
   Staff users can update/delete games via the site interface:<br>
   ![Image 2](img_2.png)<br>
   Ordinary users can only add games to the backlog:<br>
   ![Image 3](img_1.png)<br>

3. **Same applies for developer and user views.**<br>
   Staff can update/delete developers.<br>
   ![Image 4](img_3.png)<br>
   Ordinary users can only view the developers list.<br>
   ![Image 5](img_4.png)<br>

4. **Superuser can create/delete a user via the site interface.**<br>
   ![Image 6](img_5.png)<br>

5. **Staff users have no permissions for user creation.**<br>
   ![Image 7](img_6.png)<br>

6. **As you can notice, the drop-down menu is customized according to the user's permissions level.**

7. **Paginated search for games, developers, and users.**<br>
   ![Image 8](img_7.png)<br>

8. **User actions**
   Users can add games to their backlog to monitor completed games.<br>
   If a user can't find a game, they can add it via the drop-down menu "Games->Add game."<br>
   Users can add games to their backlog via the game list or game detail pages:<br>
   ![Image 9](img_8.png)<br>
   ![img_9.png](img_9.png)<br>
   Users can view their/other users' backlog on the account page.<br>
   User viewing their own page:<br>
   ![Image 10](img_10.png)<br>
   User viewing another user's page:<br>
   ![Image 11](img_11.png)<br>

9. **Creation forms**<br>
   **Game:**<br>
   ![Image 12](img_12.png)<br>
   **Developer:**<br>
   ![Image 13](img_13.png)<br>
   **User:**<br>
   ![Image 14](img_14.png)<br>

10. **Additional logic**
    Data in JSON format similar to Leinstay's database can be added via:

> python manage.py importdata

11. **Testcases for Forms, Models and Views**
12. Additional view for TOP 10 GAMES by Metacritic score.
