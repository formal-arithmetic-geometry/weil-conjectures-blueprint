+++
id = "definition-tate-twists"
kind = "definition"
title = "Tate twists"
order = 184
lean = ["AlgebraicGeometry.ProEtale.spFiniteTwist", "AlgebraicGeometry.ProEtale.spInternalComplexTwist", "AlgebraicGeometry.ProEtale.spQbarTwist", "AlgebraicGeometry.ProEtale.spSignedTwist", "AlgebraicGeometry.ProEtale.spTwists_locallyFree", "AlgebraicGeometry.ProEtale.tateTwistOne", "AlgebraicGeometry.Scheme.proEtaleRootsOfUnitySheaf", "AlgebraicGeometry.Scheme.tateTwist_finite_locallyFree"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "example-locally-constant-functions-w-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-pro-etale-site-separably-closed", "definition-relative-picard-functor"]
+++
Let $X$ be a scheme on which $\ell$ is invertible, and let $\mu_{\ell^n,X}$
be the sheaf of $\ell^n$th roots of unity on $X_{\mathrm{pro}\acute{e}t}$. Then it is locally isomorphic to
$(\mathbf Z/\ell^n\mathbf Z)_X$. For a finite ring $A$ with $\ell^rA=0$ put
$A_X(1)=\mu_{\ell^r,X}\otimes_{\mathbf Z/\ell^r\mathbf Z}A_X$, which by the
Kummer maps is independent of $r$. Put
$\mathcal O_{E,X}(1)=\varprojlim_n(\mathcal O_E/\ell^n)_X(1)$, and obtain
$E_X(1)$ and $\QbarX(1)$ by inverting $\ell$ and passing to the colimit
over $E$; equivalently, $\QbarX(1)=\QbarX\otimes_{\mathbf Z_{\ell,X}}\mathbf Z_{\ell,X}(1)$
with $\mathbf Z_{\ell,X}(1)=\varprojlim_n\mu_{\ell^n,X}$. Each $\Lambda_X(1)$
is locally free of rank one. For $d\ge0$,
$\Lambda_X(d)$ is the $d$-fold tensor power, $\Lambda_X(-d)$ its dual, and
$K(d)=K\otimes^{\mathbf L}_{\Lambda_X}\Lambda_X(d)$.
