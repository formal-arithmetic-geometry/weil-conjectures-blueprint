+++
kind  = "proof"
of    = "sk-thm-purity-transport"
uses = ["sk-thm-smooth-purity", "sk-prop-sp-integral-adjunction", "sk-prop-sp-rational", "sk-thm-sp-qbar", "sk-prop-sf-existence", "sk-thm-existence", "sk-prop-sp-unique-adjoint", "det-sp-purity-coefficient-change"]
+++
*Step 1 (compatibility with the finite reductions).* For $m\le n$
write $\mathrm{red}_{n,m}=(-)\otimes^{L}_{A_{E,n}}A_{E,m}$. By
[sk-thm-smooth-purity] the map $\gamma_{f,K}$ is the composite of three
constituents: the canonical twist reassociation, the inverse of the
diagonal identification $\omega_f\cong\Lambda_X(d)[2d]$ of
[sk-thm-smooth-purity], and the tensor formula (G11) of [sk-prop-cohsm]. Each
is compatible with $\mathrm{red}_{n,m}$: the finite-level twist
$A(1)=\mu_{\ell^N}\otimes_{\Z/\ell^N}A$ of [sk-def-purity-conv] and the
Kummer boundary $\partial\kappa(t)$ that orients it ([sk-prop-a1]) reduce to
their counterparts over $A_{E,m}$, and the exceptional adjunction
$Rf_!\dashv Rf^{!}$ is compatible with reduction of the coefficient ring.
Hence $\mathrm{red}_{n,m}(\gamma_{f,K})=\gamma_{f,\mathrm{red}_{n,m}K}$,
and likewise for the orientations, the smooth traces and the composition
and base-change squares of [sk-prop-cohsm] (G12).

*Step 2 (the coefficients $\mathcal O_E$, $E$ and $\Qlb$).* These are the
condensed coefficient rings of [def-sf-setting], and no stage is built from
another. For $\Lambda=\mathcal O_E$, [sk-prop-sp-integral-adjunction] shows that
$K\mapsto f^*_{\mathcal O_E}K(d)[2d]$ is right adjoint to $Rf_{!,\mathcal O_E}$ on
$\Dbc(-,\mathcal O_E)$. Its proof passes through the tower model of
[sk-prop-sp-tower-geometric] and uses the equivalence of $\Dbc(-,\mathcal O_E)$ with
normalized towers ([sk-lem-sp-tower]), a consequence of the integral criterion
[sk-prop-integral-criterion]. For $\Lambda=E$ the same holds by
[sk-prop-sp-rational], where integral models and Hom groups tensored with $E$
enter only as consequences of [sk-lem-integral-models] and
[sk-thm-sfb-rationalization-comparison]. For $\Lambda=\Qlb$ it holds by
[sk-thm-sp-qbar], where descent to a finite $E$ is
[sk-thm-sfb-qlbar-two-colimit].

*Step 3 (identification with $f^!$ and uniqueness).* Both adjunctions live on
$\Dctf(X,\Lambda)$ and $\Dctf(Y,\Lambda)$, and in both $Rf_!$ is the composite
$R\bar f_*\circ j_!$ of ordinary derived functors on module sheaves for a
compactification $f=\bar f\circ j$, independent of the compactification. Finite
purity ([sk-thm-smooth-purity]), the integral adjunction
([sk-prop-sp-integral-adjunction]) and its rational extensions
([sk-prop-sp-rational] and [sk-thm-sp-qbar]) show, in the respective
coefficient cases, that $K\mapsto f_\Lambda^*K(d)[2d]$ is right adjoint to
$Rf_{!,\Lambda}$. By [sk-prop-sf-existence] and [sk-thm-existence], the
restriction of $f^!$ is also right adjoint to $Rf_{!,\Lambda}$ on $\Dctf$.
[sk-prop-sp-unique-adjoint] gives the unique counit-preserving isomorphism from
the explicit adjoint $K\mapsto f_\Lambda^*K(d)[2d]$ to $f_\Lambda^!$.

*Step 4 (compatibility with change of coefficients).* By Step 1 and
[det-sp-purity-coefficient-change], the purity maps and smooth traces with
coefficients $\mathcal O_E$ reduce modulo $\ell^n$ (and modulo $\pi_E^n$) to
the finite ones, those with coefficients $E$ are obtained from integral models
by inverting $\ell$, and those with coefficients $\Qlb$ by extension of scalars
from a finite $E$. Applied to $f=a_X$ and $K=\Lambda_{\Spec k}$ this gives
$\omega_{X,\Lambda}\simeq\Lambda_X(d)[2d]$, with the counit normalized by
finite-level integration ([sk-cor-sp-all-coefficients]).

For every admissible $\Lambda$ the exceptional inverse image of a smooth
morphism is therefore the twisted and shifted inverse image, normalized by
integration on the affine line, and the smooth trace is the counit of
$Rf_!\dashv f^!$ in this form. It is compatible with change of coefficients
(Step 4), base change ([sk-prop-sp-purity-bc]) and composition
([sk-prop-sp-composition], [sk-prop-sp-trace-composition]).
