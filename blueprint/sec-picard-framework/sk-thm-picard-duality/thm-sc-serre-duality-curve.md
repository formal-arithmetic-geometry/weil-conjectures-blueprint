+++
id = "thm-sc-serre-duality-curve"
kind = "theorem"
title = "Serre duality for smooth proper curves"
order = 702
uses = ["def-sc-curves", "def-sc-function-field", "def-sc-invertible-module", "def-sc-kahler-differentials", "lem-sc-canonical-sheaf", "lem-sc-deg-principal-zero", "lem-sc-finite-duality", "lem-sc-invertible-dual", "lem-sc-morphism-from-function", "lem-sc-p1-hi-vanishing", "lem-sc-smooth-regular", "lem-weil-pbc-finite-proper", "pqf-def-coherent", "pqf-lem-affine-vanishing", "pqf-lem-fff-vanishing", "pqf-lem-finite-qf", "pqf-lem-leray", "pqf-lem-leray-lowdegree", "pqf-lem-qf-finitefibres", "pqf-lem-sheaf-zero-stalks", "thm-pqf-finite-iff-proper-finite-fibres", "thm-sc-p1-duality"]
lean = ["AlgebraicGeometry.Scheme.serreDuality"]
+++
Let $k$ be a field, $C$ a scheme over $k$ which is smooth of
relative dimension $1$ and proper over $k$, and let
$\omega_C:=\Omega^1_{C/k}$ be the sheaf of Kähler differentials of $C$
over $k$ ([def-sc-kahler-differentials]). For a finite locally free
$\mathcal O_C$-module $\mathcal M$ (a
quasi-coherent module Zariski-locally isomorphic to
$\mathcal O_C^{\oplus r}$ for some $r\ge0$) write
$\mathcal M^{\vee}:=\mathcal H om_{\mathcal O_C}(\mathcal M,\mathcal O_C)$.
Then for $p,q\ge0$ with $p+q=1$ there are $k$-linear isomorphisms

$$
e_{\mathcal M}:H^q(C,\mathcal M)^{\vee}\;\xrightarrow{\ \sim\ }\;
H^{p}\bigl(C,\;\mathcal M^{\vee}\otimes\omega_C\bigr),
$$

natural in $\mathcal M$: for every morphism
$\varphi:\mathcal M\to\mathcal N$ of finite locally free modules,
$e_{\mathcal M}\circ H^q(\varphi)^{\vee}
=H^p(\varphi^{\vee}\otimes1)\circ e_{\mathcal N}$. In particular, for
an invertible $\mathcal M$ ([def-sc-invertible-module],
so $\mathcal M^{\vee}\cong\mathcal M^{-1}$ by
[lem-sc-invertible-dual]):

$$
H^1(C,\mathcal M)^{\vee}\;\cong\;
H^0\bigl(C,\;\Omega^1_{C/k}\otimes\mathcal M^{-1}\bigr),
\qquad
H^0(C,\mathcal M)^{\vee}\;\cong\;
H^1\bigl(C,\;\Omega^1_{C/k}\otimes\mathcal M^{-1}\bigr).
$$

For a coherent
$\mathcal F$ which is not locally free the right hand side must be
replaced by $\operatorname{Ext}^{p}(\mathcal F,\omega_C)$, as in
[thm-sc-p1-duality]: e.g. for the skyscraper
$\mathcal F=\kappa(x)$ at a $k$-rational point $x$ of $C$,
$H^0(C,\mathcal F)^{\vee}=k$ but $\mathcal F^{\vee}=0$.

## Proof

All modules below are finite locally free, hence coherent on the
Noetherian scheme $C$ ([pqf-def-coherent]); their cohomology groups are
finite-dimensional $k$-vector spaces, $C$ being proper over $k$.

**Step 1 (reduction to connected $C$).** The scheme $C$ is of finite type
over $k$, hence Noetherian, so it has finitely many connected components
$C_1,\dots,C_m$, each open and closed; $C=\coprod_jC_j$, and each $C_j$
is again smooth of relative dimension $1$ and proper over $k$. Restriction
to the $C_j$ identifies a finite locally free module $\mathcal M$ with the
family $(\mathcal M|_{C_j})_j$, morphisms with families of morphisms, and
$H^q(C,\mathcal M)=\bigoplus_jH^q(C_j,\mathcal M|_{C_j})$, naturally in
$\mathcal M$; moreover $(\mathcal M^{\vee}\otimes\omega_C)|_{C_j}=
(\mathcal M|_{C_j})^{\vee}\otimes\omega_{C_j}$, since duals, tensor
products and Kähler differentials are formed locally. Since
$(\bigoplus_jV_j)^{\vee}=\bigoplus_jV_j^{\vee}$ for finitely many
$V_j$, natural isomorphisms $e^{(j)}$ on the components assemble to
$e_{\mathcal M}:=\bigoplus_je^{(j)}_{\mathcal M|_{C_j}}$, natural in
$\mathcal M$. So we may assume $C$ connected (if $C=\emptyset$ all groups
are $0$).

**Step 2 (reduction to $q=1$).** The sheaf $\Omega^1_{C/k}$ is a line
bundle ([lem-sc-canonical-sheaf]; it is locally free of rank $1$ because
$C\to\operatorname{Spec}k$ is smooth of relative dimension $1$), so
$\mathcal M^{\vee}\otimes\omega_C$ is again finite locally free (on an
open trivializing $\mathcal M$ and $\omega_C$ it is $\mathcal O^{\oplus r}$).
For finite locally free $\mathcal M$ the canonical maps
$\mathcal M\to\mathcal M^{\vee\vee}$ and
$\omega_C^{\vee}\otimes\omega_C\to\mathcal O_C$ are isomorphisms
(check on opens where the modules are free), so there is an isomorphism
$\beta_{\mathcal M}:(\mathcal M^{\vee}\otimes\omega_C)^{\vee}\otimes\omega_C\cong\mathcal M$,
natural in $\mathcal M$. Suppose the case $q=1$ is proved: natural
isomorphisms $e^1_{\mathcal N}:H^1(C,\mathcal N)^{\vee}\cong
H^0(C,\mathcal N^{\vee}\otimes\omega_C)$ for finite locally free
$\mathcal N$. Applying $e^1$ to $\mathcal N:=\mathcal M^{\vee}\otimes\omega_C$
and composing with $H^0(\beta_{\mathcal M})$ gives an isomorphism
$H^1(C,\mathcal M^{\vee}\otimes\omega_C)^{\vee}\cong H^0(C,\mathcal M)$,
natural in $\mathcal M$ (both $\mathcal M\mapsto\mathcal M^{\vee}\otimes\omega_C$
and $\beta$ are natural). Dualizing, and using that a finite-dimensional
space is naturally isomorphic to its bidual, gives
$e^0_{\mathcal M}:H^0(C,\mathcal M)^{\vee}\cong H^1(C,\mathcal M^{\vee}\otimes\omega_C)$,
natural in $\mathcal M$: the case $q=0$, $p=1$.

**Step 3 (a finite flat map to $\mathbf P^1_k$).** Let $C$ be connected.
Then $C$ is integral: its local rings are domains
([lem-sc-smooth-regular]), so its irreducible components are pairwise
disjoint (a point belonging to two components would have a local ring
with two minimal primes), and connectedness leaves a single component.
It is nonempty of dimension $1$ (smooth of relative dimension $1$), so
its function field $k(C)$ ([def-sc-function-field]) has transcendence
degree one over $k$: for an integral scheme of finite type over a field,
$\dim X=\operatorname{trdeg}_k k(X)$ by Noether normalization (as in the
proof of [lem-sc-deg-principal-zero]). The generic stalk of the line
bundle $\Omega^1_{C/k}$ is $\Omega^1_{k(C)/k}$, a one-dimensional
$k(C)$-vector space spanned by the differentials $dt$, $t\in k(C)$;
choose $t\in k(C)$ with $dt\neq0$. Then $t$ is transcendental over $k$:
since $C$ is smooth, hence geometrically reduced, over $k$, every element
of $k(C)$ algebraic over $k$ is separable over $k$, and a separable
algebraic element $a$ has $da=0$ (differentiate its minimal polynomial
$P$: $P'(a)\,da=0$ with $P'(a)\neq0$). Moreover $k(C)$ is finite over
$k(t)$ (finitely generated of transcendence degree one) and
$\Omega^1_{k(C)/k(t)}=\Omega^1_{k(C)/k}/k(C)\,dt=0$, so the finite
extension $k(C)\supset k(t)$ is separable. Let
$f:=\pi_t:C\to\mathbf P^1_k$ be the morphism of
[lem-sc-morphism-from-function]: finite, surjective and flat, of degree
$d:=[k(C):k(t)]$.

**Step 4 (transfer of the cohomology).** The morphism $f$ is proper
(finite morphisms of schemes are proper, [lem-weil-pbc-finite-proper])
with finite fibres ([pqf-lem-finite-qf], [pqf-lem-qf-finitefibres]), and
$\mathbf P^1_k$ is locally Noetherian. Let $\mathcal M$ be finite locally
free, hence coherent ([pqf-def-coherent]). Then [pqf-lem-fff-vanishing]
gives $(R^pf_*\mathcal M)_y=0$ for all $p>0$ and all $y\in\mathbf P^1_k$,
i.e. $R^pf_*\mathcal M=0$ for $p>0$ ([pqf-lem-sheaf-zero-stalks]). The
Leray spectral sequence
$E_2^{p,q}=H^p(\mathbf P^1_k,R^qf_*\mathcal M)\Rightarrow H^{p+q}(C,\mathcal M)$
([pqf-lem-leray]) is therefore concentrated on the row $q=0$ and gives
isomorphisms $H^p(\mathbf P^1_k,f_*\mathcal M)\cong H^p(C,\mathcal M)$, the
edge maps, which are natural in $\mathcal M$; in degree one this is the
low-degree exact sequence of [pqf-lem-leray-lowdegree]:
$H^1(C,\mathcal M)\cong H^1(\mathbf P^1_k,f_*\mathcal M)$.

Moreover $f_*\mathcal M$ is a finite locally free
$\mathcal O_{\mathbf P^1_k}$-module: over an affine open
$U=\operatorname{Spec}R\subset\mathbf P^1_k$ the preimage
$f^{-1}(U)=\operatorname{Spec}B$ is affine with $B$ a finite locally
free $R$-algebra (finite flat), and $f_*\mathcal M|_U$ is associated with
$\Gamma(f^{-1}(U),\mathcal M)$, a finitely generated projective
$B$-module, hence a finitely generated projective $R$-module (a direct
summand of $B^{\oplus m}$, which is finite projective over $R$); if
$\mathcal M$ has rank $r$, its rank is $rd$.

**Step 5 (duality, $q=1$).** Since $f_*\mathcal M$ is coherent,
[thm-sc-p1-duality] gives an isomorphism
$H^1(\mathbf P^1_k,f_*\mathcal M)^{\vee}\cong
\operatorname{Hom}_{\mathcal O_{\mathbf P^1}}(f_*\mathcal M,\omega_{\mathbf P^1})$,
and since $f$ is finite flat with $k(C)\supset k(t)$ separable,
[lem-sc-finite-duality] gives
$\operatorname{Hom}_{\mathcal O_{\mathbf P^1}}(f_*\mathcal M,\omega_{\mathbf P^1})\cong
H^0(C,\omega_C\otimes\mathcal M^{\vee})$. Composing,

$$
H^1(C,\mathcal M)^{\vee}
\cong H^1(\mathbf P^1_k,f_*\mathcal M)^{\vee}
\cong \operatorname{Hom}_{\mathcal O_{\mathbf P^1}}
\bigl(f_*\mathcal M,\omega_{\mathbf P^1}\bigr)
\cong H^0\bigl(C,\mathcal M^{\vee}\otimes\Omega^1_{C/k}\bigr).
$$

Each of the three isomorphisms is natural in $\mathcal M$: the first is
the dual of the Leray edge isomorphism applied to the morphisms
$f_*\varphi$; the second is the canonical duality isomorphism of
[thm-sc-p1-duality], natural in the coherent module $\mathcal G=f_*\mathcal M$;
the third is composed of the adjunction
$\operatorname{Hom}(f_*\mathcal M,\mathcal G)\cong
\operatorname{Hom}(\mathcal M,\mathcal Hom(f_*\mathcal O_C,\mathcal G))$,
natural in $\mathcal M$, the fixed trace identification
$\mathcal Hom(f_*\mathcal O_C,\omega_{\mathbf P^1})\cong f_*\omega_C$, and
the natural isomorphism
$\omega_C\otimes\mathcal M^{\vee}\cong\mathcal Hom(\mathcal M,\omega_C)$.
This is the case $q=1$, $p=0$; with Steps 1 and 2 the theorem follows.
For invertible $\mathcal M$, [lem-sc-invertible-dual] identifies
$\mathcal M^{\vee}$ with $\mathcal M^{-1}$, which gives the two displayed
particular cases.

