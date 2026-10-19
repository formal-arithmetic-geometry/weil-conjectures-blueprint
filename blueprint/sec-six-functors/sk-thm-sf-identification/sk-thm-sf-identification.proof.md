+++
kind = "proof"
of = "sk-thm-sf-identification"
uses = ["sk-cor-sp-all-coefficients", "sk-thm-sf-global-duality", "sk-lem-finite"]
+++
Corollary [sk-cor-sp-all-coefficients] identifies $\omega_X$. Tensoring the
second variable of internal Hom by an invertible Tate line and a shift commutes
with internal Hom. This gives the displayed description of $\mathbb D_XK$. In the
locally perfect case the dual is computed by a finite-projective local model and
evaluation is the familiar evaluation of that model. Under these identifications
the evaluation and exceptional counit of Theorem [sk-thm-sf-global-duality] are
precisely cup product, coefficient evaluation and the normalized smooth trace. Its
adjoint is consequently (1). The complexes on the point are perfect by
Lemma [sk-lem-finite]. Properness identifies the two direct images, proving the
last statement.

*Complement.* For a perfect point complex $C$, the shift convention
$H^r(C[m])=H^{r+m}(C)$ and the identification
$H^{-i}(C^\vee)\cong\operatorname{Hom}_\Lambda(H^i(C),\Lambda)$, applied to
$C=R\Gamma_c(X,K)=R\Gamma(X,K)$, turn $H^{-i}$ of (1) into the adjoint
$H^{2d-i}(X,K^\vee(d))\to\operatorname{Hom}_\Lambda(H^i_c(X,K),\Lambda)$ of
$\langle-,-\rangle_i$. The identification holds because
$\operatorname{Hom}_\Lambda(-,\Lambda)$ is exact on $\Lambda$-modules, so that
$R\operatorname{Hom}_\Lambda(C,\Lambda)$ is computed termwise and commutes with
taking cohomology. The ring $\Lambda=A_{E,n}=\mathcal O_E/\pi_E^n$ is
self-injective by Baer's criterion: its ideals are the $\pi_E^jA_{E,n}$, a
homomorphism $\varphi:\pi_E^jA_{E,n}\to A_{E,n}$ sends $\pi_E^j$ to an element
killed by $\pi_E^{n-j}$, hence to some $\pi_E^ja$, and $\varphi$ extends to
multiplication by $a$. Hence $H^{-i}$ of (1) is an isomorphism, and the pairings
$\langle-,-\rangle_i$ are perfect.
