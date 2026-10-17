+++
kind  = "proof"
of    = "lem-a1-affine-hc0"
+++
Write $\mathcal F$ also for the underlying lisse $\overline{\mathbf Q}_{\ell,U}$-module
([sk-lem-coefficient-heart]). The finite levels enter only as a consequence of the
condensed comparison theorems. By [p-real-integral], after enlarging $E$,
$\mathcal F\simeq\mathcal F_0\otimes_{\cO_{E,U}}\overline{\mathbf Q}_{\ell,U}$ for a lisse
$\cO_{E,U}$-module $\mathcal F_0$ whose reductions $\mathcal F_n$ are finite locally
constant sheaves of $\cO_E/\mathfrak m_E^n$-modules. By the coefficient comparisons of
[sk-prop-scalar-six],
$R\Gamma_c(U,\mathcal F)\simeq R\Gamma_c(U,\mathcal F_0)\otimes_{\cO_E}\Qlb$ and
$R\Gamma_c(U,\mathcal F_0)\otimes^{\mathbf L}_{\cO_E}\cO_E/\mathfrak m_E^n\simeq
R\Gamma_c(U,\mathcal F_n)$. The complex $R\Gamma_c(U,\mathcal F_0)$ lies in
$\Dbc(\operatorname{Spec}k,\cO_E)$ ([sk-thm-sf-ctf-stability]) and is therefore derived
complete ([sk-prop-integral-criterion]), hence the derived limit of the
$R\Gamma_c(U,\mathcal F_n)$; as there is no cohomology in degree $-1$, the Milnor
sequence ([sk-prop-pe-milnor]) gives
$H_c^0(U,\mathcal F_0)=\varprojlim_nH_c^0(U,\mathcal F_n)$.

At a finite level, a class in $H_c^0$ is a global section of $\mathcal F_n$ whose support
is proper over the base field. A global section of the finite locally constant sheaf
$\mathcal F_n$ is locally constant, so on the connected curve it is
determined by its value at one geometric point: a section vanishing at
one point is zero; consequently the support of a nonzero global section is all of
$U$, which is not proper. Hence only the zero
section has compact support, and $H_c^0(U,\mathcal F_n)=0$ for every $n$. Therefore
$H_c^0(U,\mathcal F_0)=0$, and $H_c^0(U,\mathcal F)=H_c^0(U,\mathcal F_0)\otimes_{\cO_E}\Qlb=0$,
$\Qlb$ being flat over $\cO_E$.
