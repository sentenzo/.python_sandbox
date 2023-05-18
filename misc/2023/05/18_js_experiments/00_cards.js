(function () {
    var _values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"];
    var _suits = ["♣", "♦", "♠", "♥"];
    this.Deck = function () {
        var _cards = [];
        this.getCount = function () { return _cards.length; };
        for (s in _suits) {
            for (v in _values) {
                _cards.push(new Card(_values[v], _suits[s]));
            }
        }

        this.shuffle = function () {
            for (var n = _cards.length - 1; n > 0; n -= 1) {
                var p = Math.random() * n | 0;
                var c = _cards[n];
                _cards[n] = _cards[p];
                _cards[p] = c;
            }
        }

        this.takeCard = () => _cards.pop();
        this.putCard = (card) => _cards.push(card);

        this.takeNCards = function (n) {
            var r = _cards.slice(0, n);
            _cards = _cards.slice(n);
            return r;
        }
    }

    this.Card = function (value, suit) {
        var _value = value;
        var _suit = suit;
        Object.defineProperties(this, {
            "value": {
                "get": function () { return _value; }
            },
            "suit": {
                "get": function () { return _suit; }
            }
        });
        this.getSymCode = () => "" + value + suit;
        this.toString = this.getSymCode;
        this.print = function () {
            var color = "black";
            if (_suit == "♦" || _suit == "♥") {
                color = "red";
            }
            console.log("%c " + _value + " " + _suit + " ", "color:" + color +
                "; background-color: white; border-radius: 0px 4px 0px 0px; font-weight: bold; border: 1px solid #000;");
        }

        var score = () => _values.indexOf(_value) * 100 + _suits.indexOf(_suit); // 2♠ | 4♦ | 6♦ | 6♣ | 8♦ | J♣ "
        var sortIndex = () => _suits.indexOf(_suit) * 100 + _values.indexOf(_value); // 6♣ | J♣ | 4♦ | 6♦ | 8♦ | 2♠"
        this.sortValue = sortIndex();
        this.scoreValue = score();
    }

    this.Hand = function (cards) {
        var _cards = cards;
        _cards.sort((x, y) => x.scoreValue - y.scoreValue);

        this.toString = () => _cards.reduce((x, y) => x.toString() + " | " + y.toString());

        this.isFlash = function () {
            return _cards.every((x) => x.suit == _cards[0].suit);
        }
    }


}).apply(this);


//d.shuffle();

//d.takeCard().print();

//var crds = d.takeNCards(6);
//var h = new Hand(crds);
//h.toString();

var n = 0;
var sch = 0;
for (var i = 0; i < 100000; i += 1) {
    var d = new Deck();
    d.shuffle();
    while (d.getCount() >= 6) {
        var h = new Hand(d.takeNCards(6));
        n += 1;
        if (h.isFlash()) {
            console.log(h.toString());
            sch += 1;
        }
    }
}

console.log(sch / n); // ~~ 0.000335
