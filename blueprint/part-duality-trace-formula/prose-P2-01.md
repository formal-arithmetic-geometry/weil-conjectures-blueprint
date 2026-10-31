+++
id = "prose-P2-01"
kind = "hidden"
title = "Duality and the trace formula"
order = 423
+++
Part “The six operations” gives the six operations; this part makes them
compute something. Part “The six operations” already shows that the
groups $H^i_c$ are finite, since $Rf_!$ preserves $D^b_{\mathrm{ctf}}$. Here we prove
axioms (b) and (c), the trace formula and Poincaré duality, together
with the vanishing in (a) for smooth proper $X$
(Theorem [sk-cor-trace]), and we deduce rationality and the
functional equation of the zeta function (Section [sec-tf-determinants]). The results that
carry the weight are the following.

- Smooth purity (Theorem [sk-thm-purity-transport]): for $f$ smooth of
  relative dimension $d$, $f^!\simeq f^*(d)[2d]$.
- Verdier duality (Theorems [sk-thm-pd-verdier-duality]
  and [sk-thm-sf-global-duality]): $\mathbb D=\cHom(-,\omega)$ is an
  involution of $D^b_{\mathrm{ctf}}$ exchanging $Rf_!$ with $Rf_*$, and for smooth
  proper $X$ of dimension $d$ it gives the perfect cup product pairing
  between $H^i$ and $H^{2d-i}(d)$ (Corollary [sk-cor-pd-cup-product]),
  compatibly with Frobenius (Theorem [sk-thm-frobenius]).
- The Lefschetz–Verdier formula
  (Theorem [sk-p-proper]): the trace of a cohomological
  correspondence on a proper scheme is a sum of local terms over its
  fixed locus.
- The Grothendieck–Lefschetz trace formula
  (Theorem [sk-thm-tf-uniform-formula]): for every Weil complex $K$,
  $\operatorname{tr}(\operatorname{Frob}^m\mid R\Gamma_c(X,K))$ is the sum over
  $X_0(\mathbf F_{q^m})$ of the traces of Frobenius on the stalks.

Each step uses the previous one, and the reason is the same each time:
Poincaré duality and the trace formula are both statements about the
diagonal. For a compact oriented manifold $M$, the Künneth components
of the class of the diagonal in $H^*(M\times M)$ form the copairing
inverse to the cup product pairing, and the Lefschetz number of
$\varphi$ is the intersection number of its graph with the diagonal. In
our setting smooth purity provides the trace map and the class of the
diagonal; the Künneth formula for Verdier duals
(Lemma [sk-thm-sf-kunneth-verdier]) turns a correspondence
$u:c_2^*K\to c_1^!K$ into a class supported on the graph, and evaluation
$K\otimes^{\mathbf L}\mathbb DK\to\omega$ restricts it to the diagonal,
where its integral is the trace on cohomology.

The new difficulty in the arithmetic setting is that the trace formula
for Frobenius is not a formal consequence of the Lefschetz–Verdier
formula. Its local terms are computed from $\cHom(c_2^*K,c_1^!K)$ near a
fixed point, which the stalk of $K$ does not determine
(Remark [sk-rem-tf-locality-warning]), and $X$ need not be proper. Both
problems are settled by one geometric computation on a curve: the local
term of Frobenius at a rational point is the trace on the stalk
(Proposition [sk-p-frob]). Frobenius has zero
differential, so its graph meets the diagonal transversally, with
multiplicity one at each fixed point. More than that, the graph is
tangent to a coordinate axis, and this is what makes the computation on
a curve work.

Frobenius and Weil complexes appear only at the beginning of
Section [sec-lefschetz-verdier]. Smooth purity and Verdier duality
are proved over any finite or algebraically closed field, without
Frobenius, and their compatibility with Frobenius is then a formal
consequence of their construction.
