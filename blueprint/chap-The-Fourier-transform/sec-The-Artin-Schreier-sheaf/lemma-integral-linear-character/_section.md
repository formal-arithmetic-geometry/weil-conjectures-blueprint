+++
id = "lemma-integral-linear-character"
kind = "lemma"
title = "The integral of a linear character"
order = 1228
lean = ["AlgebraicGeometry.WeilComplex.isZero_derivedLowerShriek_tensorLisse_artinSchreierOf_upperStar", "AlgebraicGeometry.WeilComplex.nonempty_iso_upperStar_comp_derivedLowerShriek_of_isPullback"]
uses = ["lemma-stability", "proposition-six-operations-change-coefficients", "lemma-artin-schreier-character-sheaf", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
Let $\lambda$ be a linear form on $\mathbf A^r$ over an algebraically
closed field of characteristic $p$. Then

$$
R\Gamma_c(\mathbf A^r,\lambda^*\mathcal L_\psi)
\simeq
\begin{cases}
E(-r)[-2r],&\lambda=0,\\
0,&\lambda\ne0.
\end{cases}
$$

For $\lambda=0$, the isomorphism is the trace map for cohomology with
compact support.
