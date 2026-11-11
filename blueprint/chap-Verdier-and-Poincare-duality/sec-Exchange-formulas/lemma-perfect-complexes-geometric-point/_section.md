+++
id = "lemma-perfect-complexes-geometric-point"
kind = "lemma"
title = "Perfect complexes at the geometric point"
order = 825
lean = ["AlgebraicGeometry.Etale.isPerfect_geometricStalk", "DerivedCategory.IsPerfect.ihom_unit", "DerivedCategory.IsPerfect.isIso_toIhomIhomUnit"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "theorem-pro-etale-refinements-weakly-etale", "definition-weak-contractibility", "proposition-pro-etale-site-separably-closed", "definition-constructible-sheaves", "lemma-constructible-sheaves", "proposition-six-operations-dctf", "definition-compactification-refinement"]
+++
Suppose $k$ is algebraically closed. The category
$D^b_{\mathrm{ctf}}(s,\Lambda)$ identifies with
$\operatorname{Perf}(\Lambda)$, the category of bounded complexes of
finite projective $\Lambda$-modules up to quasi-isomorphism. For
$K\in D^b_{\mathrm{ctf}}(X,\Lambda)$, both

$$
R\Gamma_c(X,K)=Ra_{X!}K,\qquad R\Gamma(X,K)=Ra_{X*}K
$$

and every geometric stalk $K_{\bar x}$ are perfect complexes. Their duals $R\!\operatorname{Hom}_\Lambda(-,\Lambda)$ are perfect, and
the evaluation map $P\to R\!\operatorname{Hom}_\Lambda(R\!\operatorname{Hom}_\Lambda(P,\Lambda),
\Lambda)$ is an isomorphism for each of them.
