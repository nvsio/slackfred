slackfred
=========

![](http://i.imgur.com/Vy78c78.gif)

Alfred workflow to interact, and perform various functions with the service [Slack](http://slack.com/). Now with multi-team support!

I'm currently in the process of getting this updated to work with multiple organizations where possible, as well as adding some extra workflow options like private groups, stars and a few more things. Stay tuned!

## Getting started
1. Install slackfred by visiting the download page in Github or via the [Packal page](http://www.packal.org/workflow/slackfred)
2. Open alfred and type `slt`, then hold `cmd` (apple key) and press `enter`. This will open up the Slack API page. Then look for your team (make sure you're logged in) near the bottom. Next to your team name will be your token.
3. Launch alfred and re-run `slt` to enter your token. 

##### Multi-team use instructions
In order to use the workflow with multiple organizations you will need to enter all of your keys as comma seperated strings with **no** spaces.  
Example: `team-org-api-token-1,team-org-api-token-2`

## Currently Available Functionality:
* `slk`: Let's you switch easily between channels, groups and IMs. Thanks to [buzali](https://github.com/buzali) for getting this working with Slack's URL scheme.
* `slt`: Set your API Token
  * Open alfred and type `slt`, then paste your token. If you don't have a token, then hold `cmd` to open the API page to get one (look for your team near the bottom of the page).
* `slm`: Send messages to a channel
  * Open alfred and type `slm` to populate channels. Use your arrow keys to select a channel and hit TAB. Then you can enter your message and hit ENTER.
* `slf`: Search files
  * Open alfred and type `slf` to search files. Selecting a file opens it in your browser
* `slp`: Set your presence
  * Open alfred and type `slp active` or `slp away`
* `slc`: View, leave and join channels or private groups
  * Open alfred and type `slc` to display a searchable list of channels. Selecting a channel with `alt` leaves and `ctrl` lets you join. Currently only `alt` is functional with groups.
* `slclr`: Clear unread messages
  * This currently only marks Channels as read and not groups. Depending on the size of your organizations this can also take a few seconds to run.
* `slim`: Enter a users name to search for most recent DM messages
* `slr`: Search your starred items
  * Highlight a result and hitting enter opens the web client to that result
* `sls`: Perform a query across all your channels in your organizations
  * Highlight a result and hitting enter opens the web client to that result
  * Depending on the size of your organization this can take a few seconds to run


## To-do
* Create a smoother API key/token process
* Improve speed and performance

This workflow was created in Python with the help of [Dean Jackson's](https://github.com/deanishe/alfred-workflow) Alfred  library and the [Requests](http://docs.python-requests.org/en/latest/) library.
