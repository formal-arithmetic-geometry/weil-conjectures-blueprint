+++
id = "lemma-weil-pbc-derived-exchange-bounded-injective-kinjective-v5"
kind = "lemma"
title = "Bounded-below injectives are K-injective"
order = 1520
uses = ["def-weil-pbc-derived-exchange-hom-test-v5", "lemma-weil-pbc-derived-exchange-hom-differential-v5"]
+++
Every bounded-below complex whose terms are injective is K-injective.

## Proof

After shifting the target, it suffices to treat a degree-zero Hom cocycle
$f:C\to I$. Choose $m$ with $I^n=0$ for $n<m$, and construct maps
$s^n:C^n\to I^{n-1}$ upward from $n=m$ so that

$$
f^n=d s^n+s^{n+1}d. \tag{*}
$$

Assume $s^m,\ldots,s^n$ are known (with $s^m=0$ at the initial step).
On $B^{n+1}=\operatorname{im}(d:C^n\to C^{n+1})=ker d$, define

$$
t(d x):=f^n(x)-d s^n(x)\in I^n.
$$

This is well-defined: if $dx=0$, acyclicity gives $x=dy$, and the cocycle
equation together with (*) in degree $n-1$ gives
$f^n(x)=df^{n-1}(y)=d s^n(dy)=d s^n(x)$. Injectivity extends the map
$t:B^{n+1}\to I^n$ along the monomorphism $B^{n+1}\hookrightarrow C^{n+1}$
to $s^{n+1}:C^{n+1}\to I^n$. Its defining equality is (*) in degree $n$.
Thus $f=ds$, so every Hom cocycle is a coboundary.
