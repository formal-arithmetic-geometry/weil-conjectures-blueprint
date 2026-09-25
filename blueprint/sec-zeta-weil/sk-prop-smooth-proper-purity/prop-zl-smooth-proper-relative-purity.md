+++
id = "prop-zl-smooth-proper-relative-purity"
kind = "theorem"
title = "Relative smooth-proper purity"
order = 3147
tags = ["latex:proposition"]
uses = ["cor-cbc-proper-coincidence", "cor-weil-pbc-geometric-fiber-finite", "cor-weil-pbc-geometric-fiber-qbar", "cor-zl-purity-smooth-proper", "cor-zl-rfshriek-sheaf", "def-weil-punctual-weights", "lem-tw-multiplicativity", "lem-wf-tate-twist-frobenius", "prop-weil-operations", "sbc-thm-smooth-morphisms-are-universally-locally-acyclic", "thm-fin-proper-constructibility-complete", "thm-pod-derived-poincare-duality"]
+++
Fix the finite-field datum $(p,a,q,k_0,k)$, where $q=p^a$, a prime
$\ell\neq p$, an algebraic closure $\Qlb$ of $\Ql=\mathbf Q_\ell$ and an
isomorphism $\iota:\Qlb\xrightarrow{\sim}\mathbf C$. Let
$f_0:X_0\to Y_0$ be a smooth proper morphism of separated finite-type
$k_0$-schemes of pure relative dimension $d\in\mathbf Z_{\geq0}$, with
$f_0$ and the structure morphisms exceptional-adjoint admissible (so that
the operations of [prop-weil-operations] apply), and let
$\mathcal F_0$ be a lisse $\Qlb$-Weil sheaf on $X_0$ which is punctually
$\iota$-pure of weight $w\in\mathbf R$ in the sense of
[def-weil-punctual-weights]. Then for every $i\in\mathbf Z$:

1. **(a)** the canonical map
$R^{i}f_{0!}\mathcal F_0\to R^{i}f_{0*}\mathcal F_0$ is an isomorphism of
Weil sheaves, and this sheaf is lisse;
1. **(b)** it is punctually $\iota$-pure of weight $w+i$: for every closed
point $y\in|Y_0|$, with $q_y=\#\kappa(y)$, every eigenvalue $\alpha$ of the
local geometric Frobenius $F_y$ on
$(R^{i}f_{0*}\mathcal F_0)_{\bar y}=H^{i}(X_{\bar y},\mathcal F)$
satisfies $|\iota(\alpha)|=q_y^{(w+i)/2}$.

In the absolute case $Y_0=\Spec k_0$, $\mathcal F_0=(\Qlb)_{X_0}$ ($w=0$)
clause (b) says that every eigenvalue $\alpha$ of geometric Frobenius on
$H^{i}(X,\Qlb)$ satisfies $|\iota(\alpha)|=q^{i/2}$; for $X_0$
geometrically connected this is [cor-zl-purity-smooth-proper], where the
duality step is absolute Poincaré duality and no relative duality is
needed.

## Proof

Write $f:X\to Y$ for the geometric fiber of $f_0$ and $\mathcal F$ for the
underlying sheaf of $\mathcal F_0$. The upper bound on weights is the
direct-image theorem [cor-zl-rfshriek-sheaf]; the content here is that
duality on the fibres supplies the matching lower bound.

*Step 1 (coincidence).* Since $f$ is proper, the compactification
$j=\operatorname{id}$, $p=f$ gives the canonical identification
$Rf_!\xrightarrow{\sim}Rf_*$ of [cor-cbc-proper-coincidence], and under it
the exchange map $\operatorname{Ex}_!$ defining the Weil structure on
$Rf_!\mathcal F$ is the exchange map $\operatorname{Ex}_*$ defining the Weil
structure on $Rf_*\mathcal F$ ([cor-cbc-proper-coincidence], and the
description of the Weil isomorphisms in [prop-weil-operations]). Hence
$R^{i}f_{0!}\mathcal F_0\to R^{i}f_{0*}\mathcal F_0$ is an isomorphism of
Weil sheaves for every $i$; this is the first half of (a).

*Step 2 (local constancy).* Choose a lattice for $\mathcal F$, defined over
the ring of integers $\mathcal O_E$ of a finite extension $E/\Ql$, with
reductions $\mathcal F_n$ modulo $\lambda^{n}$; since $\mathcal F$ is lisse,
each $\mathcal F_n$ is a finite locally constant sheaf of
$\mathcal O_E/\lambda^n$-modules. By [thm-fin-proper-constructibility-complete]
the sheaves $R^{q}f_*\mathcal F_n$ are constructible. For a geometric point
$\bar s$ of $Y$ and a geometric point $\bar t$ of the strict henselization
$Y_{(\bar s)}$, proper base change
[cor-weil-pbc-geometric-fiber-finite] (applied to $f$ and to its base
change to $Y_{(\bar s)}$) identifies the specialization map
$(R^{q}f_*\mathcal F_n)_{\bar s}\to(R^{q}f_*\mathcal F_n)_{\bar t}$ with the
restriction map
$H^{q}(X\times_YY_{(\bar s)},\mathcal F_n)\to H^{q}(X_{\bar t},\mathcal F_n)$.
Because $f$ is smooth it is universally locally acyclic
([sbc-thm-smooth-morphisms-are-universally-locally-acyclic]); as
$\mathcal F_n$ is étale-locally constant with torsion prime to $p$, $f$ is
locally acyclic relative to $\mathcal F_n$, and combined with properness
of $f$ (proper base change for the closed fibre over $\bar s$) this makes the
restriction map above an isomorphism (SGA 4, Exp. XVI, §2). A constructible
sheaf all of whose specialization maps are isomorphisms is locally
constant, so every $R^{q}f_*\mathcal F_n$ is finite locally constant. The
complexes $Rf_*\mathcal F_n$ form the reduction tower of
$Rf_*$ of the lattice, so passing to the limit and inverting $\lambda$
([cor-weil-pbc-geometric-fiber-qbar] for the stalks), the specialization
maps of $R^{i}f_*\mathcal F$ are isomorphisms of finite-dimensional
$\Qlb$-vector spaces and $R^{i}f_*\mathcal F$ is lisse. This completes (a).

*Step 3 (upper bound).* A punctually $\iota$-pure sheaf of weight $w$ is
$\iota$-mixed of weights at most $w$ in the sense of
[def-weil-punctual-weights] (take $m=1$, $w_1=w$). Hence
[cor-zl-rfshriek-sheaf], applied to the separated finite-type
$f_0$, shows that $R^{i}f_{0!}\mathcal F_0=R^{i}f_{0*}\mathcal F_0$ is
$\iota$-mixed of weights at most $w+i$. Taking the stalk at $\bar y$ of the
filtration in [def-weil-punctual-weights] is exact and $F_y$-equivariant,
so every eigenvalue $\alpha$ of $F_y$ on $(R^{i}f_{0*}\mathcal F_0)_{\bar y}$
is an eigenvalue on a graded piece of some weight $w_r\leq w+i$, whence
$|\iota(\alpha)|\leq q_y^{(w+i)/2}$.

*Step 4 (lower bound by duality on the fibres).* Let $\mathcal F_0^\vee$ be
the coefficient dual of $\mathcal F_0$, again a lisse Weil sheaf; its local
Frobenius at a closed point $x$ is the contragredient of that of
$\mathcal F_0$, so its eigenvalues are the $\beta^{-1}$ with $\beta$ an
eigenvalue of $F_x$ on $\mathcal F_{\bar x}$, and it is punctually
$\iota$-pure of weight $-w$ ([lem-tw-multiplicativity]). By
[lem-wf-tate-twist-frobenius] the local Frobenius on $\Qlb(d)_{\bar x}$
is $q_x^{-d}$, so $\mathcal F_0^\vee(d)$ is punctually $\iota$-pure of weight
$-w-2d$ ([lem-tw-multiplicativity]). Step 3 applied to
$\mathcal F_0^\vee(d)$ in degree $2d-i$ gives: every eigenvalue $\gamma$ of
$F_y$ on $(R^{2d-i}f_{0*}\mathcal F_0^\vee(d))_{\bar y}$ satisfies
$|\iota(\gamma)|\leq q_y^{(-w-2d+2d-i)/2}=q_y^{(-w-i)/2}$.

Now fix a closed point $y\in|Y_0|$ and a geometric point $\bar y$ over it.
By proper base change ([cor-weil-pbc-geometric-fiber-qbar]), compatibly
with the Weil structures ([prop-weil-operations]: base-change isomorphisms
are morphisms of Weil complexes), the stalks at $\bar y$ of
$R^{i}f_{0*}\mathcal F_0$ and $R^{2d-i}f_{0*}\mathcal F_0^\vee(d)$ are
$H^{i}(X_{\bar y},\mathcal F)$ and
$H^{2d-i}(X_{\bar y},\mathcal F^\vee(d))$, with $F_y$ acting through the
Frobenius of the fibre $X_{0,y}$ over $\kappa(y)=\mathbf F_{q_y}$. The fibre
$X_{\bar y}$ is smooth and proper of pure dimension $d$ over the
algebraically closed field $\bar\kappa(y)$, and $\mathcal F|_{X_{\bar y}}$ is
lisse, hence perfect over $\Qlb$. Derived Poincaré duality
[thm-pod-derived-poincare-duality], with the proper coincidence
$R\Gamma_c=R\Gamma$ of Step 1, gives on $H^{-i}$ an isomorphism

$$
H^{i}(X_{\bar y},\mathcal F)^\vee\;\cong\;
H^{2d-i}\bigl(X_{\bar y},\mathcal F^\vee(d)\bigr),
$$

which is $F_y$-equivariant because the duality isomorphisms are morphisms of
Weil complexes ([prop-weil-operations]) for the Weil structures over
$\kappa(y)$. The eigenvalues of $F_y$ on the left are the $\alpha^{-1}$
with $\alpha$ an eigenvalue of $F_y$ on $H^{i}(X_{\bar y},\mathcal F)$.
By the bound of the previous paragraph,
$|\iota(\alpha)|^{-1}\leq q_y^{(-w-i)/2}$, i.e.

$$
|\iota(\alpha)|\geq q_y^{(w+i)/2}.
$$

With Step 3 this gives $|\iota(\alpha)|=q_y^{(w+i)/2}$ for every
eigenvalue of every $F_y$, which is punctual $\iota$-purity of weight $w+i$
(Step 2 having shown the sheaf lisse). This proves (b).

*Step 5 (the absolute case).* For $Y_0=\Spec k_0$, $\mathcal F_0=(\Qlb)_{X_0}$
there is a single closed point with $q_y=q$, the constant sheaf is
punctually pure of weight $0$, and (b) reads $|\iota(\alpha)|=q^{i/2}$ for
every eigenvalue $\alpha$ of $F$ on $H^{i}(X,\Qlb)$, as asserted; for
geometrically connected $X_0$ this is the statement of
[cor-zl-purity-smooth-proper].

*What the upgrade costs.* Steps 4 and 5 use only smoothness, properness and
duality; no no-cancellation argument enters, because purity is read off
eigenvalue by eigenvalue. All the arithmetic sits in
[cor-zl-rfshriek-sheaf]: without it Step 4 bounds nothing, and with it both
inequalities are automatic.
