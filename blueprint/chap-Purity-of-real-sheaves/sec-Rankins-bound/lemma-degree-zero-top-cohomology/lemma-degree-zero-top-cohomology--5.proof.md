+++
kind = "proof"
of = "lemma-degree-zero-top-cohomology--5"
order = 1150012
uses = ["definition-weights"]
+++
Choose a nonzero global eigenvector with eigenvalue $\beta$. Since
Frobenius is invertible, $\beta\ne0$. This section defines a nonzero
morphism from the constant Weil sheaf whose Frobenius acts by $\beta$
to $\mathcal G$. Its image has a nonzero stalk at some closed point
$x$. The local Frobenius on the source acts by $\beta^{\deg(x)}$;
passing through the image gives the required nonzero eigenvector in
$\mathcal G_{\bar x}$.

Consequently, if $\mathcal G$ is punctually of weights $\le a$, then

$$
|\iota(\beta)|^{\deg(x)}\le q^{\deg(x)a/2}.
$$

Since $\deg(x)>0$, this gives $|\iota(\beta)|\le q^{a/2}$. Thus the
weights of global sections are at most $a$. On a curve this is the
bound for $H^0$, using
`AlgebraicGeometry.WeilSheaf.cohomologyZeroEquiv`. The same argument
with equality proves purity of $H^0$ when the sheaf is pure.
