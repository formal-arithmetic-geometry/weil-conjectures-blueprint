+++
id = "lem-fd-cohomology-affine-line-character"
kind = "lemma"
title = "Cohomology of an affine line with an exponential sheaf"
lean = ["AlgebraicGeometry.WeilComplex.isZero_derivedLowerShriek_tensorLisse_artinSchreierOf_upperStar", "AlgebraicGeometry.Etale.cohomology_affineLine_artinSchreierSheafOf"]
order = 3030
uses = ["lem-fd-affine-line-constant-cohomology", "lem-fd-as-characters", "lem-fd-as-cover-affine-line", "lem-fd-as-lisse", "lem-fd-finite-pushforward-cohomology"]
+++
Let $k$ be finite or algebraically closed, let $a\in k$, and let $\psi_a(x)=\psi(ax)$. Over $\mathbf A^1_k$,

$$
H^q(\mathbf A^1_{\bar k},\mathcal L_{\psi_a})=\begin{cases}\overline{\mathbf Q}_\ell,&q=0,\ a=0,\\0,&\text{otherwise.}\end{cases}
$$
