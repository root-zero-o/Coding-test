var findContentChildren = function(g, s) {
    let answer = 0;
    let obj = {};

    for(let i = 0; i < s.length; i++){
        obj[s[i]] = (obj[s[i]] || 0 ) + 1;
    }
    console.log(obj)
    for(let i = 0; i < g.length; i++){
        if(!!obj[g[i]]){
            answer++;
            obj[g[i]] = obj[g[i]] - 1;
        }
    }

    return answer;
};