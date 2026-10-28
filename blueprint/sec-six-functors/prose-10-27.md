+++
id = "prose-10-27"
kind = "hidden"
title = "Overview of Verdier and Poincaré duality"
order = 3413
+++
Weil's axiom (c) asks for a perfect pairing between $H^i_c$ and
$H^{2d-i}$ of a smooth variety of dimension $d$, under which the
Frobenius eigenvalues $\alpha$ and $q^d/\alpha$ correspond. In this
section we prove the perfect pairing over an algebraically closed field
(Theorem [sk-thm-sf-identification]); its compatibility with Frobenius is
Theorem [sk-thm-frobenius] in Section “Frobenius and Weil complexes”. It gives the functional equation in
Section “The Grothendieck–Lefschetz trace formula”, and in Section “Cohomology of smooth proper schemes and the Weil conjectures” it
turns the upper bound on weights into purity. The duality theory itself
is used again in Section “Frobenius, trace classes and the Lefschetz–Verdier formula”, where trace classes
are built from $K\boxtimes\mathbb D_XK$.

For a smooth morphism $f$ of pure relative dimension $d$,
Theorem [sk-thm-purity-transport] identifies $f^!$ with $f^*(d)[2d]$. Hence, for a smooth scheme
$X$ with structure morphism $a_X:X\to s=\operatorname{Spec}k$, the
object $a_X^!\Lambda_s$ is a twisted and shifted constant sheaf.
In general it is the dualizing complex of a
duality theory on $\Dctf(X,\Lambda)$, the $\ell$-adic analogue of
Poincaré duality for manifolds and of Serre duality for coherent
sheaves. The central result of this duality theory is Verdier biduality:
the double-dual map
$K\to\mathbb D_X\mathbb D_XK$ is an isomorphism for every
$K\in\Dctf(X,\Lambda)$ (Theorem [sk-thm-pd-verdier-duality]). Two
exchange formulas, $\mathbb D_YRf_!\simeq Rf_*\mathbb D_X$ and
$f^!\mathbb D_Y\simeq\mathbb D_Xf^*$, follow from the adjunctions alone.
Applying them to $\mathbb D_XK$ and using biduality, we obtain the
corresponding formulas for $Rf_*$ and $f^!$. Global duality is the
first formula for the structure morphism, and for smooth $X$ the isomorphism
$a_X^!\Lambda_s\simeq\Lambda_X(d)[2d]$ turns it into Poincaré duality. Biduality is proved by induction on
dimension, which reduces it to duality for perfect complexes on the point.

Since we only consider constructible complexes of finite Tor dimension,
which at a geometric point are perfect (Lemma [sk-lem-finite]),
and $R\operatorname{Hom}_A(-,A)$ is a duality on perfect complexes over any ring,
the finite ring $A$ may be arbitrary.

When $k$ is algebraically closed, $\Dctf(s,\Lambda)$ is the category
of perfect $\Lambda$-complexes (Lemma [sk-lem-finite]), so
statements about cohomology, such as perfect pairings in each degree,
are statements in $D(\Lambda)$. Over a finite field, the duality
statements are isomorphisms on $s_{\mathrm{pro\acute et}}$, and the statements about
cohomology are obtained after base change to an algebraic closure, with
the Weil action of Section “Frobenius and Weil complexes”.

All duality statements are eventually reduced to the geometric point,
where constructible complexes are perfect complexes and duality is the
duality of finite projective modules.
