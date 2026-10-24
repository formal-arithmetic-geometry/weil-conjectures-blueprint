+++
kind  = "proof"
of    = "lem-mg-common-positive-central-element"
+++
The direct sum $\rho$ of semisimple Weil representations is a
semisimple Weil representation, so it is a semisimple represented degree
datum in the sense of [d-monodromy], with geometric monodromy group $H$,
arithmetic monodromy group $G$ and $F=\rho(s)$ for the chosen degree-one
$s$. By [p-central] there is a positive central pair ([d-central]), i.e.
$N>0$ and

$$
z_{\mathrm{mat}}=hF^N\in Z(G),\qquad h\in H.
$$

Put $m=N$ and $z=(h,m)\in G^{[m]}$ in the notation of
[def-wf-degree-components]. The matrix map
$(h',n)\mapsto h'F^n$ of
[def-wf-arithmetic-monodromy-extension] is a group homomorphism with
values in $G$ ([lem-wf-degree-component-image]), and it
sends $z$ to $z_{\mathrm{mat}}$. For $x\in H$, the
commutator of $z$ with $(x,0)$ has degree $0$ and matrix
$z_{\mathrm{mat}}xz_{\mathrm{mat}}^{-1}x^{-1}=1$; the commutator of $z$
with $(1,1)$ has degree $0$ and matrix
$z_{\mathrm{mat}}Fz_{\mathrm{mat}}^{-1}F^{-1}=1$. On the degree-zero
component the matrix map $(h',0)\mapsto h'$ is injective, so both
commutators are trivial. Since $G_{\mathrm{arith}}(\rho)$ is generated
by $H\times\{0\}$ and $(1,1)$, the element $z$ is central.
Its image on every subquotient has the same
degree and remains central by the functoriality of
[lem-mg-degree-component-functoriality].
