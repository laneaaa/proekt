from PIL import Image, ImageFont, ImageDraw
from functions.getStatistics import player_stat


class Drawing:
    def __init__(self, obj: list[list[str | list]]):
        self.img: Image = Image.open(fp='assets/images/statistics.png')
        self.obj = obj

        self.draw: ImageDraw = ImageDraw.Draw(self.img)

        self.players_font_path: str = 'assets/fonts/montserrat.ttf'
        self.meta_font_path: str = 'assets/fonts/RoadRadio.ttf'
        self.titles_font_path: str = 'assets/fonts/montserrat.ttf'

        self.players_font: ImageFont = ImageFont.truetype(self.players_font_path, size=50)
        self.titles_font: ImageFont = ImageFont.truetype(self.meta_font_path, size=80)
        self.rounds_font: ImageFont = ImageFont.truetype(self.meta_font_path, size=40)

        self.font_border: int = 0

    def start_drawing(self, rounds: int = 0, matches: list | tuple = None):

        first_team_name: str = self.obj[0][0]
        first_team_list: list = self.obj[0][1]

        second_team_name: str = self.obj[1][0]
        second_team_list: list = self.obj[1][1]

        fy: int = 817
        sy: int = 1757

        good = '#00ff00'
        norm = '#ffff00'
        huinia = '#ff0000'

        for player in first_team_list:
            player: dict = player_stat(*player, rounds=rounds)

            self.draw.text((400, fy), f'{player.get("nickname")}', font=self.players_font,
                           stroke_width=self.font_border, stroke_fill='white')

            self.draw.text((1400, fy), f'{player.get("kills")} - {player.get("deaths")}', font=self.players_font,
                           stroke_width=self.font_border, stroke_fill='white')

            offset = (len(str(player.get("diff"))) - 1) * 10

            self.draw.text((1690 - offset, fy), f'{player.get("diff")}', font=self.players_font,
                           stroke_width=self.font_border, stroke_fill='white')

            if player.get("kd") < 0.8:
                color = huinia
            elif player.get("kd") >= 0.9:
                color = good
            else:
                color = norm

            kd = str(player.get("kd")) + '0' if len(str(player.get("kd"))) == 3 else str(player.get("kd"))

            self.draw.text((1900, fy), f'{kd}', font=self.players_font,
                           stroke_width=self.font_border, stroke_fill='white', fill=color)

            self.draw.text((2150, fy), f'{player.get("dpr")}', font=self.players_font,
                           stroke_width=self.font_border, stroke_fill='white')

            self.draw.text((2375, fy), f'{player.get("kpr")}', font=self.players_font,
                           stroke_width=self.font_border, stroke_fill='white')

            if player.get("impact") <= 0.8:
                color = huinia
            elif player.get("impact") >= 1.1:
                color = good
            else:
                color = norm

            impact = str(player.get("impact")) + '0' if len(str(player.get("impact"))) == 3 else str(
                player.get("impact"))

            self.draw.text((2575, fy), impact, font=self.players_font,
                           stroke_width=self.font_border, stroke_fill='white', fill=color)

            self.draw.text((2825, fy), f'{player.get("rating")}', font=self.players_font,
                           stroke_width=self.font_border, stroke_fill='white')

            fy += 105

        for player in second_team_list:
            player: dict = player_stat(*player, rounds=rounds)

            self.draw.text((400, sy), f'{player.get("nickname")}', font=self.players_font,
                           stroke_width=self.font_border, stroke_fill='white')

            self.draw.text((1400, sy), f'{player.get("kills")} - {player.get("deaths")}', font=self.players_font,
                           stroke_width=self.font_border, stroke_fill='white')

            offset = (len(str(player.get("diff"))) - 1) * 10

            self.draw.text((1690 - offset, sy), f'{player.get("diff")}', font=self.players_font,
                           stroke_width=self.font_border, stroke_fill='white')

            if player.get("kd") < 0.8:
                color = huinia
            elif player.get("kd") >= 0.9:
                color = good
            else:
                color = norm

            kd = str(player.get("kd")) + '0' if len(str(player.get("kd"))) == 3 else str(player.get("kd"))

            self.draw.text((1900, sy), f'{kd}', font=self.players_font,
                           stroke_width=self.font_border, stroke_fill='white', fill=color)

            self.draw.text((2150, sy), f'{player.get("dpr")}', font=self.players_font,
                           stroke_width=self.font_border, stroke_fill='white')

            self.draw.text((2375, sy), f'{player.get("kpr")}', font=self.players_font,
                           stroke_width=self.font_border, stroke_fill='white')

            if player.get("impact") <= 0.8:
                color = huinia
            elif player.get("impact") >= 1.1:
                color = good
            else:
                color = norm

            impact = str(player.get("impact")) + '0' if len(str(player.get("impact"))) == 3 else str(
                player.get("impact"))

            self.draw.text((2575, sy), impact, font=self.players_font,
                           stroke_width=self.font_border, stroke_fill='white', fill=color)

            self.draw.text((2825, sy), f'{player.get("rating")}', font=self.players_font,
                           stroke_width=self.font_border, stroke_fill='white')

            sy += 105

        self.draw.text((400, 460), f'{first_team_name}', font=self.titles_font,
                       stroke_width=self.font_border, stroke_fill='white')

        self.draw.text((400, 1410), f'{second_team_name}', font=self.titles_font,
                       stroke_width=self.font_border, stroke_fill='white')

        x: int = 540

        for i, match in enumerate(matches):

            map_name: str = match[0]
            first_team_rounds: int = match[1][0]
            second_team_rounds: int = match[1][1]

            first_team_rnds = f'{map_name}: {first_team_rounds},'
            second_team_rnds = f'{map_name}: {second_team_rounds},'

            amount_of_maps = len(matches)

            if i == amount_of_maps - 1:
                first_team_rnds = first_team_rnds[:-1]
                second_team_rnds = second_team_rnds[:-1]

            self.draw.text((x, 637), first_team_rnds, font=self.rounds_font,
                           stroke_width=self.font_border, stroke_fill='white')

            self.draw.text((x, 1582), second_team_rnds, font=self.rounds_font,
                           stroke_width=self.font_border, stroke_fill='white')

            x += 230

    def show(self):
        self.img.show()

    def save(self, fp: str = 'result.png'):
        self.img.save(fp=fp)

    def start(self, rounds: int = 0, matches: list | tuple = None):
        self.start_drawing(rounds=rounds, matches=matches)


if __name__ == '__main__':
    mn = ['Breeze', 'Province']
    evRo = [(10, 8), (10, 6)]
    m = list(zip(mn, evRo))
    ftn = 'Saints'
    stn = 'Mad Bulls'
    ft = [('Lunax', 35, 23, 7),
          ('Pronix', 28, 22, 7),
          ('Sid', 24, 19, 6),
          ('Rizon', 27, 23, 5),
          ('Gentleman', 18, 25, 4)]
    st = [('ZiseXC', 26, 25, 6),
          ('kivi', 26, 26, 2),
          ('neGro', 22, 24, 8),
          ('nigahtning', 15, 28, 5),
          ('plakus', 17, 30, 4)]
    ftt: int = sum(i[0] for i in evRo)
    stt: int = sum(i[1] for i in evRo)
    tpt: tuple = (ftt, stt)
    aor: int = sum(tpt)

    data = [[ftn, ft], [stn, st]]

    drawing = Drawing(data)
    drawing.start(rounds=aor, matches=m)
    drawing.save()
