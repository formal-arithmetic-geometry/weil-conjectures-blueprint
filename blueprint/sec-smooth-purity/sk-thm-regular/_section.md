+++
id = "sk-thm-regular"
kind = "theorem"
title = "Purity for regular closed immersions"
order = 1931
uses = ["sk-def-purity-conv", "sk-lem-coprojection", "sk-lem-regular-smooth", "sk-prop-a1", "sk-prop-a1-inv", "sk-prop-an", "sk-thm-dnc", "sk-thm-smooth-purity"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_dualizingComplex_of_isRegularImmersion"]
tags = ["sketch"]
+++
Let $i:Z\hookrightarrow X$ be a regular closed immersion of pure codimension
$c$, with $X$ smooth over the perfect field $k$ and $Z$ regular.

*The fundamental class.* A *frame* of $Z$ is an étale
$U\to X$ together with $f_1,\dots,f_c\in\Gamma(U,\mathcal O_U)$ generating
the ideal of $Z_U=Z\times_XU$. Each $f_j$ is a unit on $U\setminus V(f_j)$,
so it has a Kummer class $\kappa(f_j)\in H^1(U\setminus V(f_j),\Lambda(1))$
as in [sk-def-purity-conv], and the boundary of the localization sequence
of $V(f_j)\subset U$ gives
$\partial\kappa(f_j)\in H^2_{V(f_j)}(U,\Lambda(1))$. The *class of
the frame* is the cup product with supports

$$
\operatorname{cl}(f)=\partial\kappa(f_1)\cup\cdots\cup\partial\kappa(f_c)
\ \in\ H^{2c}_{Z_U}\bigl(U,\Lambda(c)\bigr).
$$

Then:
- **(a)** $Ri^{!}\Lambda_X(c)[2c]$ is concentrated in degree $0$ with
$\mathcal H^0$ free of rank one; hence
$H^0(Z,Ri^{!}\Lambda_X(c)[2c])=H^{2c}_Z(X,\Lambda(c))=\Gamma(Z,\mathcal H^0)$,
and likewise after any étale $U\to X$.
- **(b)** $\operatorname{cl}(f)$ depends only on $Z_U\subset U$, not on
the frame, and the frame classes glue to a unique global class, the
*fundamental class*

$$
[Z\subset X]=\operatorname{cl}_{Z/X}\ \in\ H^{2c}_Z\bigl(X,\Lambda(c)\bigr)
=H^0\bigl(Z,Ri^{!}\Lambda_X(c)[2c]\bigr),
$$

which generates $\mathcal H^0$ at every geometric point. (The frame
classes and their gluing make sense for every regular closed immersion;
for the zero section of $\Aaf^1_Y$ the class so defined is
$\mathrm{pur}_s$ of [sk-prop-a1], and for the zero section of $\Aaf^c_B$
it is the generator $\partial\kappa(t_1)\cup\cdots\cup\partial\kappa(t_c)$
of [cor-pur-affine-space-zero-section-purity], by the definition of those classes; these pairs are
in the situation of the theorem when $Y$, resp. $B$, is smooth over $k$.)
- **(c)** The morphism

$$
\operatorname{cl}_i:\ \Lambda_Z\ \xrightarrow{\ \sim\ }\ Ri^{!}\Lambda_X(c)[2c],
\qquad 1\longmapsto[Z\subset X],
$$

is an isomorphism, and it equals the isomorphism assembled from smooth
purity of $a_X$ and $a_Z$ in Steps 1–2 below. Since twists pass through
$Ri^{!}$ ([sk-lem-coprojection]), equivalently the inverse of
$\operatorname{cl}_i(-c)[-2c]$ is a canonical isomorphism

$$
Ri^{!}\Lambda_X\ \xrightarrow{\ \sim\ }\ \Lambda_Z(-c)[-2c].
$$

- **(d)** It is compatible with étale base change,
$[Z_U\subset U]=[Z\subset X]|_U$, and with exterior products: for two such
pairs $(X_1,Z_1)$, $(X_2,Z_2)$ over $k$, the product
$(X_1\times_kX_2,Z_1\times_kZ_2)$ is again such a pair, of codimension
$c_1+c_2$, and
$[Z_1\times Z_2\subset X_1\times X_2]=[Z_1\subset X_1]\boxtimes[Z_2\subset X_2]$
under the exterior product of classes with supports.
