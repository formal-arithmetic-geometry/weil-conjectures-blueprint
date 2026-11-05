+++
id = "prose-07-03"
kind = "hidden"
title = "Change of coefficients (1)"
order = 628
+++
Smooth base change for $E$ and $\overline{\mathbf Q}_\ell$ is deduced from the integral case
by extending scalars (Section [chap-Smooth-base-change]), and later proofs
often argue in the same way, through the reduction principle of
Proposition [proposition-isomorphisms-reduce-finite-coefficients]. For
this the six operations must commute with extension of scalars. For pullback, extension by zero and tensor product this is formal, since
extension of scalars is itself a tensor product. For $Rf_*$, by contrast, it rests on finite cohomological dimension and on continuity, and for $f^!$ it rests on a
second computation of $f^!$, for closed immersions and for $\mathbf P^1$.
These results are collected in Proposition [proposition-six-operations-change-coefficients].

A change of coefficients is derived extension of scalars along a map
of condensed rings, pulled back to $X$. For a map $\Lambda\to\Lambda'$ write

$$
K_{\Lambda'}=\Lambda'_X\otimes^{\mathbf L}_{\Lambda_X}K.
$$

This functor $D(X_{\mathrm{pro}\acute{e}t},\Lambda)\to D(X_{\mathrm{pro}\acute{e}t},\Lambda')$ is left
adjoint to the exact restriction of scalars
$D(X_{\mathrm{pro}\acute{e}t},\Lambda')\to D(X_{\mathrm{pro}\acute{e}t},\Lambda)$.
We consider the following maps of coefficient rings:

1. any homomorphism $A\to B$ of finite admissible rings;
2. the maps $\mathcal O_E\to\mathcal O_F$ and $E\to F$ for a
   finite extension $F/E$ inside $\overline{\mathbf Q}_\ell$;
3. localization $\mathcal O_E\to E$, inclusions $E\to\overline{\mathbf Q}_\ell$,
   and continuous maps $\mathcal O_E\to A$ to finite admissible rings,
   such as the reductions $\mathcal O_E\to\mathcal O_E/\pi_E^n$ (continuity
   is needed for the map to define a map of condensed rings);
4. composites of these maps.

For $E=\mathbf Q_\ell$, the list contains $\mathbf Z_\ell\to\mathcal O_F$, $\mathbf Q_\ell\to F$, $\mathbf Z_\ell\to\mathbf Q_\ell$,
$\mathbf Z_\ell\to A$ and $\mathbf Q_\ell\to\overline{\mathbf Q}_\ell$. Thus these maps connect all the admissible
coefficient rings. Note that the map $A\to B$ in (1) need not be flat, and for this reason extension of scalars is derived. As a consequence, the comparison isomorphisms below hold for complexes but not degree by degree, as the following example
shows.
