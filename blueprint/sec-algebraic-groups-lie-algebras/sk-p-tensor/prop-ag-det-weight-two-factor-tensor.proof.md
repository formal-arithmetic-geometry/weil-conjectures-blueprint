+++
kind  = "proof"
of    = "prop-ag-det-weight-two-factor-tensor"
+++
The multisets $\{V_i\}$ and $\{E_j\}$ do not depend on the chosen
series by [lem-mg-jordan-holder]. Form the Weil semisimplifications
$V^{\mathrm{ss}}=\bigoplus_iV_i$ and $E^{\mathrm{ss}}=\bigoplus_jE_j$
of [def-mg-weil-semisimplification]; both are semisimple Weil
representations on the same curve. Apply
[lem-mg-common-positive-central-element] to the pair
$V^{\mathrm{ss}},E^{\mathrm{ss}}$, i.e. to
$\rho=V^{\mathrm{ss}}\oplus E^{\mathrm{ss}}$, and let $z$ be the
resulting central element of degree $m>0$. Each $V_i$ and each $E_j$
is a Weil-stable direct summand, hence a subquotient, of $\rho$, so by
[lem-mg-degree-component-functoriality] the image of $z$ on it is
central of degree $m$; by [lem-wf-schur-scalar] it acts on $V_i$ by a
scalar $c_i$ and on $E_j$ by a scalar $d_j$. Since $V_i$ and $E_j$
have finite geometric determinant, [cor-mg-central-determinant-weight]
gives

$$
\dw_\lambda(V_i)=\frac{\lambda(c_i)}{m},\qquad
\dw_\lambda(E_j)=\frac{\lambda(d_j)}{m}.
$$

By [lem-mg-filtered-tensor-product], $V\otimes E$ has a Weil-stable
filtration whose successive quotients are the representations
$V_i\otimes E_j$, each pair $(i,j)$ occurring once. Each
$V_i\otimes E_j$ is a tensor product of two subquotients of $\rho$, so
[lem-mg-degree-component-functoriality] applies to it and to its
iterated subquotients, and the image of $z$ acts on $V_i\otimes E_j$
by $c_id_j$. By [lem-mg-filtration-refinement], every constituent $Q$
of $V\otimes E$ is a composition factor of some $V_i\otimes E_j$. The
image of $z$ on $Q$ is central of degree $m$ by the same
functoriality, acts by the scalar $c_id_j$, and $Q$ has finite
geometric determinant by hypothesis; therefore
[cor-mg-central-determinant-weight] and the fact that $\lambda$ is a
homomorphism give

$$
\dw_\lambda(Q)=\frac{\lambda(c_id_j)}{m}
=\frac{\lambda(c_i)}{m}+\frac{\lambda(d_j)}{m}
=\dw_\lambda(V_i)+\dw_\lambda(E_j).
$$

Conversely, each $V_i\otimes E_j$ is nonzero, so it has a composition
series by [lem-mg-composition-series-exists]; its factors are
constituents of $V\otimes E$ by [lem-mg-filtration-refinement], and
each has determinant weight $\dw_\lambda(V_i)+\dw_\lambda(E_j)$.
