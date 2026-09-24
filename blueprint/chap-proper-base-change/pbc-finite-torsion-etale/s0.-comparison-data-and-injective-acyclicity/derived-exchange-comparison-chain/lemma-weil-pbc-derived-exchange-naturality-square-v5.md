+++
id = "lemma-weil-pbc-derived-exchange-naturality-square-v5"
kind = "lemma"
title = "Exchange naturality is a homotopy square"
order = 1532
uses = ["def-weil-pbc-derived-exchange-presentation-v5", "def-weil-pbc-derived-exchange-target-comparison-v5", "lemma-weil-pbc-derived-exchange-target-comparison-exists-v5", "lemma-weil-pbc-underived-exchange-naturality"]
+++
Let $(I,J,q)$ and $(I',J',q')$ be presentations and let $a:I\to I'$ be a
source comparison. A target comparison $c:J\to J'$ for $q'g'^{-1}a$ and
$cq$ gives

$$
f'_*c\,E_{I,J}\simeq E_{I',J'}\,g^{-1}f_*a.
$$

## Proof

Underived naturality gives the strict degreewise equality
$f'_*g'^{-1}a\,E_I=E_{I'}g^{-1}f_*a$. The defining homotopy
$cq\simeq q'g'^{-1}a$ remains a homotopy after $f'_*$; compose it with
$E_I$ and substitute the strict equality.
