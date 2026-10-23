+++
id = "lem-tw-root-of-unity-modulus"
kind = "lemma"
title = "Modulus of a root of unity"
lean = ["norm_eq_one_of_pow_eq_one", "AlgebraicGeometry.WeilGroup.frobeniusWeight_eq_zero_of_pow_eq_one"]
order = 3855
uses = ["def-tw-eigenvalue"]
+++
Every root of unity $\zeta\in\overline{\mathbf Q}_\ell^\times$ has
absolute value $|\zeta|=1$ with respect to the absolute value of
[def-tw-eigenvalue]; in particular every root of unity is of weight
$0$. Moreover, for every field isomorphism
$\iota:\overline{\mathbf Q}_\ell\xrightarrow{\sim}\mathbf C$, the
complex number $\iota(\zeta)$ also has modulus one.
