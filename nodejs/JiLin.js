const request = require('request')
const cheerio = require('cheerio')

function login_and_run(username, password) {
  request.post('https://www.zaocanjun.com/chengji/cj2.php', {
    form: {
      zh: username,
      mm: password,
      jizhu: 'on'
    }
  }, function (error, response, body) {
    if (error) {
      return error
    } else if (response.statusCode !== 200) {
      return 'response.statusCode != 200'
    }

    console.log(body)
    console.log(analysis(body))
  }).json()
}

function analysis(html) {
  const $ = cheerio.load(html)
  const name_id = $('.weui_panel_hd').first().contents().text().match(new RegExp(/(.*?)（(.*?)）成绩如下/, 'i'))

  const results = []
  $('.weui_media_box').each(function (i, elem) {
    const result = {}
    const title = $(elem).children('.weui_media_title').text().match(new RegExp(/\s+(.*?)\s((.*?)+)/, 'i'))
    if (title) {
      result['record'] = title[1]
      result['title'] = title[2]
    } else {
      return 'get record and title error'
    }

    const detail = $(elem).children('.weui_media_desc').text().match(new RegExp(/(.*?)  绩点:(.*?)  学分:(.*?)  是否为重修:(.)/, 'i'))
    if (detail) {
      results.push(Object.assign(result, {
        term: detail[1],
        gpa: detail[2],
        credit: detail[3],
        restudy: detail[4]
      }))
    } else {
      return 'get detail error'
    }
  })

  return {
    id: name_id[2],
    name: name_id[1],
    results: results
  }
}
