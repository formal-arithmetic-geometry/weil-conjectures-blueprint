+++
id = "proposition-exceptional-inverse-image-smooth-morphism--text-1"
kind = "hidden"
title = "The exceptional inverse image of a smooth morphism"
order = 561001
uses = ["definition-relative-dualizing-complex", "theorem-existence-exceptional-inverse-image"]
+++
*Shared context for the formalized statements.* Let $A$ be a finite commutative
ring whose exponent is invertible on $X$. Let $f:X\to S$ be smooth of pure
relative dimension $d$ and admit a compactification. We work in the unbounded
étale derived categories, with
$\omega_f=f^!A_S\in D(X_{\acute{e}t},A)$ and
$N\in D(S_{\acute{e}t},A)$; no boundedness or constructibility condition is
imposed on $N$. The chart reduction below states its local hypotheses
separately. For base change, assume also that $S$ is quasi-separated and that
$f':X'\to S'$ is quasi-compact and admits a compactification. These geometric
conditions hold in the finite-type setting of the surrounding chapter.

The Lean proof first establishes the rank-one shape of $\omega_f$ and the
canonical tensor formula without choosing an identification with a Tate twist.
