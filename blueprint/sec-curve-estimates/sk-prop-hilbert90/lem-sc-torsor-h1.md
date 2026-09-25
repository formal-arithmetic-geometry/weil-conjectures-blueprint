+++
id = "lem-sc-torsor-h1"
kind = "lemma"
title = "First cohomology classifies torsors"
order = 885
uses = ["def-sc-curves", "lem-sc-ext-torsor"]
+++
Let $C$ be a curve and $G$ a sheaf of
abelian groups on $C_{\Et}$. There is a canonical bijection

$$
H^1(C_{\Et},G)\cong\{\text{isomorphism classes of }G\text{-torsors}\}.
$$

## Proof

By homological algebra,

$$
H^1(C_{\Et},G)=\operatorname{Ext}^1_{\mathrm{Ab}(C_{\Et})}(\mathbf Z_C,G):
$$

the functor $\operatorname{Hom}_{\mathrm{Ab}(C_{\Et})}(\mathbf Z_C,-)$ is canonically isomorphic to the global sections functor
$\Gamma(C_{\Et},-)$ (a homomorphism $\mathbf Z_C\to F$ is
determined by the image of $1$), so the first right derived
functor of this functor is $H^1(C_{\Et},-)$ on the one hand and
$\operatorname{Ext}^1(\mathbf Z_C,-)$ on the other. By
[lem-sc-ext-torsor], $\operatorname{Ext}^1(\mathbf Z_C,G)$ is
canonically the set of isomorphism classes of $G$-torsors, and the
group structures match (the Baer sum of extensions corresponds to
the contracted product of torsors, both being the ``addition'' of
$\mathbf Z_C$-extensions).
