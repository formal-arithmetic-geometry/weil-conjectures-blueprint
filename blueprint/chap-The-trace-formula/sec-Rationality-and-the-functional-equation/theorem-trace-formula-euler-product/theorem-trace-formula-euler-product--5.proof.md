+++
kind = "proof"
of = "theorem-trace-formula-euler-product--5"
order = 1036011
uses = ["theorem-trace-formula-euler-product--2", "theorem-trace-formula-euler-product--3", "theorem-trace-formula-euler-product--4", "lemma-degree-zero-top-cohomology"]
+++
Apply [theorem-trace-formula-euler-product--4] to the complex
$\mathcal F[0]$. The compactly supported cohomology vanishes outside
degrees $1$ and $2$, by [lemma-degree-zero-top-cohomology]. Thus the
cohomological product is the quotient of the local polynomials of
$H_c^1$ and $H_c^2$. Lean first records this coefficient identity as
`AlgebraicGeometry.WeilSheaf.coeff_prod_inv_localPolynomial_stalk_eq`.

Apply $\iota$ coefficientwise. It commutes with the inverses in these
products because each denominator has constant coefficient $1$.
For each $n$, finite products containing all points of degree at most
$n$ have the prescribed coefficient. By the convergence in
[theorem-trace-formula-euler-product--3] and continuity of coefficient
extraction, their limit has the same coefficient. Hence
$L_\iota(U_0,\mathcal F,T)=P_1(T)P_2(T)^{-1}$.
Multiplying by $P_2(T)$ gives the displayed identity.
