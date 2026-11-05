+++
id = "lemma-class-of-point--2"
kind = "lemma"
title = "The class of a point (2)"
name_showing = false
order = 868002
aliases = ["bp-r261-2"]
lean = []
uses = ["lemma-class-of-point--1", "corollary-degreewise-duality-over-fields", "definition-tate-twists"]
+++
The assertion that a closed-point class generates top cohomology is
bypassed by the mainline Lean proof.

In the setting of [theorem-trace-isomorphism-top-degree], $[x]$ generates
$H^{2d}(X,\Lambda_X(d))$. The informal deduction uses
[lemma-class-of-point--1] and the bijectivity of
$\operatorname{tr}_X(d)$: every class is a scalar multiple of the
preimage of $1$.

For the Lean route, let $X_0/\Fq$ be smooth, separated, of finite type
and geometrically connected of pure dimension $d$, put
$X=X_0\otimes_{\Fq}\Fbar$, and take coefficients $\Qbarl$, with
$\ell\ne\operatorname{char}\Fq$. The constant-coefficient case of
[corollary-degreewise-duality-over-fields] supplies a perfect,
Frobenius-invariant pairing

$$
P:H_c^{2d}(X,\Qbarl)\times H^0(X,\Qbarl(d))\longrightarrow\Qbarl.
$$

Lean chooses an isomorphism $e:H^0(X,\Qbarl(d))\simeq\Qbarl$ by
twisting the degree-zero isomorphism. With $u=e^{-1}(1)$, perfectness
makes $z\mapsto P(z,u)$ an isomorphism. Geometric Frobenius acts on $u$
by $q^{-d}$, so its invariance of $P$ makes it act on the untwisted top
group by $q^d$. Twisting by $d$ gives the invariant isomorphism in
[lemma-class-of-point--1]; for $X_0$ proper, the comparison $H_c=H$
transports it to ordinary cohomology. These are the steps of
`AlgebraicGeometry.WeilSheaf.poincareDuality_compactlySupportedCohomology_adicConstant`
and its helper `exists_linearEquiv_compactlySupportedCohomology_two_mul`.
They establish the required one-dimensional top group without
constructing a closed-point generator.
