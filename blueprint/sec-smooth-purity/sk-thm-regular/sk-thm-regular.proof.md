+++
kind  = "proof"
of    = "sk-thm-regular"
+++
*Step 1: the $\omega$-identification.* Work on a connected component of
$X$; the resulting isomorphisms assemble over the disjoint union. By
[sk-lem-regular-smooth], $a_X$ and $a_Z$ are smooth of dimensions $n$ and
$m=n-c$ with $a_Z=a_X\circ i$, so the composition law for the exceptional
inverse image gives

$$
\omega_{Z/k}=Ra_Z^{!}\Lambda_k\ \cong\ Ri^{!}Ra_X^{!}\Lambda_k=Ri^{!}\omega_{X/k},
$$

while [sk-thm-smooth-purity] applied to $a_X$ and to $a_Z$ gives
$\omega_{X/k}\cong\Lambda_X(n)[2n]$ and $\omega_{Z/k}\cong\Lambda_Z(m)[2m]$.

*Step 2: the co-projection removes the twist.* By
[sk-lem-coprojection] with $K=\Lambda_X$ and the invertible
$L=\Lambda_X(n)[2n]$,

$$
Ri^{!}\bigl(\Lambda_X(n)[2n]\bigr)\ \cong\
Ri^{!}\Lambda_X\otimes^{\mathbb L}_{\Lambda_Z}\Lambda_Z(n)[2n].
$$

Combining with Step 1 and cancelling the invertible $\Lambda_Z(n)[2n]$,

$$
Ri^{!}\Lambda_X\ \cong\ \Lambda_Z(m-n)[2m-2n]=\Lambda_Z(-c)[-2c],
$$

and twisting by $(c)[2c]$ (again [sk-lem-coprojection]) gives an
isomorphism $\Phi_i:\Lambda_Z\xrightarrow{\sim}Ri^{!}\Lambda_X(c)[2c]$.
This proves (a): $H^0(Z,Ri^{!}K)=H^0R\Gamma_Z(X,K)$ because $Ri_*Ri^{!}$
is $R\underline\Gamma_Z$, and the construction restricts to every étale
$U\to X$ since $Ru^{!}=u^{*}$ for étale $u$.

*Step 3: the frame class is well defined.* By (a), frame classes are
sections of the sheaf $\mathcal H^0$ on $Z_{\Et}$, so it suffices to compare
two frames $f,f'$ on the same $U$ Zariski-locally. There $f'=Mf$ with
$M\in GL_c(\mathcal O)$, and after shrinking $M$ is a product of diagonal,
permutation and elementary matrices. The frame-change argument for the zero section of $\Aaf^c$
applies verbatim: a unit $u$ has $\kappa(u)$ defined on all of $U$, so
$\partial\kappa(u)=0$ and $\partial\kappa(uf_j)=\partial\kappa(f_j)$; the
factors $\partial\kappa(f_j)$ have even degree, so permuting them costs no
sign; for a shear $f_1+tuf_2$ the frame over $\Aaf^1_U$ of the pair
$(\Aaf^1\times U,\Aaf^1\times Z_U)$, to which (a) applies, gives a section of
the constant rank-one $\mathcal H^0$ on $\Aaf^1_{Z_U}$, constant along the
line by [sk-prop-a1-inv](i), so its values at $t=0,1$ agree. The sheaf axiom
for $\mathcal H^0$ glues the local frame classes (frames exist locally, $i$
being regular) to a unique global $[Z\subset X]$.

*Step 4: comparison with the smooth-purity isomorphism.* We show
$\Phi_i(1)=(-1)^c[Z\subset X]$; both are sections of $\mathcal H^0$, so this is
étale-local on $X$. Let $z\in Z$, choose a frame $f_1,\dots,f_c$ near $z$
and functions $g_1,\dots,g_m$ near $z$ whose restrictions to $Z$ (smooth by
[sk-lem-regular-smooth]) have differentials forming a basis of
$\Omega_{Z/k}\otimes k(z)$. The conormal sequence
$0\to I/I^2\otimes k(z)\to\Omega_{X/k}\otimes k(z)\to\Omega_{Z/k}\otimes k(z)\to0$
shows that $u=(f,g):U\to\Aaf^c_k\times\Aaf^m_k=\Aaf^n_k$ is étale near $z$,
and $u^{-1}(0\times\Aaf^m_k)=V(f)=Z_U$; call $u':Z_U\to\Aaf^m_k$ the
restriction and $i_0:\Aaf^m_k\hookrightarrow\Aaf^n_k$ the zero section of
$p:\Aaf^c_{\Aaf^m}\to\Aaf^m$.
(i) Since $u,u'$ are étale, $Ri_U^{!}u^{*}=R(u i_U)^{!}=R(i_0u')^{!}=u'^{*}Ri_0^{!}$.
(ii) As $a_U=a_{\Aaf^n}\circ u$ and $a_{Z_U}=a_{\Aaf^m}\circ u'$ with
$\omega_u=\Lambda$, $\omega_{u'}=\Lambda$, compatibility of
[sk-thm-smooth-purity] with composition gives $\Phi_{i_U}=u'^{*}\Phi_{i_0}$.
(iii) On the model, $a_{\Aaf^n}=a_{\Aaf^m}\circ p$ and $p\,i_0=\mathrm{id}$, so by
composition compatibility again $\Phi_{i_0}$ is $Ri_0^{!}$ of the
smooth-purity isomorphism $\Lambda(c)[2c]\cong Rp^{!}\Lambda$ of
[sk-thm-smooth-purity] for $p$, composed with
$Ri_0^{!}Rp^{!}=\mathrm{id}$ (twists passing through $Ri_0^{!}$ by
[sk-lem-coprojection]). By the agreement clause of
[sk-thm-smooth-purity] ($p$ is the projection of a trivial vector bundle;
the clause rests on the normalization of [sk-thm-dnc] in standard
coordinates), that isomorphism is the affine-space purity comparison $\gamma_{p,\Lambda}$
of [sk-prop-an] ([def-pur-affine-space-comparison]), and by the normalization in [cor-pur-affine-space-zero-section-purity],
$Ri_0^{!}\gamma_{p,\Lambda}$ composed with $Ri_0^{!}Rp^{!}=\mathrm{id}$ is
$(-1)^c$ times the inverse of the Thom class
$\mathrm{pur}_s\boxtimes\cdots\boxtimes\mathrm{pur}_s$: it carries
$\partial\kappa(t_1)\cup\cdots\cup\partial\kappa(t_c)$ to $(-1)^c$, each
$\partial\kappa(t_j)$ being minus the Cartier class of $V(t_j)$, which the
projective-line trace normalizes to $1$. Hence
$\Phi_{i_0}(1)=(-1)^c\,\partial\kappa(t_1)\cup\cdots\cup\partial\kappa(t_c)$
([cor-pur-affine-space-zero-section-purity], with [det-prop-a1]): $(-1)^c$
times the class of the coordinate frame.
(iv) Kummer classes, boundaries and cup products with supports commute with
pullback and $u^{*}t_j=f_j$, so $\Phi_i(1)|_{Z_U}=u'^{*}\Phi_{i_0}(1)
=(-1)^c\operatorname{cl}(f)=(-1)^c[Z\subset X]|_{Z_U}$. Such $U$ cover $Z$, hence
$\Phi_i(1)=(-1)^c[Z\subset X]$. As $\Phi_i$ is an isomorphism and $(-1)^c$ is
a unit, $[Z\subset X]$ generates every stalk and
$\operatorname{cl}_i=(-1)^c\Phi_i$; this is (b) and (c).

*Step 5: compatibilities.* An étale $X'\to X$ pulls frames back to
frames and frame classes to frame classes, so
$[Z_{X'}\subset X']=[Z\subset X]|_{X'}$, and by (c) $\operatorname{cl}_i$
restricts to $\operatorname{cl}_{i'}$. For products, $Z_1\times_kZ_2$ is smooth
over $k$, and frames $f$ on $U_1$, $g$ on $U_2$ give the frame
$(\mathrm{pr}_1^{*}f,\mathrm{pr}_2^{*}g)$ on $U_1\times_kU_2$, whose class is
$\mathrm{pr}_1^{*}\operatorname{cl}(f)\cup\mathrm{pr}_2^{*}\operatorname{cl}(g)
=\operatorname{cl}(f)\boxtimes\operatorname{cl}(g)$ by naturality and
associativity of supported cup products (no signs, all degrees even);
gluing gives the asserted identity, and by (c) the exterior product of
$\operatorname{cl}_{i_1}$ and $\operatorname{cl}_{i_2}$ is
$\operatorname{cl}_{i_1\times i_2}$.
