+++
id = "fix-lem-exchanges-proper"
kind = "lemma"
title = "Exchange functoriality: proper coincidence"
order = 1922
uses = ["cor-cbc-proper-coincidence", "def-exchange-projection", "fix-lem-exchanges"]
+++
In the situation of [fix-lem-exchanges], for proper $f$, the exchange transformation
$\operatorname{Ex}_!$ is the exchange transformation
$\operatorname{Ex}_*$ under the identification $Rf_!\cong Rf_*$
of [cor-cbc-proper-coincidence], i.e. the compact-support base
change specializes to the proper base change.

## Proof

For proper $f$ the compactification
$j=\operatorname{id}$ is admissible, the extension-by-zero
identification of [def-exchange-projection] is the identity, and
the identification $Rf_!\cong Rf_*$ is
[cor-cbc-proper-coincidence], so
$\operatorname{Ex}_!=\operatorname{Ex}_*$.
