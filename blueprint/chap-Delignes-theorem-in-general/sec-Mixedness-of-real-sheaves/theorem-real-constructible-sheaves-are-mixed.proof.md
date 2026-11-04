+++
kind = "proof"
of = "theorem-real-constructible-sheaves-are-mixed"
order = 1336
uses = ["theorem-purity-real-sheaves-curves", "corollary-curve-preserving-geometric-irreducibility", "lemma-geometric-constituents-after-constant-extension", "lemma-mixedness-descends-constant-extension", "lemma-mixedness-open-closed"]
+++
We join a fixed point $x_*$ to an arbitrary point $x$ by a
curve on which the geometrically irreducible constituents stay
irreducible. On that curve each constituent is pure by
Theorem [theorem-purity-real-sheaves-curves]. Its weight can be
read off at $x_*$, so it does not depend on the curve. This handles a
lisse sheaf on a smooth affine scheme, and stratifying handles an
arbitrary constructible sheaf. Descent along constant extensions and
gluing of strata preserve mixedness
(Lemmas [lemma-mixedness-descends-constant-extension]
and [lemma-mixedness-open-closed]), so nothing about curves is used
beyond Theorem [theorem-purity-real-sheaves-curves].

*The lisse case.* Suppose that $X_0$ is smooth, geometrically
connected and affine, and that the sheaf $G$ is lisse. The curves
of Corollary [corollary-curve-preserving-geometric-irreducibility]
preserve geometric irreducibility, so we first split $G$ into
geometrically irreducible pieces. To do so, we make the constant
extension of
Lemma [lemma-geometric-constituents-after-constant-extension] and
write $S_1,\ldots,S_r$ for the quotients of its Weil filtration. The
sheaf $G$ remains real after this extension, because the powers of a
conjugation-stable multiset of eigenvalues again form a
conjugation-stable multiset.

Fix a closed point $x_*$ of $X_0$, and let $x$ be any other closed
point. By Corollary [corollary-curve-preserving-geometric-irreducibility], there is a curve
through chosen geometric points above $x_*$ and $x$ on which every
$S_j$ remains irreducible. The restriction of $G$ to this curve is
real. Theorem [theorem-purity-real-sheaves-curves] says that the
irreducible constituents of a real sheaf on a curve are pure. The
restriction of $S_j$ is one of them, because it is irreducible, and so
it is pure. Let $\alpha$ be an eigenvalue of $S_j$ at $x_*$, and let
$e$ be the residue degree over $\kappa(x_*)$ of the point of the curve
above $x_*$. At that point the corresponding eigenvalue is $\alpha^e$
and the residue cardinality is $q_{x_*}^e$. If the restriction is pure
of weight $u$, then $|\iota(\alpha)|^e=q_{x_*}^{eu/2}$. The weight of
the restriction of $S_j$ must therefore be

$$
w_j=2\log_{q_{x_*}}|\iota(\alpha)|,
$$

which does not depend on the curve. All eigenvalues of $S_j$ at $x_*$
have this modulus. At $x$, the same calculation with powers
shows that $S_j$ is pure of weight $w_j$. As $x$ was arbitrary, each
$S_j$ is pure of weight $w_j$ on $X_0$. The chosen Weil filtration then
shows that $G$ is mixed after the constant extension, and by
Lemma [lemma-mixedness-descends-constant-extension], $G$ is mixed.

*The general case.* Now let $G$ be an arbitrary constructible
real sheaf. Since nilpotents do not change the étale site, we may
assume that $X_0$ is reduced. In each irreducible component, choose a
dense smooth affine open on which $G$ is lisse and which avoids the
other components. The complement has smaller dimension. Iterating, we
obtain a finite chain of closed subschemes whose differences are
disjoint unions of smooth connected affine pieces on which $G$ is
lisse. After one finite constant extension these pieces are
geometrically connected. Such an extension is allowed by
Lemma [lemma-mixedness-descends-constant-extension], and it keeps
$G$ real. The lisse case applies
to the positive-dimensional pieces. At a zero-dimensional piece, a
Frobenius-stable full flag of each stalk has quotients of rank one,
which are pure. The restriction of $G$ to every piece is therefore mixed,
and Lemma [lemma-mixedness-open-closed], applied successively along
the chain of closed subschemes, shows that $G$ is mixed.
