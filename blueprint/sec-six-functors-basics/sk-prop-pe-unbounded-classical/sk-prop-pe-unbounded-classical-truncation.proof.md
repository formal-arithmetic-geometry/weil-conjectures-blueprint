+++
kind = "proof"
of = "det-pe-unbounded-classical-truncation"
+++
*(1).* For $n\geq0$ the complex $\tau_{\geq-n}L$ has finitely many nonzero
cohomology sheaves, all classical, in degrees $[-n,b]$. For a single sheaf
$H[-q]$ with $q\leq b$, $H^mR\Gamma(W,H[-q])=H^{m-q}(W,H)=0$ when $m>b+e$. By
induction on the number of nonzero cohomology sheaves, using the triangles of
the canonical truncations and the long exact sequences,
$H^mR\Gamma(W,\tau_{\geq-n}L)=0$ for $m>b+e$ and all $n$.

By left completeness of $D(X_{\Proet},A)$ ([sk-prop-pe-left-complete]),
$L\simeq R\varprojlim_n\tau_{\geq-n}L$. The functor $R\Gamma(W,-)$ is a
triangulated functor preserving products, and the derived limit is the fibre of
a map between products, so
$R\Gamma(W,L)\simeq R\varprojlim_nR\Gamma(W,\tau_{\geq-n}L)$. The Milnor sequence
([sk-prop-pe-milnor])

$$
0\to\varprojlim\nolimits^1_nH^{m-1}R\Gamma(W,\tau_{\geq-n}L)\to H^mR\Gamma(W,L)
\to\varprojlim_nH^mR\Gamma(W,\tau_{\geq-n}L)\to0
$$

shows $H^mR\Gamma(W,L)=0$ as soon as $m-1>b+e$.

*(2).* Apply (1) to $L=\tau_{<N}K$, with $b=N-1$: its derived sections vanish in
degrees $>N+e$. In the long exact sequence of the triangle
$\tau_{<N}K\to K\to\tau_{\geq N}K\to$, the terms $H^mR\Gamma(W,\tau_{<N}K)$ and
$H^{m+1}R\Gamma(W,\tau_{<N}K)$ vanish because $m>N+e+1$. Hence the map is an
isomorphism.
