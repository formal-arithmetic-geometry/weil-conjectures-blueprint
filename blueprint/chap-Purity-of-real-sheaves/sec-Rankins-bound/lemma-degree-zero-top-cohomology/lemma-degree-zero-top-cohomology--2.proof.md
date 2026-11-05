+++
kind = "proof"
of = "lemma-degree-zero-top-cohomology--2"
order = 1150009
uses = ["corollary-degreewise-duality-over-fields", "lemma-degree-zero-top-cohomology--1"]
+++
The untwisted degreewise Poincaré pairing of Corollary
[corollary-degreewise-duality-over-fields] is perfect:

$$
P:H_c^2(U,\mathcal F)\times H^0(U,\mathcal F^\vee)
\longrightarrow\overline{\mathbf Q}_\ell,\qquad
P(Fx,Fy)=qP(x,y).
$$

It identifies the first factor with the dual of the second, with
Frobenius multiplied by $q$.
`AlgebraicGeometry.WeilSheaf.cohomologyZeroEquiv` identifies the second
factor with $\Gamma(U,\mathcal F^\vee)$. This gives the asserted
isomorphism with $Q(\mathcal F)(-1)$. By
[lemma-degree-zero-top-cohomology--1], applied to $\mathcal F^\vee$,
$Q(\mathcal F)$ is the geometric coinvariant space $V_{\pi_1(U)}$.
