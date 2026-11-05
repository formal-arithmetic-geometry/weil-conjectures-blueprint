+++
kind = "proof"
of = "proposition-base-change-larger-algebraically-closed--1"
order = 687002
uses = ["theorem-cohomology-curves"]
+++
Apply the slicing lemma to the smooth map $U\to S$. It gives an étale
covering by affine schemes $U_i$ such that $U_i\to S$ factors through
an affine scheme $V_i$ étale over $S$, and $U_i\to V_i$ is smooth with
geometrically connected fibres and a section. This is
`AlgebraicGeometry.Smooth.exists_etaleCover_factorization`.
Since $S$ is normal with algebraically closed function field, each
$V_i\to S$ is a local isomorphism by
`AlgebraicGeometry.Etale.isLocalIso_of_isSepClosed_functionField`.
Cover $V_i$ by nonempty affine opens $W$ whose maps to $S$ are open
immersions. The field $L$ is also the function field of $W$, and the
geometric generic point factors through $W$.

Put $B=U_i\times_{V_i}W$. Then $B\to W$ is affine and smooth of relative
dimension one, has geometrically connected fibres and a section, and
$e$ is invertible on $W$ because $e\mid m$. Restrict $\xi$ to $B_\Omega$.
By $(C_6)$ of Theorem [theorem-cohomology-curves], in its étale form
`AlgebraicGeometry.bijective_cohomologyMap_constantZMod_of_smoothOfRelativeDimension`,
this restriction comes from a class $\xi_L\in H^1(B_L,\mathbf Z/e)$.
Represent $\xi_L$ by a finite étale $\mathbf Z/e$-torsor $t$ on $B_L$.
The torsor interpretation of $H^1$ says that the pullback of $\xi_L$
along a map is zero precisely when that map lifts to $t$; this is
`AlgebraicGeometry.Scheme.EtaleTorsor.exists_forall_cohomologyMap_eq_zero_iff`.

The restriction of $\xi_L$ along the generic point of the section is
zero, since $H^1(\operatorname{Spec}L,\mathbf Z/e)=0$. Thus $t$ has an
$L$-rational point above that section. The torsor extension theorem
`AlgebraicGeometry.Scheme.EtaleTorsor.exists_isPullback_of_genericFibre`
extends $t$ to a finite étale $\mathbf Z/e$-torsor $T\to B$. Its pullback
to $B_\Omega$ kills the restricted class. More generally, the class
vanishes after pullback along any map to $B_\Omega$ whose composite to
$B$ lifts to $T$; this is the conclusion of
`AlgebraicGeometry.Etale.exists_etaleTorsor_cohomologyMap_eq_zero`.

Use the composites $T\to B\to U$ for all the chosen opens and slices.
They are étale and jointly surjective, since the slices cover $U$,
the opens cover each $V_i$, and each torsor map is surjective. The
compatibility of cohomological pullback with composition shows that
$\xi$ vanishes over every member of this covering.
