+++
kind = "proof"
of = "lemma-frobenius-fixed-scheme--1"
order = 959006
uses = ["definition-frobenius-correspondences-their-operators"]
+++
First consider a morphism $t:\Spec A\to X$, with $A$ a local ring,
fixed by $\Phi_X^m$. The induced map from the stalk of $X_0$ at the
image of the closed point takes values in elements $r\in A$ satisfying
$r^{q^m}=r$. Every such element is a scalar from $k$: the polynomial
$T^{q^m}-T$ splits over $k$, and a root differs from some scalar root by
$n$ in the maximal ideal; then $n^{q^m}=n$ and
$n(1-n^{q^m-1})=0$, where the second factor is a unit. Thus $n=0$.
The pullback property of $X$ now factors $t$ through a fixed $k$-rational
point. This is `IsModelFrobenius.exists_eq_comp_of_comp_eq_self`.

For a fixed morphism $g:T\to X$, apply this to each stalk of $T$.
Since $X$ is locally of finite type over $k$, the equality with a constant
map spreads to an open neighbourhood
(`IsModelFrobenius.exists_opens_comp_eq`). The fibres $V_x=g^{-1}(x)$
are therefore open, disjoint, and cover $T$. On $V_x$, the map $g$ is
the composite $V_x\to s\xrightarrow{x}X$. These maps give the unique
factorization $T\to\coprod_{x\in I_m}s\to X$, proving the equalizer
property.

Finally, the pullback property identifies $k$-rational points of $X$ with
$k_0$-morphisms $s\to X_0$. Naturality of Frobenius gives
$\Phi_X^m\circ x=x$ if and only if
$(p\circ x)\circ\Spec(\sigma^m)=p\circ x$, which proves the asserted
bijection.
