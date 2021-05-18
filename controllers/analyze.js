const pyAnalyze = global.pyAnalyze

module.exports = {
    'POST /analyze': async (ctx, next) => {
        ctx.response.body = await analyzeByPython(ctx.request.body)
    }
}

async function analyzeByPython(commentsString = '[]') {
    const comments = JSON.parse(commentsString)
    let result = []
    for (let i = 0; i < comments.length; i++) {
        result.push(await pyAnalyze(comments[i] + '\n'))
    }
    return { data: result }
}
