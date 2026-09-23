+++
id = "lemma-weil-pbc-etale-degree-zero"
kind = "lemma"
title = "Etale henselian restriction in degree zero"
order = 1610
uses = ["def-weil-pbc-strict-henselian-setup", "lemma-weil-pbc-finite-pullback-closed-fibre", "lemma-weil-pbc-finite-pullback-composition", "lemma-weil-pbc-finite-pullback-descent", "lemma-weil-pbc-finite-pullback-identity", "lemma-weil-pbc-finite-refinement-etale-cover", "lemma-weil-pbc-stein-connectedness"]
+++
For every etale abelian sheaf $F$ on $X$, restriction induces
$\Gamma(X,F)\xrightarrow{\sim}\Gamma(X_0,F_0)$.

## Proof

The canonical map from the etale to Zariski restriction is injective on
stalks because a geometric point has a strictly local etale neighbourhood.
For surjectivity, lift a fibre section etale-locally; quasi-compactness of
$X_0$ gives finitely many local lifts, and Lemma
[lemma-weil-pbc-finite-refinement-etale-cover] gives a finite surjective
refinement on which all lifts exist.
The two lifts agree on the finite overlap after restriction to $X_0$ by the
Zariski result, and the equalizer sheaf descends the lift to $X$. Uniqueness
is stalkwise injectivity. The finite-pullback compatibility required in
Stacks Tag `09ZF` is recorded as four explicit equalities:
identity pullback preserves the lift, composition of finite pullbacks preserves
the lift, restriction to $X_0$ recovers the given section, and the descended
section pulls back to each local lift; these are the four preceding lemmas.
The finite refinement lemma proves existence and finite-presentation stage,
and its stalkwise equalizer argument proves equality of the local lifts on
the self-intersection. Thus the four finite-pullback compatibilities
complete the descent.
