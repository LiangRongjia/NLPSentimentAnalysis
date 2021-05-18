/* 引入文件模块，用于搜索控制器 .js 文件 */
const fs = require('fs')

/* 
 * 导出控制器函数
 * 职能：添加所有控制器
 * 传入参数：控制器所在目录的相对路径（非必需，默认为 controllers）
 */
module.exports = function () {
    /* 引入 koa-router 模块，创建 router 实例 */
    const router = require('koa-router')()

    /* 添加所有控制器 */
    addControllers(router)

    /* 返回 router.routes()，将被添加为中间件执行 */
    return router.routes()
}

/* 注册控制器内每个映射 */
function addMapping(router, mapping) {
    for (let url in mapping) {
        if (url.startsWith('GET ')) {
            const path = url.substring(4)
            router.get(path, mapping[url])
        }
        else if (url.startsWith('POST ')) {
            const path = url.substring(5)
            router.post(path, mapping[url])
        }
        else if (url.startsWith('PUT ')) {
            const path = url.substring(4)
            router.put(path, mapping[url])
        }
        else if (url.startsWith('DELETE ')) {
            const path = url.substring(7)
            router.del(path, mapping[url])
        }
    }
}

/* 添加所有控制器 */
function addControllers(router) {
    fs.readdirSync(`${__dirname}/controllers`)
        .filter(f => f.endsWith('.js'))
        .forEach(f => {
            console.log(`process controller: ${f}...`)
            const mapping = require(`${__dirname}/controllers/${f}`)
            addMapping(router, mapping)
        })
}