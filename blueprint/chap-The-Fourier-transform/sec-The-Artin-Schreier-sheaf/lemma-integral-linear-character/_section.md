+++
id = "lemma-integral-linear-character"
kind = "lemma"
title = "The integral of a linear character"
order = 1228
lean = ["AlgebraicGeometry.WeilComplex.isZero_derivedLowerShriek_tensorLisse_artinSchreierOf_upperStar"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-sp-unique-adjoint", "lemma-artin-schreier-character-sheaf", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
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
