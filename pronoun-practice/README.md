# German Pronoun Practice

Add to your terminal prompt for extra fun!

```
Translate: the Fruit as genative
Answer: 
```

Enjoy being wrong *all the time*

```
Translate: the Fruit as genative
Answer: des Obst
WRONG: des Obsts
```

Just as unforgiving as oma down the street who used to be a grammar teacher

```
Translate: we dative
Answer: uns
Slow.
```

Bonus: logs data to `~/.de_practice` so someday you can make graphs showing how long it took you to finally nail german pronouns.


time               | def/indef | gender | case | Right? | Observed   | Expected   | Response Speed
----               | --------- | ------ | ---- | ------ | --------   | --------   | --------------
1512942119.6173344 | the       | n      | nom  | False  | das Obst   | der Obst   | 11.717899799346924
1512942319.550696  | the       | f      | dat  | True   | der Blumen | der Blumen | 19.246328115463257
1512946897.6865299 | the       | m      | nom  | True   | der Mann   | der Mann   | 3.906935691833496
1512948464.2680597 | _pronoun_ | she    | akk  | True   | sie        | sie        | 3.621692419052124
1512950109.4609056 | a         | m      | akk  | False  | der Mann   | einen Mann | 3.5954036712646484
1512982093.7201095 | the       | f      | dat  | True   | der Blumen | der Blumen | 6.770673036575317
1512982260.6745229 | the       | n      | gen  | False  | des Obst   | des Obsts  | 6.113694906234741
1512983319.7528772 | a         | f      | akk  | False  | einer Frau | eine Frau  | 8.076109409332275
1512983330.287123  | the       | m      | dat  | False  | den Mann   | dem Mann   | 3.9201772212982178

## Features

- Good coverage of pronouns + nom/dat/akk/gen + genders.
- Also covers personal pronouns.
- Complete unconfigurable.
- Does not respect `XDG_anything`.
- py2/py3 compatible
- prepositions

## Coming Soon

cleaner code!

## LICENSE

AGPLv3
