var express = require('express');
var router = express.Router();

router.get('/cool', function(req, res, next) {
  res.render('index', { title: 'Rat' });
});

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

module.exports = router;
