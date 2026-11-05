+++
kind = "proof"
of = "lemma-removing-finitely-many-points--1"
order = 1605002
uses = ["prose-D-14", "lemma-finite-morphisms", "lemma-finite-morphisms-cohomology", "lemma-sheaves-finite-support-finite-morphisms"]
+++
Give $Z=C\setminus U$ its reduced closed subscheme structure and write
$i:Z\hookrightarrow C$. Density removes every generic point of the
curve, so $Z$ is a finite union of $k$-rational points. The open–closed
sequence of [prose-D-14] is

$$
0\longrightarrow G\xrightarrow{\varepsilon}F
\longrightarrow i_*i^*F\longrightarrow0.
$$

It remains exact after forgetting to abelian sheaves and after inverse
image. By [lemma-finite-morphisms-cohomology] and
[lemma-sheaves-finite-support-finite-morphisms], its last term has no
positive cohomology. The long exact sequence gives (1); after restriction
to $W$, the same argument applies to the closed term on
$W\times_C Z$, using finite base change [lemma-finite-morphisms]. This
is `AlgebraicGeometry.IsCurve.dense_open_high_cohomology`.

Under the hypotheses of (2), $G$ is constructible and killed by $\ell$.
The stalks of $i^*F$ are finite, so $H^0(Z,i^*F)$ is finite. The exact
sequence

$$
\begin{split}
0\to H^0(C,G)\to H^0(C,F)\to H^0(Z,i^*F)\to{}\qquad\qquad\\
H^1(C,G)\to H^1(C,F)\to0
\end{split}
$$

and (1) show that all cohomology groups of $F$ are finite if and only
if those of $G$ are finite. In degrees zero and one, this follows by
taking finite kernels and images in the displayed sequence. This is
`AlgebraicGeometry.IsCurve.dense_open_cohomology_finiteness`, and gives
$(C_5)$ when $C$ is proper.

For $(C_3)$, if $\ell=\operatorname{char}k$, both sheaves are
$\ell$-primary and (1) transfers the vanishing. If a different prime
$p$ is the characteristic, a $p$-primary sheaf killed by $\ell$ is
zero. For $(C_4)$, if $\ell$ is invertible in $k$, both sheaves have
invertible-order torsion and the finiteness comparison applies. If
$\ell=\operatorname{char}k$, an invertible-order hypothesis on either
sheaf forces that sheaf to be zero. These cases prove the conditional
equivalences in (2), as in
`AlgebraicGeometry.IsCurve.dense_open_primary_finiteness`; they do not
require the torsion hypotheses on $F$ and $G$ to be equivalent.

For (3), after an algebraically closed field extension $k'/k$, the
closed term has the same degree-zero cohomology and still has no
positive cohomology. The pullback maps form a commuting ladder of the
displayed exact sequences. The five lemma transfers bijectivity in
degrees zero and one in both directions, using the two degrees
together. In higher degrees, use the counit isomorphisms before and
after base change and their naturality. This proves $(C_7)$ under
properness. For $(C_6)$, apply the same argument when $\ell$ is
invertible in $k$; otherwise the invertible-order hypothesis makes the
relevant sheaf and its pullback zero. These are the steps of
`AlgebraicGeometry.IsCurve.dense_open_base_change`.

Finally, (1) transfers $(C_1)$ and $(C_2)$. Its degree-two comparisons
on $C$ and on every $W$, together with naturality of restriction,
transfer surjectivity in $(C_8)$. Combining these with (2) and (3) gives
the equivalence of the eight assertions bundled by
`AlgebraicGeometry.IsCurve.assertions_iff_dense_open_prime`.
