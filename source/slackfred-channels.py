import sys
import argparse
from workflow import Workflow, web, PasswordNotFound


def slack_keys():
    wf_password = Workflow()
    try:
        slack_keys = wf_password.get_password('slack_api_key')
    except PasswordNotFound:
        wf.add_item(title='No API key set. Please run slt',
                    valid=False)
        wf.send_feedback()
        return 0
    keys = slack_keys.split(",")

    return keys


def slack_channels(keys):
    channels_list = []
    for key in keys:
        api_key = str(key)
        slack_auth = web.get('https://slack.com/api/auth.test?token=' + api_key + '&pretty=1').json()
        if slack_auth['ok'] is False:
            wf.add_item(title='Authentication failed. Check your API key',
                        valid=False)
            wf.send_feedback()
            break
        else:
            channels = web.get('https://slack.com/api/channels.list?token=' + api_key + '&count=50&pretty=1').json()
            for channel in channels['channels']:
                channels_list.append({'team': slack_auth['team'],'name': channel['name'], 'member': channel['is_member']
                    , 'id': channel['id']})

    return channels_list


def search_slack_channels(channels):
    elements = []
    elements.append(channels['name'])
    return u' '.join(elements)


def leave_channel(keys, query):
    for key in keys:
        api_key = str(key)
        channels_list = web.get('https://slack.com/api/channels.list?token=' + api_key + '&pretty=1').json()
        for channels in channels_list['channels']:
            if query == channels['name']:
                web.get('https://slack.com/api/channels.leave?token=' + api_key + '&channel=' + channels['id'] + '&pretty=1')

def join_channel(keys, query):
    for key in keys:
        api_key = str(key)
        channels_list = web.get('https://slack.com/api/channels.list?token=' + api_key + '&pretty=1').json()
        for channels in channels_list['channels']:
            if query == channels['name']:
                web.get('https://slack.com/api/channels.join?token=' + api_key + '&name=' + query + '&pretty=1')

def main(wf):

    parser = argparse.ArgumentParser()
    parser.add_argument('--join', nargs='?')
    parser.add_argument('--leave', dest='leave', nargs='?')
    parser.add_argument('query', nargs='?', default=None)
    args = parser.parse_args(wf.args)

    if args.leave:
        leave_channel(keys=slack_keys(), query=args.leave)
    elif args.join:
        join_channel(keys=slack_keys(), query=args.join)

    def wrapper():
        return slack_channels(keys=slack_keys())

    channels_list = wf.cached_data('channels', wrapper, max_age=60)

    query = args.query

    if query:
        channels_list = wf.filter(query, channels_list, key=search_slack_channels)

    for channels in channels_list:
        if channels['member'] == True:
            wf.add_item(title=channels['name']+' - '+channels['team'],
                subtitle='Member',
                arg=channels['name'],
                valid=True)
        elif channels['member'] == False:
            wf.add_item(title=channels['name']+' - '+channels['team'],
                subtitle='Not a member',
                arg=channels['name'],
                valid=True)

    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))