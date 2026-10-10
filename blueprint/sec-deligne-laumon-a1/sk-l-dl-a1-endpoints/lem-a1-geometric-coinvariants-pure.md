+++
id = "lem-a1-geometric-coinvariants-pure"
kind = "lemma"
title = "Purity of the geometric coinvariants"
order = 2730
uses = ["def-weil-frobenius-module-weights", "def-weil-punctual-weights", "def-wf-fundamental-representation", "p-linear-filtration"]
lean = ["AlgebraicGeometry.LAdicWeilSheaf.isPureOfWeightOver_geometricCoinvariants"]
+++
Let $X_0$ be a scheme locally of finite type over $k_0=\mathbf F_q$,
$X=X_0\otimes k$, and let $\mathcal F$ be a lisse Weil sheaf on $X_0$
which is punctually $\iota$-pure of weight $w$. Its *geometric
coinvariants* are $W:=\Gamma(X,\mathcal F^\vee)^\vee$, the dual of the
global sections of the dual sheaf, with the Frobenius $F_W$ dual to the
one induced by the Weil structure. When $X$ is connected, with geometric
fundamental representation $V$ ([def-wf-fundamental-representation]),
$\Gamma(X,\mathcal F^\vee)=(V^\vee)^{\pi_1(X)}=(V_{\pi_1(X)})^\vee$, so $W$
is the coinvariant quotient $V_{\pi_1(X)}$ — the maximal geometrically
constant quotient of $\mathcal F$ — with its induced Frobenius; in
general $\Gamma(X,-)$ is a product over the connected components of $X$.
Then $(W,F_W)$ is $\iota$-pure of weight $w$ (possibly $W=0$).

## Proof

*Step 1: $X_0$ geometrically connected.* Write $U_0=X_0$, $U=X$. The
geometric subgroup $\pi_1(U)$ of the Weil group of
[def-wf-fundamental-representation] is normal, so the subspace of $V$
spanned by the vectors $gv-v$, $g\in\pi_1(U)$, is stable under the Weil
group and $V\twoheadrightarrow W$ is a quotient Weil representation. On
$W$ the geometric subgroup acts trivially, so the action of any element
of degree one of the Weil group on $W$ is a single operator $F_W$,
independent of the chosen lift; an element of degree $d$ acts by
$F_W^d$.

If $U_0$ is empty, $W=0$. Otherwise choose a closed point $x\in U_0$
(a maximal ideal of the coordinate ring of a nonempty affine open; its
residue field is finite over $\mathbf F_q$ because $U_0$ is locally of
finite type) and put $d=[\kappa(x):\mathbf F_q]$. A local Frobenius
at $x$ is an element of degree $d$ of the Weil group, and under the
identification of $V$ with the stalk $\mathcal F_{\bar x}$ it acts as
the operator $F_x$ of [def-weil-punctual-weights]. Hence
$V\twoheadrightarrow W$ is an $F_x$-equivariant quotient onto
$(W,F_W^d)$. In a basis of $V$ extending a basis of the kernel, the
matrix of $F_x$ is block upper triangular ([p-linear-filtration]), so
every eigenvalue of $F_W^d$ is an eigenvalue of $F_x$ on
$\mathcal F_{\bar x}$, and has $\iota$-modulus
$|\kappa(x)|^{w/2}=q^{dw/2}$ by punctual purity
([def-weil-punctual-weights]). If $\lambda$ is an eigenvalue of $F_W$,
then $\lambda^d$ is an eigenvalue of $F_W^d$, so
$|\iota(\lambda)|^d=q^{dw/2}$ and $|\iota(\lambda)|=q^{w/2}$. Thus
$(W,F_W)$ is $\iota$-pure of weight $w$ in the sense of
[def-weil-frobenius-module-weights].

*Step 2: the general case.* Each connected component $X_{0,i}$ of $X_0$
is open, locally of finite type, and contains a closed point $x$ with
finite residue field; the algebraic closure $k_i$ of $k_0$ in
$\Gamma(X_{0,i},\mathcal O)$ embeds into $\kappa(x)$, so it is a finite
field, of degree $d_i$ say, and $X_{0,i}$ is geometrically connected
over $k_i$. Hence $X_{0,i}\otimes_{k_0}k$ is the disjoint union of the
$d_i$ connected schemes $X_{i,\sigma}=X_{0,i}\otimes_{k_i,\sigma}k$,
$\sigma\in\operatorname{Hom}_{k_0}(k_i,k)$, permuted cyclically by the
Frobenius, and $F^{d_i}$ preserves each $X_{i,\sigma}$ and acts there as
the Frobenius of $X_{0,i}$ over $k_i$. Over $k_i$ the sheaf $\mathcal F$
is still punctually $\iota$-pure of weight $w$, since $F_x$ and
$q_x=|\kappa(x)|$ do not depend on the base field.

Put $\Gamma=\Gamma(X,\mathcal F^\vee)=\prod_{i,\sigma}\Gamma(X_{i,\sigma},\mathcal F^\vee)$.
By Step 1 applied over $k_i$, each $\Gamma(X_{i,\sigma},\mathcal F^\vee)$
is the dual of a module pure of weight $w$ for $F^{d_i}$, so every
eigenvalue of $F^{d_i}$ on it has $\iota$-modulus $q^{-d_iw/2}$. Let
$\mu$ be an eigenvalue of the Frobenius on $\Gamma$, with eigenvector
$s\neq0$, and choose $(i,\sigma)$ with $s|_{X_{i,\sigma}}\neq0$. Since
$F^{d_i}$ maps $X_{i,\sigma}$ to itself, comparing restrictions in
$F^{d_i}s=\mu^{d_i}s$ shows that $\mu^{d_i}$ is an eigenvalue of $F^{d_i}$
on $\Gamma(X_{i,\sigma},\mathcal F^\vee)$, so $|\iota(\mu)|=q^{-w/2}$. The
eigenvalues of the dual Frobenius $F_W$ on $W=\Gamma^\vee$ are the
inverses of those on $\Gamma$, hence all have $\iota$-modulus $q^{w/2}$:
$(W,F_W)$ is $\iota$-pure of weight $w$.
