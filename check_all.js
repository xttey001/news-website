const nd = require('./news-data.js');
const dates = Object.keys(nd).filter(k => k !== 'availableDates').sort().reverse();
dates.forEach(d => {
    const wk = nd[d].wukong_judgment;
    const bj = nd[d].bajie_conclusion;
    console.log(d + ': 悟空=' + (!!wk) + ' 八戒=' + (!!bj));
});
