+++
kind = "proof"
of = "det-pe-bounded-continuity-direct-image"
+++
For a complex $K$ on $X_{\mathrm{proét}}$, $R^qf_*K=H^q(Rf_*K)$ is the sheafification of
the presheaf $P_K\colon V\mapsto H^q(X\times_YV,K)$ on $Y_{\mathrm{proét}}$: with a
K-injective resolution $K\to J$, $Rf_*K=f_*J$ (base change functor of
[det-pe-topos-functoriality-inverse-image]), $(f_*J)(V)=J(X\times_YV)$, and cohomology
sheaves are sheafified sectionwise cohomology.

Let $K=\varinjlim_iK_i^\bullet$. The canonical maps give a map of presheaves
$\varphi\colon\varinjlim_iP_{K_i}\to P_K$ (presheaf colimit). For an affine object $V$ of
$Y_{\mathrm{proét}}$, the morphism $X\times_YV\to V$ is quasi-compact and quasi-separated
and $V$ is affine, so $X\times_YV$ is a quasi-compact, quasi-separated object of
$X_{\mathrm{proét}}$, and $\varphi(V)$ is an isomorphism by
[det-pe-bounded-continuity-sections]. Every object of $Y_{\mathrm{proét}}$ has a covering
by affine objects ([det-pe-wcb-cover]). A map of presheaves that is bijective on a class of
objects covering every object is locally injective and locally surjective, so
$\varphi^{\#}$ is an isomorphism. Sheafification is a left adjoint and commutes with
colimits, so $(\varinjlim_iP_{K_i})^{\#}=\varinjlim_iP_{K_i}^{\#}=\varinjlim_iR^qf_*K_i$
(colimit of sheaves). Hence $\varinjlim_iR^qf_*K_i^\bullet\to R^qf_*K$ is an isomorphism.
