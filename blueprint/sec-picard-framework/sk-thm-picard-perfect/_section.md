+++
id = "sk-thm-picard-perfect"
kind = "section"
title = "Openness of the perfect locus"
order = 686
uses = ["sk-def-av-jacobian", "sk-def-av-pic"]
+++
*Theorem (sketch).*

With $f$ and $\cF$ as above, the set of $t\in T$ such
that $Rf_{T,*}\cF$ is isomorphic to a finite locally free
$\cO_T$-module placed in a fixed degree is *open* in $T$:
the locus where $R^qf_*\cF=0$ for all $q\neq i$ and the $i$-th
direct image is of rank $\le r$ is open, and on it the restriction
is flat of rank $r$.

## Proof

This is the direct statement obtained from [sk-thm-picard-semicon]
by fixing the allowed degrees: upper semicontinuity makes each
condition $\dim_{\kappa(t)}H^q(X_t,\cF_t)=0$ ($q\neq i$) and
$\dim_{\kappa(t)}H^i(X_t,\cF_t)\le r$ an open condition. On the
resulting open locus the bounded complex of finite free modules of the
proof of [sk-thm-picard-semicon], whose formation commutes with base
change, has fibre cohomology only in degree $i$; by Nakayama it is
locally quasi-isomorphic to a finite free module placed in degree $i$,
which gives flatness of rank $r$ (no reducedness of $T$ is needed here).
