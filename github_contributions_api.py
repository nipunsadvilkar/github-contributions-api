import requests
from bs4 import BeautifulSoup


def get_yearly_contribution_daywise(soup):
    yearly_contri_daywise = []
    for each_rect in soup.find_all('rect'):
        each_rect_attrs = each_rect.attrs
        if int(each_rect_attrs['data-count']) > 0:
            each_day = {}
            each_day['date'] = each_rect_attrs['data-date']
            each_day['count'] = each_rect_attrs['data-count']
            each_day['color'] = each_rect_attrs['fill']
            yearly_contri_daywise.append(each_day)
    return yearly_contri_daywise


def overall_yearly_contributions(soup):
    overall_contributions_tag = soup.findAll("div", {'js-yearly-contributions'})[0]
    overall_number = overall_contributions_tag.h2.get_text()
    return overall_number.strip().split(' ')[0]


if __name__ == '__main__':
    res = requests.get(
        'https://github.com/users/nipunsadvilkar/contributions?from=2016-12-28&to=2016-12-29'
    )
    soup = BeautifulSoup(res.text, features="html5lib")
    yearly_contribution_daywise = get_yearly_contribution_daywise(soup)
    overall_count = overall_yearly_contributions(soup)
    print("Daywise yearly contributions: {}, overall count {}".format(len(yearly_contribution_daywise), overall_count))
