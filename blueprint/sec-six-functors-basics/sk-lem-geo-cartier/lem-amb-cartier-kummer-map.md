+++
id = "lem-amb-cartier-kummer-map"
kind = "lemma"
title = "A Cartier divisor gives a supported Kummer map"
order = 2332
uses = ["def-coefficient-twists-detailed", "def-nagata-invertible-ideal", "def-sc-kummer-sequence", "def-weil-pbc-derived-categories", "lem-amb-closed-support-hom", "lem-amb-kummer-any-base"]
+++
Let $i:D\hookrightarrow T$ be an effective Cartier divisor.
There is a natural morphism in the ordinary derived category

$$
c_D:i_*A_D\longrightarrow A_T(1)[2].
$$

Its image after forgetting support is
$c_1(\mathcal O_T(D))$. For any base change under which
the pullback divisor remains Cartier, the map pulls back to
the corresponding map for that divisor.
