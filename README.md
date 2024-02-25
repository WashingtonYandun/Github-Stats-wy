# Github-Stats-wy

Github Stats Card for readme files in GitHub.

SVG cards for your GitHub profile, repositories, and languages.

> [!WARNING]
> The UI is not the best, but it works. I will be improving it in the future.
> There are some bugs that I will be fixing soon.

> [!IMPORTANT]
> If you have any suggestions, please let me know. I will be happy to receive your feedback.
> Feel free to contribute to the project.
> Thanks for using it. Remember to give it a star if you like it.

## Cards

-   Github language stats card for your profile based on the number of repositories you have in each language. (The most representative)

-   (Soon) Github language stats card for a specific repository based on the number of lines of code you have in each language.

-   (Soon) Github Profile Stats Card for your profile based on the number of repositories, stars, followers, and following.

-   (Soon) Github Profile Stats Card for a specific repository based on the number of stars, forks, issues, and pull requests.

### Language Card

Based on the number of repositories you have in each language.

There are three types of cards:

-   Bar Chart
-   Pie Chart
-   Donut Chart

#### Example of how to use it

```md
[![WashingtonYandun's stats](https://github-stats-wy.vercel.app/langs/username/chart)]
```

-   The `username` is the username of the user you want to get the stats from (GitHub user).
-   The `chart` is the type of chart you want to use. It can be `bar`, `pie`, or `donut`.

For example:

```md
[![WashingtonYandun's stats](https://github-stats-wy.vercel.app/langs/washingtonyandun/bar)]
```

```md
[![WashingtonYandun's stats](https://github-stats-wy.vercel.app/langs/washingtonyandun/pie)]
```

```md
[![WashingtonYandun's stats](https://github-stats-wy.vercel.app/langs/washingtonyandun/donut)]
```

#### Example of how it looks

| Bar Chart                                                                   | Pie Chart                                                                   | Donut Chart                                                                     |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| ![Bar Chart](https://github-stats-wy.vercel.app/langs/washingtonyandun/bar) | ![Pie Chart](https://github-stats-wy.vercel.app/langs/washingtonyandun/pie) | ![Donut Chart](https://github-stats-wy.vercel.app/langs/washingtonyandun/donut) |

## Graph customization

You can customize the graph by adding the following parameters to the URL (In the future, I will add more customization options):

-   `border_color`: The color of the border of the graph in hexadecimal format. Example: `border_color=000000`

-   `background_color`: The color of the background of the graph in hexadecimal format. Example: `background_color=000000`

-   `title_color`: The color of the title of the graph in hexadecimal format. Example: `title_color=000000`

-   `text_color`: The color of the text of the graph in hexadecimal format. Example: `text_color=000000`

-   `hole_radius_percentage`: The percentage of the hole in the donut chart. Example: `hole_radius_percentage=50`

Here is one example of how to use it:

```md
[![WashingtonYandun's GitHub stats](https://github-stats-wy.vercel.app/langs/washingtonyandun/donut?hole_radius_percentage=60&border_color=00ff00&background_color=ff22&title_color=00ff00&text_color=00ff00)]
```

Example of how it looks:

![WashingtonYandun's stats](https://github-stats-wy.vercel.app/langs/washingtonyandun/donut?hole_radius_percentage=60&border_color=00ff00&background_color=ff22&title_color=00ff00&text_color=00ff00)
