# yt-descriptions

## getting input.json
go to `https://www.youtube.com/feed/you` and run this in the console and right-click -> Copy object:
```js
ytInitialData.contents.twoColumnBrowseResultsRenderer.tabs[0].tabRenderer.content.sectionListRenderer.contents[2].itemSectionRenderer.contents[0].shelfRenderer.content.gridRenderer.items.map(x => x.gridPlaylistRenderer).filter(x => x !== undefined).map(x => new Object({ title: x.title.simpleText, playlistId: x.playlistId }))
```
note that you can also add filtering to the end of the command, for example:
```js
x.filter(x => /^S[1-9]/.test(x.title))
// where x = output of the previous command
```

---

ignore changes to `input.json`: `git update-index --skip-worktree input.json`  
(source: https://www.google.com/search?q=git+ignore+future+changes+to+file -> https://stackoverflow.com/a/39776107/17299754)
