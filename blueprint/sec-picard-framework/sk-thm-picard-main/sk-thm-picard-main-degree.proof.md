+++
kind  = "proof"
of    = "det-picard-main-degree"
+++
(1) The projection $\pi:C\times\underline{\operatorname{Pic}}_{C/k}\to\underline{\operatorname{Pic}}_{C/k}$
is proper, flat and of finite presentation, and $\cL$ is invertible,
hence flat over the base. By [det-thm-picard-coherence] (a), every point
has an affine neighbourhood $U$ on which $R\pi_*\cL$ is represented by a
bounded complex $K^\bullet$ of finite free modules whose formation
commutes with base change; so for $t\in U$,
$\chi(\cL_t)=\sum_q(-1)^q\dim_{\kappa(t)}H^q(K^\bullet\otimes\kappa(t))=\sum_q(-1)^q\operatorname{rk}K^q$,
which does not depend on $t\in U$ (the Euler characteristic of a finite
complex of vector spaces equals the alternating sum of the dimensions of
its terms). Hence $\chi(\cL_t)$, and with it $\delta$, is locally
constant, and the fibres $\delta^{-1}(d)$ are open, hence also closed
(their complement is a union of open sets). By Riemann–Roch
([lem-sc-riemann-roch], applied over an algebraic closure of
$\kappa(t)$, using [lem-pc-degree-base-change]) $\delta(t)$ is the
divisor degree of $\cL_t$.

(2) A morphism $h:T\to\underline{\operatorname{Pic}}_{C/k}$ classifies
$(\mathrm{id}\times h)^*\cL$, whose fibre at $s\in T$ is
$\cL_{h(s)}\otimes_{\kappa(h(s))}\kappa(s)$, of the same Euler
characteristic (flat base change). So $h$ factors through the open and
closed subscheme $\delta^{-1}(d)$ iff all fibres of the classified sheaf
have degree $d$. For $T=\Spec k$ this identifies the $k$-points with
$\operatorname{Pic}(C)$ in degree $d$ (rigidification is automatic since
$\operatorname{Pic}(\Spec k)=0$).

(3) Degree is additive under tensor product of invertible sheaves on a
curve over a field ([lem-pc-degree-base-change]); the dual has the
opposite degree. Hence $\operatorname{Pic}^0_{C/k}$ is a subgroup functor,
represented by the open and closed subscheme
$\underline{\operatorname{Pic}}^0_{C/k}$, which is therefore a subgroup
scheme ([rem-pc-group-structure]). The class of $\cO_C(dP)$ (rigidified
along $P$) is a $k$-point of degree $d$, and multiplication by it is an
automorphism of the group scheme $\underline{\operatorname{Pic}}_{C/k}$
with inverse multiplication by $\cO_C(-dP)$; by additivity it carries
$\delta^{-1}(0)$ onto $\delta^{-1}(d)$.
