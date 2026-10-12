+++
id = "sk-d-real-weights"
kind = "definition"
title = "Local weights and reality"
order = 2928
uses = ["sk-d-real-setup", "sk-d-real-weil"]
lean = ["AlgebraicGeometry.WeilGroup.IsPunctuallyPure", "AlgebraicGeometry.WeilGroup.frobeniusWeight", "AlgebraicGeometry.WeilGroup.localPolynomial", "AlgebraicGeometry.WeilGroup.HasWeightsAtMost", "AlgebraicGeometry.WeilGroup.IsReal"]
tags = ["sketch"]
+++
For a Weil sheaf $\mathcal F$, given by a representation $\rho$ of
$W(C_0)$ on a finite-dimensional $\Qlb$-vector space $V$,
and a closed point $x$ with local Frobenius $F_x$ of [sk-d-real-weil], use the
determinant to set

$$
P_x(\mathcal F,T)=\det(1-T\rho(F_x)\mid V),\qquad
\wt_{\iota,q_x}(\alpha)=
\frac{2\log|\iota(\alpha)|}{\log q_x}
$$

for a nonzero local eigenvalue $\alpha$ (an eigenvalue of $\rho(F_x)$,
i.e. an inverse root of $P_x$) and the
residue cardinality $q_x$ of $x$.
The sheaf is punctually $\iota$-pure of weight $w$ if, at every closed
point $x$, all these weights are $w$, and has weights at most $w$ if all
are $\le w$.
It is $\iota$-real if $\iota P_x(\mathcal F,T)\in\mathbf R[T]$ for every
$x$, equivalently if each complex local eigenvalue multiset is stable
under complex conjugation. This condition is imposed on polynomials.
For a constructible Weil sheaf the same definitions are made with the
stalk $\mathcal F_{\bar x}$ and its Frobenius $F_x$ in place of $V$ and
$\rho(F_x)$.
