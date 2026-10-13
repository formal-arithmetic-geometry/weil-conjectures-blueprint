+++
kind  = "proof"
of    = "lem-pur-co-smooth-composition"
+++
The three conditions to verify are those of [def-pur-co-smoothness]; pullback and tensor commute by the canonical reassociation in [def-weil-derived-pullback-tensor-hom].
Using the composition rule $R(gf)^!\simeq Rf^!Rg^!$ of
[def-weil-exceptional-inverse-image] for the two tensor formulas:

$$
R(gf)^!K
\;\simeq\;Lf^*\bigl(Lg^*K\otimes^L\omega_g\bigr)\otimes^L\omega_f
\;\simeq\;L(gf)^*K\otimes^L\bigl(\omega_f\otimes^LLf^*\omega_g\bigr).
$$

The tensor product in the parentheses is invertible (a product of
invertible objects of [def-weil-derived-tensor]), which gives (1)
and (2) for $gf$; the same calculation after arbitrary base change
gives (3).
