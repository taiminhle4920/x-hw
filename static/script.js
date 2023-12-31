

// code by Tai
function make_tweet(){
    const text = document.getElementById("tweet_text").value;
    console.log(text);
    fetch(`/tweet`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: `text=${text}`,})
        .then((response) => response.text())
        .then(result => document.getElementById('result').textContent = result);
}

// code by Tai

function delete_tweet() {
    const tweetId = document.getElementById('delete_id').value;
    console.log(tweetId);
    fetch(`/delete?tweetId=${tweetId}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(response => response.text())
        .then(result => document.getElementById('result').textContent = result);
}

