+++
id = "thm-weil-poincare-duality"
kind = "theorem"
title = "Poincare duality for smooth proper schemes"
order = 2793
uses = ["cor-pod-reciprocal-eigenvalues", "cor-pod-untwisted-similitude", "def-coefficient-twists-detailed", "def-pod-dual-tate-datum", "def-trf-frobenius-operators", "def-weil-algebraically-closed-coefficients", "def-weil-exceptional-adjoint-admissibility", "def-weil-exceptional-inverse-image", "def-weil-finite-field-fiber", "def-weil-frobenius-coefficient-twists", "def-weil-frobenius-detailed", "def-weil-geometric-hypotheses", "def-weil-global-geometric-frobenius", "def-weil-ordinary-compact-cohomology", "def-weil-poincare-trace-cup", "def-weil-weil-sheaf-complex", "lem-fix-weil-operations", "prop-cohomological-finiteness", "thm-pod-degreewise-perfectness-over-a-field", "thm-pod-proper-poincare-duality", "thm-pod-qbar-coefficient-pairing", "thm-pod-trace-isomorphism"]
+++
Let $p$ be prime, let $a\in \mathbf Z_{\geq 1}$, put $q=p^a$, and set $k_0=\mathbf F_q$, and let $k=\overline{\mathbf F}_q$ be the fixed algebraic closure of $k_0$. Fix a prime $\ell \neq p$, write $\mathbf Q_{\ell }=\mathbf Q_\ell$, and choose an algebraic closure $\overline{\mathbf Q}_{\ell }$ of $\mathbf Q_{\ell }$. Let $X_0/k_0$ be smooth, proper, geometrically connected of pure dimension $d\in \mathbf Z_{\geq 0}$, and put $X=X_0\times _{k_0}k$. Let $a_X:X\to \operatorname{Spec}k$ be the structure morphism; no admissibility hypothesis is imposed on it, its exceptional inverse image $Ra_X^!$ being the constructible one of [def-weil-exceptional-inverse-image], which exists for every separated finite-type morphism (the ambient datum of [def-weil-exceptional-adjoint-admissibility], which fails for smooth proper curves, is not used). Let $K_X=(\mathbf Q_{\ell })_X$ be the constant Weil sheaf with its canonical structure, and let $F$ be the global geometric Frobenius endomorphism of $R\Gamma (X,K_X)$ in the geometric-Frobenius convention; write $F$ also for its automorphisms of the cohomology groups, and let $\langle -,-\rangle _i$ be the trace–cup-product pairing with values in the Tate twist $\mathbf Q_{\ell }(-d)$. Then:

*Trace.* The trace map

$$
\operatorname {tr}^{(-d)}_X:H^{2d}(X,\mathbf Q_{\ell })\xrightarrow {\  \sim \  }\mathbf Q_{\ell }(-d)
$$

is an isomorphism.

*Finiteness.* For every integer $i$, $H^i(X,\mathbf Q_{\ell })$ is finite-dimensional, and it is zero for $i\notin [0,2d]$.

*Pairing.* The pairing

$$
H^i(X,\mathbf Q_{\ell })\times H^{2d-i}(X,\mathbf Q_{\ell })\longrightarrow \mathbf Q_{\ell }(-d)
$$

is perfect for every $0\leq i\leq 2d$.

*Frobenius similitudine.* Geometric Frobenius acts on $\mathbf Q_{\ell }(-d)$ by $q^d$, and

$$
\langle Fx,Fy\rangle _i=q^d\langle x,y\rangle _i \qquad (x\in H^i(X,\mathbf Q_{\ell }),\  y\in H^{2d-i}(X,\mathbf Q_{\ell })),
$$

for every $0\leq i\leq 2d$.

*Reciprocity.* For every finite-dimensional $\mathbf Q_{\ell }$-vector space $V$, write $V^\vee =\operatorname {Hom}_{\mathbf Q_{\ell }}(V,\mathbf Q_{\ell })$; then

$$
H^{2d-i}(X,\mathbf Q_{\ell })\simeq H^i(X,\mathbf Q_{\ell })^\vee (-d),
$$

Frobenius-equivariantly, and the eigenvalues of $F$ on $H^{2d-i}(X,\mathbf Q_{\ell })$ are the $q^d/\alpha$, with multiplicity, for the eigenvalues $\alpha$ of $F$ on $H^i(X,\mathbf Q_{\ell })$.

*Base change.* For every finite extension $k_0'/k_0$ contained in $k$, put

$$
r=[k_0':k_0],\qquad q'=\# k_0'=q^r,\qquad X_0'=X_0\times _{k_0}k_0', \qquad X'=X_0'\times _{k_0'}k,
$$

and identify $X'$ with $X$ by the canonical geometric-fiber identification; the base-change map is the pullback induced by $X'\to X$ on the complexes $R\Gamma (X,(\mathbf Q_{\ell })_X)$ and $R\Gamma (X',(\mathbf Q_{\ell })_{X'})$. Under this identification the geometric Frobenius for $k_0'$ is $F'=F^r$, the pairings remain perfect, and

$$
\langle F^r x,F^r y\rangle _i=(q^r)^d\langle x,y\rangle _i
$$

for $x\in H^i(X,\mathbf Q_{\ell })$ and $y\in H^{2d-i}(X,\mathbf Q_{\ell })$.
