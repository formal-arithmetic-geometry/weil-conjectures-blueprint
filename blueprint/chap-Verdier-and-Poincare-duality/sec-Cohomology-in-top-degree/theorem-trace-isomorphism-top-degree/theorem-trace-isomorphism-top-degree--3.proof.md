+++
kind = "proof"
of = "theorem-trace-isomorphism-top-degree--3"
order = 866007
uses = ["theorem-proper-base-change-classical-pro--2"]
+++
The finite-coefficient vanishing bound is clause [theorem-trace-isomorphism-top-degree--2].

Now let $\Lambda=\mathbf Z/\ell^n$. Since this ring is injective as a module over
itself,
$R\!\operatorname{Hom}_{\mathbf Z/\ell^n}(-,\mathbf Z/\ell^n)$ has cohomology equal to
the ordinary dual of the opposite cohomology. Hence Poincaré
duality (Theorem [theorem-poincare-duality]) in degree zero identifies $H^{2d}(X,\mathbf Z/\ell^n(d))$
with $\Hom(H^0(X,\mathbf Z/\ell^n),\mathbf Z/\ell^n)=\mathbf Z/\ell^n$.
By Theorem [theorem-poincare-duality] this identification is given by
pairing with $H^0$ and applying the trace map, so it is
$\operatorname{tr}_X(d)$.

A general finite ring $A$ need not be injective over itself, so we reach
it by extension of scalars instead. Every finite $A$ is an algebra over some $\mathbf Z/\ell^n$, and by
Proposition [proposition-six-operations-change-coefficients] the complexes with constant coefficients
and their traces over $A$ are obtained by derived extension of
scalars from $\mathbf Z/\ell^n$. For a complex $P$ with cohomology in
degrees $\le2d$, right exactness of the tensor product gives
$H^{2d}(P\otimes^{\mathbf L}A)=H^{2d}(P)\otimes A$. The top cohomology is therefore
$\mathbf Z/\ell^n\otimes A=A$, and the trace is an isomorphism. The same
upper bound holds.

*Source:* the proof of Theorem [theorem-trace-isomorphism-top-degree].
