+++
id = "lem-sc-line-bundle-torsor"
kind = "lemma"
title = "Line bundles and $\\mathbf G_m$-torsors"
order = 887
uses = ["def-sc-gm-torsor", "def-sc-invertible-module", "def-sc-picard-group", "lem-pc-fpqc-descent"]
+++
Let $X$ be a scheme (for instance a curve $C$ as in
[def-sc-curves], in which case the left-hand side below is
$\operatorname{Pic}(C)$ of [def-sc-picard-group]). For an invertible
$\mathcal O_X$-module $\mathcal L$ ([def-sc-invertible-module]) write
$\mathcal L_{\Et}$ for the etale sheaf
$(\varphi:U\to X)\mapsto\Gamma(U,\varphi^*\mathcal L)$, a module over
$\mathcal O_{X_{\Et}}:=(\mathcal O_X)_{\Et}$. The construction

$$
\mathcal L\longmapsto\underline{\operatorname{Isom}}(\mathcal O_{X_{\Et}},\mathcal L_{\Et})
$$

(with the action $u\cdot\varphi=u\circ\varphi$ of
$\mathbf G_m$) and the construction

$$
T\longmapsto\mathcal L(T),\qquad
\mathcal L(T)_{\Et}\cong(T\times\mathcal O_{X_{\Et}})/\mathbf G_m
$$

(with the diagonal action $g\cdot(t,a)=(g\cdot t,g^{-1}a)$) are
mutually inverse bijections

$$
\{\text{invertible }\mathcal O_X\text{-modules}\}/{\cong}
\;\longleftrightarrow\;
\{\text{isomorphism classes of }\mathbf G_m\text{-torsors on }X_{\Et}\},
$$

carrying the tensor product $\mathcal L\otimes\mathcal M$ to the
contracted product of torsors and $\mathcal O_X$ to the trivial
torsor. The same statement holds on the Zariski site, with
$\mathcal O_X^{\times}$-torsors on $X_{\mathrm{Zar}}$ and
$\underline{\operatorname{Isom}}(\mathcal O_X,\mathcal L)$.
