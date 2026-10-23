+++
kind  = "proof"
of    = "det-prop-sfb-qlbar-colimit-x-pullback"
+++
(2) and (3). The isomorphisms are $p_Y^*$, resp. $p_X^*$, applied to the colimit
presentations $\underline E=\varinjlim(\underline{\cO_E}\xrightarrow{\ell}\cdots)$ and
$\underline{\Qlb}=\varinjlim_E\underline E$ on the point. Since
$f^{-1}\circ p_Y^*\cong p_X^*$ by the natural isomorphism $\alpha$ of
[det-def-sfb-pullback-from-point-comp], and $f^{-1}$ preserves colimits (it is a left
adjoint), $f^{-1}$ of the colimit presentation over $Y$ is identified, via the components
of $\alpha$, with the colimit presentation over $X$. Naturality of $\alpha$ in the
condensed ring gives the compatibility of all structure maps.

(1). For $V\in Y_{\mathrm{proét}}$, the inverse image $f^{-1}$ of the sheaf represented by
$V$ is the sheaf represented by $V\times_YX$ (inverse image along the continuous,
finite-limit preserving base change functor, and subcanonicity). Apply this to
$V=Y[\cO_E]=\varprojlim_n\coprod_{\cO_E/\pi_E^n}Y$: since fibre products commute with
limits, $Y[\cO_E]\times_YX=\varprojlim_n\coprod_{\cO_E/\pi_E^n}X=X[\cO_E]$. Likewise
$f^{-1}$ of the sheaf represented by $\coprod_{\cO_E/\pi_E^n}Y$ is represented by
$\coprod_{\cO_E/\pi_E^n}X$, i.e. $f^{-1}((\cO_E/\pi_E^n)_Y)=(\cO_E/\pi_E^n)_X$. Hence $f^{-1}$
of the representing-scheme identification of
[det-prop-sfb-qlbar-colimit-x-integral-limit] over $Y$ is the one over $X$, and, as
$X[\cO_E]$ represents $\varprojlim_n(\cO_E/\pi_E^n)_X$, $f^{-1}$ preserves this particular
limit. The identification of the representing scheme with $p_X^*\underline{\cO_E}$ is the
component of $\alpha_f$ at $\underline{\cO_E}$, because both come from
$u_Y(S)\times_YX=u_X(S)$ for profinite $S$. Ring structures match by naturality.
