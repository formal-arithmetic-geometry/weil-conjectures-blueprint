+++
id = "sbc-lem-local-acyclicity-constant"
kind = "lemma"
title = "Constant-sheaf form of local acyclicity"
order = 2814
uses = ["sbc-def-local-acyclicity", "sbc-def-specialization-map", "sbc-lem-strict-henselian-constant-cohomology"]
+++
Let $M$ be an abelian group. Local acyclicity of $f:X\to S$ with
respect to the constant sheaf $\underline M$ boils down to the
requirement

$$
H^q\bigl(F_{\bar x,\bar t},\underline M\bigr)=
\begin{cases}M,&q=0,\\0,&q\neq0,\end{cases}
$$

for every geometric point $\bar x$ of $X$ and every geometric point
$\bar t$ of $\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{S,f(\bar x)}$.

## Proof

The source of the specialization map of [sbc-def-specialization-map] is
$R\Gamma(X_{(\bar x)},K)$, whose cohomology is $M$ in degree $0$
and $0$ above by strict henselianity
([sbc-lem-strict-henselian-constant-cohomology]), so the
specialization map being an isomorphism in every degree is exactly the
displayed condition, and
[sbc-def-local-acyclicity] says this is local acyclicity.
