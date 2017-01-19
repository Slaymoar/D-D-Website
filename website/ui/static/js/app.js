window.onload = function() {

    function getName(player) {
        var val = player.val();
        if (!val) {
            val = player.attr('placeholder');
        }
        return val;
    }

    function saveGame(data) {
        $.ajax({
            'url': '/api/games',
            'async': true,
            'method': 'POST',
            'dataType': 'json',
            'data': JSON.stringify(data)
        }).done(function(data, status, xhr) {
            createGamesTable(data.games);
        }).fail(function()  {
            alert("Failed to save the game!");
        });

        // this happens immediately after the ajax starts to make the request.
    }

    function onClick(event) {
        var player1 = $('.player[data-player=player1]');
        var player2 = $('.player[data-player=player2]');
        var playerContainer = $(event.currentTarget).parents('.player');
        var nameInput = $(event.currentTarget).parents('.player').find(".name input[type=text]");
        var name = getName(nameInput);
        
        var direction = $(event.currentTarget).attr('data-direction');
        
        var scoreInput = $(event.currentTarget).parents('.player').find(".score input[type=text]");
        var score = parseInt(scoreInput.val());

        if (direction === "minus") {
            score -= 1;
        } else if (direction === "plus") {
            score += 1;
        }

        scoreInput.val(score);

        if (score <= 0) {
            var winner;
            if (playerContainer.next('.player').length > 0) {
                winner = playerContainer.next('.player');
            }
            if (playerContainer.prev('.player').length > 0) {
                winner = playerContainer.prev('.player');
            }
            if (winner) {
                var message = getName(winner.find(".name input[type=text]")) + " wins!!!";
                var data = {
                    "player1_name": player1.find("#name1").val() || player1.find("#name1").attr('placeholder'),
                    "player1_score": parseInt(player1.find("#score1").val()),
                    "player2_name": player2.find("#name2").val() || player2.find("#name2").attr('placeholder'),
                    "player2_score": parseInt(player2.find("#score2").val()),
                    "timestamp": Number(new Date())
                };
                window.setTimeout(function() {
                    saveGame(data);
                }.bind(data), 20);

                $(".score input[type=text]").val(20);
            }
        }
    }

    $("button").on('click', onClick);


    function createGamesTable(games) {
        console.log("games", games);
        // #todo sort the list of games
        var table = $('.table[data-id=games] table');
        var tbody = table.find("tbody");
        tbody.html("");
        for(i=0; i<games.length; i++) {
            var game = games[i];
            tbody.prepend("<tr><td>" + new Date(game.timestamp) + "</td><td>" + game.player1_name + "</td><td>" + game.player1_score + "</td><td>" + game.player2_name + "</td><td>" + game.player2_score + "</td></tr>");
        }
    };

    $.ajax({
        'url': '/api/games',
        'async': true,
        'method': 'GET',
        'dataType': 'json'
    }).done(function(data, status, xhr) {
        if (status === "success" && data.games) {
            createGamesTable(data.games);
        }
    }).fail(function()  {
        // @todo
        // add something for the failure case
        // maybe grey out the table and say, "could not load data at this time"

        // if (status === "failure") {
        //
        // }

    });


};