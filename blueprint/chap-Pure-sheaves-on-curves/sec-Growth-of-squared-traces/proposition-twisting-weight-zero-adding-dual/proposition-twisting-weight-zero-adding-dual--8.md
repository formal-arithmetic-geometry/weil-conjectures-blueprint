+++
id = "proposition-twisting-weight-zero-adding-dual--8"
kind = "proposition"
title = "Trace"
order = 1197014
aliases = ["bp-r368-8"]
lean = ["AlgebraicGeometry.WeilSheaf.map_traceFunction_dual"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "definition-small-pro-etale-site--1", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "definition-change-of-coefficients-maps--6", "proposition-six-operations-change-coefficients--23", "proposition-sp-unique-adjoint--1", "definition-weil-structure--1", "definition-weil-structure--3", "theorem-grothendieck-lefschetz-trace-formula--6", "definition-weights--2"]
+++
Let $\mathcal G$ be lisse and pure of weight zero. For a point $x$ over
$k_n$ write $t_{\mathcal G,n}(x)=\operatorname{Tr}(\operatorname{Frob}_{x,n}\mid\mathcal G_{\bar x})$
for the trace of the Frobenius $\operatorname{Frob}_{x,n}$ at $x$. Then

$$
\iota\bigl(t_{\mathcal G^\vee,n}(x)\bigr)
=\overline{\iota\bigl(t_{\mathcal G,n}(x)\bigr)}.
$$

In particular, if $\mathcal F$ is lisse and pure of weight $w$ and
$|\iota(b)|=q^{-w/2}$, then

$$
\iota\bigl(t_{\mathcal E,n}(x)\bigr)
=2\operatorname{Re}\iota\bigl(t_{\mathcal F^0,n}(x)\bigr).
$$
