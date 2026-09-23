+++
id = "lem-weil-pbc-underived-exchange-naturality"
kind = "lemma"
title = "Naturality of the underived exchange morphism"
order = 1283
uses = ["def-weil-pbc-cartesian-square-detailed", "def-weil-pbc-underived-exchange-detailed"]
+++
For every morphism $a:F\to G$ in $\Ab(X_{\Et})$, the square

$$
 \begin{array}{ccc}
 g^{-1}f_*F&\xrightarrow{\Ex^0_{\square,F}}&f'_*g'^{-1}F\\
 g^{-1}f_*a\downarrow&&\downarrow f'_*g'^{-1}a\\
 g^{-1}f_*G&\xrightarrow{\Ex^0_{\square,G}}&f'_*g'^{-1}G
 \end{array}
$$

commutes.

## Proof

Each arrow in the defining composite of
[def-weil-pbc-underived-exchange-detailed] is an adjunction unit, the
specified pseudofunctorial isomorphism $\theta_\square$ of
[def-weil-pbc-cartesian-square-detailed], or an adjunction counit; all three
transformations are natural in $F$, so the displayed square commutes.
