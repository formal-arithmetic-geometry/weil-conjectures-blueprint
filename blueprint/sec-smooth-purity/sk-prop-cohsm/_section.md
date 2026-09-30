+++
id = "sk-prop-cohsm"
kind = "section"
title = "Cohomological smoothness"
order = 1991
uses = ["sk-prop-a1", "sk-prop-an"]
lean = ["AlgebraicGeometry.Etale.isInvertible_dualizingComplex", "AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_obj_derivedTensor", "AlgebraicGeometry.Etale.nonempty_iso_leftDerivedUpperStar_comp_rightDerivedUpperShriek"]
+++
*Proposition (sketch).*

For every smooth separated $f:X\to Y$ of pure relative dimension
$d$:

1. **(a)** $\omega_f=Rf^{!}\Lambda_Y$ is *invertible* (lisse
rank-one object, canonically formed, compatible with base change);
1. **(b)** *tensor formula:* for every
$K\in D^b_{ctf}(Y,\Lambda)$,
$Lf^{*}K\otimes^{\mathbb L}\omega_f\ \cong\ Rf^{!}K$;
1. **(c)** *smooth base change for $R^{!}$:* in a Cartesian
square with $f$ smooth and $f'$ the base change,
$Rp'^{!}Lf^{*}\cong Lg^{*}Rf^{!}$; in particular, in the diagonal
square,
$\omega_{p_1}\cong Lp_2^{*}\omega_f$, $\omega_{p_2}\cong Lp_1^{*}\omega_f$.

Content: the proof is Steps 1–6 below; the model case is Move
(2$'$) ([sk-prop-an]: $\Aaf^n$-purity, iterating the
$\Aaf^1$-computation), the étale machinery is the local normal
form (Blueprint 07-new) and the lemma that isomorphisms descend
along étale surjections. *(The abstract criterion
``ULA $\Rightarrow$ cohomological smoothness'' — Zavyalov 5.7.7,
with ULA of smooth morphisms, Blueprint 07-new / Stacks
`0GJM` — is *not* used here: it belongs to the
general six-functor dictionary, while for smooth morphisms the
proof below is self-contained once the $\Aaf^n$-model is known.)*

## Proof

Let $\varphi_K:Lf^{*}K\otimes^{\mathbb L}\omega_f\to Rf^{!}K$ be the
canonical map (the mate of the projection formula of the package).
We use three elementary facts throughout: geometric stalks are
conservative for sheaves (a sheaf morphism is an isomorphism iff it
is one at every geometric stalk); for étale $u:U\to X$ and a
geometric point $\bar x\to X$ with a lift $\bar y\to U$, the stalk
$(Lu^{*}\mathcal G)_{\bar y}$ is the stalk $\mathcal G_{\bar x}$
(functor $u^{-1}$ on sheaves, and for complexes on the cohomology
sheaves); a bounded complex with all cohomology sheaves zero is
zero (induction on the cohomological range via the exact triangle of
the truncations).

*Step 1: the model case (the trace-cycle content).* For
$f=p_d:\Aaf^d_Y\to Y$, [sk-prop-an] gives the canonical comparison
$\gamma_{p_d,K}:Lp_d^{*}K(d)[2d]\to Rp_d^{!}K$, an isomorphism for
every $K$; by the twist reassociation it is exactly
$\varphi_{p_d,K}$. In particular

$$
\omega_{p_d}\ \cong\ \Lambda(d)[2d],
$$

which is invertible — so (a), (b) hold for $p_d$. This one
dimension is the whole trace-cycle content: the boundary of the
Kummer class is the rank-one class of Move (1), the
$\mathbf P^1$-formula is the triviality $H^q(\Aaf^1,\Lambda(1))=0$
for $q>0$ with the Kummer computation on the punctured line, and
excision is the localization triangle.

*Step 2: étale locality.* For étale $u:X'\to X$ with
$f'=f\circ u$: the étale normalisation $Ru^{!}=Lu^{*}$ and the
composition rule give

$$
Lu^{*}\omega_f=Lu^{*}Rf^{!}\Lambda_Y\cong R(f\circ u)^{!}\Lambda_Y=\omega_{f'},
$$

and $Lu^{*}\varphi_K=\varphi_{K}$ for the base-changed map, by
naturality of the adjunction.

*Step 3: charts, then the local-to-global argument for
$\varphi_K$.* By the étale-local normal form (Blueprint 07-new),
every $x\in X$ has an étale neighbourhood $u_x:X'_x\to X$ and
étale $v_x:X'_x\to\Aaf^d_Y$ with $f\circ u_x=p_d\circ v_x$. By
Step 2, $Lu_x^{*}\varphi_K$ is the pullback (along $v_x$) of the
model map $\varphi_{p_d,K}$, hence an isomorphism on each chart.
Let $U=\coprod_xX'_x\xrightarrow{u}X$ (surjective étale). We
prove: $Lu^{*}\varphi_K$ iso $\Rightarrow$ $\varphi_K$ iso.

- **(i)** It suffices that all $\mathcal H^r(\varphi_K)$ are
isomorphisms of sheaves: then all $\mathcal H^r$ of the mapping
cone vanish, so the cone is zero by the third elementary fact
above.
- **(ii)** A morphism of sheaves is an isomorphism iff it is
isomorphic at every geometric stalk (conservativity: kernel and
cokernel have zero stalks, and a sheaf with zero stalks is zero —
its sections vanish on an étale neighbourhood of every point and
the sheaf axiom glues this to a zero section).
- **(iii)** For a geometric point $\bar x\to X$ of $X$ choose a
geometric point $\bar y\to U$ above it ($u$ surjective); since
$u^{*}\mathcal H^r(\varphi_K)$ has stalk $\mathcal H^r(\varphi_K)_{\bar x}$
at $\bar y$ (the second elementary fact), and since $Lu^{*}\varphi_K$
is an isomorphism, all stalks of $\mathcal H^r(\varphi_K)$ are
isomorphisms; by (ii), $\mathcal H^r(\varphi_K)$ is an
isomorphism; by (i), $\varphi_K$ is an isomorphism — (b) for
every smooth $f$.

*Step 4: invertibility of $\omega_f$ — (a), without making
or gluing any object.*

- **(4a)** *Concentration.* On each chart $X'_x$,
$Lu_x^{*}\omega_f\cong\Lambda(d)[2d]$ is concentrated in one degree
($\mathcal H^r=0$ for $r\neq-2d$). For any geometric point $\bar x$
of $X$, the stalk $\mathcal H^r(\omega_f)_{\bar x}$ equals the
stalk of $\mathcal H^r(Lu_x^{*}\omega_f)$ at a lift $\bar y$, by the
second elementary fact; hence
$\mathcal H^r(\omega_f)_{\bar x}=0$ for $r\neq-2d$ at every
geometric point, so $\mathcal H^r(\omega_f)=0$ for $r\neq-2d$ by
conservativity. As $\omega_f$ is bounded, the $t$-structure gives
$$
\omega_f\ \cong\ \mathcal L[2d],\qquad
\mathcal L:=\mathcal H^{-2d}(\omega_f).
$$
(Here $\mathcal L$ is a sheaf that *already exists* as a
cohomology sheaf of the given object $\omega_f$; nothing is
constructed by descent.)
- **(4b)** *Lisse of rank one is a local property of this
given sheaf.* By Step 2 and Step 1,
$\mathcal L|_{X'_x}\cong\Lambda(d)$ for every chart — a trivial
costant sheaf of rank one; the $X'_x$ form an étale cover of $X$
trivializing $\mathcal L$, so $\mathcal L$ is lisse of rank one
(this is the *definition* of lisse for the sheaf $\mathcal L$;
only the given sheaf and its existing restrictions are used).
- **(4c)** *Inverse.* A lisse rank-one sheaf $\mathcal L$ is
invertible under $\otimes$: put
$\mathcal L^{-1}:=\mathcal H\!om(\mathcal L,\Lambda)$; the
evaluation $\mathcal L\otimes\mathcal L^{-1}\to\Lambda$ is
étale-locally — when restricted to a trivializing $X'_x$ — the
identity of $\Lambda$, hence it is an isomorphism at every geometric
stalk, hence an isomorphism of sheaves by conservativity (no gluing:
both sides are existing sheaves).
- **(4d)** Since $\Lambda(d)=\Lambda(1)^{\otimes d}$ is invertible
for the twist, $\omega_f\cong\mathcal L[2d]$ is invertible, with
inverse $\mathcal L^{-1}[-2d]$ (the shift is compatible with
$\otimes^{\mathbb L}$ on bounded objects): this is (a).

*Step 5: base change and (c).* Let $v:Y'\to Y$ be a base
change and $f'$ the base-changed morphism. The canonical map
$Lv^{*}\omega_f\to\omega_{f'}$: after the base change of the
charts (the normal form and the model base-change of
[sk-prop-an]), the diagram is transported to the model case
$p_d:\Aaf^d_{Y'}\to Y'$, where the map is the identity of the
constant $\Lambda(d)[2d]$; hence it is étale-locally (in the
source and the base) the identity, and by the same stalk/step-(iii)
argument it is an isomorphism — so
$Lv^{*}\omega_f\cong\omega_{f'}$, and, together with the naturality
of $\varphi$, the same argument gives the compatibility of
$\varphi$ with base change. Read in the Cartesian square with $f$
smooth,

$$
Rp_1^{!}Lf^{*}\ \cong\ Lp_2^{*}Rf^{!},
$$

in particular $\omega_{p_1}\cong Lp_2^{*}\omega_f$ and
$\omega_{p_2}\cong Lp_1^{*}\omega_f$ (the case $K=\Lambda_Y$ with
$v=p_2$; general $K$ follows by the projection formula, the two
canonical maps being compatible). This is (c).

*Step 6: composition.* The canonical map is natural in $f$;
for composable smooth morphisms both the associators and the
composition isomorphism $c_{g,f}:R(gf)^{!}\cong Rf^{!}Rg^{!}$ are
canonical, and the two assemblies agree because the model case is
compatible with the tower of affine-space projections — hence the
composition compatibility used in the diagonal argument (the chain
rule $\omega_{vu}\cong\omega_u\otimes Lu^{*}\omega_v$).

Uses: [sk-prop-a1], [sk-prop-an]
