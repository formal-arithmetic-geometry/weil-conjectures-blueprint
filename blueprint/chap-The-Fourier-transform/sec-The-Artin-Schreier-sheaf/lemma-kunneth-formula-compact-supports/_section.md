+++
id = "lemma-kunneth-formula-compact-supports"
kind = "lemma"
title = "Künneth formula for compact supports"
order = 1222
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleExceptionalProjectionMorphism", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleLowerShriekBaseChange_padicAlgCl"]
uses = ["proposition-construction-independence-rf-shriek", "proposition-six-operations-dctf"]
+++
In this situation, let $K,L$ be bounded constructible complexes with
coefficients in a field. Then the maps in

$$
Rh_!(p_1^*K\otimes p_2^*L)
\simeq Rf_!(K\otimes Rp_{1!}p_2^*L)
\simeq Rf_!(K\otimes f^*Rg_!L)
\simeq Rf_!K\otimes Rg_!L
$$

of the projection formula for $p_1$, the proper base change isomorphism
$Rp_{1!}p_2^*L\to f^*Rg_!L$ and the projection formula for $f$ are
isomorphisms. We call their composite
$Rh_!(K\boxtimes_SL)\simeq Rf_!K\otimes Rg_!L$ the
*Künneth isomorphism*.
