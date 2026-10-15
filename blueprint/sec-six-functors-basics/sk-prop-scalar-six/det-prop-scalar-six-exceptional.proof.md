+++
kind  = "proof"
of    = "det-prop-scalar-six-exceptional"
uses = ["det-prop-scalar-six-compact-support", "det-prop-scalar-six-direct-image", "det-prop-scalar-six-pullback", "det-prop-scalar-six-ctf", "sk-thm-existence", "sk-thm-sf-ctf-stability", "sk-lem-formal-closed-support", "sk-prop-geo-p1-adjunction", "sk-prop-diagonal-tower"]
+++
*Definition and formal properties.* By [sk-thm-existence] (4), $f^!K\in\Dctf(X,\Lambda)$,
so $\gamma^!_{f,f^!K}$ is defined and invertible, and $(f^!K)_{\Lambda'}\in\Dctf(X,\Lambda')$
by [det-prop-scalar-six-ctf]; hence $\beta_{f,K}$ is a morphism in $\Dctf(X,\Lambda')$. The
counit of a composite adjunction $R(gf)_!=Rg_!Rf_!\dashv f^!g^!$ is the composite of the
counits, and $\gamma^!$ is compatible with composition
([det-prop-scalar-six-compact-support]); transposing gives
$\beta_{gf,K}=f^!(\beta_{g,K})\circ\beta_{f,g^!K}$. For an open immersion $u$, $Ru_!=u_!$ and
$u^!=u^*$ with counit $u_!u^*\to\mathrm{id}$; the transpose of the extension of scalars of
this counit is the pullback identification of [det-prop-scalar-six-pullback]. In
particular $\beta$ is compatible with open restriction ($u^*f^!=(fu)^!$).

*Closed immersions.* Let $i\colon Z\hookrightarrow Y$ be closed with open complement
$j\colon V\hookrightarrow Y$; here $Ri_!=i_*$. By [sk-lem-formal-closed-support] there is a
distinguished triangle
$i_*R\underline\Gamma_ZK\to K\to Rj_*j^*K\to$ whose first map is the counit of
$i_*\dashv R\underline\Gamma_Z$. For $K\in\Dctf(Y,\Lambda)$ the third term lies in $\Dctf$
([sk-thm-sf-ctf-stability]), hence so does $i_*R\underline\Gamma_ZK$, and
$R\underline\Gamma_ZK=i^*i_*R\underline\Gamma_ZK\in\Dctf(Z,\Lambda)$. For $C$ in
$\Loc(\Dctf(Z,\Lambda))$, $\Hom(C,R\underline\Gamma_ZK)=\Hom(i_*C,K)=\Hom(C,i^!K)$, so by
Yoneda in $\Loc(\Dctf(Z,\Lambda))$, $R\underline\Gamma_ZK\simeq i^!K$ compatibly with the
counits. So we have a triangle in $\Dctf(Y,\Lambda)$
$$
i_*i^!K\xrightarrow{\epsilon_K}K\longrightarrow Rj_*j^*K\longrightarrow i_*i^!K[1],
$$
and the same over $\Lambda'$ for $K_{\Lambda'}$. Extension of scalars is triangulated, so
it carries the first triangle to a triangle. Compare it with the second via the
maps
$$
(i_*i^!K)_{\Lambda'}\simeq i_*\bigl((i^!K)_{\Lambda'}\bigr)\xrightarrow{i_*\beta_{i,K}}i_*i^!(K_{\Lambda'}),\qquad\mathrm{id}_{K_{\Lambda'}},\qquad(Rj_*j^*K)_{\Lambda'}\xrightarrow{\gamma_{j}}Rj_*\bigl((j^*K)_{\Lambda'}\bigr)\simeq Rj_*j^*(K_{\Lambda'}).
$$
The left square commutes by the definition of $\beta_{i,K}$ as a transpose of
$(\epsilon_K)_{\Lambda'}$; the right square commutes because $\gamma_j$ is compatible with
the units of $j^*\dashv Rj_*$ ([det-prop-scalar-six-direct-image] (2)). The right vertical
map is an isomorphism by [det-prop-scalar-six-direct-image] (1) and
[det-prop-scalar-six-pullback] (1). In a morphism of distinguished triangles whose
second and third components are isomorphisms, the first is an isomorphism. So
$i_*\beta_{i,K}$ is an isomorphism, and since $i_*$ is fully faithful
($i^*i_*=\mathrm{id}$), $\beta_{i,K}$ is an isomorphism.

*The projective line.* Let $q\colon\mathbf P^1_Y\to Y$. By [sk-prop-geo-p1-adjunction] and
[sk-prop-diagonal-tower], $Rq_*\dashv q^*(1)[2]$ on $\Dctf$, with unit built from the
diagonal class $\delta_\Lambda$ and counit $\epsilon_N=(1\otimes\operatorname{Tr}_q)\circ(\text{projection formula})$;
since $q$ is proper, $Rq_!=Rq_*$ and therefore $q^!\simeq q^*(1)[2]$ with this counit.
The classes $\delta_\Lambda$ and $\operatorname{Tr}_q$ commute with every listed coefficient map:
for finite rings they are constructed from the Kummer sequence and derived scalar
extension, and are compatible with change of finite coefficients
([sk-prop-geo-p1-adjunction]); the $\mathcal O_E$-classes are the compatible limits of the
finite ones; the $E$- and $\Qlb$-classes are their scalar extensions
([sk-prop-diagonal-tower]). For $\mathcal O_E\to A$, the finite free resolution of $A_X$
constructed in [det-prop-scalar-six-direct-image] shows that $A_X\otimes^{\mathbf L}-$ commutes
with the inverse limits defining the integral classes, and the resulting classes
are exactly the finite coefficient classes. Consequently the counit over $\Lambda'$ at
$N_{\Lambda'}$ is the extension of scalars of the counit over $\Lambda$ at $N$, modulo the
comparisons $\gamma_q$ and the projection formula. With $K=N$ this says that
$\beta_{q,K}$ is the pullback-and-twist identification
$(q^*K(1)[2])_{\Lambda'}\simeq q^*(K_{\Lambda'})(1)[2]$, an isomorphism.

*Affine space.* The projection $\mathbf A^1_Y\to Y$ is $q\circ u$ with
$u\colon\mathbf A^1_Y\hookrightarrow\mathbf P^1_Y$ open; by compatibility with composition and
the open case, $\beta$ is an isomorphism for it, and then for $\mathbf A^n_Y\to Y$ as a
composite of $n$ such projections.

*General $f$.* Since $\beta$ is compatible with open restriction and isomorphisms in
$\D(X_{\mathrm{proét}},\Lambda')$ can be checked on an open cover, we may replace $X$ by the
members of a finite affine open cover. For $X$ affine of finite type over $k$,
choose a closed immersion $\iota\colon X\hookrightarrow\mathbf A^n_k$; then
$(\iota,f)\colon X\to\mathbf A^n_k\times_kY=\mathbf A^n_Y$ is a closed immersion (its composite
with the separated projection to $\mathbf A^n_k$ is one), and $f$ is $(\iota,f)$ followed by
the projection $\mathbf A^n_Y\to Y$. By the closed-immersion and affine-space cases and
compatibility with composition, $\beta_{f,K}$ is an isomorphism.
