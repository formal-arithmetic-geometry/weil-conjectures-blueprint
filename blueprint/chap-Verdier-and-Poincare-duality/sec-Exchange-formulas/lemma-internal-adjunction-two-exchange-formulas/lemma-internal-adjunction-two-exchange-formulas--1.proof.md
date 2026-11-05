+++
kind = "proof"
of = "lemma-internal-adjunction-two-exchange-formulas--1"
order = 829005
uses = ["theorem-exceptional-inverse-image", "proposition-proper-direct-image-constructible-complexes", "proposition-projection-formula-rational-coefficients"]
+++
For finite $\Lambda$, the projection formula holds on the unbounded
étale derived categories. In Lean this is
`AlgebraicGeometry.Etale.isIso_projectionMap_of_finite`: choose a
compactification $f=pj$ and combine the unbounded proper projection
formula with the projection isomorphism for extension by zero along $j$.
The proper constructible case is part of
[proposition-proper-direct-image-constructible-complexes].

The adjunctions $f^*\dashv Rf_*$, $Rf_!\dashv f^!$ and the tensor–Hom
adjunction give, for every test object $N$,

$$
\begin{aligned}
\Hom_Y(N,Rf_*\cHom_X(K,f^!L))
&\simeq\Hom_X(f^*N,\cHom_X(K,f^!L))\\
&\simeq\Hom_X(K\otimes^{\mathbf L}f^*N,f^!L)\\
&\simeq\Hom_Y(Rf_!(K\otimes^{\mathbf L}f^*N),L)\\
&\simeq\Hom_Y(Rf_!K\otimes^{\mathbf L}N,L)\\
&\simeq\Hom_Y(N,\cHom_Y(Rf_!K,L)).
\end{aligned}
$$

Conjugating the projection isomorphism along these adjunctions gives
the natural isomorphism
`AlgebraicGeometry.Etale.derivedHomLowerShriekIsoOfAdjunction`;
`AlgebraicGeometry.Etale.derivedHomRightDerivedLowerShriekIsoOfFinite`
specializes it to the right adjoint $f^!$.

For $\overline{\mathbf Q}_\ell$, the same calculation takes place inside
$\Dbc$. The exceptional projection formula is obtained from the proper
projection formula and extension by zero along the open part of a
compactification. The calculation identifies composition with the
exchange map with a bijection on every Hom set.
`CategoryTheory.Verdier.isIso_exchange_of_isIso` then applies Yoneda.
