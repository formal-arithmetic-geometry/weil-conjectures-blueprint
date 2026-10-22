+++
kind  = "proof"
of    = "lem-pc-flf-properties"
+++
Both assertions are local on $S$, so let $V=\operatorname{Spec}(A)\subseteq S$
be an affine open. The morphism $f$ is finite, hence affine, so
$f^{-1}(V)=\operatorname{Spec}(B)$ with $B=\Gamma(f^{-1}(V),\mathcal{O}_X)$, and
$f_*\mathcal{O}_X|_V$ is the quasi-coherent module $\widetilde B$ attached to the
$A$-module $B$. Since $f$ is finite, flat and locally of finite presentation
([def-pc-finite-locally-free]), $B$ is a finite $A$-module, flat over $A$, and
a finitely presented $A$-algebra; a finite algebra of finite presentation is a
finitely presented module, and a finitely presented flat module is finite
projective. Hence $f_*\mathcal{O}_X|_V=\widetilde B$ is finite locally free.

*The fibres.* Let $s\in V$ correspond to the prime $\mathfrak p\subset A$.
Fibre products of affine schemes are spectra of tensor products
([def-pc-base-change]), so
$X_s=f^{-1}(V)\times_V\operatorname{Spec}\kappa(s)=\operatorname{Spec}(B\otimes_A\kappa(s))$
and $\Gamma(X_s,\mathcal{O}_{X_s})=B\otimes_A\kappa(s)$, the map
$B\to\Gamma(X_s,\mathcal{O}_{X_s})$ being restriction of functions. The stalk of
$\widetilde B$ at $s$ is the localization $B_{\mathfrak p}=B\otimes_AA_{\mathfrak p}$,
so

$$
(f_*\mathcal{O}_X)_s\otimes_{\mathcal{O}_{S,s}}\kappa(s)
=B_{\mathfrak p}\otimes_{A_{\mathfrak p}}\kappa(s)=B\otimes_A\kappa(s)
=\Gamma(X_s,\mathcal{O}_{X_s}),
$$

and this composite is the canonical map of the statement, which is therefore
an isomorphism.

*The rank.* The rank of the finite projective module $B$ at $s$ is
$\dim_{\kappa(s)}B\otimes_A\kappa(s)=\dim_{\kappa(s)}\Gamma(X_s,\mathcal{O}_{X_s})=d$
by the definition of degree $d$ ([def-pc-finite-locally-free]). Hence
$f_*\mathcal{O}_X$ is locally free of rank $d$.
