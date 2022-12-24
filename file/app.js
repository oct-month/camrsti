// const dotenv = require('dotenv')
const fs = require('fs')
const express = require('express')
const multer = require('multer')
// const crypto = require('crypto')
const path = require('path')

const logger = require('./logger')
const config = require('./config')


const upload = multer({
    storage: multer.memoryStorage(),
    limits: {
        fileSize: 4 * 1024 * 1024  // 限制4MB
    },
    fileFilter(req, file, cb) {
        var re = /(\.jpg|\.png|\.jpeg)$/i
        if (file.originalname.match(re)) {
            cb(null, true)
        }
        else {
            cb(new Error('仅支持jpg或png图片'), false)
        }
    }
})

const upload2 = multer({
    storage: multer.memoryStorage(),
    limits: {
        fileSize: 4 * 1024 * 1024   // 限制4MB
    },
    fileFilter(req, file, cb) {
        var re = /(\.TXT|\.txt)$/i
        if (file.originalname.match(re)) {
            cb(null, true)
        }
        else {
            cb(new Error('仅支持txt文件'), false)
        }
    }
})

const upload3 = multer({
    storage: multer.memoryStorage(),
    limits: {
        fileSize: 8 * 1024 * 1024   // 限制8MB
    },
    fileFilter(req, file, cb) {
        var re = /(\.xls|\.xlsx)$/i
        if (file.originalname.match(re)) {
            cb(null, true)
        }
        else {
            cb(new Error('仅支持txt文件'), false)
        }
    }
})

const app = express()

// 静态资源 BaseUrl/api/image/*.png
app.use('/api/image', express.static(__dirname + '/public/images'))
app.use('/api/txt', express.static(__dirname + '/public/txts'))
app.use('/api/excel', express.static(__dirname + '/public/excels'))

// 跨域
if (process.env.NODE_ENV !== 'product') {
    app.use('/', (req, res, next) => {
        res.header('Access-Control-Allow-Headers', 'Content-Type, x-requested-with')
        res.header('Access-Control-Allow-Origin', `http://${config.host}:8080`)
        next()
    })
}

app.post('/api/image', (req, res, next) => {
    upload.array('upload')(req, res, (err) => {
        if (err) {
            res.json({
                msg: err.message
            }, 400)
        }
        else {
            var filenames = []
            req.files.forEach(v => {
                var date = new Date().toISOString().replaceAll(':', '')
                var filename = `IMG_${date}` + path.extname(v.originalname)
                filenames.push(filename)
                var filepath = path.join(__dirname, 'public/images', filename)
                if (fs.existsSync(filepath)) {
                    logger.warn(`--${filepath}-- 已存在`)
                }
                fs.writeFileSync(filepath, v.buffer)
            })
            res.json({
                data: filenames
            }, 200)
        }
    })
})

app.post('/api/txt', (req, res, next) => {
    upload2.single('upload')(req, res, (err) => {
        if (err) {
            res.json({
                msg: err.message
            }, 400)
        }
        else {
            var date = new Date().toISOString().replaceAll(':', '')
            var filename = `TXT_${date}` + path.extname(req.file.originalname)
            var filepath = path.join(__dirname, 'public/txts', filename)
            if (fs.existsSync(filepath)) {
                logger.warn(`--${filepath}-- 已存在`)
            }
            fs.writeFileSync(filepath, req.file.buffer)
            res.json({
                data: filename
            }, 200)
        }
    })
})

app.post('/api/excel', (req, res, next) => {
    upload3.single('upload')(req, res, (err) => {
        if (err) {
            res.json({
                msg: err.message
            }, 400)
        }
        else {
            var date = new Date().toISOString().replaceAll(':', '')
            var filename = `EXCEL_${date}` + path.extname(req.file.originalname)
            var filepath = path.join(__dirname, 'public/excels', filename)
            if (fs.existsSync(filepath)) {
                logger.warn(`--${filepath}-- 已存在`)
            }
            fs.writeFileSync(filepath, req.file.buffer)
            res.json({
                data: filename
            }, 200)
        }
    })
})

app.listen(config.serverPort, () => {
    logger.debug(`Server start on http://127.0.0.1:${config.serverPort}`)
})
