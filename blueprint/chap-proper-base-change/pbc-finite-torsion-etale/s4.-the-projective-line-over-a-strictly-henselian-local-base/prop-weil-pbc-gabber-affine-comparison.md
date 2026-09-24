+++
id = "prop-weil-pbc-gabber-affine-comparison"
kind = "theorem"
title = "Gabber affine comparison"
order = 1723
tags = ["latex:proposition"]
uses = ["lemma-weil-pbc-etale-degree-zero", "lemma-weil-pbc-gabber-effacement"]
+++
For an affine henselian pair $(T,T_0)$ and torsion $F$,
$H^q(T,F)\xrightarrow{\sim}H^q(T_0,F_0)$ for all $q\geq0$.

## Proof

Degree zero is the etale henselian restriction lemma applied on the affine.
For $q>0$, assume comparison in all degrees below $q$. To prove injectivity,
take a nonzero $\xi\in H^q(T,F)$ and apply effacement with closed subscheme
$T$ itself, obtaining $F\hookrightarrow F'$ in which $\xi$ dies. Put
$Q=F'/F$. Exactness lifts $\xi$ from $H^{q-1}(T,Q)$. The induction
isomorphism in degree $q-1$ carries any such lift to $T_0$; if $\xi$ restricted
to zero, exactness and the commutative boundary square would force the lift
to come from $H^{q-1}(T,F')$, contradicting the choice of nonzero $\xi$.

For surjectivity, take $\eta\in H^q(T_0,F_0)$ and use effacement with closed
subscheme $T_0$ to choose $F\hookrightarrow F'$ killing $\eta$. Exactness
lifts $\eta$ from $H^{q-1}(T_0,Q_0)$. By induction this lift is the
restriction of a class in $H^{q-1}(T,Q)$, whose boundary in $H^q(T,F)$
restricts to $\eta$. Thus the comparison is separately injective and
surjective. This expands Tag `09ZI`; no statement is imported from
that tag.
